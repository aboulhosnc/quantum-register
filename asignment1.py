class quantumRegister:
    """ This is the doc for the class quantum Register IT is supposed to print this out for the
    assignment. """
    def __init__(self, quebit_number, example ):
        self.q_number = quebit_number
        self.name = example
        
    
    def norm(self):
        """This is to find the norm of the vector that is input """
    

    def inner_product(self):
        """This takes the another register of the same size and returns a single complex number, The Hermitian innnerproduct with that register"""
    
    def tensor_product(self):
        """Takes two registers with n = n1 and n = n2, and produces a register with n1+n2 qubits, in the correct state"""

    def measurement(self):
        """ measures in a computational basis"""
    








msg = "How many quebits ?"
print(msg)
s = int(input('Enter your input : '))





run_loop = True

while (run_loop):
    if((s<1) or (s>15)):
        print("The number you enetered was not a valid number try again")
        s = int(input('Enter your input : '))
    else:
        run_loop = False
        print("You entered: ", s)


p = input('Enter in your name : ')
print("You entered: ", p)

q_register = quantumRegister(s,p)
print(q_register.q_number)
print(q_register.name)






