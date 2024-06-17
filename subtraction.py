def add(A,B):
    A = A[::-1]
    B = B[::-1]
    carry = 0
    rev_Result = ""
    for i in range(len(A)):
        sum = int(A[i])^int(B[i])^carry
        carry = int(A[i])&int(B[i]) | ((int(A[i])^int(B[i]))&carry)
        rev_Result += str(sum)
    return (rev_Result[::-1])


def number_justify(n1,n2):
    if len(n1)>len(n2):
        if n2[0] == "0" :
            n2 = n2.rjust(len(n1),"0")
        else:
            n2 = n2.rjust(len(n1),"1")
    else:
        if n1[0] == "0" :
            n1 = n1.rjust(len(n2),"0")
        else:
            n1 = n1.rjust(len(n2),"1")
    return (n1,n2)


def twos_complement(n):
    sum = ""
    for i in range(len(n)):
        if n[i] == "0":
            sum+="1"
        else:
            sum+="0"
    sum,num = number_justify(sum,"01")
    return add(sum,num)

def main():
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")
    n1 = "0" + n1
    n2 = "0" + n2

    n2 = twos_complement(n2)
    n1,n2 = number_justify(n1,n2)
    result = add(n1,n2)
    
    print(f"The result is {result}.")
    
main()



