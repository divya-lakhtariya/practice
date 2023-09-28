def get_largest_smallest_sum(numbers):
    if not numbers:
        print("The list is empty.")
        

    largest = numbers[0]
    smallest = numbers[0]
    sum = 0

    for num in numbers:
        sum += num
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Sum of all numbers:",sum)
    
my_list = [10,30,4,20,30]
get_largest_smallest_sum(my_list)
