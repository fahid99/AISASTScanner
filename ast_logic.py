import ast
from config import *

class InsecurityDetector(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Call(self, node):
        func_name = self.get_full_construct_name(node.func)
        module_name = self.get_full_construct_name(node.func)
        print(ast.dump(node, indent=4))
        if func_name in INSECURE_FUNCTIONS:
            self.issues.append({
                "function": func_name,
                "lineno": node.lineno,
                "col_offset": node.col_offset,
            })
        if module_name in INSECURE_MODULES:
            self.issues.append({
                "function": module_name,
                "lineno": node.lineno,
                "col_offset": node.col_offset,
            })
        self.generic_visit(node)

    def get_full_construct_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            parts = []
            while isinstance(node, ast.Attribute):
                parts.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name):
                parts.append(node.id)
            return ".".join(reversed(parts))
        return ""

def ast_scan(code: str):
    tree = ast.parse(code)
    detector = InsecurityDetector()
    detector.visit(tree)
    return detector.issues

print_ast = ast_scan(code)
print(print_ast)