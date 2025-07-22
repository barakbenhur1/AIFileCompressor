import torch
import torch.nn as nn
import torch.optim as optim
from ai_model import TransformerDecompressor

def train_model(compressed, original, epochs=50):
    model = TransformerDecompressor()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    src = torch.tensor(compressed).unsqueeze(1).float()
    tgt = torch.tensor(original).unsqueeze(1).float()

    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(src, tgt)
        loss = criterion(output, tgt)
        loss.backward()
        optimizer.step()
        if loss.item() < 1e-5:
            break
    return model, loss.item()
