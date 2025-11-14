from collections import Counter
import re

def n_common_words(text, n=1):
    words = re.findall(r"\w+", text)
    count = Counter(words)

    if n < 1:
        n = 1
    elif n > len(words):
        n = len(words)

    return count.most_common(n)

text = """
The morning sun peeked over the rooftops, warming the quiet street.
A gentle breeze swept through, carrying the scent of fresh bread from a nearby bakery.
People began to stir, stepping outside with sleepy eyes and hopeful thoughts.
Somewhere in the distance, a dog barked, breaking the soft rhythm of dawn.
It felt like the start of a day that held endless small possibilities.
"""

print(n_common_words(text,100))


