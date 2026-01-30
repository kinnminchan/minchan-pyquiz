## +1. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

arr = [2, 3, 5, 7, 11]
i = int(input())
total = 0
n = 0

while i < 5:
    j = 0
    while j <= n:
        if (arr[i] + j) % 2 == 0:
            total += arr[i] - j
        j += 1
    i += 1
    n += 1

print(total)

## +2. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

nums = [1, 2, 3, 4, 5]
total = 0
i = 0

while i < 5:
    j = 0
    while j <= i:
        total += nums[i] * j
        j += 1
    i += 1

print(total)

## +3. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [3, 6, 9, 12, 15]
i = int(input())
total = 0
step = 1

while i < 5:
    if nums[i] % 3 == 0:
        total += (nums[i] + step) // 2
    i += 2
    step += 1

print(total)

## +4. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

nums = [2, 4, 6, 8]
i = int(input())
total = 0
count = 1

while i < 4:
    j = 0
    while j < count:
        if j % 2 == 0:
            total += nums[j] * (i + 1)
        j += 1
    i += 1
    count += 1

print(total)

## +5. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

arr = [2, 4, 6, 8, 10]
i = int(input())
total = 0

for idx in range(i, 5):
    if arr[idx] % 2 == 0:
        total += arr[idx] * (idx - i + 1)

print(total)

## +6. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

nums = [1, 3, 5, 7, 9]
i = int(input())
total = 1

for idx in range(i, 5):
    if nums[idx] % 2 != 0:
        total *= nums[idx] + idx

print(total)

## +7. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'을 입력했을 때 출력되는 값은?

arr = [2, 3, 5, 7, 11]
i = int(input())
total = 0
step = 0

while i < 5:
    total += arr[i] + step
    step += i
    i += 1

print(total)

## +8. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '3'을 입력했을 때 출력되는 값은?

nums = [1, 2, 3, 4, 5]
i = int(input())
total = 0

for idx in range(0, i+1):
    total += nums[idx] * (i - idx + 1)

print(total)

## +9. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

arr = [2, 4, 6, 8, 10]
i = int(input())
total = 0

for idx in range(i, 5, 2):
    total += arr[idx] * 2 - idx

print(total)

## +10. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '3'를 입력했을 때 출력되는 값은?

nums = [1, 2, 3, 4, 5]
i = int(input())
total = 0
step = 1

for idx in range(0, i+2):
    if idx % 2 == 0:
        total += nums[idx] * step
        step += 1

print(total)