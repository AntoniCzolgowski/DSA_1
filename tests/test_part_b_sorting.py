# Testing
#Test 1
def test_all_sorts_with_plot():
    sizes = [50, 500, 5000]

    # Store times for plotting
    times_insertion_array, times_merge_array, times_quick_array = [], [], []
    times_insertion_ll, times_merge_ll, times_quick_ll = [], [], []

    print(f"{'N':>8} | {'Insertion Array (s)':>18} | {'Merge Array (s)':>15} | {'Quick Array (s)':>15} | {'Insertion LL (s)':>15} | {'Merge LL (s)':>12} | {'Quick LL (s)':>12}")
    print("-" * 105)

    for n in sizes:
        events = generate_random_events(n)

        #Array Insertion Sort
        arr = EventArrayList()
        arr.events = events.copy()
        arr.size = n
        start = time.perf_counter()
        insertion_sort_array(arr)
        t_insertion_array = time.perf_counter() - start

        #Array Merge Sort
        start = time.perf_counter()
        merge_sort_array(events.copy())
        t_merge_array = time.perf_counter() - start

        #Array Quick Sort
        start = time.perf_counter()
        quick_sort_array(events.copy())
        t_quick_array = time.perf_counter() - start

        #Linked Insertion Sort
        ll = EventLinkedList()
        for e in events:
            ll.append(e)
        start = time.perf_counter()
        insertion_sort_linkedlist(ll)
        t_insertion_ll = time.perf_counter() - start

        #Linked Merge Sort
        ll2 = EventLinkedList()
        for e in events:
            ll2.append(e)
        start = time.perf_counter()
        ll2.head = merge_sort_linkedlist(ll2.head)
        t_merge_ll = time.perf_counter() - start

        #Linked Quick Sort
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
    plt.xscale("log")  # log-scale for clearer separation
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

#Test 2
def test_sorted_event_order():
    print("\nSORTED EVENT LIST TEST\n")
    random.seed(42)
    events = generate_random_events(8)

    print("Original Events (unsorted):")
    for e in events:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    print("\nARRAY BASED SORTS")

    #Array Insertion Sort
    arr1 = EventArrayList()
    arr1.events = events.copy()
    arr1.size = len(events)
    insertion_sort_array(arr1)
    print("\n Arr Insertion Sort:")
    for e in arr1.events:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    # Array Merge Sort
    sorted_merge = merge_sort_array(events.copy())
    print("\nArr Merge Sort:")
    for e in sorted_merge:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    #Array Quick Sort
    sorted_quick = quick_sort_array(events.copy())
    print("\n Arr Quick Sort:")
    for e in sorted_quick:
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    print("\nLINKED LIST BASED SORTS")

    #Linked Insertion Sort
    ll1 = EventLinkedList()
    for e in events:
        ll1.append(e)
    insertion_sort_linkedlist(ll1)
    print("\n LL Insertion Sort:")
    for e in ll1.to_list():
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    #Linked Merge Sort
    ll2 = EventLinkedList()
    for e in events:
        ll2.append(e)
    ll2.head = merge_sort_linkedlist(ll2.head)
    print("\nLL Merge Sort:")
    for e in ll2.to_list():
        print(f"  {e.title:<15}  {e.date}  {e.time}")

    #Linked Quick Sort
    ll3 = EventLinkedList()
    for e in events:
        ll3.append(e)
    quick_sort_linkedlist(ll3)
    print("\nLL Quick Sort:")
    for e in ll3.to_list():
        print(f"  {e.title:<15}  {e.date}  {e.time}")


