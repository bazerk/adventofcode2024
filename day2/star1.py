import sys


def check_safe(report) -> bool:
    slope = 0
    prev_val = None
    print(report)
    for val in report:
        if prev_val is None:
            prev_val = val
            continue
        diff = abs(val - prev_val)
        if diff < 1 or diff > 3:
            return False
        test = 1 if val > prev_val else -1
        if slope == 0:
            slope = test
        if slope != test:
            return False
        prev_val = val
    return True
        

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    safe = 0
    for line in lines:
        split = line.split()
        if check_safe([int(val) for val in split]):
            safe += 1
    print(safe)
