# code_generator/generator.py

from groq import Groq


class CodeGenerator:
    def __init__(
            self,
            model: str = "llama-3.3-70b-versatile",
            temperature: float = 0.5,
            max_tokens: int = 1024,
            top_p: float = 1.0
    ):
        """
        Initialize the code generator with the desired model and parameters.
        """
        self.client = Groq()
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p

    def generate_code(self, suggestion: str) -> str:
        """
        Generate code using the Groq API based on the suggestion prompt.

        Args:
            suggestion (str): A string prompt (e.g., "add two numbers").

        Returns:
            str: The generated code.
        """
        messages = [
            {
                "role": "system",
                "content": "you are a helpful assistant. helping you to generate code.  and generate code if any comment or text always put in # . never generate excess text or ``` and ``` "
            },
            {
                "role": "user",
                "content": suggestion
            }
        ]

        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=self.temperature,
            max_completion_tokens=self.max_tokens,
            top_p=self.top_p,
            stop=None,
            stream=False,
        )

        # Retrieve the generated code from the response.
        code = chat_completion.choices[0].message.content
        return code

    def write_code_to_file(self, suggestion: str, filename: str) -> None:
        """
        Generate code based on the suggestion and write it to a file.

        Args:
            suggestion (str): The code suggestion prompt.
            filename (str): Path to the output file.
        """
        code = self.generate_code(suggestion)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
