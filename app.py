import gradio as gr
import time
import random

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35

    idx, comps = interpolation_search(arr, target)

    output = f"Array: {arr}\n"
    output += f"Searching for: {target}\n\n"
    output += f"Found at index: {idx}, Comparisons: {comps}\n\n"

    sizes = [1000, 5000, 10000, 50000, 100000]

    output += "Size\tIS Time(ms)\tBS Time(ms)\tIS Comparisons\tBS Comparisons\n"
    output += "-" * 70 + "\n"

    for size in sizes:
        test_arr = sorted(random.sample(range(size * 10), size))
        test_target = test_arr[random.randint(0, size - 1)]

        start = time.perf_counter()
        for _ in range(100):
            _, comp_is = interpolation_search(test_arr, test_target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()
        for _ in range(100):
            _, comp_bs = binary_search(test_arr, test_target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        output += f"{size}\t{is_time:.4f}\t{bs_time:.4f}\t{comp_is}\t{comp_bs}\n"

    return output


demo = gr.Interface(
    fn=performance_analysis,
    inputs=[],
    outputs=gr.Textbox(label="Performance Results", lines=15),
    title="Interpolation Search vs Binary Search",
    description="Click Run to compare performance across different array sizes."
)

demo.launch()