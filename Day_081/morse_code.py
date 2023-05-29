morse_dict = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

user_input = input("Please enter a text to transform it into morse code:\n").lower()
morse_code = ''
for letter in user_input:
    if letter != ' ':
        morse_code += morse_dict[letter]
    else:
        morse_code += ' '
print(morse_code)
