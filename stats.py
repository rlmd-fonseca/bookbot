from collections import Counter

def word_counter(text: str) -> int:
    return len(text.split())

def character_counter(text: str) -> dict[ str, int]:
    character_count = Counter()

    for character in text:
        if character.isalpha():
            character_count[character.casefold()] += 1

    return dict(character_count)

def sorted_counter(counter: dict[str, int]):
    return dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))