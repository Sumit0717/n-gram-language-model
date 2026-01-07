import re
import random
from collections import defaultdict

def load_and_clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    text = re.sub(r'\*\*\*.*?\*\*\*', '', text, flags=re.DOTALL)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def tokenize(text):
    return text.split()


def build_ngram_model(tokens, n=5):
    model = defaultdict(list)

    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i:i + n - 1])
        next_word = tokens[i + n - 1]
        model[context].append(next_word)

    return model


def generate_text(model, seed_text, length=50):
    words = seed_text.lower().split()

    if len(words) < 4:
        raise ValueError("Seed text must have at least 4 words")

    for _ in range(length):
        context = tuple(words[-4:])

        if context not in model:
            context = random.choice(list(model.keys()))
            words.extend(list(context))
            continue

        next_word = random.choice(model[context])
        words.append(next_word)

    return ' '.join(words)


def main():
    file_path = "poe.txt" 
    cleaned_text = load_and_clean_text(file_path)
    tokens = tokenize(cleaned_text)

    ngram_model = build_ngram_model(tokens, n=5)

    samples = [
        "in the middle of",
        "i felt a sense",
        "there was a strange"
    ]


    print("\nGENERATED TEXT (EDGAR ALLAN POE STYLE) \n")

    for sample in samples:
        print(f"Sample Text: {sample}")
        output = generate_text(ngram_model, sample, length=40)
        print(f"Generated Text:\n{output}\n")


if __name__ == "__main__":
    main()
