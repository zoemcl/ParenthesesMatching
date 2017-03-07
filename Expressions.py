from Stack import Stack

def isBalanced(expression):
    s = Stack()
    i = 0
    while i < len(expression):
        elem = expression[i]
        if elem == "(":
            s.push(elem)
        elif elem == ")":
            if s.isEmpty():
                return False
            else:
                if s.pop() != "(":
                    return False
        i += 1
        
    if s.isEmpty():
        return True
    else:
        return False
    
print "Input arithmetic expression you wish to check to see if parentheses are balanced. Ex: (1+2)"

expression = raw_input("> ")

if isBalanced(expression) == True:
    print "The expression is balanced"
else:
    print "The expression is not balanced"
                
            
   
            
    