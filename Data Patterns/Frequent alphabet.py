line = input("Enter a line: ")

freq = {}

for ch in line:

    if ch.isalpha():

        freq[ch] = freq.get(ch, 0) + 1

max_freq = max(freq.values())

result = []

for ch in freq:

    if freq[ch] == max_freq:
        result.append(ch)

result.sort(key=lambda x: (x.islower(), x))

print("Highest Frequency Letters:")

for ch in result:
    print(ch, end=" ")