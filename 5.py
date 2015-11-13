check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = solution(20)
    if solution is None:
        print "No answer found"
    else:
        print solution
