from app.models.base_model import BaseAPIModel

class OpenAIMessage(BaseAPIModel):
    """
    The OpenAIMessage model represents a message structure that is used for interaction with the OpenAI API.

    This model mainly captures the role and content of a message, which are essential for generating responses using the OpenAI chat models.
    The `OpenAIMessage` class inherits from the `BaseAPIModel`, which provides utility methods for converting tuples to model instances.
    """
    
    role: str
    """
    The role associated with the message. Typically, it is either "system" or "user".
    - "system": Provides instructions or context to guide the AI's responses.
    - "user": Represents a user's input or query to which the AI should respond.
    """
    
    content: str
    """
    The actual content or body of the message.
    For a role of "system", this might contain instructions or context.
    For a role of "user", it contains the query or input that we want the AI to respond to.
    """