import itertools as it

def all_variants(text):
    return it.chain.from_iterable(it.combinations(text, r) for r in range(1, len(text) + 1))


a = all_variants("abc")
for i in a:
    print(i)