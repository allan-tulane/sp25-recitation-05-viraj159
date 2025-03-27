import random, time
import tabulate

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        # print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        # print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])
        
def qsort(a, pivot_fn):
    if len(a) < 2:
        return a
    # Select the pivot using the provided function:
    pivot_index = pivot_fn(a)
    pivot_value = a[pivot_index]
    # Partition the list into elements less than, equal to, and greater than the pivot.
    left = [x for x in a if x < pivot_value]
    middle = [x for x in a if x == pivot_value]
    right = [x for x in a if x > pivot_value]
    return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)

    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    # Define two variants of quicksort using currying:
    qsort_fixed_pivot = lambda lst: qsort(lst, lambda lst: 0)
    qsort_random_pivot = lambda lst: qsort(lst, lambda lst: random.randrange(len(lst)))
    tim_sort = lambda lst: sorted(lst)

    
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist.copy()),
            time_search(qsort_random_pivot, mylist.copy()),
            time_search(tim_sort, mylist.copy())
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'timsort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
