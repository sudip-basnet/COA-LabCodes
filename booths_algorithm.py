def add(A, M): 
    carry = 0
    Sum = '' 
  
    # Iterating through the number 
    # A. Here, it is assumed that  
    # the length of both the numbers 
    # is same 
    for i in range (len(A)-1, -1, -1): 
  
        # Adding the values at both  
        # the indices along with the  
        # carry 
        temp = int(A[i]) + int(M[i]) + carry 
  
        # If the binary number exceeds 1 
        if (temp>1): 
            Sum += str(temp % 2) 
            carry = 1
        else: 
            Sum += str(temp) 
            carry = 0
  
    # Returning the sum from  
    # MSB to LSB 
    return Sum[::-1]     
  
# Function to find the compliment 
# of the given binary number 
def compliment(m): 
    M = '' 
  
    # Iterating through the number 
    for i in range (len(m)): 
  
        # Computing the compliment 
        M += str((int(m[i]) + 1) % 2) 
  
    # Adding 1 to the computed  
    # value by making the length of A equal to the number of bits of M 
    A='0'*(len(M)-1)
    A=A+"1"
    M = add(M, A) 
    return M

def BoothsAlgo(M,Q):
    # Computing the length of the 
    # number 
    A = '0'*len(M)
    count = len(Q) 
  
  
    comp_M = compliment(M) 
    #print(comp_M)
  
    Q = Q[:]+"0"
    while(count):
        q = Q[-2:]
        if(q=="10"):
            A=add(A,comp_M)
            print("Subtract M from A and right shift ")
            Q = A[-1]+Q[0:-1]
            A = A[0]+A[0:-1]
        elif (q =="01"):
            A = add(A,M)
            print("Add A and M and Right shift ")
            Q = A[-1]+Q[0:-1]
            A = A[0]+A[0:-1]
        elif(q=="00" or q=="11"):
            print("Right shift only ")
            Q = A[-1]+Q[0:-1]
            A = A[0]+A[0:-1]
        count-=1
    Q = Q[:-1]
    print("Final answer is ","A = ",A, "Q = ",Q)

BoothsAlgo("1011","1101")

        


