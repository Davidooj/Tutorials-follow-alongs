import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r"https")

matched = pattern.finditer(urls)

print(matched)

# This was apart of a tutorial on freecodecamp when I was doing Scientific Computing with Python course.