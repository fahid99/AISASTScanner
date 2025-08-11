import ast
from config import *

class InsecurityDetector(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Call(self, node):
        func_name = self.get_full_construct_name(node.func)
        module_name = func_name.split(".")[0] if "." in func_name else ""
        if func_name in INSECURE_FUNCTIONS:
            self.issues.append({
                "type": "Insecure Function Use",
                "function": func_name,
                "lineno": node.lineno,
                "col_offset": node.col_offset,
                "recommendation": f"Do not use {func_name} or replace it with a safer alternative."
            })
        if module_name in INSECURE_MODULES:
            self.issues.append({
                "type": "Insecure Module Use",
                "function": module_name,
                "lineno": node.lineno,
                "col_offset": node.col_offset,
                "recommendation": f"Do not use {module_name} or replace it with a safer alternative."
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

