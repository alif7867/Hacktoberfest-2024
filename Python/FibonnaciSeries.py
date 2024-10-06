# Python program to print Fibonacci sequence

def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0

    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, "term: ", a)
    else:
        print("Fibonacci sequence up to", n, "terms:")
        while count < n:
            print(a, end=" ")
            # Update values for the next term
            a, b = b, a + b
            count += 1

# Number of terms to print
num_terms = 10

# Call the function
fibonacci_sequence(num_terms)
