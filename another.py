def print_multiplication_table(n):


    print("  |", end="")
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
    print() 


    print("--+" + "-" * (n * 3 - 1))

    # Print the table rows
    for i in range(1, n + 1):
        print(f"{i:2}|", end=" ")
        for j in range(1, n + 1):
            print(f"{i * j:2}", end=" ")
        print()  

print_multiplication_table(10)
