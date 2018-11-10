import text_utility

file_lyrics = 'lyrics.txt'
file_data = 'data.txt'

str_lyrics = text_utility.read(file_lyrics)
print(str_lyrics)

number_of_lines = text_utility.count_by_lines(file_lyrics)
number_of_words = text_utility.count_by_words(file_lyrics)
number_of_chars = text_utility.count_by_chars(file_lyrics)
print('Number of lines: ', number_of_lines)
print('Number of words: ', number_of_words)
print('Number of chars: ', number_of_chars)

text_utility.erase(file_lyrics)

text_utility.write(file_data, str_lyrics)