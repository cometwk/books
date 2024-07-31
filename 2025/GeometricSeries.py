import numpy as np
import matplotlib.pyplot as plt

# 定义几何级数的参数
a = 1  # 首项
r = 0.5  # 公比
n_terms = 10  # 项数

# 生成几何级数
n = np.arange(n_terms)
geometric_series = a * r**n

# 绘制几何级数的函数图像
plt.figure(figsize=(10, 6))
plt.plot(n, geometric_series, 'o-', label='Geometric Series: $a * r^n$')
plt.title('Geometric Series $a=1, r=0.5$')
plt.xlabel('n')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()

