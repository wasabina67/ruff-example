def print_multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def main():
    print_multiplication_table()

if __name__ == "__main__":
    main()
