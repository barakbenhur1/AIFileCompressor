from utils import *
from ai_model import TransformerDecompressor
import torch
from pathlib import Path

def decompress(input_path):
    content = load_compressed_file(input_path)
    header = content['header']
    compressed_bytes = content['data']
    model_bytes = content['model']

    original_ext = header.get('original_extension', '')

    model_path = Path('models/trained_model.pt')
    model_path.write_bytes(model_bytes)

    model = TransformerDecompressor()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    compressed_tensor = torch.tensor(compressed_bytes).unsqueeze(1).float()
    decompressed = model(compressed_tensor, compressed_tensor).detach().numpy().flatten().astype('uint8')

    input_base = Path(input_path).stem
    output_file = get_nonexistent_original_path(Path(input_path).parent / input_base, original_ext)
    output_file.write_bytes(decompressed)

    print(f"✅ Decompressed to: {output_file}")
    return output_file
