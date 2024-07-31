import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

# 使用 100,000 个样本来估计 pi
num_samples = 100000
pi_estimate = estimate_pi(num_samples)
print(f"使用 {num_samples} 个样本估计的 π 值为：{pi_estimate}")

