from fim_lexer import Literals


class AST:
    pass


class Root(AST):
    def __init__(self, children):
        self.children = children


class Compound(AST):
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Print(AST):
    def __init__(self, expr):
        self.expr = expr


class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f"Var({self.token})"


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
        self.value = self._convert(token.type)

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
    def __init__(self, name, superclass, implementations, body, methods, fields, programmer):
        self.name = name
        self.superclass = superclass
        self.implementations = implementations
        self.body = body
        self.methods = methods
        self.fields = fields
        self.programmer = programmer


class Interface(AST):
    def __init__(self, name, methods, programmer):
        self.name = name
        self.methods = methods
        self.programmer = programmer

    def __str__(self):
        raise Exception("Cannot print interface")


class Get(AST):
    def __init__(self, object, name, has_parameters):
        self.object = object
        self.name = name
        self.has_parameters = has_parameters


class Set(AST):
    def __init__(self, object, name, value):
        self.object = object
        self.name = name
        self.value = value


class Function(AST):
    def __init__(self, name, return_type, params, body, is_main):
        self.token = name
        self.name = name
        self.return_type = return_type
        self.params = params
        self.body = body
        self.is_main = is_main


class Return(AST):
    def __init__(self, value):
        self.value = value


class FunctionCall(AST):
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


class Increment(AST):
    def __init__(self, variable):
        self.variable = variable


class Decrement(AST):
    def __init__(self, variable):
        self.variable = variable


class If(AST):
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class Switch(AST):
    def __init__(self, variable, cases, default):
        self.variable = variable
        self.cases = cases
        self.default = default


class While(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class DoWhile(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
