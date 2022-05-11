try: from exe2png import encode, decode
except ImportError: from __init__ import encode, decode
from argparse import ArgumentParser
def main():
    parser = ArgumentParser(description="Encode or decode a file to or from a PNG image.")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("-e", "--encode", action="store_true", help="encode a file to a PNG image")
    action.add_argument("-d", "--decode", action="store_true", help="decode a PNG image to a file")
    parser.add_argument("-c", "--color", action="store_true", help="encode or decode a color image")
    parser.add_argument("-H", "--height", type=int, help="height of the image")
    parser.add_argument("-f", "--file", required=True, help="the file to encode or decode")
    parser.add_argument("-o", "--output", required=True, help="the file to output to")
    args = parser.parse_args()
    if args.encode:
        assert args.height, "height is required"
        encode(args.height, args.file, args.output, args.color)
    elif args.decode:
        decode(args.file, args.output, args.color)
if __name__ == "__main__":
    main()