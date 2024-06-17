def number_justify(n1,n2):
    if len(n1)>len(n2):
        n2 = n2.rjust(len(n1),"0")
    else:
        n1 = n1.rjust(len(n2),"0")
    return (n1,n2)

def add(n1,n2):
    n1 = n1[::-1]
    n2 = n2[::-1]

    carry = 0
    rev_result =""

    for i in range(len(n1)):
        sum = int(n1[i])^int(n2[i])^int(carry)
        carry = int(n1[i])&int(n2[i]) | (int(n1[i])^int(n2[i]))&int(carry)

        rev_result+= str(sum)
    result =(rev_result[::-1])
    return (result)


def partial_product(num1,num2):
    multiplier,multiplicand = number_justify(num1,num2)
    A = "0"

    for i in range(len(multiplier)):
        if multiplier[-1]== "1":
            A,multiplier = number_justify(A,multiplier)
            A = add(A,multiplicand)
        multiplier = A[-1] + multiplier[:len(multiplier)-1]
        A = "0" + A[:len(A)-1]

    return (A+multiplier)


def main():
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")

    result = partial_product(number1,number2)
    print(f"The final result is {result}.")



main()
