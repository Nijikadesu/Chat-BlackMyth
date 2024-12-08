from zhipuai import ZhipuAI
from typing import Any, Optional, Dict
from .base import BaseLLM


class zhipuLLM(BaseLLM):
    """Implementation of the BaseLLM interface using zhipuai."""

    def __init__(
        self,
        model_name: str,
        api_key: str,
        model_params: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        super().__init__(model_name, model_params, **kwargs)
        self.client = ZhipuAI(api_key=api_key)

    def predict(self, input: str) -> str:
        """Sends a text input to the zhipuai model and retrieves a response.

        Args:
            input (str): Text sent to the zhipuai model

        Returns:
            str: The response from the zhipuai model.
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": input}],
        )
        return response.choices[0].message.content
