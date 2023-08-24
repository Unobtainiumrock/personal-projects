from tiktoken import Tokenizer, tokenizers
from typing import Tuple

class OpenAITokenCounter:
    def __init__(self) -> None:
        self.tokenizer = tokenizers.ByteLevelTokenizer()

    def count_tokens(self, text: str) -> int:
        tokens = self.tokenizer.encode(text)
        return len(tokens.ids)

def tokens_and_text_length(text: str) -> Tuple[int, int]:
    counter = OpenAITokenCounter()
    token_count = counter.count_tokens(text)
    return token_count, len(text)

if __name__ == "__main__":
    sample_text = "This is a sample text for token counting."
    tokens, length = tokens_and_text_length(sample_text)
    print(f"Text Length: {length}")
    print(f"Token Count: {tokens}")
