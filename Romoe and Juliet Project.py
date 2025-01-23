from romeo_and_juliet import PLAY

def get_words(text):
    words = text.split()  # Split the text into words
    return words


def words_frequency(text):
    words = get_words(text)
    word_count = {}

    for word in words:  # Iterate over each word
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    return word_count


def top_n_words(freq, n):
    word_items = freq.items()
    sorted_words = sorted(word_items, key=lambda x: x[1], reverse=True)
    print(f"Top {n} words:")
    for word, count in sorted_words[:n]:  # Take the top N words
        print(f"{word}: {count}")





def main():
    text = PLAY
    freq = words_frequency(text)
    top_n_words(freq, 50)


if __name__ == "__main__":
    main()