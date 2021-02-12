# Calculator

    
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
