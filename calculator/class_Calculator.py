class Calculator():
    
    """
    Python class - a simple calculator. 
    
    The function performs four fundamental operations, deals with brackets 
    and may perform an exponentiation.
    
    The class takes an argument - a mathematical expression and returns the result in a type float.  
    For example, object '( 2 + 3 ) / 2 ** 2' will be transformed into 1.25.  
    
    To make a calculation with the class use the following syntax:  
    
    ```
    x = '( 2 + 3 ) / 2 ** 2'
    q = Calculator(x)
    q.calculation()
    
    >>> 1.25
    ```
    
    The computation process performs four steps. First, if the input contains brackets,   
    the function splits the string into special tokens, according to brackets operations queue.  
    Next, we compute math operations under the brackets. 
    After that, we combine changed tokens into a new expression and compute the rest operations. 
    
    Tokens may starts or ends with math symbols. These types of tokens are calling 'left' and 'right',  
    according to a position of a special symbol. For example, token '/ 2 + 4' is the 'right one'.  
    This approach is using during the performance of the right queue of math operations.
    
    In case without the brackets into the input expression, we skip the first step to reduce the computation time.  
    
    Class is sensitive for proper using the brackets. In some rare cases, 
    the exponentiation of expression under the brackets may cause a wrong computation. 
    Please, carefully check the places of brackets.
    
    Single spaces should split the characters in the input expression.
    
    
    Parameters
    ----------
    param_1 : str
        A math expression in the special object form.
   
    Returns  
    ------- 
    float  
        The result of the computation.
    """
    
    def __init__(self, string):
        
        self.string = string
        self.exp = None
        self.bracket = None
        self.mult_div = None
        self.add_sub = None
        self.result = None
        
        if type(self.string) != str:
            raise ValueError('Wrong input type. Only str allowed')
        
        if self.string.count(' ') % 2 != 0:
            raise ValueError('Check the spaces between the characters')
        
    
    
    # Function splits the input string into special tokens, according to brackets queue.
    def brackets_split(self):

        expr = self.string.split()  
        
        chars = '/-+*'
        res, temp = [], []
        br = 0
    
        for i in range(len(expr)):
        
            if expr[i] == '(' and br == 0:
                br += 1
                temp = []             
            elif expr[i] != '(' and br == 0:
                res.append(expr[i])      
            elif expr[i] == '(' and br > 0:
                res.append(' '.join(temp))
                temp = []
                br += 1
            elif  br > 0 and expr[i] != ')':
                temp.append(expr[i])
            elif expr[i] == ')':
                res.append(' '.join(temp))
                temp = []
                br -= 1
            
        for i in reversed(range(len(res))):
            if len(res[i]) == 0:
                del res[i]
        
        print('brackets done', res)
        
        self.bracket = res
        
        
    
    # The function performs the exponentiation. It deal with both '**' and '^' operands.
    def exponent(self, arg=None):
        
        if arg is not None:
            self.exp = arg.split()
        else:
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
        
        if arg is not None:
            return ' '.join(res)
        else:
            self.result = ' '.join(res)

    
    
    # The function performs multiplication and division. Only '*' and '/' math symbols allowed.
    def mult_and_div(self, arg=None):
        
        if arg is not None:
            self.mult_div = arg.split()
        elif self.result is not None:
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
        
        if arg is not None:
            return ' '.join(self.mult_div)
        else:
            self.mult_div = ' '.join(self.mult_div) 
            self.result = self.mult_div       
 


    # The function performs addition and subtraction. Only '+' and '-' math symbols allowed.
    def add_and_subs(self, arg=None):
    
        if arg is not None:
            self.add_sub = arg.split()
        elif self.result is not None:
            self.add_sub = self.result.split()
        else:
            self.add_sub = self.string.split()
        
        res = float(self.add_sub[0])
        
        for i in range(1, len(self.add_sub)-1):
            if self.add_sub[i] == '+':
                res += float(self.add_sub[i+1])
            if self.add_sub[i] == '-':
                res -= float(self.add_sub[i+1])
                
        if arg is not None:
            return res
        else:
            self.result = res
        
    
    
    # The main calculation procedure
    def calculation(self):
         
        #in case of brackets in input expression performs the long way
        if self.string.count('(') > 0:
            self.brackets_split()
            res, temp = [], []
            chars = '/*+-'
            for i in range(len(self.bracket)):
                if len(self.bracket[i]) > 1 and self.bracket[i][0] not in chars and self.bracket[i][-1] not in chars:
                    exp = self.exponent(arg=self.bracket[i])
                    m_d = self.mult_and_div(arg=exp)
                    a_s = self.add_and_subs(arg=m_d)
                    res.append(str(a_s))
                else:
                    res.append(self.bracket[i]) 
            print('calc brackets {}'.format(res))
            
            #perform exponentiation of expression under the breakets        
            for i in range(len(res)):
                if res[i][:2] == '**' and len(res[i]) > 3:              
                    temp.pop()
                    unit = res[i-1] + ' ' + res[i]
                    exp = self.exponent(arg=unit)
                    m_d = self.mult_and_div(arg=exp)
                    a_s = self.add_and_subs(arg=m_d)
                    temp.append(str(a_s))                
                else:
                    temp.append(res[i])
                    
            res = temp
            #print('exp.done', res)
            temp = []
            
            # computing the 'right side' operations
            for i in range(len(res)):
                if res[i][0] in chars and len(res[i]) > 2:       
                    unit = temp[-1] + ' ' + res[i]
                    temp.pop()
                    exp = self.exponent(arg=unit)
                    m_d = self.mult_and_div(arg=exp)
                    a_s = self.add_and_subs(arg=m_d)
                    temp.append(str(a_s))  
                else:
                    temp.append(res[i])
            
            res = temp
            temp = []
            #print('rigth_done', res)
            
            # computing the 'left side' operations
            for i in reversed(range(len(res))):
                if res[i][-1] in chars and len(res[i]) > 2: 
                    unit = res[i] + ' ' + temp[-1] 
                    temp.pop()
                    exp = self.exponent(arg=unit)
                    m_d = self.mult_and_div(arg=exp)
                    a_s = self.add_and_subs(arg=m_d)
                    temp.append(str(a_s)) 
                else:
                    temp.append(res[i])
            
            temp = temp[::-1]
            res = ' '.join(temp)
            temp = []
            #print('left_done', res)
            
            temp = self.exponent(arg=res)
            temp = self.mult_and_div(arg=temp)
            self.result = self.add_and_subs(arg=temp)
            
            return self.result
         
        #if there are no brackets, only three steps needed
        else:
            if self.string.count('**') > 0:
                self.exponent()
            if self.string.count('*') > 0 or self.string.count('/') > 0:
                self.mult_and_div()
            self.add_and_subs()
            
            return self.result
