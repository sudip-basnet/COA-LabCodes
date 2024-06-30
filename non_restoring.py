def rjust_number(n1, n2):
    l1 = len(n1)
    l2 = len(n2)
    if l1 > l2:
        n2 = n2 .rjust(l1, '0')
    elif l2 > l1 :
        n1 = n1.rjust(l2, '0')

    return (n1, n2)

def twoComplement(B):
    B_1C = ""

    for i in range(len(B)):
        temp = '1' if B[i] == '0' else '0'
        B_1C = B_1C + temp
        temp = ''

    B_1C, ones = rjust_number(B_1C, '1')
    B_2C = add(B_1C, ones , len(ones))
    
    return B_2C

def add(A, B, N):
    A = A[::-1]
    B = B[::-1]

    res = ""
    Carry = 0 
    for i in range(N):
        S = int(A[i]) ^ int(B[i]) ^ Carry 
        Carry = ( int(A[i]) & int(B[i]) ) | ( Carry & ( int(A[i]) ^ int(B[i] ) ) )
        res = str(S) + res

    res = str(Carry) + res 

    return res 

def sub(A, B, N):

    B_2C = twoComplement(B)
    
    B_2C , A  = rjust_number(B_2C, A)

    res = add(A, B_2C, len(A))

    res = res[len(res)-N:]

    return res



def nonRestoring(Q, M):
    A='0'
    A,M = rjust_number(A,M)

    for i in range(len(Q)):

        if(A[0] == "1"):
            A = A[1:] + Q[0]
            A = add(A,M,len(M))
            A=A[len(A) - len(M):]

        else:
            A = A[1:] + Q[0]
            A = sub(A,M, len(M))

        if(A[0] == "1"):
            Q = Q[1:] + '0'
        else:
            Q = Q[1:] + '1'

    if(A[0]=="1"):
        A = add(A,M, len(M))
        A = A[len(A) - len(M):]


    return (Q,A)


def main():
    dividend = input("Enter the value of dividend:")
    divisor = input("Enter the value of divisor:")
    Quiotent, Remainder = nonRestoring(dividend,divisor)
    print(Quiotent)
    print(Remainder)

if __name__ == "__main__":
    main()
