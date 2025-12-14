# Magic File Type Analyzer 🔍

A simple Python-based file type analyzer that detects the **real file type**
using **magic numbers** instead of file extensions.

## 🚀 Features
- Detects documents, images, executables, archives
- Supports common **audio formats** (MP3, WAV, FLAC, OGG, AAC)
- Identifies file masquerading attempts
- CLI-based tool (Kali/Linux friendly)

## 📦 Supported File Types
- PDF
- PNG, JPEG, GIF
- ZIP
- EXE, ELF
- MP3, WAV, FLAC, OGG, AAC

## 🛠 Usage
```bash
python analyzer.py <file>
python analyzer.py suspicious.pdf
🔐 Cybersecurity Use Cases

Malware analysis

Digital forensics

SOC triage

CTF challenges

Author

Vatsal Shrivastava


Save and exit.

---

### 📄 `.gitignore`
```bash
nano .gitignore


__pycache__/
*.pyc
*.log
.env
