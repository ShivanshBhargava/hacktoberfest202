# fizzbuzz.py
# This program prints numbers from 1 to 100.
# For multiples of 3, it prints "Fizz" instead of the number.
# For multiples of 5, it prints "Buzz" instead of the number.
# For multiples of both 3 and 5, it prints "FizzBuzz".

def fizzbuzz(n=100):
    """Prints the FizzBuzz sequence up to n."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
if __name__ == "__main__":
    fizzbuzz()
