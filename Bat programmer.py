def findNumOfStepsRequired(num_of_patients, starting_step):
    total_steps = starting_step
    for i in range(2, num_of_patients + 1):
        total_steps += i * starting_step
    return total_steps

# take user input
num_of_patients = int(input("Enter the number of escaped patients: "))
starting_step = int(input("Enter the starting step: "))

# calculate the number of steps required
num_of_steps = findNumOfStepsRequired(num_of_patients, starting_step)

# print the result
print(f"Number of steps required: {num_of_steps}")