from pathlib import Path
import sys

from stats import word_counter, character_counter, sorted_counter


def get_book_text(file_path: Path) -> str:
    # Explicitly decode as UTF-8 to avoid platform-default encoding issues (e.g., cp1252 on Windows).
    with file_path.open("r", encoding="utf-8") as f:
        return f.read()


def print_report(book_path: Path, num_words: int, sorted_character_count: dict[str, int]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path.as_posix()}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character, count in sorted_character_count.items():
        print(f"{character}: {count}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = Path(f"{sys.argv[1]}")
    book_text = get_book_text(book_path)

    num_words = word_counter(book_text)
    char_counts = character_counter(book_text)
    sorted_char_counts = sorted_counter(char_counts)

    print_report(book_path, num_words, sorted_char_counts)


if __name__ == "__main__":
    main()
