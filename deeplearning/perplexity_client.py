"""
perplexity_client.py
A simple wrapper for calling Perplexity AI LLMs
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

class PerplexityClient:
    def __init__(self, model: str = "sonar"):
        """
        Initialize the Perplexity client.

        :param api_key: Your Perplexity API key
        :param model: Default model (e.g., 'sonar-medium-online', 'sonar-small-chat', 'sonar-pro')
        """
        # Load environment variables from .env (if exists)
        # .env file must be saved in the same directory as this script
        load_dotenv()
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.perplexity.ai")
        self.model = model

    def ask(self, prompt: str, system_prompt: str = "You are a helpful assistant.") -> str | None:
        """
        Send a prompt to the Perplexity LLM and get a response.

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
