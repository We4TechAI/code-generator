### Code Generator


![Banner](banner.png)

A Python package to generate code from natural language suggestions using the Groq API. This package lets you quickly create code files from descriptive prompts, making it ideal for rapid prototyping and AI-assisted development.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Importing as a Module](#importing-as-a-module)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Development & Testing](#development--testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Easy Code Generation:** Generate code based on natural language prompts.
- **File Output:** Write the generated code directly to a specified file.
- **CLI and API Support:** Use via a command-line interface or import as a Python module.
- **Configurable:** Customize model parameters like temperature, token limits, and more.

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

3. **Install the Package in Editable Mode:**

   ```bash
   pip install -e .
   ```

   *Note: This package depends on the `groq` library. Ensure that it is available via pip or install it separately if necessary.*

## Usage

### Command-Line Interface (CLI)

After installation, a console script named `code-generator` is available. You can generate code from a natural language prompt and write it to a file as follows:

```bash
code-generator "add two numbers" add.py
```

This command will:
- Generate code based on the prompt `"add two numbers"`.
- Write the generated code into `add.py`.

### Importing as a Module

You can also use the package directly within your Python code:

```python
from code_generator import CodeGenerator

# Initialize the code generator
generator = CodeGenerator()

# Generate code for a given prompt
generated_code = generator.generate_code("add two numbers")
print("Generated Code:\n", generated_code)

# Write the generated code to a file
generator.write_code_to_file("add two numbers", "add.py")
```

## Project Structure

```
code_generator/
├── code_generator
│   ├── __init__.py         # Exposes the CodeGenerator class.
│   ├── cli.py              # Command-line interface for code generation.
│   └── generator.py        # Contains the CodeGenerator class.
├── banner.png              # Project banner image (displayed in the README).
├── setup.py                # Setup script for package installation.
└── README.md               # This file.
```

## Configuration

You can configure the code generation process by modifying the parameters in `code_generator/generator.py`. Key parameters include:
- `model`: The model name (default: `"llama-3.3-70b-versatile"`).
- `temperature`: Controls randomness (default: `0.5`).
- `max_tokens`: Maximum number of tokens for the generated code (default: `1024`).
- `top_p`: Controls diversity via nucleus sampling (default: `1.0`).

## Development & Testing

1. **Set Up a Virtual Environment (Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install in Editable Mode:**

   ```bash
   pip install -e .
   ```

3. **Run the CLI Module Directly (for testing):**

   ```bash
   python3 -m code_generator.cli "add two numbers" add.py
   ```

4. **Run Your Custom Test Scripts:**

   Create scripts or use your preferred test framework (e.g., `pytest`) to test the functionality of the package.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request describing your changes.

Please ensure your code adheres to the project's style guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding!
```

