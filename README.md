
# 📦 AIFileCompressor

An experimental **AI-powered file compression and decompression tool** using a Transformer-based model.  
Trains a neural network to reconstruct the original file from a compressed representation, while ensuring **lossless recovery**.  
Built with Python, PyTorch, and PyQt6 for a user-friendly interface.

---

## 🚀 Features
✅ Compress any file into `.aip`  
✅ Store original extension in the file header  
✅ Prevent overwriting by appending `-1`, `-2`, … if needed  
✅ Decompress `.aip` back to original file with correct extension  
✅ PyQt6 GUI with drag-and-browse, logs, and clear feedback  
✅ Transformer-based placeholder AI model that trains on the fly  

---

## 📁 Installation

### 1️⃣ Clone or Download
Download the zipped project or clone:
```bash
git clone <your-repo-url>
cd AIFileCompressor
```

Or just extract the provided `.zip` file.

---

### 2️⃣ Install dependencies
We recommend a virtualenv:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Dependencies:
- PyTorch
- PyQt6
- numpy
- transformers

---

## 🖥️ Usage

### Run the GUI
```bash
python gui.py
```

### Compression
- Switch to the **Compress** tab.
- Select a file (any type) using the *Browse* button or type path manually.
- Click **Compress**.
- Output file: `<file>.aip` in the same folder (or `<file>-1.aip`, etc. if already exists).

### Decompression
- Switch to the **Decompress** tab.
- Select a `.aip` file.
- Click **Decompress**.
- Output file: `<file>.<original_extension>` in the same folder (or `<file>-1.ext`, etc. if already exists).

---

## 📂 Example

| Original File   | Compressed File  | Decompressed File  |
|-----------------|------------------|--------------------|
| `image.png`     | `image.aip`      | `image.png`        |
| `p.exe`         | `p.aip`          | `p.exe`            |
| `image.aip` + existing `image.png` | `image.aip`        | `image-1.png` |

---

## ⚙️ Project Structure
```
AIFileCompressor/
├── gui.py
├── compressor.py
├── decompressor.py
├── trainer.py
├── ai_model.py
├── utils.py
├── requirements.txt
├── models/
```

---

## 💡 Notes
- This is a proof of concept and uses a placeholder Transformer model. The AI does not yet achieve true compression ratios comparable to traditional methods.
- Training is done on-the-fly per file. Future versions can implement pre-trained models and smarter codecs.
- Works on CPU but can be extended to use GPU for faster training.

---

## 📈 Roadmap (suggestions)
- Add drag-and-drop support.
- Add progress bar and estimated time.
- Improve compression ratio with entropy coding.
- Persist trained models for reuse.
- Implement true AI-based lossless coding schemes.

---

### 👨‍💻 Author
Built by [Barak] — feel free to extend & contribute!
