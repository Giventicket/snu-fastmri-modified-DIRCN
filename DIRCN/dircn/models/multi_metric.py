from typing import Dict

import torch


class MultiMetric(torch.nn.Module):

    def __init__(self, metrics: Dict[str, callable]):
        super(MultiMetric, self).__init__()
        self.metrics = metrics

    def __getitem__(self, key):
        return self.metrics[key]

    def to(self, device):
        for key, metric in self.metrics.items():
            self.metrics[key] = metric.to(device=device)
        return self

    def cpu(self):
        for key, metric in self.metrics.items():
            self.metrics[key] = metric.cpu()
        return self

    def items(self):
        return self.metrics.items()
