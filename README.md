# 🔍 Magic File Type Analyzer

**Magic File Type Analyzer** is a lightweight Python-based CLI tool that detects the
**actual file type** using **magic numbers**, rather than trusting file extensions.

It is useful for **malware analysis, digital forensics, SOC triage, and CTF challenges**,
where files are often **masqueraded** to hide their true nature.

---

## ✨ Features

- 🔎 Detects real file types using **magic numbers**
- 📁 Supports documents, images, executables, and archives
- 🎵 Detects common **audio formats**
- 🕵️ Identifies **file extension spoofing**
- ⚡ Simple CLI interface (Kali / Linux friendly)

---

## 📦 Supported File Types

- **Documents:** PDF  
- **Images:** PNG, JPEG, GIF  
- **Archives:** ZIP  
- **Executables:** EXE (Windows), ELF (Linux)  
- **Audio:** MP3, WAV, FLAC, OGG, AAC  

---

## 🛠 Usage

### ▶ Basic Usage
    ```bash
    python analyzer.py <file>
▶ Example
    python analyzer.py suspicious.pdf
🔐 Cybersecurity Use Cases

● Malware analysis
● Digital forensics
● SOC triage
● CTF challenges

📂 Project Setup
Clone the Repository

    git clone https://github.com/VATSAL200600/magic-file-analyzer.git
    cd magic-file-analyzer
    
Run the Tool 

    python analyzer.py sample.file
📄 .gitignore

    Create a .gitignore file with the following content:

    __pycache__/
    *.pyc
    *.log
    .env
👤 Author
Vatsal Shrivastava


