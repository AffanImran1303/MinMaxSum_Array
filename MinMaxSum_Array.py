def minMaxsum(numbers_array):
  #Sorting the array
    numbers_array.sort()
  #Finding the length of array
    total_length=len(numbers_array)
  #Setting values of min_sum and max_sum to 0 as default
    min_sum=0
    max_sum=0
  #One less than total length of array, i.e the Second last position of array.
    second_last=total_length-1
    for n in range(total_length-1):
        min_sum+=numbers_array[n]
        max_sum+=numbers_array[second_last]
        second_last-=1
    print(min_sum,max_sum)
        
minMaxsum([1,2,3,4])
