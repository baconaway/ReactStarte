import openai
from typing import List, Union
from app.models.openai_message import OpenAIMessage
from fastapi import HTTPException


class BaseTextGenerator:
    """
    A base class for text generation using OpenAI.

    This class offers utility methods for text generation with OpenAI models, 
    handling both singular and batch requests.
    """
    DEFAULT_MODEL = "gpt-3.5-turbo-16k"
    DEFAULT_MAX_TOKENS = 600
    DEFAULT_TEMPERATURE = 0.5

    def __init__(self):
        """
        Initializes the BaseTextGenerator class.

        Configures the OpenAI API key using the provided settings.
        """
        openai.api_key = "YOUR_OPENAI"

    async def generate_text_with_openai_async(
        self,
        openai_message: Union[OpenAIMessage, List[OpenAIMessage]],
        model: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE
    ) -> str:
        """
        Asynchronously generates text using the OpenAI API based on the provided messages.

        Args:
        - openai_message (Union[OpenAIMessage, List[OpenAIMessage]]): The message or list of messages to process.
        - model (str, optional): The OpenAI model to use. Defaults to "gpt-3.5-turbo-16k".
        - max_tokens (int, optional): The maximum number of tokens for the generated text. Defaults to 600.
        - temperature (float, optional): The sampling temperature. Defaults to 0.5.

        Returns:
        - str: The generated text from the OpenAI model.

        Raises:
        - HTTPException: If there's an API error or if the OpenAI request is malformed.
        """

        if isinstance(openai_message, OpenAIMessage):
            openai_message = [openai_message]

        dict_openai_message = [message.dict() for message in openai_message]

        try:
            result = await openai.ChatCompletion.acreate(
                model=model,
                messages=dict_openai_message,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            
            return result.choices[0].message.content
        except openai.APIError as ex:
            raise HTTPException(
                status_code=500,
                detail=f"An error occurred on OpenAI during chat completion operation. Exception: {ex}"
            )
        except openai.InvalidRequestError as ex:
            raise HTTPException(
                status_code=500,
                detail=f"The OpenAI request was malformed or missing required parameters. Please check the request. Exception: {ex}"
            )