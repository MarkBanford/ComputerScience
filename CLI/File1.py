import sys
from typing import List, Dict


# Run program as a module with two command-line arguments
# 1. Name of the file to search
# 2. Search term we are looking for
# Print out all lines containing the search term and total number of matches


def main() -> None:
    """Entry point of program run as module"""
    args: Dict[str, str] = read_args()
    results: List[str] = search_file(args["file_path"], args["keyword"])
    print(len(results))


def read_args() -> Dict[str, str]:
    """Check for valid CLI args and return in dict"""
    if len(sys.argv) != 3:
        print("Usage: File1 [file] [keyword]")
        exit()
    return {
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]
    }


def search_file(file_path: str, keyword: str) -> List[str]:
    """Open file_path reads each line and returns a list of lines"""
    matches: List[str] = []
    file_handle = open(file_path, "r", encoding="utf8")
    for line in file_handle:
        if keyword in line:
            matches.append(line)

    file_handle.close()

    return matches


if __name__ == '__main__':
    main()
