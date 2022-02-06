#To print letters in a string in decreasing order
def most_frequent(S):
    d = {}
    for key in S:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    d = dict(sorted(d.items(),key=lambda key:key[1],reverse=True))
    print(d)
most_frequent("Mississippi")




