##Sum of even numbers: Write a program that sums all the even numbers from 1 to 100.
# 3 METHODS

#METHOD 1
def func1():
    even_number = [number for number in range(2,101,2)]
    sum_even_number = sum(even_number)
    
    print("METHOD 1. Sum of even numbers: ", sum_even_number)





#METHOD 2
def func2():
    result=0
    number = 2
    while number<=100:
        result += number
        number += 2

    print("METHOD 2. Sum of even numbers: ",result)






#METHOD 3

def func3():
    sum_even=0
    for number in range(2,101,2):
        sum_even+=number

    print("METHOD 3. Sum of even numbers: ", sum_even)


def main():
    func1()
    func2()
    func3()

if __name__ == "__main__":
    main()
