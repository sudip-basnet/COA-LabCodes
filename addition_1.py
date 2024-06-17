def add(A,B):
    #reversing the string
    A = A[::-1]
    B = B[::-1]
    carry = 0
    rev_Result = ""
    for i in range(len(A)):
        sum = int(A[i])^int(B[i])^carry
        carry = int(A[i])&int(B[i]) | ((int(A[i])^int(B[i]))&carry)
        #Sum = A XOR B XOR carry
        #carry = (A AND B) OR ((A XOR B) AND carry)
        rev_Result += str(sum)
    return (rev_Result[::-1],carry)
        

def main():
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")

   #making the size of each digits the same by padding with "0"...
    if len(num1) > len(num2):
        num2 = num2.rjust(len(num1),"0")
 
    else:
        num1 = num1.rjust(len(num2),"0")


    result = add(num1,num2)
    print(f"The sum of : \n{num1}\n{num2}\n--------\n{result[0]}\nCarry: {result[1]}")


main()

if __name__ == "__main__":
    main()