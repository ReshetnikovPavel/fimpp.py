import sys
import traceback
from colorama import Fore, Style
from pathlib import Path
import special_words

from fim_lexer import Lexer
from fim_parser import Parser
from fim_interpreter import Interpreter
from fim_resolver import Resolver
from fim_exception import FimException


def handle_errors(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except FimException as e:
            print(f'{Fore.RED}{type(e).__name__}:'
                  f' {str(e)}{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'{Fore.RED}Program interrupted by user{Style.RESET_ALL}')
        except RecursionError:
            print(f'{Fore.RED}Recursion error{Style.RESET_ALL}')
        except Exception as e:
            traceback.print_exc()
            print(f'{Fore.RED}Oops! There is some bug in the interpreter!:'
                  f' {str(e)}{Style.RESET_ALL}')

    return wrapper


@handle_errors
def interpret(program):
    lexer = Lexer(program)
    lexer.lex()
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    tree = parser.parse()
    resolver = Resolver(interpreter)
    resolver.resolve(tree)
    interpreter.interpret(tree)


def interpret_file(absolute_path):
    if not absolute_path.is_file():
        print(f'{Fore.RED}File not found{Style.RESET_ALL}')
        return

    if absolute_path.suffix != special_words.extension:
        print(f'{Fore.RED}File extension must be {special_words.extension}'
              f'{Style.RESET_ALL}')
        return

    with absolute_path.open('r') as program_file:
        program = program_file.read()
        interpret(program)


def interpret_from_command_line():
    path = ' '.join(sys.argv[1:])
    interpret_file(Path(path).absolute())


interpret("""
I learned how to do stuff to get a number result.
    Then you get 1!
That's all about how to do stuff.
""")


if __name__ == '__main__':
    # cmd cannot handle unicode characters such as ‘ and ’
    interpret_from_command_line()