import time
import matplotlib.pyplot as plt
from src.utils.generator import generate_random_events
from src.part_a_structures.event_arraylist import EventArrayList
from src.part_a_structures.event_linkedlist import EventLinkedList
from src.part_c_search_conflicts.searching import (
    linear_search_array_partc,
    linear_search_linkedlist_partc,
    binary_search_array_partc,
)


def test_function():
    num = [10, 100, 1000, 10000]
    linear_array_times = []
    linear_ll_times = []
    binary_array_times = []

    for n in num:
        events = generate_random_events(n)

        arr = EventArrayList()
        for e in events:
            arr.insert(e)
        arr.events = sorted(arr.list_all(), key=lambda ev: ev.id)
        arr.size = len(arr.events)

        ll = EventLinkedList()
        for e in events:
            ll.insert(e)

        test_id = events[-1].id

        start = time.perf_counter()
        linear_search_array_partc(arr, test_id)
        linear_array_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        linear_search_linkedlist_partc(ll, test_id)
        linear_ll_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        binary_search_array_partc(arr, test_id)
        binary_array_times.append(time.perf_counter() - start)

    plt.figure(figsize=(5, 5))
    plt.plot(num, linear_array_times, '-', label="Linear_search_srray")
    plt.plot(num, linear_ll_times, '--', label="Linear_search_linked_list")
    plt.plot(num, binary_array_times, '-', label="Binary_search_array")
    plt.title("Runtime of search algorithms")
    plt.xlabel("Number of events")
    plt.ylabel("Runtime in seconds")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()
