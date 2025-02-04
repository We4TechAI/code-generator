# code_generator/cli.py

import argparse
from code_generator.generator import CodeGenerator

def main():
    parser = argparse.ArgumentParser(
        description="Generate code based on a suggestion and write it to a file. remember only to output code  no comments or anything else like explanation or text only code must be generated or else it will not work  ."
    )
    parser.add_argument(
        "suggestion",
        type=str,
        help="The code suggestion prompt (e.g., 'add two numbers')."
    )
    parser.add_argument(
        "output_file",
        type=str,
        help="The file path where the generated code will be saved."
    )

    args = parser.parse_args()

    generator = CodeGenerator()
    try:
        generator.write_code_to_file(args.suggestion, args.output_file)
        print(f"Code successfully written to {args.output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
