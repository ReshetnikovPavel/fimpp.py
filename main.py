from fim_lexer import Lexer
from fim_parser import Parser
from fim_interpreter import Interpreter

lexer = Lexer("""
2 plus 2
""")
lexer.lex()
parser = Parser(lexer)
interpreter = Interpreter(parser)
interpreter.interpret()
print(interpreter.GLOBAL_SCOPE)
