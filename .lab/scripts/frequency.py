import sys
from collections import defaultdict

if len(sys.argv) < 3:
    print('Usage: python frequency.py <filename> <number_of_letters>')
    sys.exit(1)

filename = sys.argv[1]
number = 0
file = None

try:
    number = int(sys.argv[2])
except:
    print('Please enter a number for <number_of_letters>')
    sys.exit(1)

try:
    file = open(filename, 'r')
except:
    print(f'File "{filename}" not found')
    sys.exit(1)

content = file.read()
content = content.replace(' ', '').replace('\n', '')

frequencies = defaultdict(int)

if number < 2:
    for letter in content:
        frequencies[letter] += 1
else:
    for index in range(len(content)):
        if index + (number - 1) < len(content):
            key = content[index]
            for sub in range(number - 1, 0, -1):
                key += content[index + (number - sub)]
            frequencies[key] += 1

for letter in sorted(frequencies, key=frequencies.get, reverse=True):
    print(letter, frequencies[letter])
