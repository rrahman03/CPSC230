# creating the print_sorted function
def print_sorted(mylist): 
        # sorts the list of numbers in ascending order
        mylist.sort()
        print("The sorted list is: ", mylist)
        # send the function's result back
        return mylist

# creating the compute_mean function
def compute_mean(mylist):
      # returns the length of the object
      count = len(mylist)
      # returns the number
      total = sum(mylist)
      average = total/count
      # sends the average result back
      return average

# creating the compute_variance function
def compute_variance(mylist):
      # this computes the mean
      mean = compute_mean(mylist)
      # equation that returns the variance
      variance = sum((x - mean) ** 2 for x in mylist)/len(mylist)
      return variance

# creating the compute_standard_dev function
def compute_standard_dev(variance):
      # standard deviation equation
      standard_deviation = variance ** (1/2)
      return standard_deviation

# creating the getstddev function
def getstddev(mylist):
      variance = compute_variance(mylist)
      # computing standard deviation
      standard_deviation = compute_standard_dev(variance)
      # sends the final computation back
      return standard_deviation

# user input to enter positive integers 
# stops asking when user puts in negative number
input1 = int(input("Enter a positive integer: "))
mylist = []
while (input1 >= 0):
    mylist.append(input1)
    input1 = int(input("Enter a positive integer: "))

# prints the list of integers
sorted_list = print_sorted(mylist)

# computes the mean, variance, and standard deviation
# prints out the computation to the user
average = compute_mean(mylist)
print("The average is: ", average)

variance = compute_variance(mylist)
print("The variance is: ", variance)
standard_deviation = compute_standard_dev(variance)
print("The standard deviation is: ", standard_deviation)


