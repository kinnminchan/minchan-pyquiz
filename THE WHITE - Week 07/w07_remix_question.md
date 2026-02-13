## 1번. (2주차 11번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'를 입력했을 때 출력되는 값은?

```python
nums = [3, 6, 9, 12]
i = int(input())

value = nums[i]
result = value + nums[value // 3 - 1]

print(result)
```

---

## 2번. (2주차 12번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때, '30'이 출력되도록 빈칸에 들어갈 값은?

```python
arr = [10, 20, 30]
idx = [2, 0, 1]

n = int(input())
print(arr[idx[____]])
```

---

## 3번. (2주차 14번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

```python
a = [2, 0, 1, 3]
b = [10, 20, 30, 40]

i = int(input())

x = a[i]
y = b[x]
z = a[y // 10]

print(z)
```

---

## 4번. (2주차 15번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'를 입력했을 때, '500'이 출력되도록 빈칸에 들어갈 값은?

```python
nums = [100, 200, 300, 400, 500]
order = [4, 2, 0, 1, 3]

n = int(input())

print(nums[order[____]])
```

---

## 5번. (3주차 9번)

다음은 파이썬으로 작성된 코드이다. 실행 결과가 '12'일 때, 빈칸에 들어가야 할 값은?

```python
nums = [4, 8, 12, 16]
i = 0
total = 0

while i < ____:
    total += nums[i]
    i += 1

print(total)
```

---

## 6번. (3주차 16번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

```python
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
```

---

## 7번. (3주차 17번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

```python
nums = [1, 3, 5, 7, 9]
i = int(input())
total = 0

while i < 4:
    for j in range(0, i + 2):
        total += nums[j]
    i += 1
    if total >= 20:
        break

print(total)
```

---

## 8번. (3주차 18번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

```python
nums = [2, 4, 6, 8, 10]
i = int(input())
total = 0

while i < 4:
    total += nums[i]
    for j in range(i):
        total -= 1
    i += 1

print(total)
```

---

## 9번. (3주차 19번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

```python
nums = [1, 2, 3, 4, 5]
i = int(input())
total = 0

while i < 5:
    total += nums[i]
    i += 2
    for j in range(i - 1):
        total += 1

print(total)
```

---

## 10번. (3주차 20번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

```python
nums = [2, 4, 6, 8, 10]
i = int(input())
total = 0

while i < 5:
    for j in range(i, 5):
        if nums[j] % 4 == 0:
            total += nums[j]
    i += 1

print(total)
```

---

## 11번. (4주차 18번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
nums = [2, 4, 6, 8]
total = 0

for i in range(len(nums)):
    for j in range(i + 1):
        total += nums[i] // (j + 1)

print(total)
```

---

## 12번. (4주차 19번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '1'을 입력했을 때 출력되는 값은?

```python
nums = [5, 10, 15, 20]
i = int(input())
total = 0

while i < len(nums):
    total += (nums[i] + i) // 5
    i += 2

print(total)
```

---

## 13번. (4주차 20번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '0'을 입력했을 때 출력되는 값은?

```python
nums = [1, 2, 3, 4]
i = int(input())
total = 0

while i < len(nums):
    for j in range(len(nums) - i):
        total += nums[j] * (j % 2)
    i += 1

print(total)
```

---

## 14번. (5주차 9번)

다음은 파이썬으로 작성된 코드이다. 실행 결과가 12가 되도록 빈칸에 들어갈 값은?

```python
def sum_n(nums, n):
    s = 0
    for i in range(n):
        s += nums[i]
    return s

print(sum_n([2, 4, 6, 8], ____))
```

---

## 15번. (5주차 14번)

다음은 파이썬으로 작성된 코드이다. 실행 결과가 6이 되도록 빈칸에 들어갈 값은?

```python
def func(n):
    return n * (n + 1) // 2

print(func(____))
```

---

## 16번. (5주차 16번)

다음은 파이썬으로 작성된 코드이다. 코드 실행 후 사용자가 '2'를 입력했을 때 출력되는 값은?

```python
def func(nums, i):
    return nums[i] * i

arr = [3, 6, 9, 12]
x = int(input())
print(func(arr, x))
```

---

## 17번. (5주차 17번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(n):
    if n == 0:
        return 1
    return n * func(n - 1)

print(func(3))
```

---

## 18번. (5주차 18번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i] * i
    return s

print(func([1, 2, 3]))
```

---

## 19번. (6주차 2번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(n):
    if n < 10:
        return n
    return func(n // 10)

print(func(456))
```

---

## 20번. (6주차 3번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(n):
    if n == 0:
        return 0
    return 1 + func(n // 2)

print(func(8))
```

---

## 21번. (6주차 6번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(nums, i):
    if i < 0:
        return 0
    if nums[i] % 2 == 0:
        return nums[i] + func(nums, i - 1)
    return func(nums, i - 1)

print(func([1, 2, 3, 4], 3))
```

---

## 22번. (6주차 7번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(n):
    if n <= 1:
        return 1
    return func(n - 1) + func(n - 2)

print(func(4))
```

---

## 23번. (6주차 8번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(nums):
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], func(nums[1:]))

print(func([3, 1, 5, 2]))
```

---

## 24번. (6주차 9번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(s):
    if len(s) <= 1:
        return s
    return s[-1] + func(s[:-1])

print(func("abcd"))
```

---

## 25번. (6주차 11번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(nums, i):
    if i == len(nums):
        return 1
    if nums[i] == 0:
        return 0
    return nums[i] * func(nums, i + 1)

print(func([2, 3, 0, 4], 0))
```

---

## 26번. (6주차 12번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(n):
    if n < 10:
        return n
    return func(func(n // 10) + n % 10)

print(func(987))
```

---

## 27번. (6주차 13번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(arr, i):
    if i == 0:
        return arr[0]
    return arr[i] - func(arr, i - 1)

print(func([10, 3, 2], 2))
```

---

## 28번. (6주차 14번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(s, i):
    if i == len(s):
        return ""
    if i % 2 == 0:
        return s[i] + func(s, i + 1)
    return func(s, i + 1)

print(func("abcdef", 0))
```

---

## 29번. (6주차 15번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
def func(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return func(n // 2)
    return func(n - 1) + 1

print(func(7))
```

---

## 30번. (3주차 11번)

다음은 파이썬으로 작성된 코드이다. 실행 결과로 출력되는 값은?

```python
i = 10
cnt = 0

while i > 0:
    cnt += 1
    i -= 3

print(cnt)
```