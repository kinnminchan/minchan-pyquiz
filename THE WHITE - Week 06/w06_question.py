## 01. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + func(nums[1:])

print(func([1, 2, 3]))

## 02. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n < 10:
        return n
    return func(n // 10)

print(func(456))

## 03. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n == 0:
        return 0
    return 1 + func(n // 2)

print(func(8))

## 04. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(arr, i):
    if i == len(arr):
        return 0
    return arr[i] + func(arr, i + 1)

print(func([2, 4, 6], 0))

## 05. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(s):
    if s == "":
        return 0
    return 1 + func(s[1:])

print(func("abc"))

## 06. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums, i):
    if i < 0:
        return 0
    if nums[i] % 2 == 0:
        return nums[i] + func(nums, i - 1)
    return func(nums, i - 1)

print(func([1, 2, 3, 4], 3))

## 07. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n <= 1:
        return 1
    return func(n - 1) + func(n - 2)

print(func(4))

## 08. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], func(nums[1:]))

print(func([3, 1, 5, 2]))

## 09. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(s):
    if len(s) <= 1:
        return s
    return s[-1] + func(s[:-1])

print(func("abcd"))

## 10. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n, k):
    if k == 0:
        return 1
    return n * func(n, k - 1)

print(func(2, 4))

## 11. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums, i):
    if i == len(nums):
        return 1
    if nums[i] == 0:
        return 0
    return nums[i] * func(nums, i + 1)

print(func([2, 3, 0, 4], 0))

## 12. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n < 10:
        return n
    return func(func(n // 10) + n % 10)

print(func(987))

## 13. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(arr, i):
    if i == 0:
        return arr[0]
    return arr[i] - func(arr, i - 1)

print(func([10, 3, 2], 2))

## 14. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(s, i):
    if i == len(s):
        return ""
    if i % 2 == 0:
        return s[i] + func(s, i + 1)
    return func(s, i + 1)

print(func("abcdef", 0))

## 15. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return func(n // 2)
    return func(n - 1) + 1

print(func(7))