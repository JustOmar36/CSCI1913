1. Omar Masri , Brandon Weinstein

2. backwards.png
   sorted_list.png
   random.png
   near_sorted.png
   
3. The algorithm's behavior depends on how the lists are sorted. 
		- In the case of backwards lists the merge sort preformed the least number of operations, which means it is a lot more effiecent in run-time/CPU and it had a run-time of O(logn). 
		  Where as the selection and insertion sort had a run-time O(N^2). The reason merge sort was the most effiecent due to its tendency to divide and conquer unlike the others which 
		  checks each element in the lists. 
		- As for near_sorted and sorted the selection sort had a run-time of O(N^2), insertion had a runtime of O(N) and merge had a run-time of O(logn). Inseration sort did well here, because it has to 
		  preform a short amount of operations.
		- In the case of random_sort, merge sort preformed the least amount of operations, similar to the reasoning before of dividing up the lists and then sorting them. For the sorted_list merge 
		  had the run-time of O(nlogN), insertion had O(N^2), and selection had O(N^2).

4. Our expectations for the selection sort was O(N^2), because it has to preform the same steps with no bearing on how the input data is sorted to begin with. 
   Merge sort had the run-time of O(NlogN), because the amount of operations it had to do with each list followed the same pattern of dividing and sorting. As for the insertion sort, 
   it depended on how the initial list was sorted, and from there the number of operations varied.

5. In the case of the near_sorted or sorted, the insertion sort can be faster than merge sort.

6. Merge sort, due to its effeceiency when sorting random data (since we don't know anything about how the input is sorted)
