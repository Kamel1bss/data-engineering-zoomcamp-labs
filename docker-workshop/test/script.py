from pathlib import Path
import chardet

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        raw_bytes = filepath.read_bytes()  # read as bytes
        result = chardet.detect(raw_bytes)
        encoding = result['encoding'] or 'utf-8'
        content = raw_bytes.decode(encoding, errors='replace')
        print(f"    Content: {content}")