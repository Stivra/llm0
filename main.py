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


def file_get_tokens(filename, pattern=r'(\s)'):
    # Print the contents of the file:
    with open(filename, "r") as f:
        ft = f.read()
        tokens = re.split(pattern, ft)
        return tokens


class TokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: word for word, i in vocab.items()}

    def encode(self, text):
        text = re.split(r'([,.?_!"()\']|--|\s)', text)
        text = [item.strip() for item in text if item.strip()]
        return [self.str_to_int[word] if word in self.str_to_int else -1 for word in text ]

    def decode(self, encoded_text):
        text = " ".join(self.int_to_str[i] for i in encoded_text)


if __name__ == "__main__":
    file_url = ("https://raw.githubusercontent.com/rasbt/"
                "LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt")
    target_file_location = "data/short_story.txt"
    download_file(file_url, target_file_location)
    print_file_stats(target_file_location)

    tokens = file_get_tokens(target_file_location, r'(\s)')
    print("File: ", target_file_location, " Tokens Count: ", len(tokens), " Words: ", tokens[0:10])

    tokens = file_get_tokens(target_file_location, r'([,.]|\s)')
    print("File: ", target_file_location, " Tokens Count: ", len(tokens), " Words: ", tokens[0:10])

    tokens = [item.strip() for item in tokens if item.strip()]
    print("File: ", target_file_location, " Tokens Count: ", len(tokens), " Words: ", tokens[0:10])

    tokens = file_get_tokens(target_file_location, r'([,.:;?_!"()\']|--|\s)')
    tokens = [item.strip() for item in tokens if item.strip()]
    print("File: ", target_file_location, " Tokens Count: ", len(tokens), " Words: ", tokens[0:10])

    # Vocabulary
    vocabulary = sorted(set(tokens))
    print("Vocabulary: ", len(vocabulary))

    # Enumerate the vocabulary
    word_to_index = {word: i for i, word in enumerate(vocabulary)}
    # print("Word to Index: ", word_to_index)

    # Tokenize the text
    tokenizer = TokenizerV1(word_to_index)
    encoded_text = tokenizer.encode("The verdict was a surprise to everyone.")
    print("Encoded Text: ", encoded_text)
