import argparse
from .core import zip, unzip

def main():
    parser = argparse.ArgumentParser(description="NinjaZipPy - 7z Zipper/Unzipper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Zip command
    zip_parser = subparsers.add_parser("zip", help="Compress files/folders into .7z")
    zip_parser.add_argument("src", help="Source file or folder to compress")
    zip_parser.add_argument("dest", help="Destination .7z archive")

    # Unzip command
    unzip_parser = subparsers.add_parser("unzip", help="Extract .7z archive")
    unzip_parser.add_argument("archive", help="Archive file (.7z)")
    unzip_parser.add_argument("dest", help="Destination folder")

    args = parser.parse_args()

    if args.command == "zip":
        zip(args.src, args.dest)
        print(f"Compressed {args.src} → {args.dest}")
    elif args.command == "unzip":
        unzip(args.archive, args.dest)
        print(f"Extracted {args.archive} → {args.dest}")

if __name__ == "__main__":
    main()
