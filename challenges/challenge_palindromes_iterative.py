def is_palindrome_iterative(word):
    if not word:
        return False

    return all(
        word[i] == word[len(word) - 1 - i] for i in range(len(word) // 2)
    )
