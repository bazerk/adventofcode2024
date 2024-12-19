from collections import defaultdict
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    list_a = []
    list_b = []
    for line in lines:
        split = line.split()
        list_a.append(int(split[0]))
        list_b.append(int(split[1]))
    
    occurences = defaultdict(int)
    for val in list_b:
        occurences[val] += 1
    
    similarity = 0
    for val in list_a:
        similarity += val * occurences[val]
    
    print(similarity)
