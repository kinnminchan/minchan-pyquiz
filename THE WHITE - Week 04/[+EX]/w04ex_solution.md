## +1번 문제

정답: 28  
해설:  
(1) 입력 i = 1, 초기 total = 0, n = 0  
(2) 반복:  
    i = 1, n = 0 → j = 0 → (arr[1] + 0) = 3 → 홀수 → total = 0  

    i = 2, n = 1 → j = 0 → 5 → 홀수 → total = 0  
    j = 1 → 5 + 1 = 6 → 짝수 → total += 5 - 1 = 4 → total = 4  

    i = 3, n = 2 → j = 0 → 7 → 홀수  
    j = 1 → 8 → 짝수 → total += 7 - 1 = 6 → total = 10  
    j = 2 → 9 → 홀수  

    i = 4, n = 3 → j = 0 → 11 → 홀수  
    j = 1 → 12 → 짝수 → total += 11 - 1 = 10 → total = 20  
    j = 2 → 13 → 홀수  
    j = 3 → 14 → 짝수 → total += 11 - 3 = 8 → total = 28  
(3) 반복 종료 (i = 5) → 출력값 28

---

## +2번 문제

정답: 85  
해설:  
(1) 반복:  
    i = 0 → j = 0 → 1 * 0 = 0 → total = 0  

    i = 1 → j = 0 → 2 * 0 = 0, j = 1 → 2 * 1 = 2 → total = 2  

    i = 2 → j = 0 → 3 * 0 = 0, j = 1 → 3 * 1 = 3, j = 2 → 3 * 2 = 6 → total = 11  

    i = 3 → j = 0 → 4 * 0 = 0, j = 1 → 4 * 1 = 4, j = 2 → 4 * 2 = 8, j = 3 → 4 * 3 = 12 → total = 35  

    i = 4 → j = 0 → 5 * 0 = 0, j = 1 → 5 * 1 = 5, j = 2 → 5 * 2 = 10, j = 3 → 5 * 3 = 15, j = 4 → 5 * 4 = 20 → total = 85  
(2) 최종 total = 85

---

## +3번 문제

정답: 10  
해설:  
(1) 입력 i = 1 → total = 0, step = 1  
(2) 반복:  
    i = 1 → nums[1] = 6 → 6 % 3 == 0 → total += (6 + 1) // 2 = 3 → total = 3  
    i += 2 → i = 3, step += 1 → step = 2  

    i = 3 → nums[3] = 12 → 12 % 3 == 0 → total += (12 + 2) // 2 = 7 → total = 10  
    i += 2 → i = 5 → 종료  
(3) 최종 total = 10

---

## +4번 문제

정답: 62  
해설:  
(1) 입력 i = 0, total = 0, count = 1  
(2) 반복:  
    i = 0 → j = 0 → j % 2 = 0 → total += 2 * (0 + 1) = 2 → total = 2  
    i += 1 → i = 1, count += 1 → count = 2  

    i = 1 → j = 0 → 2 * (1 + 1) = 4 → total = 6  
    j = 1 → 홀수 → skip  
    i += 1 → i = 2, count += 1 → count = 3  

    i = 2 → j = 0 → 2 * (2 + 1) = 6 → total = 12  
    j = 1 → 홀수 → skip  
    j = 2 → 6 * (2 + 1) = 18 → total = 30  
    i += 1 → i = 3, count += 1 → count = 4  

    i = 3 → j = 0 → 2 * (3 + 1) = 8 → total = 38  
    j = 1 → skip  
    j = 2 → 6 * 4 = 24 → total = 62  
    j = 3 → skip  
(3) 반복 종료 → 최종 total = 62

---

## +5번 문제

정답: 56  
해설:  
(1) 입력 i = 1 → 초기 total = 0  
(2) 반복:  
    idx = 1 → arr[1] = 4 → 짝수 → total += 4 * (1 - 1 + 1) = 4 → total = 4  
    idx = 2 → arr[2] = 6 → 짝수 → total += 6 * (2 - 1 + 1) = 12 → total = 16  
    idx = 3 → arr[3] = 8 → 짝수 → total += 8 * (3 - 1 + 1) = 24 → total = 40  
    idx = 4 → arr[4] = 10 → 짝수 → total += 10 * (4 - 1 + 1) = 16 → total = 56  
(3) 반복 종료 → 출력값 56

---

## +6번 문제

정답: 3640  
해설:  
(1) 입력 i = 1 → 초기 total = 1  
(2) 반복:  
    idx = 1 → nums[1] = 3 → 홀수 → total *= 3 + 1 = 4 → total = 4  
    idx = 2 → nums[2] = 5 → 홀수 → total *= 5 + 2 = 7 → total = 28  
    idx = 3 → nums[3] = 7 → 홀수 → total *= 7 + 3 = 10 → total = 280  
    idx = 4 → nums[4] = 9 → 홀수 → total *= 9 + 4 = 13 → total = 3640  
(3) 반복 종료 → 출력값 3640

---

## +7번 문제

정답: 30  
해설:  
(1) 입력 i = 2 → 초기 total = 0, step = 0  
(2) 반복:  
    i = 2 → total += 5 + 0 = 5 → total = 5, step += 2 → step = 2, i = 3  
    i = 3 → total += 7 + 2 = 9 → total = 14, step += 3 → step = 5, i = 4  
    i = 4 → total += 11 + 5 = 16 → total = 30, step += 4 → step = 9, i = 5  
(3) 반복 종료 → 출력값 30

---

## +8번 문제

정답: 20  
해설:  
(1) 입력 i = 3 → 초기 total = 0  
(2) 반복:  
    idx = 0 → total += 1 * (3 - 0 + 1) = 4 → total = 4  
    idx = 1 → total += 2 * (3 - 1 + 1) = 6 → total = 10  
    idx = 2 → total += 3 * (3 - 2 + 1) = 6 → total = 16  
    idx = 3 → total += 4 * (3 - 3 + 1) = 4 → total = 20  
(3) 반복 종료 → 출력값 20

---

## +9번 문제

정답: 30  
해설:  
(1) 입력 i = 0 → 초기 total = 0  
(2) 반복:  
    idx = 0 → total += 2 * 2 - 0 = 4 → total = 4  
    idx = 2 → total += 6 * 2 - 2 = 10 → total = 14  
    idx = 4 → total += 10 * 2 - 4 = 16 → total = 30  
(3) 반복 종료 → 출력값 30

---

## +10번 문제

정답: 7  
해설:  
(1) 입력 i = 3 → 초기 total = 0, step = 1  
(2) 반복:  
    idx = 0 → idx % 2 == 0 → total += 1 * 1 = 1 → step = 2  
    idx = 1 → idx % 2 != 0 → skip  
    idx = 2 → idx % 2 == 0 → total += 3 * 2 = 6 → step = 3  
    idx = 3 → idx % 2 != 0 → skip  
(3) 반복 종료 → 출력값 7