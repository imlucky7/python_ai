"""
chatgpt_client.py
A simple wrapper to interact with OpenAI ChatGPT models.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

class ChatGPTClient:
    def __init__(self, model: str = "gpt-4o-mini"): # was gpt-5-nano
        """
        Initialize the ChatGPT client.

        :param api_key: Your OpenAI API key
        :param model: Default model (e.g., 'gpt-4o', 'gpt-4o-mini', 'gpt-3.5-turbo')
        """
        # Load environment variables from .env (if exists)
        # .env file must be saved in the same directory as this script
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model  

    def ask(self, prompt: str, system_prompt: str = "You are a helpful assistant.") -> str | None:
        """
        Send a prompt to ChatGPT and get a response.

        :param prompt: User's question or instruction
        :param system_prompt: System instruction (default = helpful assistant)
        :return: Model's response text
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def stream(self, prompt: str, system_prompt: str = "You are a helpful assistant."):
        """
        Stream ChatGPT responses (prints tokens as they generate).

        :param prompt: User's question or instruction
        :param system_prompt: System instruction
        """
        with self.client.chat.completions.stream(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        ) as stream:
            for event in stream:
                if event.type == "content.delta":
                # print incremental text as it arrives
                    print(event.delta, end="", flush=True)
                elif event.type == "content.done":
                    print("\n--- Stream complete ---")
