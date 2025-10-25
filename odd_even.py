def check_odd_even(number):
  """
  This function checks if a number is odd or even.
  """
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

if __name__ == "__main__":
  try:
    num = int(input("Enter a number: "))
    result = check_odd_even(num)
    print(f"The number {num} is {result}.")
  except ValueError:
    print("Invalid input. Please enter an integer.")
