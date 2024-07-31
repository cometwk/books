import random

def simulate_coin_tosses(num_experiments):
    count_hh = 0

    for _ in range(num_experiments):
        # 模拟抛三次硬币
        tosses = [random.choice(['H', 'T']) for _ in range(3)]
        
        # 检查是否有连续的HH
        for i in range(len(tosses) - 1):
            if tosses[i] == 'H' and tosses[i + 1] == 'H':
                count_hh += 1
                break

    # 计算连续出现HH的概率
    probability_hh = count_hh / num_experiments
    return probability_hh

# 模拟 100,000 次实验来估计概率
num_experiments = 100000
probability_hh = simulate_coin_tosses(num_experiments)
print(f"连续出现两个正面的概率估计值为：{probability_hh}")

