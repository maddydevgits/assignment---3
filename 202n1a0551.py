num_terms = int(input("Enter the number of terms: "))

# First two terms
term1 = 0
term2 = 1

# Check if the number of terms is valid
if num_terms <= 0:
    print("Number of terms should be a positive integer.")
elif num_terms == 1:
    print("Fibonacci sequence up to", num_terms, "term:")
    print(term1)
else:
    print("Fibonacci sequence up to", num_terms, "terms:")
    print(term1, ",", term2, end=", ")
    for i in range(2, num_terms):
        next_term = term1 + term2
        print(next_term, end=", ")
        term1 = term2
        term2 = next_term
    print()
