# put your python code here
from string import ascii_lowercase
base = dict(zip(list(ascii_lowercase), list(ascii_lowercase)))
additive = dict(zip(list(ascii_lowercase), list(ascii_lowercase)))
double_alphabet = {key: value + additive[key] for key, value in base.items() if key in additive}
