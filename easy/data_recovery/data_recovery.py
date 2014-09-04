__author__ = 'apuhach'
# https://www.codeeval.com/open_challenges/140/
import sys
from collections import Counter

with open(sys.argv[1], 'r') as f:
    for line in f:
        text, hint_str = line.split(';')
        tokens = text.split()
        hints = [int(c) for c in hint_str.split()]
        hint_dict = dict(zip(hints, tokens))
        if len(hints) < len(tokens):
            residual_hint = set(range(1, len(tokens) + 1)) - set(hints)
            residual_token = list((Counter(tokens) - Counter(hint_dict.values())).elements())
            hint_dict[residual_hint.pop()] = residual_token.pop()
        recovered = [hint_dict[k] for k in sorted(hint_dict)]

        print(' '.join(recovered))
