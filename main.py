import re
import urllib.request


def download_file(url, filename):
    # Download the file from `url` and save it locally under `filename`:
    urllib.request.urlretrieve(url, filename)


def print_file_stats(filename):
    # Print the contents of the file:
    with open(filename, "r") as f:
        ft = f.read()
        print("=====================================")
        print("File location:", filename, "Chat Count: ", len(ft))
        print("=====================================")


def file_get_tokens(filename):
    # Print the contents of the file:
    with open(filename, "r") as f:
        ft = f.read()
        tokens = re.split(r'\s', ft)
        return tokens


if __name__ == "__main__":

    file_url = ("https://raw.githubusercontent.com/rasbt/"
                "LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt")
    target_file_location = "data/short_story.txt"
    download_file(file_url, target_file_location)
    print_file_stats(target_file_location)

    tokens = file_get_tokens(target_file_location)
    print("File: ", target_file_location, " Tokens: ", len(tokens)), " Words: ", tokens[0:10]

