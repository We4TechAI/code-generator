# code_generator/analyzer.py

import ast
import os
from typing import Dict, List, Any


class CodeAnalyzer:
    def __init__(self):
        """Initialize the code analyzer."""
        self.metrics: Dict[str, Any] = {
            "lines_of_code": 0,
            "functions": [],
            "classes": [],
            "imports": [],
            "complexity": 0
        }

    def analyze_file(self, filename: str) -> Dict[str, Any]:
        """
        Analyze a Python file and return metrics.

        Args:
            filename (str): Path to the Python file to analyze

        Returns:
            Dict[str, Any]: Analysis metrics
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reset metrics for new analysis
        self.metrics = {
            "lines_of_code": len(content.splitlines()),
            "functions": [],
            "classes": [],
            "imports": [],
            "complexity": 0
        }

        try:
            tree = ast.parse(content)
            self._analyze_ast(tree)
        except SyntaxError as e:
            raise ValueError(f"Invalid Python syntax in {filename}: {str(e)}")

        return self.metrics

    def _analyze_ast(self, tree: ast.AST) -> None:
        """Analyze the AST to gather metrics."""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                self.metrics["functions"].append({
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "line_number": node.lineno
                })
                self.metrics["complexity"] += self._calculate_complexity(node)

            elif isinstance(node, ast.ClassDef):
                self.metrics["classes"].append({
                    "name": node.name,
                    "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)],
                    "line_number": node.lineno
                })

            elif isinstance(node, ast.Import):
                self.metrics["imports"].extend(n.name for n in node.names)
            elif isinstance(node, ast.ImportFrom):
                self.metrics["imports"].append(f"{node.module}.{node.names[0].name}")

    def _calculate_complexity(self, node: ast.AST) -> int:
        """Calculate cyclomatic complexity of a function."""
        complexity = 1  # Base complexity
        for n in ast.walk(node):
            if isinstance(n, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
        return complexity

    def generate_readme(self, filename: str, metrics: Dict[str, Any]) -> str:
        """
        Generate a README markdown file with the analysis results.

        Args:
            filename (str): Name of the analyzed file
            metrics (Dict[str, Any]): Analysis metrics

        Returns:
            str: Markdown formatted analysis
        """
        readme_content = f"""# Code Analysis for {os.path.basename(filename)}

## Overview
- Total lines of code: {metrics['lines_of_code']}
- Cyclomatic complexity: {metrics['complexity']}

## Structure
### Functions ({len(metrics['functions'])})
{self._format_functions(metrics['functions'])}

### Classes ({len(metrics['classes'])})
{self._format_classes(metrics['classes'])}

### Imports ({len(metrics['imports'])})
{self._format_imports(metrics['imports'])}

## Guidelines Compliance
- Function count: {'✅' if len(metrics['functions']) < 10 else '⚠️'} ({len(metrics['functions'])} functions)
- Complexity: {'✅' if metrics['complexity'] < 20 else '⚠️'} (Score: {metrics['complexity']})
- Import count: {'✅' if len(metrics['imports']) < 15 else '⚠️'} ({len(metrics['imports'])} imports)

## Recommendations
{self._generate_recommendations(metrics)}
"""
        return readme_content

    def _format_functions(self, functions: List[Dict[str, Any]]) -> str:
        if not functions:
            return "No functions found.\n"

        result = ""
        for func in functions:
            args_str = ", ".join(func["args"])
            result += f"- `{func['name']}({args_str})` (line {func['line_number']})\n"
        return result

    def _format_classes(self, classes: List[Dict[str, Any]]) -> str:
        if not classes:
            return "No classes found.\n"

        result = ""
        for cls in classes:
            result += f"- `{cls['name']}` (line {cls['line_number']})\n"
            if cls["methods"]:
                for method in cls["methods"]:
                    result += f"  - `{method}`\n"
        return result

    def _format_imports(self, imports: List[str]) -> str:
        if not imports:
            return "No imports found.\n"

        return "\n".join(f"- `{imp}`" for imp in sorted(imports))

    def _generate_recommendations(self, metrics: Dict[str, Any]) -> str:
        recommendations = []

        if metrics["complexity"] > 20:
            recommendations.append("- Consider breaking down complex functions to improve maintainability")

        if len(metrics["functions"]) > 10:
            recommendations.append("- Consider splitting the file into multiple modules")

        if len(metrics["imports"]) > 15:
            recommendations.append("- Consider reorganizing imports or splitting functionality")

        if not recommendations:
            recommendations.append("- Code structure appears to follow good practices")

        return "\n".join(recommendations)