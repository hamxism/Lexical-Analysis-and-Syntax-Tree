# Muhammad Hamza Farooq
# 200901019
import re
import ast 

def L_A(analysis):               #-----------LEXICAL ANALYZER FUNCTION----------#
    
    
    operators_re =r'[=<|>!%^+~/*&-]'#-----------Operators in RE----------#
    no_re =r'[0-9]'#-----------Numbers/Constants in RE----------#
    all_sc_re =r'[%#&^`<$@!>?/*~"|]' #-----------All available characters other than operators and puntuators in RE----------#
    V_re = r'[A-Z]'#-----------Variable in RE----------#
    T_re =r'[a-z]'#------------Terminal or identifier----------#
    punctuators_re =r'[:;(){}\[\].,]'#-----------Puntuators in RE----------#
    code = analysis
    
    
    print("\nTokenization of Expression is as following:")
    
    for i in code:
        if re.match(V_re, i):
            print(f'{i} = Variable')
        elif re.match(operators_re, i):
            print(f'{i} = Operator')
        elif re.match(T_re, i):
            print(f'{i} = Terminal / Identifier')
        elif re.match(all_sc_re, i):
            print(f'{i} = Character')    
        elif re.match(no_re, i):
            print(f'{i} = Constant')
        elif re.match(punctuators_re, i):
            print(f'{i} = Punctuator')       
        else:
            pass
if __name__ == "__main__":
    analysis = input("Input any expression for Tokenization like (2*5)/(4/2) : ")
    L_A(analysis)
    
        
syntaxtree = analysis        #-----------------Generating the tokens in syntax tree----------#
newcode = ast.parse(syntaxtree, mode='eval')     
print(ast.dump(newcode)) 
 
  
