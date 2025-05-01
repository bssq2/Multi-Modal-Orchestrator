import torch
import torch.nn as nn

class AttentionRouter(nn.Module):
    """Simple learned router that chooses among N experts."""
    def __init__(self, num_experts: int = 4, embed_dim: int = 768):
        super().__init__()
        self.linear = nn.Linear(embed_dim, num_experts)

    def forward(self, embeds: torch.Tensor):
        """
        embeds : [B, embed_dim]
        returns idx : [B] · argmax, probs : [B, num_experts]
        """
        logits = self.linear(embeds)
        probs = logits.softmax(dim=-1)
        return probs.argmax(-1), probs