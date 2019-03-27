n = int(input())
names = [input() for i in range(n)]
raw_names = [name.lower() for name in names]
first = [name[0] for name in raw_names]
letters = [first.count(letter) for letter in first]
lengths = [len(name) for name in raw_names]
frequency = [(letters[i], ord(first[i]), -1*lengths[i], i) for i in range(n)]
print(names[frequency.index(min(frequency))])