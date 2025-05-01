import torch
import torch.nn.functional as F
from torch.optim import Adam

class PPOTrainer:
    def __init__(self, model, lr=3e-4):
        self.model = model
        self.opt   = Adam(model.parameters(), lr=lr)

    def train_step(self, embeds, target_idx):
        """
        Single, simplified PPO-style step (really CE for demo).
        """
        self.opt.zero_grad()
        _, probs = self.model(embeds)
        loss = F.cross_entropy(probs, target_idx)
        loss.backward()
        self.opt.step()
        return loss.item()