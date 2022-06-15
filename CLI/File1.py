import sys
from typing import List, Dict

print(sys.argv)  # current file


# Run program as a module with two command-line arguments
# 1. Name of the file to search
# 2. Search term we are looking for
# Print out all lines containing the search term and total number of matches


def main() -> None:
    """Entry point of program run as module"""
    args: Dict[str, str] = read_args()
    print(args)


def read_args() -> Dict[str, str]:
    """Check for valid CLI args and return in dict"""
    if len(sys.argv) != 3:
        print("Usage: File1 [file] [keyword]")
        exit()
    return {
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]
    }


if __name__ == '__main__':
    main()
