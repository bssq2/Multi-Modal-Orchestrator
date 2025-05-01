import torch
from src.orchestrator.attention_router import AttentionRouter
from src.models.text_model   import GPT4Model
from src.models.image_model  import CLIPModel
from src.models.speech_model import WhisperModel
from src.models.video_model  import SoraModel

class MultiModalOrchestrator:
    def __init__(self):
        self.text   = GPT4Model()
        self.image  = CLIPModel()
        self.speech = WhisperModel()
        self.video  = SoraModel()
        self.router = AttentionRouter()

    def _embed(self, _):
        # Mock embedding (replace with real model or pipeline)
        return torch.randn(1, 768)

    def process_request(self, data, mode="text"):
        # We ignore the router’s actual output for demonstration.
        _ = self.router(self._embed(data))  # could do something with these
        # Dispatch to the correct model based on 'mode'
        return {
            "text":   self.text.infer,
            "image":  self.image.infer,
            "speech": self.speech.infer,
            "video":  self.video.infer
        }.get(mode, self.text.infer)(data)