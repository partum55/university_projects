GREEN = "\033[92m{}\033[00m"
YELLOW = "\033[93m{}\033[00m"
GRAY = "\033[90m{}\033[00m"

def check_user_word(user_word: str, word: str, length: int) -> tuple[str, bool]:
    if len(user_word) != length:
        return "Wrong word, please try again", False
    if not user_word.isalpha():
        return "Wrong format, please try again", False
    output_word = ""
    word_letter_count = {letter: word.count(letter) for letter in set(word)}
    used_letters = {letter: 0 for letter in set(word)}
    result = [""] * length

    # First pass: mark green letters
    for i, letter in enumerate(user_word):
        if letter == word[i]:
            result[i] = GREEN.format(letter)
            used_letters[letter] += 1
    for i, letter in enumerate(user_word):
        if letter in word and used_letters[letter] < word_letter_count[letter]:
            result[i] = YELLOW.format(letter)
            used_letters[letter] += 1
        else:
            result[i] = GRAY.format(letter)
    output_word = "".join(result)
    return output_word, True


print(check_user_word("leave", "score", 5)[0])

