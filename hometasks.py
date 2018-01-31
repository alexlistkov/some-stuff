from pprint import pprint
from itertools import  groupby
import collections
from datetime import date
# text = open('romeo.txt').read().replace('.', ',').replace(' ', ',').lower().split(',')
#
# count = 0
# result = {}
# for word in text:
#     if word not in result:
#         result[word] = 1
#     else:
#         result[word] = result[word] + 1
#
# print(result)

#
# def checkio(text):
#     text.lower()
#     result = {}
#     result2 = []
#     for letter in text:
#         if letter == ' ' or letter == '.' or letter == '!' or letter == '?':
#             continue
#         elif letter not in result:
#             result[letter] = 1
#         else:
#             result[letter] = result[letter] + 1
#
#     for key, value in result.items():
#         if value == max(result.values()):
#             result2.append(key)
#
#     return min(result2)
#
# print(checkio('Lorem ipsum dolor sit amet'))

# def checkio(data):
#     if len(data) >= 10:
#         if data.isalpha() or data.isdigit() or data.islower() or data.isupper():
#             return False
#         else:
#             return True
#     else:
#         return False
#
# print(checkio('SSSSSSSSSSSSSSSs1'))

# def count_words(text, words):
#     string = text.lower().replace(' ', '')
#     count = 0
#     print(string)
#     for word in words:
#         if string.find(word) >= 0:
#             count += 1
#
#     return count
#
# print(count_words('How aresjfhdskfhskd you?', {'how', 'are', 'you', 'hello'}))

# def checkio(game_result):
#     if game_result[0] == 'XXX' or game_result[1] == 'XXX' or game_result[2] == 'XXX':
#         return 'X'
#     elif (game_result[0][0] == 'X' and game_result[1][0] == 'X' and game_result[2][0] == 'X') or (
#             game_result[0][1] == 'X' and game_result[1][1] == 'X' and game_result[2][1] == 'X') or (
#             game_result[0][2] == 'X' and game_result[1][2] == 'X' and game_result[2][2] == 'X') or (
#             game_result[0][0] == 'X' and game_result[1][1] == 'X' and game_result[2][2] == 'X') or (
#             game_result[0][2] == 'X' and game_result[1][1] == 'X' and game_result[2][0] == 'X'):
#         return 'X'
#     elif game_result[0] == 'OOO' or game_result[1] == 'OOO' or game_result[2] == 'OOO':
#         return 'O'
#     elif (game_result[0][0] == 'O' and game_result[1][0] == 'O' and game_result[2][0] == 'O') or (
#             game_result[0][1] == 'O' and game_result[1][1] == 'O' and game_result[2][1] == 'O') or (
#             game_result[0][2] == 'O' and game_result[1][2] == 'O' and game_result[2][2] == 'O') or (
#             game_result[0][0] == 'O' and game_result[1][1] == 'O' and game_result[2][2] == 'O') or (
#             game_result[0][2] == 'O' and game_result[1][1] == 'O' and game_result[2][0] == 'O'):
#         return 'O'
#     else:
#         return 'D'
#
#
# print(checkio(["O..","XXX","XXO"]))
# print(checkio(["XXO","XXO","XOX"]))
# print(checkio(["O.O","OOX","OXO"]))
# print(checkio(["XOX","X.O","OOO"]))
# print(checkio(["OX.","OXX",".O."]))

# def checkio(data):
#     result = []
#     for el in data:
#         if data.count(el) > 1:
#             result.append(el)
#     return result

# def correct_sentence(text: str) -> str:
#     """
#         returns a corrected sentence which starts with a capital letter
#         and ends with a dot.
#     """
#     text = text.capitalize()
#     if not text.endswith('.'):
#         text = text + '.'
#     return text
#
# print(correct_sentence("greetings, friends"))
# def second_index(text: str, symbol: str):
#     """
#         returns the second index of a symbol in a given text
#     """
#     index = text.index(symbol, text.index(symbol) + 1)
#     return index
#
# print(second_index("sims", "s"))
# def between_markers(text: str, begin: str, end: str) -> str:
#     if not text.index(begin) + len(begin):
#         return text[:text.index(end)]
#     elif not text.index(end):
#         return text[text.index(begin) + len(begin):]
#     elif not text.index(begin) + len(begin) and text.index(end):
#         return text[:]
#     else:
#         return text[text.index(begin) + len(begin):text.index(end)]
# def between_markers(text: str, begin: str, end: str) -> str:
#     if text.find(begin) == -1 and text.find(end) == -1:
#         return text[:]
#     elif text.find(begin) == -1:
#         return text[:text.find(end)]
#     elif text.find(end) == -1:
#         return text[text.find(begin) + len(begin):]
#     else:
#         return text[text.find(begin) + len(begin):text.find(end)]
#
# print(between_markers('What is >apple<', '>', '<'))
# print(between_markers('No[/b] hi', '[b]', '[/b]'))
# print(between_markers('No hi', '[b]', '[/b]'))
# def best_stock(data):
#     for key in data:
#         if data[key] == max(data.values()):
#             return key
# print(best_stock({
#     'CAC': 10.0,
#     'ATX': 390.2,
#     'WIG': 1.2
# }))

            # def popular_words(text, words):
            #     text = text.lower().replace(',', ' ').replace('.', ' ')
            #
            #     print(popular_words('''
            # When I was One,
            # I had just begun.
            # When I was Two,
            # I was nearly new.
            # ''', ['i', 'was', 'three']))
# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     text = text.replace('.', ' ').replace(',', ' ').split()
#     return text[0]
#
# print(first_word("Hello world"))
# def bigger_price(limit, data):
#     result =[]
#     count = 0
#     for el in sorted(data, key=lambda product: product['price'], reverse=True):
#         result.append(el)
#         count += 1
#         if count == limit:
#             return result
#
# pprint(bigger_price(2, [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ]))
# def checkio(*args):
#     if len(args) == 0:
#         return 0
#     else:
#         return max(args) - min(args)
# def checkio(array):
#     data = array[::2]
#     if len(array) == 0:
#         return 0
#     else:
#         return sum(data) * array[-1]
#
# print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]))
# def find_message(text):
#     msg = ""
#     for letter in text:
#         if letter.isupper():
#             msg += letter
#     return msg
#
# print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
# def popular_words(text, words = None):
#     result = {}
#     text = text.lower().replace(',', ' ').replace('.', ' ')
#     for word in words:
#         if text.count(word) == 0:
#             result[word] = 0
#         else:
#             result[word] = text.count(word)
#     return result
#
# print(popular_words('''
# When I was One,
# I had just begun.
# When I was Two,
# I was nearly new.''', ['i', 'was', 'three']))
# def left_join(phrases):
#     result = ','.join(phrases).replace('right', 'left')
#     return result
#
# print(left_join(("left", "right", "left", "stop")))
# def checkio(number):
#     number = list(filter(lambda x: x != '0', (str(number))))
#     total = 1
#     for i in number:
#         total *= int(i)
#     return total
#
# print(checkio(1000))
# def checkio(words):
#     words = words.split()
#     count = 0
#     print(words)
#     if len(words) >= 3:
#         for word in words:
#             if not word.isdigit():
#                 count += 1
#                 if count == 3:
#                     return True
#             else:
#                 count = 0
#                 continue
#         else:
#             return False
#     else:
#         return False
#
# print(checkio("Hello World hello"))
# print(checkio("He is 123 man"))
# print(checkio("Hi"))
# print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
# def index_power(array, n):
#     try:
#         return array[n] ** n
#     except IndexError:
#         return -1
#
# print(index_power([1, 2, 3, 4], 2))
# def checkio(str_number, radix):
#     try:
#         number = int(str_number, base=radix)
#         return number
#     except ValueError:
#         return -1
# def checkio(numbers_array):
#     result = sorted(list(numbers_array), key=lambda x: abs(x))
#     return result
#
# print(checkio((-20, -5, 10, 15)))
# def most_frequent(data):
#     result = {}
#     for i in data:
#         result[i] = data.count(i)
#     return sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]
#
# print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))
# def min(*args, key = None):
#     if len(args) == 1:
#         result = sorted(args[0], key=key)[0]
#         return result
#     else:
#         result = sorted(args, key=key)[0]
#         return result
#
#
# def max(*args, key = None):
#     if len(args) == 1:
#         result = sorted(args[0], key=key, reverse=True)[0]
#         return result
#     else:
#         result = sorted(args, key=key, reverse=True)[0]
#         return result
#
# print(min([3, 4]))
# print(min(5, 6))
# print(min(6.2, 5.6, 5.3))
# print(min(6.2, 5.6, 5.3, key=int))
# print(min([[1, 2], [3, 4], [9, 0]]))
# print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
# print('______________')
# print(max([3, 4]))
# print(max(5, 6))
# print(max(6.2, 5.3, 5.6))
# print(max(6.2, 5.6, 5.3, key=int))
# print(max([[1, 2], [3, 4], [9, 0]]))
# print(max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
            # def long_repeat(line):
            #     result = []
            #     counter = 1
            #     if len(line) > 0:
            #         for index in range(0, len(line) - 1):
            #             if line[index] == line[index + 1]:
            #                 counter += 1
            #             elif line[index - 2] != line[index - 1]:
            #                 result.append(1)
            #             else:
            #                 result.append(counter)
            #                 counter = 1
            #         return result
            #     else:
            #         return 0
# def long_repeat(line):
#     if len(line) > 0:
#         result = [len(list(group)) for key, group in groupby(line)]
#         return max(result)
#     else:
#         return 0
#
# print(long_repeat('sdsffffse'))
# print(long_repeat("aa"))
# def checkio(data):
#     data = sorted(data)
#     print(data)
#     if len(data) % 2 == 0:
#         result = (data[int(len(data) / 2)] + data[int(len(data) / 2 - 1)]) / 2
#         return result
#     else:
#         result = data[int((len(data) - 1) / 2)]
#         return result
#
# print(checkio([1, 2, 300, 200, 1]))
# print(checkio([3, 6, 20, 99, 10, 15]))
# def days_diff(date1, date2):
#     year1, month1, day1 = date1
#     year2, month2, day2 = date2
#     if date(year1, month1, day1) > date(year2, month2, day2):
#         result = date(year1, month1, day1) - date(year2, month2, day2)
#         return result.days
#     else:
#         result = date(year2, month2, day2) - date(year1, month1, day1)
#         return result.days
#
# print(days_diff((1982, 4, 19), (1982, 4, 22)))
# VOWELS = "AEIOUY"
# CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
#
#
# def checkio(text): TODO
#     count = 0
#     data = []
#     text = text.replace('.', ' ').replace(',', ' ').upper().split()
#     for word in text:
#         for letter in word:
#             if word.index(letter) % 2 != 0:
#                 data.append(letter)
#                 print(data)
#                 data = []
#     return data
#
#
#
#
# print(checkio("Dog,cat,mouse,bird.Human."))
# def recall_password(cipher_grille, ciphered_password):TODO
#     return ""
#
# print(recall_password(
#         ('X...',
#          '..X.',
#          'X..X',
#          '....'),
#         ('itdf',
#          'gdce',
#          'aton',
#          'qrdi')) == 'icantforgetiddqd')

# def checkio(first, second):
#     result = []
#     first = first.split(',')
#     second = second.split(',')
#     for word in first:
#         if word in second:
#             result.append(word)
#     return ','.join(sorted(result))
#
#
# print(checkio("hello,world", "hello,earth"))
# print(checkio("one,two,three", "four,five,six"))
# print(checkio("one,two,three", "four,five,one,two,six,three"))
