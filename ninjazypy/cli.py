import sys
from ninjazypy.core import zip, unzip

def main():
    if len(sys.argv) < 4:
        print("Usage: ninjazypy zip/unzip <input> <output>")
        return

    cmd, inp, outp = sys.argv[1:4]

    if cmd.lower() == "zip":
        zip(inp, outp)
    elif cmd.lower() == "unzip":
        unzip(inp, outp)
    else:
        print("Invalid command! Use 'zip' or 'unzip'.")

if __name__ == "__main__":
    main()
