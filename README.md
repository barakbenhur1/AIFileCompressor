# AIFileCompressor

A PyQt5 desktop app for per‑file lossless compression by training and updating a shared ML model.

## Features

- **Compress** any file into `${name}.aic`  
- **Decompress** a `.aic` back to the original file  
- **Shared model** (`model/shared_model.pt`) is pulled/pushed to GitHub  
- Drag‑and‑drop inputs + real‑time logs  

## Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/barakbenhur1/AIFileCompressor.git
   cd AIFileCompressor
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate.bat  # Windows cmd
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure GitHub PAT**  
   ```bash
   export GITHUB_TOKEN=<your_personal_access_token>      # macOS/Linux
   set GITHUB_TOKEN=<your_personal_access_token>         # Windows cmd
   $env:GITHUB_TOKEN="<your_personal_access_token>"      # PowerShell
   ```

5. **Run the app**  
   ```bash
   python scripts/gui.py
   ```

## Project Layout

```
AIFileCompressor/
├── scripts/
│   ├── git_utils.py
│   ├── compressor.py
│   └── gui.py
├── model/                  # may start empty
├── venv/                   # virtual environment
├── requirements.txt
├── README.md
├── .gitignore
```

## Example & Test Cases

- **Text file**  
  - Compress: `test.txt` → `test.aic`  
  - Decompress: `test.aic` → `test.txt`  

- **Image file**  
  - Compress: `test.gif` → `test.aic`  
  - Decompress: `test.aic` → `test.gif`  

Verify that the decompressed content matches the original exactly.
