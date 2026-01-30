## 01. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

arr = [1, 2, 3]
print(arr[0] + arr[2])

## 02. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [5, 10, 15, 20]
print(nums[1])

## 03. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'를 입력했을 때 출력되는 값은?

arr = [3, 6, 9]
i = int(input())
print(arr[i])

## 04. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

arr = [4, 8, 12]
result = 0

for x in arr:
    result += x

print(result)

## 05. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [2, 4, 6, 8]
i = 0
total = 0

while i < 3:
    total += nums[i]
    i += 1

print(total)

## 06. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

arr = [10, 20, 30]
i = int(input())

print(arr[i] * 2)

## 07. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [1, 3, 5, 7]
i = 0

while nums[i] < 5:
    i += 1

print(nums[i])

## 08. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

arr = [2, 4, 6, 8]
result = 1

for i in range(2):
    result *= arr[i]

print(result)

## 09. 다음은 파이썬으로 작성된 코드이다. 실행 결과가 '9'가 되도록 빈칸에 들어갈 값은?

nums = [1, 3, 5]
total = 0

for i in range(____):
    total += nums[i]

print(total)

## 10. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '3'을 입력했을 때 출력되는 값은?

arr = [5, 10, 15, 20]
i = int(input())

print(arr[i - 1])

## 11. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [1, 2, 3, 4, 5]
i = 0
total = 0

while i < len(nums):
    if nums[i] % 2 == 0:
        total += nums[i]
    i += 1

print(total)

## 12. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

arr = [3, 6, 9, 12]
i = int(input())
total = 0

for j in range(i, len(arr)):
    total += arr[j]

print(total)

## 13. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [2, 5, 8]
result = 0

for i in range(len(nums)):
    result += nums[i] * i

print(result)

## 14. 다음은 파이썬으로 작성된 코드이다. 실행 결과가 '6'이 되도록 빈칸에 들어갈 값은?

arr = [1, 2, 3, 4]
total = 0

for i in range(____):
    total += arr[i]

print(total)

## 15. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'를 입력했을 때 출력되는 값은?

nums = [2, 4, 6, 8]
i = int(input())
total = 0

while i < len(nums):
    total += nums[i]
    i += 2

print(total)

## 16. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [2, 4, 6, 8, 10]
i = int(input())
total = 0

while i < 5:
    total += nums[i]
    i += 2

print(total)

## 17. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

arr = [1, 2, 3, 4, 5]
i = int(input())
total = 0

while i < len(arr):
    total += arr[i] * (i % 2)
    i += 1

print(total)

## 18. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [2, 4, 6, 8]
total = 0

for i in range(len(nums)):
    for j in range(i + 1):
        total += nums[i] // (j + 1)

print(total)

## 19. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [5, 10, 15, 20]
i = int(input())
total = 0

while i < len(nums):
    total += (nums[i] + i) // 5
    i += 2

print(total)

## 20. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

nums = [1, 2, 3, 4]
i = int(input())
total = 0

while i < len(nums):
    for j in range(len(nums) - i):
        total += nums[j] * (j % 2)
    i += 1

print(total)