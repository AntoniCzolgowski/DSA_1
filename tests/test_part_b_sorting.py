import time
import random
import matplotlib.pyplot as plt
from src.part_a_structures.event import Event
from src.part_a_structures.event_arraylist import EventArrayList
from src.part_a_structures.event_linkedlist import EventLinkedList
from src.utils.generator import generate_random_events
from src.part_b_sorting.insertion_sort import insertion_sort_array, insertion_sort_linkedlist
from src.part_b_sorting.merge_sort import merge_sort_array, merge_sort_linkedlist
from src.part_b_sorting.quick_sort import quick_sort_array, quick_sort_linkedlist



# Testing
#Test 1
def test_all_sorts_with_plot():
    sizes = [50, 500, 5000]

    times_insertion_array, times_merge_array, times_quick_array = [], [], []
    times_insertion_ll, times_merge_ll, times_quick_ll = [], [], []

    print(f"{'N':>8} | {'Insertion Array (s)':>18} | {'Merge Array (s)':>15} | {'Quick Array (s)':>15} | {'Insertion LL (s)':>15} | {'Merge LL (s)':>12} | {'Quick LL (s)':>12}")
    print("-" * 105)

    for n in sizes:
        events = generate_random_events(n)

        #Arr Insertion Sort
        arr = EventArrayList()
        arr.events = events.copy()
        arr.size = n
        start = time.perf_counter()
        insertion_sort_array(arr)
        t_insertion_array = time.perf_counter() - start

        #Arr Merge Sort
        start = time.perf_counter()
        merge_sort_array(events.copy())
        t_merge_array = time.perf_counter() - start

        #Arr Quick Sort
        start = time.perf_counter()
        quick_sort_array(events.copy())
        t_quick_array = time.perf_counter() - start

        #LL Insertion Sort
        ll = EventLinkedList()
        for e in events:
            ll.append(e)
        start = time.perf_counter()
        insertion_sort_linkedlist(ll)
        t_insertion_ll = time.perf_counter() - start

        #LL Merge Sort
        ll2 = EventLinkedList()
        for e in events:
            ll2.append(e)
        start = time.perf_counter()
        ll2.head = merge_sort_linkedlist(ll2.head)
        t_merge_ll = time.perf_counter() - start

        #LL Quick Sort
        ll3 = EventLinkedList()
        for e in events:
            ll3.append(e)
        start = time.perf_counter()
        quick_sort_linkedlist(ll3)
        t_quick_ll = time.perf_counter() - start


        times_insertion_array.append(t_insertion_array)
        times_merge_array.append(t_merge_array)
        times_quick_array.append(t_quick_array)
        times_insertion_ll.append(t_insertion_ll)
        times_merge_ll.append(t_merge_ll)
        times_quick_ll.append(t_quick_ll)

        print(f"{n:8d} | {t_insertion_array:18.5f} | {t_merge_array:15.5f} | {t_quick_array:15.5f} | {t_insertion_ll:15.5f} | {t_merge_ll:12.5f} | {t_quick_ll:12.5f}")


    plt.figure()
    plt.title("Sorting Algorithm Performance (Time vs Number of Events)")
    plt.plot(sizes, times_insertion_array, 'r-o', label='Insertion Sort (Array)')
    plt.plot(sizes, times_merge_array, 'g-o', label='Merge Sort (Array)')
    plt.plot(sizes, times_quick_array, 'b-o', label='Quick Sort (Array)')
    plt.plot(sizes, times_insertion_ll, 'r--o', label='Insertion Sort (LinkedList)')
    plt.plot(sizes, times_merge_ll, 'g--o', label='Merge Sort (LinkedList)')
    plt.plot(sizes, times_quick_ll, 'b--o', label='Quick Sort (LinkedList)')
    plt.xlabel("Number of Events")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

#Test 2
def test_sorted_event_order():
    print("\nSORTED EVENT LIST TEST\n")
    random.seed(42)
    events = generate_random_events(10)

    print("Original Events:")
    for e in events:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    print("\nARRAY BASED SORTS")

    #Arr Insertion Sort
    arr1 = EventArrayList()
    arr1.events = events.copy()
    arr1.size = len(events)
    insertion_sort_array(arr1)
    print("\n Arr Insertion Sort:")
    for e in arr1.events:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    # Arr Merge Sort
    sorted_merge = merge_sort_array(events.copy())
    print("\nArr Merge Sort:")
    for e in sorted_merge:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    #Arr Quick Sort
    sorted_quick = quick_sort_array(events.copy())
    print("\n Arr Quick Sort:")
    for e in sorted_quick:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    print("\nLINKED LIST BASED SORTS")

    #LL Insertion Sort
    ll1 = EventLinkedList()
    for e in events:
        ll1.append(e)
    insertion_sort_linkedlist(ll1)
    print("\n LL Insertion Sort:")
    for e in ll1.to_list():
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    #LL Merge Sort
    ll2 = EventLinkedList()
    for e in events:
        ll2.append(e)
    ll2.head = merge_sort_linkedlist(ll2.head)
    print("\nLL Merge Sort:")
    for e in ll2.to_list():
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    #LL Quick Sort
    ll3 = EventLinkedList()
    for e in events:
        ll3.append(e)
    quick_sort_linkedlist(ll3)
    print("\n LL Quick Sort:")
    for e in ll3.to_list():
        print(f"  {e.title:<15}  {e.date}  {e.time}")


