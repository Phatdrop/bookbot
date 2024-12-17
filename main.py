def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words = file_contents.split()
        print(len(number_of_words))


def count_characters(text):
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    char_list = [{"char": char, "num": count} for char, count in char_freq.items()]

    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)
    print(char_list)


count_characters("books/frankenstein.txt")
