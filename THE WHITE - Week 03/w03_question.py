## 01. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

x = 2
y = 4
print(x * y + 1)

## 02. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

arr = [5, 10, 15]
print(arr[1] + arr[2])

## 03. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '4'를 입력했을 때, 출력되는 값은?

n = int(input())
print(n + 6)

## 04. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [3, 6, 9, 12]
i = 0

while i < 3:
    i += 1

print(nums[i])

## 05. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '5'를 입력했을 때 출력되는 값은?

x = int(input())
i = 0
result = 0

while i < x:
    result += 2
    i += 1

print(result)

## 06. 다음은 파이썬으로 작성된 코드이다. 실행 결과가 15일 때, 빈칸에 들어가야 할 값은?

total = 0
i = 1

while i <= ____:
    total += i
    i += 1

print(total)

## 07. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

arr = [1, 3, 5, 7]
i = 0

while arr[i] < 5:
    i += 1

print(i)

## 08. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '3'을 입력했을 때 출력되는 값은?

n = int(input())
i = 1
result = 1

while i <= n:
    result *= 2
    i += 1

print(result)

## 09. 다음은 파이썬으로 작성된 코드이다. 실행 결과가 '12'일 때, 빈칸에 들어가야 할 값은?

nums = [4, 8, 12, 16]
i = 0
total = 0

while i < ____:
    total += nums[i]
    i += 1

print(total)

## 10. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'를 입력했을 때 출력되는 값은?

a = [1, 2, 3]
b = [10, 20, 30, 40]

i = int(input())
x = a[i]

print(b[x])

## 11. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

i = 10
cnt = 0

while i > 0:
    cnt += 1
    i -= 3

print(cnt)

## 12. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때, '9'가 출력되도록 하기 위해 빈칸에 들어갈 값은?

nums = [3, 6, 9]
i = int(input())

print(nums[____])

## 13. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

arr = [2, 4, 6]
i = 0
result = 0

while i < len(arr):
    result += arr[i]
    i += 1

print(result)

## 14. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 4를 입력했을 때 출력되는 값은?

n = int(input())
i = 0

while n > 1:
    n -= 1
    i += 1

print(i)

## 15. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '3'을 입력했을 때, '6'이 출력되도록 하기 위해 빈칸에 들어갈 값은?

i = 0
total = 0

while i < ____:
    i += 1
    total += i

print(total)

## 16. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [2, 4, 6, 8, 10, 12]
i = int(input())
total = 0

while i < 5:
    for j in range(i, 6, 2):
        total += nums[j]
    i += 1
    if total > 20:
        break

print(total)

## 17. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

nums = [1, 3, 5, 7, 9]
i = int(input())
total = 0

while i < 4:
    for j in range(0, i+2):
        total += nums[j]
    i += 1
    if total >= 20:
        break

print(total)

## 18. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [2, 4, 6, 8, 10]
i = int(input())
total = 0

while i < 4:
    total += nums[i]
    for j in range(i):
        total -= 1
    i += 1

print(total)

## 19. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

nums = [1, 2, 3, 4, 5]
i = int(input())
total = 0

while i < 5:
    total += nums[i]
    i += 2
    for j in range(i-1):
        total += 1

print(total)

## 20. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [2, 4, 6, 8, 10]
i = int(input())
total = 0

while i < 5:
    for j in range(i, 5):
        if nums[j] % 4 == 0:
            total += nums[j]
    i += 1

print(total)