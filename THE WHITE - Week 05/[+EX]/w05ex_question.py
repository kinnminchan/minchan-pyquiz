## +1. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    total = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            total += nums[i]
        else:
            total -= nums[i]
    return total

print(func([3, 5, 2, 7, 4]))

## +2. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 2를 입력했을 때 출력되는 값은?

def func(nums, i):
    s = 0
    while i < len(nums):
        s += nums[i] * (i + 1)
        i += 2
    return s

arr = [1, 3, 5, 7, 9]
x = int(input())
print(func(arr, x))

## +3. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    if n <= 1:
        return n
    return func(n - 1) + func(n - 2)

print(func(5))

## +4. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == i % 2:
            result.append(nums[i])
    return sum(result)

print(func([4, 3, 6, 1, 8]))

## +5. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    return m - nums[-1]

print(func([2, 7, 1, 8, 3]))

## +6. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 1을 입력했을 때 출력되는 값은?

def func(nums, i):
    total = 0
    for j in range(i, len(nums)):
        if j % 2 == 1:
            total += nums[j] // 2
        else:
            total += nums[j]
    return total

arr = [5, 8, 6, 3, 4]
x = int(input())
print(func(arr, x))

## +7. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += i
    return s

print(func(12))

## +8. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(i):
            total += nums[j]
    return total

print(func([1, 2, 3, 4]))

## +9. 다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

def func(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                cnt += 1
    return cnt

print(func([3, 1, 4, 2]))

## +10. 다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 3을 입력했을 때 출력되는 값은?

def func(nums, n):
    result = 0
    for i in range(n):
        result += nums[i] * (n - i)
    return result

arr = [2, 4, 6, 8, 10]
x = int(input())
print(func(arr, x))
