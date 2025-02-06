# code_generator/cli.py

import argparse
import os
from code_generator.generator import CodeGenerator
from code_generator.analyzer import CodeAnalyzer


def main():
    parser = argparse.ArgumentParser(
        description="Generate or analyze Python code."
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Generate command
    generate_parser = subparsers.add_parser('generate', help='Generate code from suggestion')
    generate_parser.add_argument(
        "suggestion",
        type=str,
        help="The code suggestion prompt (e.g., 'add two numbers')."
    )
    generate_parser.add_argument(
        "output_file",
        type=str,
        help="The file path where the generated code will be saved."
    )

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze existing Python code')
    analyze_parser.add_argument(
        "input_file",
        type=str,
        help="The Python file to analyze."
    )

    args = parser.parse_args()

    try:
        if args.command == 'generate':
            generator = CodeGenerator()
            generator.write_code_to_file(args.suggestion, args.output_file)
            print(f"Code successfully written to {args.output_file}")

        elif args.command == 'analyze':
            analyzer = CodeAnalyzer()

            # Analyze the code
            metrics = analyzer.analyze_file(args.input_file)

            # Generate readme filename
            base_name = os.path.splitext(args.input_file)[0]
            readme_file = f"{base_name}readme.md"

            # Generate and write the readme
            readme_content = analyzer.generate_readme(args.input_file, metrics)
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(readme_content)

            print(f"Analysis complete! Results written to {readme_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()