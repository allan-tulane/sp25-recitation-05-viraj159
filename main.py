import random, time
import tabulate

def ssort(L):
    ### selection sort
    for i in range(len(L)):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L

def qsort(a, pivot_fn):
    if len(a) < 2:
        return a
    pivot_index = pivot_fn(a)
    pivot_value = a[pivot_index]
    left = [x for x in a if x < pivot_value]
    middle = [x for x in a if x == pivot_value]
    right = [x for x in a if x > pivot_value]
    return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)

def time_search(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000

def compare_sort(sizes=[50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000]):
    """
    Compare the running time of different sorting algorithms.
    """
    qsort_fixed_pivot = lambda lst: qsort(lst, lambda lst: 0)
    qsort_random_pivot = lambda lst: qsort(lst, lambda lst: random.randrange(len(lst)))
    tim_sort = lambda lst: sorted(lst)
    
    results_random = []
    results_sorted = []
    
    for size in sizes:
        mylist = list(range(size))
        random.shuffle(mylist)
        results_random.append([
            size,
            time_search(ssort, mylist.copy()) if size <= 1000 else None,
            time_search(qsort_fixed_pivot, mylist.copy()),
            time_search(qsort_random_pivot, mylist.copy()),
            time_search(tim_sort, mylist.copy())
        ])
        
        mylist_sorted = list(range(size))
        results_sorted.append([
            size,
            time_search(ssort, mylist_sorted.copy()) if size <= 1000 else None,
            time_search(qsort_fixed_pivot, mylist_sorted.copy()),
            time_search(qsort_random_pivot, mylist_sorted.copy()),
            time_search(tim_sort, mylist_sorted.copy())
        ])
    
    return results_random, results_sorted

def print_results(results, title):
    print(f"\n{title}")
    print(tabulate.tabulate(results, headers=['n', 'ssort', 'qsort-fixed', 'qsort-random', 'timsort'], floatfmt=".3f", tablefmt="github"))

def test_print():
    results_random, results_sorted = compare_sort()
    print_results(results_random, "Comparison on Random Permutations")
    print_results(results_sorted, "Comparison on Sorted Lists")

random.seed()
test_print()
