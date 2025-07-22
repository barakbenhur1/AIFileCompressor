from utils import *
from trainer import train_model
import torch
from pathlib import Path

def compress(file_path):
    file_path = Path(file_path)
    original_bytes = file_path.read_bytes()
    compressed_bytes = compress_initial(file_path)

    model, loss = train_model(compressed_bytes, original_bytes)

    model_path = Path('models/trained_model.pt')
    model_path.parent.mkdir(exist_ok=True)
    torch.save(model.state_dict(), model_path)
    model_bytes = model_path.read_bytes()

    header = {
        'magic': 'AICOMPRESS',
        'original_extension': file_path.suffix,
        'loss': loss
    }

    output_path = get_nonexistent_aip_path(file_path)
    save_compressed_file(output_path, header, compressed_bytes, model_bytes)

    print(f"✅ Compressed to: {output_path}")
    return output_path
