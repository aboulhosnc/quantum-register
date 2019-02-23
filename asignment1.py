import cmath


class quantumRegister:
    """ This is the doc for the class quantum Register IT is supposed to print this out for the
    assignment. """
    def __init__(self,vector, quebit_number = 1,   amp = 0,  ):
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
        
        for x in (vec3):
            conj(x)
        
        for y in (vec4):
            conj(y)

        for y in (vec4):
            for x in (vec3):
                x= x*y
                outer_product.append(x)
        self.matrix = outer_product
        return outer_product


    def add_Operator(self, alpha,beta, mat_x=0, mat_y=0):
        #msg = "this is a test"

        if(mat_x != 0):
            matrix_x = mat_x
            print("there was a matrix x")
        else:
            matrix_x = self.matrix
            print("there was no matrix x")

        if(mat_y != 0):
            print("there was a matrix y")
            matrix_y = mat_y
        else:
            matrix_y = mat_x
            print("there was no matrix y")

        """
        print("The self matrix is")
        for i in (self.matrix):
            print(i)
        """
        original_matrix = self.matrix
        result_matrix = matrix_x

        for x in range(len(matrix_x)):
            for y in range(len(matrix_x[0])):
                result_matrix[x][y] =  alpha*matrix_x[x][y] +  beta*matrix_y[x][y]

        """
        self.matrix = original_matrix
        print("The original matrix is")
        for i in (original_matrix):
            print(i)
        """    
        return result_matrix
        
    
    
    def matrix_multiplication(self,register):
        """ Takes a Quantum register of size n and transforms it through this linear operator"""
        multi_matrix = (self.matrix)
        #multi_matrix_t =map(list, zip(*self.matrix))
        t_matrix =  zip(*matrix)
        #[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
        """
        multi_t = []
        for i in range(len(multi_matrix)):
            for j in range (len(multi_matrix[0])):
                multi_t[j][i] = multi_matrix[i][j]
        """
        

        print ("The transposed matrix is")
        for i in (multi_t):
            print(i)

        rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
        print("\n") 
        for row in rez: 
	        print(row) 

        #multi_matrix = [[1 for x in range(length)] for y in range (length)]
        change_state = []

        for x in (multi_matrix_t):
            change_state.append(quantumRegister.inner_product(x,register))
        print("the change state is")
        for i in (change_state):
            print(i)
        return change_state
        

    

 
def conj(num):
    """checks if a number is a complex number or not. If it is  then it does the complex conjugate of it"""
    if(isinstance(num,complex)):
        num = num.conjugate()
        

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


#p = input('Enter in your name : ')
p = "Chady"
print("You name is : ", p)

#amp = int(input('Enter the amplitude: '))
amp = 2
print("You entered an amplitude of  : ", amp)




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
q_register = quantumRegister(v1,s,amp)

#Testing without an amplitude entered
#q_register = quantumRegister(v1,s)
print(q_register.q_number)

print ("The vector you entered is ",q_register.vec)

print("The amplitude is :",q_register.amplitude)


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

greek_a = 2
greek_b = 3


print ("if you want to initialize through the matrix pick 1")
print ("if you want to  find it through the outher product of two registers pick another number")

#user_input = int(input("Enter your choice :"))
user_input = 1
if(user_input == 1):
    l_operator = LinearOperator(3,mx)
    print("The matrix given is ")
    for x in (l_operator.matrix):
        print(x)
    
    
    test23 = l_operator.add_Operator(greek_a,greek_b,my,my)
    print("The result of the add operator is  matrix") 
    for x in (test23):
        print(x)

    V1 =  [1,2,3]
    
    test24 = l_operator.matrix_multiplication(V1)
    print("The changed state is ", test24)

else:
    v3 = [ 3,4]
    v4 = [ 1,2]

    print("If you initialize with an outer product instead :")
    #l_operator = LinearOperator()
    test22 = LinearOperator.outer_product(v3,v4)
    print("The result of the outer product operator is  matrix") 
    for x in (test22):
        print(x)
    
    test23 = LinearOperator.add_Operator(greek_a,greek_b,mx,my)
    print("The result of the add operator is  matrix") 
    for x in (test23):
        print(x)
    
    V1 =  [1,2,3]
    
    test24 = LinearOperator.matrix_multiplication(V1)
    print("The changed state is ")
    for x in (test24):
        print(x)




#print("The quebits given is : ", l_operator.quebit)














