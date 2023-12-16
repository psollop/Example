## Sum of even numbers: Write a program that sums all the even numbers from 1 to 100.
def calculation():
    # Method 2: Using a while loop
    result = 0 #Inizialize variable result
    number = 2  #Inizialize variable result
    while number <= 100:     #Generate the proper while loop
        result += number
        number += 2       # Update number variable for even.

    print("Sum of even numbers (Method 2):", result)


def main():
    calculation()

if __name__ ==  "__main__":
    main()