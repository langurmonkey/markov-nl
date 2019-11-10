#!/usr/bin/env python3

import random, re, argparse

def strip_nonalnum_re(word):
    return re.sub(r"\W+|\W+", "", word)

def genchain(text: str) -> {str: [str]}:
    chain = dict()
    for line in filter(bool, text.split('\n')):
        lastword, *wordlist = line.split()
        for word in wordlist:
            word = strip_nonalnum_re(word)
            chain.setdefault(lastword, []).append(word)
            lastword = word
        chain.setdefault(lastword, []).append(None)
    return chain

def usechain(chain: {str: [str]}, length: int) -> str:
    story = []
    for i in range(length):
        word = random.choice(list(chain.keys()))
        j = 0
        while word:
            story.append(word.capitalize() if j == 0 else word)
            word = random.choice(chain[word])
            j = j + 1
        story[-1] = story[-1] + "."
    return ' '.join(story)


if __name__ == '__main__':
    import sys

    parser = argparse.ArgumentParser(description='Markov chain NLP')
    parser.add_argument('file', type=str, help='text file')
    parser.add_argument('-l', '--len', type=int, default=10, help='length in sentences of output')

    args = parser.parse_args()

    with open(args.file, 'r') as f:
        print(usechain(genchain(f.read()), args.len))
