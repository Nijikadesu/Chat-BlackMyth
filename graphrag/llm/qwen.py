import json
import requests
from typing import Any, Optional
from .base import BaseLLM
from typing import Dict, List

class Qwen2_5(BaseLLM):
    """Implementation of the BaseLLM interface using InternLM."""

    def __init__(
        self,
        model_name: str,
        url: str,
        model_params: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        super().__init__(model_name, model_params, **kwargs)
        self.url = url


    def predict(self, input: str) -> str:
        headers = {'Content-Type': 'application/json'}
        data = {"prompt": input}
        response = requests.post(url=self.url, headers=headers, data=json.dumps(data))
        response = response.json()['response']
        return response
