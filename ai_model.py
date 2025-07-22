import torch.nn as nn

class TransformerDecompressor(nn.Module):
    def __init__(self, input_dim=256, hidden_dim=512):
        super().__init__()
        self.transformer = nn.Transformer(
            d_model=input_dim,
            num_encoder_layers=2,
            num_decoder_layers=2,
            dim_feedforward=hidden_dim
        )
        self.linear = nn.Linear(input_dim, 256)

    def forward(self, src, tgt):
        out = self.transformer(src, tgt)
        return self.linear(out)
