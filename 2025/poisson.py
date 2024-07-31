import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# 定义泊松分布的参数
lambda_ = 3
k = np.arange(0, 15)  # 我们只绘制0到14起事故的概率

# 生成泊松分布的 PMF
pmf = poisson.pmf(k, lambda_)

# 绘制泊松分布的 PMF
plt.figure(figsize=(10, 6))
plt.stem(k, pmf, use_line_collection=True)
plt.title('Poisson Distribution of Daily Car Accidents (λ = 3)')
plt.xlabel('Number of Accidents (k)')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

