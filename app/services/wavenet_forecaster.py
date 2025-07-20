import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

class WaveNetBlock(nn.Module):
    def __init__(self, in_channels, out_channels, dilation):
        super().__init__()
        self.conv = nn.Conv1d(in_channels, out_channels, kernel_size=2, dilation=dilation, padding=dilation)
        self.relu = nn.ReLU()
    def forward(self, x):
        return self.relu(self.conv(x))

class WaveNetForecast(nn.Module):
    def __init__(self, in_channels=1, residual_channels=16, dilations=[1,2,4,8]):
        super().__init__()
        self.blocks = nn.ModuleList([
            WaveNetBlock(residual_channels, residual_channels, d) for d in dilations
        ])
        self.final = nn.Conv1d(residual_channels, 1, kernel_size=1)

    def forward(self, x):
        for block in self.blocks:
            x = block(x) + x
        return self.final(x)