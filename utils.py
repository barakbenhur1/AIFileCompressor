from pathlib import Path
import gzip
import pickle

def compress_initial(file_path):
    with open(file_path, 'rb') as f_in:
        return gzip.compress(f_in.read())

def decompress_initial(data):
    return gzip.decompress(data)

def save_compressed_file(output_path, header, compressed_data, model_bytes):
    with open(output_path, 'wb') as f_out:
        pickle.dump({
            'header': header,
            'data': compressed_data,
            'model': model_bytes
        }, f_out)

def load_compressed_file(input_path):
    with open(input_path, 'rb') as f_in:
        return pickle.load(f_in)

def get_nonexistent_aip_path(input_path):
    path = Path(input_path)
    candidate = path.parent / f"{path.stem}.aip"
    counter = 1
    while candidate.exists():
        candidate = path.parent / f"{path.stem}-{counter}.aip"
        counter += 1
    return candidate

def get_nonexistent_original_path(base_path, original_ext):
    path = Path(base_path)
    candidate = path.parent / f"{path.stem}{original_ext}"
    counter = 1
    while candidate.exists():
        candidate = path.parent / f"{path.stem}-{counter}{original_ext}"
        counter += 1
    return candidate
