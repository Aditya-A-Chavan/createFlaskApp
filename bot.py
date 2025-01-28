import argparse
from createFlaskAppBackend.main import test
import os

def main():
    parser = argparse.ArgumentParser(description="A bot that renames files in a directory based on their content.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output (show filenames during renaming)")

    args = parser.parse_args()
    current_directory = os.getcwd()

    if args.verbose:
        print("Verbose mode is enabled.")

    test()

if __name__ == "__main__":
    main()
