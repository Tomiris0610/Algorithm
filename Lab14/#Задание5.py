#Задание5
from collections import Counter
import re

text = "hello world hello python world hello code"

words = re.findall(r'\w+', text.lower())
counter = Counter(words)

print(counter.most_common(3))