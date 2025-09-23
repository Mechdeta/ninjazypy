import subprocess
import os
from pathlib import Path

class BitArchiveWriter:

    def __init__(self):
        pass

    def compress_to(self, output_archive: str, items: list[str]):
        cmd = ["7z", "a", output_archive] + items
        subprocess.run(cmd, check=True)
        print(f"Compressed {items} → {output_archive}")

class BitArchiveReader:

    def __init__(self):
        pass

    def extract_to(self, archive: str, output_dir: str):
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        cmd = ["7z", "x", archive, f"-o{output_dir}", "-y"]
        subprocess.run(cmd, check=True)
        print(f"Extracted {archive} → {output_dir}")

# Simple helper functions for CLI
def zip(input_path: str, output_archive: str):
    writer = BitArchiveWriter()
    # Support both file and folder
    if os.path.isdir(input_path):
        items = [input_path + "/*"]
    else:
        items = [input_path]
    writer.compress_to(output_archive, items)

def unzip(input_archive: str, output_folder: str):
    reader = BitArchiveReader()
    reader.extract_to(input_archive, output_folder)
