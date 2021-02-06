class Calculator():
    
    """
    Python class - calculator
    The class takes an argument - a mathematical expression and return the result in a type float.
    """
    
    def __init__(self, string):
        
        self.string = string
        self.exp = None
        self.mult_div = None
        self.add_sub = None
        self.result = None
        
        if type(self.string) != str:
            raise ValueError('Wrong input type. Only str allowed')
    
    
    
    # Perform the exponential operation. The function may conduct several exponential operations one by one, just like  
    # 2 ** 2 ** 2 without getting an error.
    
    def exponent(self):
    
        self.exp = self.string.split()  
        res = []  
    
        for i in range(len(self.exp) - self.exp.count('**')):
        
            if self.exp[i] != '**' or self.exp[i] != '^':
                res.append(self.exp[i])              
            if self.exp[i] == '**' or self.exp[i] == '^':   
                del res[-1]
                res.append(str(float(res[-1]) ** float(self.exp[i+1])))
                del res[-2]
                del self.exp[i]
                
        self.result = ' '.join(res)
    
    
    
    # Perform the multiplication and division operations.
    
    def mult_and_div(self):
        
        if self.result is not None:
            self.mult_div = self.result.split()
        else:
            self.mult_div = self.string.split()
    
        for i in range(len(self.mult_div)):   
            if self.mult_div[i] == '/':
                unit = float(self.mult_div[i-1]) / float(self.mult_div[i+1])
                self.mult_div[i+1] = str(unit)           
            if self.mult_div[i] == '*':
                unit = float(self.mult_div[i-1]) * float(self.mult_div[i+1])
                self.mult_div[i+1] = str(unit)

        for i in range(len(self.mult_div) - self.mult_div.count('*') - self.mult_div.count('/')):
            if self.mult_div[i] == '*' or self.mult_div[i] == '/':
                del self.mult_div[i-1]
        
        self.mult_div = list(filter(lambda a: a != '*', self.mult_div))
        self.mult_div = list(filter(lambda a: a != '/', self.mult_div))
        
        self.mult_div = ' '.join(self.mult_div) 
        self.result = self.mult_div       
 


    # Perfomr the addition and subtraction operations.

    def add_and_subs(self):
    
        if self.result is not None:
            self.add_sub = self.result.split()
        else:
            self.add_sub = self.string.split()
    
        res = float(self.add_sub[0])
        
        for i in range(1, len(self.add_sub)-1):
            if self.add_sub[i] == '+':
                res += float(self.add_sub[i+1])
            if self.add_sub[i] == '-':
                res -= float(self.add_sub[i+1])
            
        self.result = res
        
        
        
    # Main function. It performs three types of math operations sequentially.
    # To reduce computation time, first, we check the input expression for exponential,
    # addition and division operations. 
    # If non of them exists, we perform only addition or subtraction operations.
    
    def calculation(self):
        
        if self.string.count('**') > 0:
            self.exponent()
        if self.string.count('*') > 0 or self.string.count('/') > 0:
            self.mult_and_div()
        self.add_and_subs()
        
        return self.result
    
    
    #def __repr__(self):
        #return '{}'.format(self.calculation())
