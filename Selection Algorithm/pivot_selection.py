#unlike the randomized selection, we dont use the first index as the pivot, we select the median first and then choose a pivot
def partition(unsorted_array,first_index,last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median= median_of_medians(unsorted_array[first_index:last_index])
    index_of_nearest_median = get_index_of_nearest_median(unsorted_array,first_index,last_index,nearest_median)
    swap(unsorted_array,first_index,index_of_nearest_median)
    pivot=unsorted_array[first_index]
    pivot_index=first_index
    index_of_last_element=last_index
    less_than_pivot_index=index_of_last_element
    greater_than_pivot_index=first_index + 1