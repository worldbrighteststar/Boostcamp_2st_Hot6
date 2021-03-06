# 1051번 숫자 정사각형 실버 3

n, m = map(int, input().split())
data = []
num = int(0)
result = 0

for _ in range(n):
  data.append(list(input()))

for i in range(n):
  for j in range(m):
    for k in range(n): # 정사각형 찾기
      if i + k < n and j + k < m: # 데이터에서 범위 벗어나지 않을 경우
        left1 = data[i][j]
        left2 = data[i][j + k]
        right1 = data[i + k][j]
        right2 = data[i + k][j + k]

        if left1 == left2 and left2 == right1 and right1 == right2: # 꼭짓점에 쓰여 있는 수가 모두 같을 경우
          result = max(result, (k + 1) * (k + 1)) # 이전 값과 비교했을 때 큰 값을 저장

print(result)
