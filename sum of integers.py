user_input = input("Enter a list of integers separated by spaces: ")
integer_list = list(map(int, user_input.split()))

sum_of_integers = sum(integer_list)

print(f"Sum of the integers: {sum_of_integers}")