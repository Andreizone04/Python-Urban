from pprint import pprint
import io


class WordsFinder:
    def __init__(self, *files):
        self.files = list(files)
        self.files_words = {}

    def get_all_words(self):
        all_words = []
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_x in self.files:
            with open(file_x, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    word = ''
                    for char in line:
                        for i in punctuation:
                            if char == i:
                                char = ''
                        if char != ' ' and char != '\n':
                            word += char
                        else:
                            all_words.append(word)
                            # print(word)
                            word = ''
                self.files_words[file_x] = all_words
        return self.files_words

    def find(self, word):
        word_search = word.lower()
        x = {}
        for elem in self.files_words:
            x[elem] = self.files_words[elem].index(word_search) + 1
        return x

    def count(self, word):
        word_search = word.lower()
        x = {}
        for elem in self.files_words:
            x[elem] = self.files_words[elem].count(word_search)
        return x


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
