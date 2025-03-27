# CMPS 2200 Reciation 5
## Answers

**Name:**Viraj Choksi


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
The provided data on sorting algorithm performance generally aligns with their asymptotic time complexities, excluding Timsort for now. Selection sort (ssort) consistently shows a quadratic growth in running time (O(n^2)) regardless of input type. Quicksort with a fixed pivot (qsort-fixed) exhibits behavior between O(nlogn) and O(n^2), performing poorly on sorted lists where its fixed pivot leads to unbalanced partitions. Quicksort with a random pivot (qsort-random) demonstrates performance closer to the average-case O(nlogn), showing better efficiency than the fixed pivot version, especially on sorted inputs. Changing the input from random permutations to sorted lists significantly improves the relative performance of algorithms like qsort-random, highlighting their sensitivity to the initial order of the data.

- **1c.**
Comparing the fastest implementation from the previous analysis (likely quicksort with random pivot) to (Timsort), Python's sorting is generally faster and more efficient, especially on partially sorted data. Timsort's adaptive nature, a combination of merge sort and insertion sort, allows it to leverage existing order, leading to better performance than a standard quicksort implementation across a broader range of input types and sizes. While quicksort with a random pivot provides good average-case performance, Timsort is specifically optimized for real-world data and exhibits superior speed.
