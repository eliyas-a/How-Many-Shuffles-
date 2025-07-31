import sys

def shuffle_count(num):

# Making a list with "num" amount of integers

    list = []
    for i in range(num):
        list.append(i)
    


# Saving an original list to compare to
    original_list = list

# Function for the shuffle
    def shuffle(list, num):
        first_half = list[:int(num/2)]
        second_half = list[int(num/2):]
        shuff = []
        for i in range(int(num/2)):
            shuff.append(first_half[i])
            shuff.append(second_half[i])
            
        
        return shuff

# Running first shuffle
    list = shuffle(list, num)
# Making a variable for number of shuffles
    runs = 1

# Shuffles until the same
    while list != original_list:
        list = shuffle(list, num)
        runs += 1
    
    return runs
    


try:

# Finding length of list
    number = int(input("How many values are in the list: "))
    if number % 2 != 0:
        print("Please enter an even number.")
        sys.exit()


    print(f"It will take {shuffle_count(number)} shuffles to reach the original list")


except ValueError:
    sys.exit()

