import cmath
import sys
import random
from copy import deepcopy

class quantumRegister:
    """ This is the doc for the class quantum Register IT is supposed to print this out for the
    assignment. """
    def __init__(self,vector, quebit_number = 1,   amp = 0,  ):

        if(quebit_number < 1):
            print("quebit too low default is 1")
            quebit_number = 1
        elif (quebit_number > 15):
            quebit_number = 15
            print("quebit was too high quebit will be 15")
        else:
            pass

        self.q_number = quebit_number
        self.vec  = vector
        
        if(amp != 0):
            self.amplitude = 1/ (cmath.sqrt(2**amp))
            #print("The amplitude is :", self.amplitude)
        else:
            print("you did not enter an amplitude")
            msg = "default amplitude will be 0"
            print(msg)
            self.amplitude = 0
        

    
    def norm(self):
        """This is to find the norm of the vector that is input """
        
        z = 0
        for x in (self.vec):
            x=(x**2)
            z = z + x
        norm = cmath.sqrt(z)
        return norm


    

    def inner_product( vec1, vec2):
        """This takes the another register of the same size and returns a single complex number, The Hermitian innnerproduct with that register"""
        inner_product = 0
        
        for x in (vec1):
            conj(x)
        
        for y in (vec2):
            conj(y)
      
        for i,j in zip(vec1,vec2):
            #print(i,j)
            inner_product  = inner_product  + (i * j)

        return inner_product
        


    def tensor_product(vec3, vec4):
        """Takes two registers with n = n1 and n = n2, and produces a register with n1+n2 qubits, in the correct state"""
        tensor_product = []
        
        for x in (vec3):
            conj(x)
        
        for y in (vec4):
            conj(y)

        for y in (vec4):
            for x in (vec3):
                x= x*y
                tensor_product.append(x)
        
        return tensor_product


    def measurement(self):
        """ measures in a computational basis"""

        quebits = self.q_number
        Y = self.vec
        amplitude = self.amplitude
        
        print(" quebit number is ",quebits)
        
        """
        for i in range(0,quebits):
            
            multi_row = [0] * (quebits -1)
            multi_row.insert(i,1)
            if(multi_row == register):
                print("it matched")
                multi_row = [x *amplitude for x in multi_row]
                print(multi_row)
            else:
                print(multi_row)
            """
        high = 0
        highI = 0
        measurement = 0
        allState = []
        for i in Y:
            #z = (Y.real, Y.imag)
            imagN = i.imag
            realN = i.real
            ampReal = amplitude * realN
            
            allState.append(realN)
            allState.append(imagN)
            ampimag = amplitude * imagN
            """
            #imaginary = im
            print("whole number is ", i)
            print("real number is ", realN)
            print("imaginary number is ", imagN)
            print("real number with amp is ", ampReal)
            print("imaginary number with amp is ", ampimag)
            """

        for i in allState:
            print(i) 
        
        randN = random.randint(0,len(allState))
        measurement = allState[randN]
        print
        print("measurement is ",measurement)   
        print("") 
        
        #to exit afterwards
        #sys.exit()
       
        
        
    
    def permute(v6):
        """This will change the state of the register to the new numbeing of quebits"""
        test = v6.pop(len(v6)-1)
        v6.insert(0,test)
        return v6
        
    



class LinearOperator:
    """This class is a matrix class that will alow you to do multiple things with it"""
    
    def __init__(self,n_quebits = 1, two_darray=0  ):
        """This is a test class right now nothing in it"""
        self.quebit = n_quebits
        m = []
        if(two_darray != 0):
            self.matrix = two_darray
            print("a matrix was given")
        else:
            nq = self.quebit
            print("no matrix was given")
            print("using identity matrix")
            m = [[0 for x in range(nq)] for y in range (nq)]

            for i in range(0,nq):
                m[i][i] = 1

            self.matrix = m

    def outer_product(self,vec3, vec4):
        """takes two quantum registers of the same size n and creates linear operator"""
        outer_product = []
        """
        print("self matrix old  is ")
        for i in (self.matrix):
            print(i)
        """
        for x in (vec3):
            conj(x)
        
        for y in (vec4):
            conj(y)

        length = len(vec3)
        #print("length is : ",length)
        for i in vec3:
            multi_row = []
            #print("row is ",multi_row)
            for row in (vec4):
                #print("i is ",i)
                multi_row.append(i*row)
            outer_product.append(multi_row)
        
        self.matrix = deepcopy(outer_product)
        """
        print("self matrix old  is ")
        for i in (self.matrix):
            print(i)
        
        
        print("new self  matrix is ")
        for i in (self.matrix):
            print(i)
        """
        return outer_product


    def add_Operator(self, alpha,beta, mat_x=0, mat_y=0):
        """This function adds two linear operators together to form a another one. can have scalars of the operators first"""
 

        if(mat_x != 0):
            matrix_x = mat_x
            #print("there was a matrix x")
        else:
            matrix_x = deepcopy(self.matrix)
            print("there was no matrix x")

        if(mat_y != 0):
            #print("there was a matrix y")
            matrix_y = mat_y
        else:
            matrix_y = deepcopy(self.matrix)
            print("there was no matrix y")

        result_matrix = deepcopy(matrix_x)


        for x in range(len(matrix_x)):
            for y in range(len(matrix_x[0])):
                result_matrix[x][y] =  alpha*matrix_x[x][y] +  beta*matrix_y[x][y]


        return result_matrix
        
    
    
    def matrix_multiplication(self,register):
        """ Takes a Quantum register of size n and transforms it through this linear operator"""
        multi_matrix = (self.matrix)
        
        print("Linear operator is")
        for i in multi_matrix:
            print (i)
        
        
        multi_t = []

        for i in range(len(multi_matrix[0])):
            multi_row = []
            for row in multi_matrix:
                multi_row.append(row[i])
            multi_t.append(multi_row)
    
        change_state = []

        for x in (multi_t):
            change_state.append(quantumRegister.inner_product(x,register))

        return change_state
        

    

 
def conj(num):
    """checks if a number is a complex number or not. If it is  then it does the complex conjugate of it"""
    if(isinstance(num,complex)):
        num = num.conjugate()
        
"""
run_loop = True

while (run_loop):
    msg = "How many quebits ?"
    print(msg)  
    #s = int(input('Enter your input : '))
    s = 2
    #s.conjugate()

    if((s<1) or (s>15)):
        print("The number you enetered was not a valid number try again")
    else:
        run_loop = False
        print("You entered quebits of : ", s)

"""
#p = input('Enter in your name : ')
p = "Chady"
print("You name is : ", p)

#amp = int(input('Enter the amplitude: '))
amp = 2
print("You entered an amplitude of  : ", amp)

s = 3
print("You entered quebits of : ", s)


z= complex(2,3)
print ("original value is ", z)
conj(z)


test1 = 5
print("original value is ", test1)
conj(test1)

v1 = [ complex(1, 1), complex(2, -1)]
v2 = [complex(3,-2), complex(1,1)]
v3 = [ 3,4]
v4 = [ 1,2]


#Testing with an amplitude entered
#v1 = [complex(1,-1), complex(0,-1)
q_register = quantumRegister(v1,s,amp)

#Testing without an amplitude entered
#q_register = quantumRegister(v1,s)
print(q_register.q_number)

print ("The vector you entered is ",q_register.vec)

print("The amplitude is :",q_register.amplitude)

q_register.measurement()


c = quantumRegister.inner_product(v1,v2)
print("inner product is : ", c)



tensor = quantumRegister.tensor_product(v3,v4)

print("tensor product of an array is", tensor)


v6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

test = quantumRegister.permute(v6)

print("The permutation of the quebits are ", test) 

mx = [[1,2,3],
        [4,5,6],
        [7,8,9]]

my = [[9,8,7],
        [6,5,4],
        [3,2,1]]

mxx = [[1,2,3,4],
        [2,4,6,8],
        [3,6,9,12],
        [4,8,12,16]]

mxy = [[1,2,3,4],
        [2,4,6,8],
        [3,6,9,12],
        [4,8,12,16]]


greek_a = 2
greek_b = 3


print ("if you want to initialize through the matrix pick 1")
print ("if you want to  find it through the outher product of two registers pick another number")

#user_input = int(input("Enter your choice :"))
user_input = 2
if(user_input == 1):
    # without a given matrix defaults to identity
    #l_operator = LinearOperator(3)
    #with a given matrix does not default to identity
    l_operator = LinearOperator(3,mx)
    # with four 4x4 matrix instead
    l_operator = LinearOperator(4,mxx)
    print("The matrix  used is  with option 1 ")
    for x in (l_operator.matrix):
        print(x)
    
    #If no matrixes are given then it uses the identity matrixes
    #test23 = l_operator.add_Operator(greek_a,greek_b)
    #IF matrixes are given for the add operation
    test23 = l_operator.add_Operator(greek_a,greek_b,my,my)
    print("The result of the add operator is  matrix with option 1") 
    for x in (test23):
        print(x)

    V1 =  [1,2,3]

    # with 4 quebits
    V11 = [1,2,3,4]
    
    test24 = l_operator.matrix_multiplication(V11)
    print("The changed state through multiplication with option 1 is  ", test24)

else:
    v3 = [ 1,2,3,4]
    v4 = [ 1,2,3,4]

    print("If you initialize with an outer product instead with option 2 :")
    length = len(v3)
    l_operator = LinearOperator(length)
    test22 = l_operator.outer_product(v3,v4)
    print("The result of the outer product operator is  matrix option 2") 
    for x in (test22):
        print(x)
    
    print("The result of the add operator is  matrix option 2") 
    #With no default add operation
    #test23 = l_operator.add_Operator(greek_a,greek_b,mx,my)
    #with default add operation
    test23 = l_operator.add_Operator(greek_a,greek_b)
    
    for x in (test23):
        print(x)
    
    V1 =  [1,2,3,4]
    
    test24 = l_operator.matrix_multiplication(V1)
    print("The changed state through multiplication is option 2", test24)




