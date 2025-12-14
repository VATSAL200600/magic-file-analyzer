import sys

def analyze_file_type(file_path):
    magic_numbers = {
        # Documents & Archives
        b'\x25\x50\x44\x46': 'PDF document',
        b'\x50\x4B\x03\x04': 'ZIP archive',

        # Images
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'PNG image',
        b'\xFF\xD8\xFF': 'JPEG image',
        b'\x47\x49\x46\x38': 'GIF image',

        # Executables
        b'\x4D\x5A': 'Windows EXE',
        b'\x7F\x45\x4C\x46': 'ELF executable',

        # Audio Files
        b'\x49\x44\x33': 'MP3 audio (ID3)',
        b'\xFF\xFB': 'MP3 audio',
        b'\x52\x49\x46\x46': 'WAV audio',
        b'\x66\x4C\x61\x43': 'FLAC audio',
        b'\x4F\x67\x67\x53': 'OGG audio',
        b'\xFF\xF1': 'AAC audio'
    }

    try:
        with open(file_path, 'rb') as f:
            header = f.read(16)

        for magic, ftype in magic_numbers.items():
            if header.startswith(magic):
                print(f"[+] File Type Detected: {ftype}")
                return

        print("[-] Unknown file type")

    except FileNotFoundError:
        print("[-] File not found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <file>")
    else:
        analyze_file_type(sys.argv[1])
