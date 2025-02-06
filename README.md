# Code Generator & Analyzer

![Banner](banner.png)

A Python package to generate and analyze code using the Groq API. This package lets you quickly create code files from descriptive prompts and analyze existing Python code for metrics and best practices, making it ideal for rapid prototyping and AI-assisted development.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Importing as a Module](#importing-as-a-module)
- [Code Analysis](#code-analysis)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Development & Testing](#development--testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Easy Code Generation:** Generate code based on natural language prompts
- **Code Analysis:** Analyze Python code for metrics, complexity, and best practices
- **Detailed Reports:** Generate markdown reports with code analysis insights
- **File Management:** Write generated code and analysis reports to specified files
- **CLI and API Support:** Use via command-line interface or import as a Python module
- **Configurable:** Customize model parameters like temperature, token limits, and more

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/code_generator.git
   cd code_generator
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Package:**

   ```bash
   pip install .
   ```

4. **Add to PATH:**
   
   Add the following line to your ~/.bashrc file:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```
   Then either start a new terminal or run:
   ```bash
   source ~/.bashrc
   ```

## Usage

### Command-Line Interface (CLI)

After installation, you can use the `code-generator` command in two ways:

1. **Generate Code:**
   ```bash
   code-generator generate "add two numbers" add.py
   ```
   This will:
   - Generate code based on the prompt "add two numbers"
   - Write the generated code into add.py

2. **Analyze Code:**
   ```bash
   code-generator analyze existing_code.py
   ```
   This will:
   - Analyze the Python file for various metrics
   - Generate a detailed report in existingcodereadme.md

### Importing as a Module

You can use the package directly within your Python code:

```python
# For code generation
from code_generator import CodeGenerator

generator = CodeGenerator()
generated_code = generator.generate_code("add two numbers")
generator.write_code_to_file("add two numbers", "add.py")

# For code analysis
from code_generator import CodeAnalyzer

analyzer = CodeAnalyzer()
metrics = analyzer.analyze_file("existing_code.py")
analyzer.generate_readme("existing_code.py", metrics)
```

## Code Analysis

The analyzer provides comprehensive code metrics including:

- Lines of code
- Function and class count
- Import analysis
- Cyclomatic complexity
- Guidelines compliance
- Recommendations for improvement

Analysis reports include:
- Code structure overview
- Detailed function and class listings
- Import dependencies
- Complexity metrics
- Best practices compliance
- Improvement suggestions

## Project Structure

```
code_generator/
├── code_generator
│   ├── __init__.py         # Package initialization
│   ├── cli.py              # Command-line interface
│   ├── generator.py        # Code generation functionality
│   └── analyzer.py         # Code analysis functionality
├── banner.png              # Project banner image
├── setup.py                # Package installation script
└── README.md              # Documentation
```

## Configuration

### Generator Configuration
You can configure the code generation process by modifying the parameters in `CodeGenerator`:
- `model`: Model name (default: "llama-3.3-70b-versatile")
- `temperature`: Controls randomness (default: 0.5)
- `max_tokens`: Maximum token limit (default: 1024)
- `top_p`: Controls diversity (default: 1.0)

### Analyzer Configuration
The analyzer provides default thresholds for:
- Function count (warning at > 10)
- Cyclomatic complexity (warning at > 20)
- Import count (warning at > 15)

## Development & Testing

1. **Set Up Development Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   ```

2. **Test Code Generation:**

   ```bash
   python3 -m code_generator.cli generate "add two numbers" add.py
   ```

3. **Test Code Analysis:**

   ```bash
   python3 -m code_generator.cli analyze existing_code.py
   ```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

Please ensure your code adheres to the project's style guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🚀
