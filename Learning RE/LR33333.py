import re


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ  
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

[54, 19, 16 ,51, 43]

[54+4, 72-65, 3+5]

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r"Start")

match = pattern.findall(sentence)

x = re.search("321", text_to_search)

print(match)








