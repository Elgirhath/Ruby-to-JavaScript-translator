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
from syntax_tree.factories.method_call_factory import MethodCallFactory
from syntax_tree.nodes.list import List
from syntax_tree.nodes.list_access_operator import ListAccessOperator
from syntax_tree.nodes.identifier import Identifier
from syntax_tree.nodes.built_in import BuiltIn
from syntax_tree.nodes.not_operator import Not
from syntax_tree.nodes.parenthesis import Parenthesis

tokens = [

    'INT',
    'FLOAT',
    'BOOLEAN',
    'STRING',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'POWER',
    'MODULO',
    'EQUALS',
    'PLUS_EQUALS',
    'MINUS_EQUALS',
    'NEWLINE',
    'PARENTHESIS_OPEN',
    'PARENTHESIS_CLOSE',
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
    'RETURN',
    'SQUARE_BRACKET_OPEN',
    'SQUARE_BRACKET_CLOSE',
    'METHOD_COMPLEX_NAME',
    'AND',
    'OR',
    'NOT'
]

# Use regular expressions to define what each token is
t_PLUS = r'\+'
t_MINUS = r'\-'
t_PLUS_EQUALS = r'\+\='
t_MINUS_EQUALS = r'\-\='
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\*\*'
t_MODULO = r'%'
t_EQUALS = r'\='
t_PARENTHESIS_OPEN = r'\('
t_PARENTHESIS_CLOSE = r'\)'
t_DOUBLE_EQUALS = r'\=\='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_OR_EQUAL = r'<\='
t_GREATER_OR_EQUAL = r'>\='
t_SQUARE_BRACKET_OPEN = r'\['
t_SQUARE_BRACKET_CLOSE = r'\]'
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
    
def t_BOOLEAN(t):
    r'true|false'
    t.value = bool(t.value)
    return t
    
def t_STRING(t):
    r'".*?"'
    t.value = str(t.value[1 : -1])
    return t

def t_AND(t):
    r'\&\&|and'
    return t
    
def t_OR(t):
    r'\|\||or'
    return t
    
def t_NOT(t):
    r'!|not'
    return t
    
def t_METHOD_COMPLEX_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*(\.[a-zA-Z_][a-zA-Z_0-9]*)+'
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
    statement_list : statement statement_list
    '''

    statement_list = p[2]
    statement_list.children.insert(0, p[1])
    p[0] = statement_list
        

def p_statement_list_whitespace(p):
    '''
    statement_list : NEWLINE statement_list
                   | empty
    '''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = NodeList([])
        

def p_method(p):
    '''
    statement : DEF NAME PARENTHESIS_OPEN argument_list PARENTHESIS_CLOSE NEWLINE statement_list END
    '''
    p[0] = Method(p[2], p[4], p[7])

def p_method_no_parenthesis(p):
    '''
    statement : DEF NAME NEWLINE statement_list END
    '''
    p[0] = Method(p[2], [], p[4])

# we don't handle methods with no parameters and no parenthesis at this stage
# as it is undistinguishable from a single identifier. This will be resolved on another stage
def p_method_call_with_parenthesis(p):
    '''
    method_call : method_name_with_parenthesis PARENTHESIS_CLOSE
                | method_name_with_parenthesis expression_list PARENTHESIS_CLOSE
    '''
    if len(p) > 3:
        p[0] = MethodCallFactory.get(p[1], p[2])
    else:
        p[0] = MethodCallFactory.get(p[1], NodeList([]))

def p_method_call_no_parenthesis(p):
    '''
    method_call : method_name expression_list
    '''
    p[0] = MethodCallFactory.get(p[1], p[2])
    
def p_method_call_no_parenthesis_empty(p):
    '''
    method_call : METHOD_COMPLEX_NAME empty
    '''
    p[0] = MethodCallFactory.get(p[1], NodeList([]))
    
def p_method_name(p):
    '''
    method_name : METHOD_COMPLEX_NAME
    '''
    p[0] = p[1]
    
def p_method_name_identifier(p):
    '''
    method_name : identifier
    '''
    p[0] = p[1].name

def p_method_name_with_parenthesis(p):
    '''
    method_name_with_parenthesis : NAME PARENTHESIS_OPEN
    '''
    p[0] = p[1]

def p_expression_list(p):
    '''
    expression_list : expression COMMA expression_list
                  | expression
    '''
    if len(p) > 2:
        expression_list = p[3]
        expression_list.children.insert(0, p[1])
        p[0] = expression_list
    elif p[1] == None:
        p[0] = None
    else:
        p[0] = NodeList([p[1]])

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
               | identifier PLUS_EQUALS expression
               | identifier MINUS_EQUALS expression
    '''
    p[0] = OperatorFactory.get(p[2], p[1], p[3])

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
               | expression POWER expression
               | expression MODULO expression
               | expression AND expression
               | expression OR expression
    '''

    p[0] = OperatorFactory.get(p[2], p[1], p[3])
    
def p_expression_not(p):
    '''
    expression : NOT expression
    '''

    p[0] = Not(p[2])

def p_expression_brackets(p):
    '''
    expression : PARENTHESIS_OPEN expression PARENTHESIS_CLOSE
    '''
    p[0] = Parenthesis(p[2])

def p_expression_list_definition(p):
    '''
    expression : SQUARE_BRACKET_OPEN expression_list SQUARE_BRACKET_CLOSE
    '''
    p[0] = List(p[2])

def p_expression_compare(p):
    '''
    expression : expression DOUBLE_EQUALS expression
               | expression LESS_THAN expression
               | expression GREATER_THAN expression
               | expression LESS_OR_EQUAL expression
               | expression GREATER_OR_EQUAL expression
    '''
    p[0] = OperatorFactory.get(p[2], p[1], p[3])
    
def p_list_access_operator(p):
    '''
    expression : identifier SQUARE_BRACKET_OPEN expression SQUARE_BRACKET_CLOSE
    '''
    p[0] = ListAccessOperator(p[1], p[3])

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
    factor : built_in
           | identifier
    '''
    p[0] = p[1]

def p_builtin(p):
    '''
    built_in : INT
           | FLOAT
           | STRING
           | BOOLEAN
    '''
    p[0] = BuiltIn(p[1])
    

def p_identifier(p):
    '''
    identifier : NAME
    '''
    p[0] = Identifier(p[1])

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
        print("at line %d" % p.lineno)
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
    
def build_tree(text):
    return parser.parse(text)