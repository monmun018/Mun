#問題
# https://www.codewars.com/kata/54b724efac3d5402db00065e
def decode_word(word):
    result = list(map(lambda t: MORSE_CODE[t],word.split()))
    return ''.join(result)
def decodeMorse(morse_code):
    result = list(map(decode_word,morse_code.split('   ')))
    return ' '.join(result).strip()