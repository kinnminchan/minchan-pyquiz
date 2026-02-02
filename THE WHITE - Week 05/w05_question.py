## 01. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def add(a, b):
    return a + b

print(add(2, 3))

## 02. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def square(x):
    return x * x

print(square(4))

## 03. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 3을 입력했을 때 출력되는 값은?

def double(n):
    return n * 2

x = int(input())
print(double(x))

## 04. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def calc(a, b):
    return a * b + 1

print(calc(2, 4))

## 05. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(x):
    if x > 5:
        return x - 2
    return x + 2

print(func(6))

## 06. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def total(nums):
    s = 0
    for n in nums:
        s += n
    return s

print(total([1, 2, 3]))

## 07. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def count_even(nums):
    cnt = 0
    for n in nums:
        if n % 2 == 0:
            cnt += 1
    return cnt

print(count_even([1, 2, 4, 5]))

## 08. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(a):
    return a[0] + a[-1]

print(func([3, 6, 9]))

## 09. 다음은 파이썬으로 작성된 코드이다. 실행 결과가 12가 되도록 빈칸에 들어갈 값은?

def sum_n(nums, n):
    s = 0
    for i in range(n):
        s += nums[i]
    return s

print(sum_n([2, 4, 6, 8], ____))

## 10. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 5를 입력했을 때 출력되는 값은?

def f(x):
    return x // 2

n = int(input())
print(f(n))

## 11. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    r = 1
    for n in nums:
        r *= n
    return r

print(func([1, 2, 3]))

## 12. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(x):
    return x % 2 == 0

print(func(4))

## 13. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    return nums[len(nums)//2]

print(func([1, 3, 5, 7, 9]))

## 14. 다음은 파이썬으로 작성된 코드이다. 실행 결과가 6이 되도록 빈칸에 들어갈 값은?

def func(n):
    return n * (n + 1) // 2

print(func(____))

## 15. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(a, b):
    if a > b:
        return a - b
    return b - a

print(func(3, 10))

## 16. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 2를 입력했을 때 출력되는 값은?

def func(nums, i):
    return nums[i] * i

arr = [3, 6, 9, 12]
x = int(input())
print(func(arr, x))

## 17. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n == 0:
        return 1
    return n * func(n - 1)

print(func(3))

## 18. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i] * i
    return s

print(func([1, 2, 3]))

## 19. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 4를 입력했을 때 출력되는 값은?

def func(n):
    return n * n - n

x = int(input())
print(func(x))

## 20. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    return max(nums) - min(nums)

print(func([3, 7, 2, 9]))