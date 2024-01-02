def readvalues():
    numbers = []
    num_count = int(input("Enter the number of elements in the list: "))
    print("Enter the elements one by one:")
    for i in range(1,num_count+1):

        num = float(input("Enter {} value:".format(i)))
        numbers.append(num)
    return numbers  # Return the list of numbers
def sumavg(numbers):
    total_sum = sum(numbers)
    if len(numbers) > 0:
        average = total_sum / len(numbers)
    else:
        average = 0
    return total_sum, average
# Call the function to read values and calculate sum and average
numbers = readvalues()
sum_result, average_result = sumavg(numbers)
print("Sum of numbers: {}".format(sum_result))
print("Average of numbers: {}".format(average_result))


