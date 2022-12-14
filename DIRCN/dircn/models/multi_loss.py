from typing import List, Tuple

import torch

class MultiLoss(torch.nn.Module):

    def __init__(self, losses: List[Tuple[float, callable]]):
        super(MultiLoss, self).__init__()
        self.losses = losses

    def to(self, device):
        for i, (weight, loss_func) in enumerate(self.losses):
            self.losses[i] = (weight, loss_func.to(device=device))
        return self

    def cpu(self):
        for i, (weight, loss_func) in enumerate(self.losses):
            self.losses[i] = (weight, loss_func.cpu())
        return self

    def forward(self, x, y):
        loss = 0
        for (weight, loss_func) in self.losses:
            loss += weight*loss_func(x, y)

        return loss


