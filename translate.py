import ply.lex as lex
import ply.yacc as yacc
import sys

from syntax_tree.factories.operator_factory import OperatorFactory
from syntax_tree.nodes.node_list import NodeList
from syntax_tree.nodes.if_statement import If
from syntax_tree.nodes.while_statement import While
from syntax_tree.nodes.return_statement import Return
from syntax_tree.nodes.method_argument import MethodArgument
from syntax_tree.nodes.method import Method
from syntax_tree.nodes.else_if import ElseIf
from syntax_tree.nodes.method_call import MethodCall

tokens = [

    'INT',
    'FLOAT',
    'STRING',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'NEWLINE',
    'PARENTHESES_OPEN',
    'PARENTHESES_CLOSE',
    'IF',
    'END',
    'ELSE',
    'DOUBLE_EQUALS',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_OR_EQUAL',
    'GREATER_OR_EQUAL',
    'ELSIF',
    'WHILE',
    'DO',
    'DEF',
    'COMMA',
    'RETURN'
]

# Use regular expressions to define what each token is
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_PARENTHESES_OPEN = r'\('
t_PARENTHESES_CLOSE = r'\)'
t_DOUBLE_EQUALS = r'\=\='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_OR_EQUAL = r'<\='
t_GREATER_OR_EQUAL = r'>\='
t_COMMA = r'\,'

t_ignore = r' '

def t_IF(t):
    r'if'
    return t

def t_END(t):
    r'end'
    return t

def t_ELSE(t):
    r'else'
    return t
    
def t_ELSIF(t):
    r'elsif'
    return t

def t_WHILE(t):
    r'while'
    return t
    
def t_DO(t):
    r'do'
    return t

def t_DEF(t):
    r'def'
    return t
    
def t_RETURN(t):
    r'return'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_STRING(t):
    r'".*?"'
    t.value = str(t.value[1 : -1])
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal character: \"%s\" at line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)
    
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value) # number of \n
    return t

lexer = lex.lex()

# Ensure our parser understands the correct order of operations.
# The precedence variable is a special Ply variable.
precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')

)

def p_program(p):
    '''
    program : statement_list
    '''
    p[0] = p[1]

def p_statement_list(p):
    '''
    statement_list : statement empty statement_list
                   | statement NEWLINE statement_list
                   | NEWLINE
                   | empty
    '''
    if len(p) > 2:
        statement_list = p[3]
        statement_list.children.insert(0, p[1])
        p[0] = statement_list
    else:
        p[0] = NodeList([])
        

def p_method(p):
    '''
    statement : DEF NAME PARENTHESES_OPEN argument_list PARENTHESES_CLOSE NEWLINE statement_list END
    '''
    p[0] = Method(p[2], p[4], p[7])

def p_method_no_parenthesis(p):
    '''
    statement : DEF NAME NEWLINE statement_list END
    '''
    p[0] = Method(p[2], [], p[4])

def p_method_call_no_parenthesis(p):
    '''
    method_call : NAME calling_argument_list
    '''
    p[0] = MethodCall(p[1], p[2])
    
def p_method_call_with_parenthesis(p):
    '''
    method_call : NAME PARENTHESES_OPEN PARENTHESES_CLOSE
                | NAME PARENTHESES_OPEN calling_argument_list PARENTHESES_CLOSE
    '''
    if len(p) > 4:
        p[0] = MethodCall(p[1], p[3])
    else:
        p[0] = MethodCall(p[1], [])

def p_calling_argument_list(p):
    '''
    calling_argument_list : expression COMMA calling_argument_list
                  | expression
    '''
    if len(p) > 2:
        p[0] = [p[1]] + p[3]
    elif p[1] == None:
        p[0] = []
    else:
        p[0] = [p[1]]

def p_argument_list(p):
    '''
    argument_list : argument COMMA argument_list
                  | argument
                  | empty
    '''
    if len(p) > 2:
        argument_list = p[3]
        argument_list.children.insert(0, p[1])
        p[0] = argument_list
    elif p[1] == None:
        p[0] = NodeList([])
    else:
        p[0] = NodeList([p[1]])

def p_argument(p):
    '''
    argument : identifier EQUALS factor
             | identifier
    '''
    if len(p) > 2:
        p[0] = MethodArgument(p[1], p[3])
    else:
        p[0] = MethodArgument(p[1], None)

def p_if_statement(p):
    '''
    statement : IF expression NEWLINE statement_list elsif_list empty empty END
              | IF expression NEWLINE statement_list elsif_list ELSE statement_list END
    '''
    p[0] = If(p[2], p[4], p[5], p[7])
    

def p_elsif_list(p):
    '''
    elsif_list : elsif elsif_list
               | empty
    '''
    if len(p) > 2:
        elsif_list = p[2]
        elsif_list.children.insert(0, p[1])
        p[0] = elsif_list
    else:
        p[0] = NodeList([])

def p_elsif(p):
    '''
    elsif : ELSIF expression NEWLINE statement_list
    '''
    p[0] = ElseIf(p[2], p[4])
    
def p_while_statement(p):
    '''
    statement : WHILE expression DO NEWLINE statement_list END
    '''
    p[0] = While(p[2], p[5])

def p_statement(p):
    '''
    statement : assignment
              | expression
    '''
    p[0] = p[1]

def p_return_statement(p):
    '''
    statement : RETURN expression
    '''
    p[0] = Return(p[2])

def p_assignment(p):
    '''
    assignment : identifier EQUALS expression
    '''
    p[0] = OperatorFactory.get(p[2], p[1], p[3])

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''

    p[0] = OperatorFactory.get(p[2], p[1], p[3])

def p_expression_brackets(p):
    '''
    expression : PARENTHESES_OPEN expression PARENTHESES_CLOSE
    '''
    p[0] = p[2]

def p_expression_compare(p):
    '''
    expression : expression DOUBLE_EQUALS expression
               | expression LESS_THAN expression
               | expression GREATER_THAN expression
               | expression LESS_OR_EQUAL expression
               | expression GREATER_OR_EQUAL expression
    '''
    p[0] = OperatorFactory.get(p[2], p[1], p[3])

def p_expression_method_call(p):
    '''
    expression : method_call
    '''
    p[0] = p[1]

def p_expression_factor(p):
    '''
    expression : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : INT
           | FLOAT
           | STRING
           | identifier
    '''
    p[0] = p[1]

def p_identifier(p):
    '''
    identifier : NAME
    '''
    p[0] = p[1]

# Output to the user that there is an error in the input as it doesn't conform to our grammar.
# p_error is another special Ply function.
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

def p_error(p):
    print("Syntax error")
    if p:
        print("unexpected token \"%s\"" % p.value)
        print("at line %d, column %d" % (p.lineno, p.lexpos))
    else:
        print("unexpected EOF")
    exit(0)

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# Build the parser
parser = yacc.yacc()
    
def translate(file_path):
    file = open(file_path, "r")
    text = file.read()
    parsed = parser.parse(text)
    print(parsed)

if __name__ == "__main__":
    translate(sys.argv[1])