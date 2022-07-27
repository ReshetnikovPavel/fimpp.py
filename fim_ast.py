from fim_lexer import Literals


class AST:
    pass


class Compound(AST):
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Print(AST):
    def __init__(self, expr):
        self.expr = expr


class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Number(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Char(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        if token.value[0] == "'" and token.value[-1] == "'":
            self.value = token.value[1:-1]


class Bool(AST):
    def __init__(self, token):
        self.token = token
        self.value = self._convert(token.name)

    @staticmethod
    def _convert(token_name):
        if token_name == Literals.TRUE:
            return True
        elif token_name == Literals.FALSE:
            return False
        else:
            raise NameError(repr(token_name))


class Null(AST):
    def __init__(self, token):
        self.token = token
        self.value = None


class String(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        if token.value[0] in ['"', '”', '“']\
                and token.value[-1] in ['"', '”', '“']:
            self.value = token.value[1:-1]

class NoOp(AST):
    pass


class Class(AST):
    def __init__(self, name, superclass, implementations, body, programmer):
        self.name = name
        self.superclass = superclass
        self.implementations = implementations
        self.body = body
        self.programmer = programmer


class Method(AST):
    def __init__(self, name, return_type, arguments, body):
        self.name = name
        self.return_type = return_type
        self.arguments = arguments
        self.body = body


class Return(AST):
    def __init__(self, expr):
        self.expr = expr


class MethodCall(AST):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class Read(AST):
    def __init__(self, variable):
        self.variable = variable


class Prompt(AST):
    def __init__(self, read_node, expr):
        self.read_node = read_node
        self.expr = expr


class VariableDeclaration(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right