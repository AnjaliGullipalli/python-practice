a='anjali is a good girl'
freq={}
for char in a:
    if char==' ':
        continue
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
most_repeated = max(freq, key=freq.get)
print(freq)
print(most_repeated)
print("count:",freq[most_repeated])