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



def restoring(dividend,divisor):
    A = "0"
    dividend,A = number_justify(dividend,A)
    for i in range(len(dividend)):
        if  A[0] == "1":
            if i == len(dividend)-1:
                A,divisor = number_justify(A,divisor)
                A = add(A,divisor)
                
            else:
                A = A[1:] + dividend[0]
                A,divisor = number_justify(A,divisor)
                A = add(A,divisor)
                if A[0] == "0":
                    dividend = dividend[1:] + "1"
                else:
                    dividend = dividend[1:] + "0"
                
        
        else:
            A = A[1:] + dividend[0]
            neg_divisor = twos_complement(divisor)
            A,neg_divisor = number_justify(A,neg_divisor)
            A= add(A,neg_divisor)
            if A[0] == "0" :
                dividend = dividend[1:] + "1"
            else:
                dividend = dividend[1:] + "0"

    
    return dividend,A




dividend = input("Enter the value of dividend.")
divisor = input("Enter the value of divisor")
dividend = "0" + dividend
divisor = "0" + divisor

quotient,remainder = restoring(dividend,divisor)

print(f"Quotient = {quotient} \nRemainder = {remainder}")