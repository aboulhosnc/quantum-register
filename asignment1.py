import cmath


class quantumRegister:
    """ This is the doc for the class quantum Register IT is supposed to print this out for the
    assignment. """
    def __init__(self,vector, quebit_number = 1,   amp = 0,  ):
        self.q_number = quebit_number
        self.vec  = vector
        
        if(amp != 0):
            self.amplitude = 2**amp
        else:
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
        
        for y in (vec4):
            for x in (vec3):
                x= x*y
                tensor_product.append(x)
        
        return tensor_product


    def measurement(self):
        """ measures in a computational basis"""
        
    



class LinearOperator:
    """This is a test class for linear operator right now will fill in more"""
    
    def __init__(self):
        """This is a test class right now nothing in it"""

    def year(self):
        #msg = "this is a test"
        year = 15
        
        return int(year)
    

    
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
        print("You entered: ", s)


#p = input('Enter in your name : ')
p = "Chady"
print("You entered: ", p)

#amp = int(input('Enter the amplitude: '))
amp = 2
print("You entered: ", amp)




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

q_register = quantumRegister(v1,s,amp)
print(q_register.q_number)

print (q_register.vec)

print(q_register.amplitude)

#quantumRegister.inner_product(v2,v1,v2)
c = quantumRegister.inner_product(v1,v2)
print("inner product is : ", c)
#for i,j in zip(v1,v2):
 #   print(i,j)





normRegister = q_register.norm()
print ("norm of a register is ", normRegister)



tensor = quantumRegister.tensor_product(v3,v4)

print("tensor product of an array is", tensor)


