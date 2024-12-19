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
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    
    distance = 0
    for i in range(len(list_a)):
        distance += abs(list_a[i] - list_b[i])
    
    print(distance)
