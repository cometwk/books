import numpy as np

# 定义转移矩阵
P = np.array([
    [0.5, 0.5, 0.0],
    [0.5, 0.0, 0.5],
    [0.0, 0.0, 1.0]
])

# 初始状态向量
v0 = np.array([1, 0, 0])

# 抛硬币 n 次后的状态向量
def calculate_probability(n):
    vn = np.linalg.matrix_power(P, n).dot(v0)
    return vn[2]

# 输入抛硬币的次数
n = 10
prob = calculate_probability(n)
print(f"抛硬币 {n} 次至少出现一次连续两个正面的概率为：{prob:.4f}")

