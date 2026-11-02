import time
from algorithms import selection_sort, insertion_sort, merge_sort, quick_sort, block_sort
import random

def generate_large_list(size):
    return random.sample(range(1, 10**12), size)

def test_sorting_algorithms():
    large_list_size = 10**8
    large_unsorted_list = generate_large_list(large_list_size)
    print("List created")
    time.sleep(1)

    algorithms = {
        # "Selection Sort": (selection_sort, large_unsorted_list),
        # "Insertion Sort": (insertion_sort, large_unsorted_list),
        # "Merge Sort": (merge_sort, large_unsorted_list),
        # "Quick Sort": (quick_sort, large_unsorted_list),
        "Block Sort": (block_sort, large_unsorted_list)
    }

    for name, (sort_func, test_list) in algorithms.items():
        print(f"Testing {name}...")
        start_time = time.time()
        sorted_list = sort_func(test_list.copy())
        end_time = time.time()
        assert sorted_list == sorted(test_list), f"{name} failed to sort correctly."
        print(f"{name} completed in {end_time - start_time:.2f} seconds.\n")

if __name__ == "__main__":
    test_sorting_algorithms()
