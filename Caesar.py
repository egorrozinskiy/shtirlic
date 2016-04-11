__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-



class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode =dict(lowercase_code)
    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])


line = open('shtirlic2.txt', 'r')
s = line.read()
for key in range(1,33):
    cipher = Caesar(key)
    print(cipher.encode(s))
    line = s
    print(key)



key = int(input('Ээъыцмъ фубз:'))
cipher = Caesar(key)
line = open('shtirlic2.txt', 'r')
s = line.read()
while line:
    print(cipher.encode(s))
    line = input()
