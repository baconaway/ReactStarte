from fastapi import Response
from app.text_generation.base_text_generator import BaseTextGenerator

class AIService: 
    def __init__(self):
        self,
        self.generator = BaseTextGenerator()
        self.DEFAULT_TEMPERATURE = 0.5
        self.DEFAULT_MAX_TOKENS = 600
    
    async def generate_answer(self, question: str):
        answer = await self.generator.generate_text_with_openai_async(            
            openai_message=question,
            temperature=self.DEFAULT_TEMPERATURE,
            max_tokens=self.DEFAULT_MAX_TOKENS
        )

        return Response(
            content=answer,
            message="Successfully generated an answer",
        )