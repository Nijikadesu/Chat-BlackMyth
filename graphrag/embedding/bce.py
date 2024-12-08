import json
import requests
from .base import BaseEmb
from typing import List, Dict, Any, Optional

class BCEEmb(BaseEmb):
    def __init__(self, model_name: str, url: str, **kwargs):
        super().__init__(model_name=model_name, path=url, **kwargs)
        self.url=url

    def get_emb(self, text: str) -> List[float]:
        headers = {'Content-Type': 'application/json'}
        data = {"text": text}
        response = requests.post(url=self.url, headers=headers, data=json.dumps(data))
        embedding = response.json()['embedding'][0]
        return embedding
