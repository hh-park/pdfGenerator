# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
def solution1(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break

    return answer

# 전화번호가 문자열 phone_number로 주어졌을 때,
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수
def solution2(ph):
    tmp = '*' * (len(ph)-4) + ph[-4:]
    return tmp

def solution3(x):
    answer = False
    sum = 0
    for i in str(x):
        sum += int(i)

    if x % sum == 0:
        answer = True
    return answer

def solution4_(strings, n):
        answer = []
        tmp = []
        sort = []
        for i in strings:
            tmp.append(list(i))

        for i in range(len(tmp)):
            sort.append(tmp[i][n]+strings[i])

        sort.sort()
        for i in sort:
            answer.append(i[1:])

        return answer

def solution4(strings, n):
    def sortkey(x):
        return x[n]
    # strings.sort(key=sortkey)
    return sorted(sorted(strings), key=lambda x: x[n])

def solution5(s):
    print(''.join(sorted(s, reverse=True)))
    return ''.join(sorted(s, reverse=True))

def solution6_(num):
    answer = 0
    while True:
        if num == 1:
            break

        if answer == 500:
            break
        if num % 2 == 0:
            num = num / 2
            print(num)
            answer += 1
            print(answer)

        if num % 2 != 0:
            num = (num * 3) + 1
            answer += 1

    return answer

def solution6(num):
    for i in range(1, 501):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i

    return -1

def solution7(n):
    return 1

if __name__ == "__main__":

    # solution1(2, 5)
    # solution2('01033334444')
    # solution3(10)
    # solution4(['sun','bed','car'], 1)
    # solution5('Zbcdefg')
    # solution6(6)
    solution7()