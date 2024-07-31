
## 条件独立性的定义

随机变量 \(X\) 和 \(Y\) 在给定事件 \(A\) 条件下是条件独立的，如果：

\[ P(X = x, Y = y \mid A) = P(X = x \mid A) \cdot P(Y = y \mid A) \]

对于所有 \(x\) 和 \(y\)。


**简写**: 
- 若 \(X \perp Y \mid A\)
- 则 \(P(X, Y \mid A) = P(X \mid A) \cdot P(Y \mid A)\)

\[
\begin{align*}
若 \quad & X \perp Y \mid A  \\
则 \quad & P(X, Y \mid A) = P(X \mid A) \cdot P(Y \mid A)
\end{align*}
\]

### 条件概率的关系

1. **联合条件概率**：条件独立性允许我们将联合条件概率分解为边际条件概率的乘积。
   
2. **边际条件概率**：边际条件概率 \(P(X = x \mid A)\) 和 \(P(Y = y \mid A)\) 分别描述了在事件 \(A\) 发生的条件下，\(X\) 和 \(Y\) 的单独分布。


### 证明和分析

- `BOOK-1.2.4` 定义了 Probability Law  概率律，即概率空间的定义。(满足三条公理)
- `BOOK-1.3.1` Conditional Probabilities Specify a Probability Law (条件概率指定了一个概率律)
  - 在给定某些事件 A 发生的条件下，条件概率可以用来定义一个新的概率空间.
- `BOOK-2.6.1` 给定了条件概率的定义: \[ P(X = x \mid A) = \frac{P(X = x, A)}{P(A)} \]
- 随机变量 \(X\) 和 \(Y\) 在给定事件 \(A\) 条件下的 **联合条件概率** 为

\[
\begin{align*}
P(X = x, Y = y \mid A) = \frac{P(X = x, Y = y, A)}{P(A)}
\end{align*}
\]

- 每个单独的条件概率：

\[
P(X = x \mid A) = \frac{P(X = x, A)}{P(A)}
\] 

\[
P(Y = y \mid A) = \frac{P(Y = y, A)}{P(A)}
\]

- 最后，条件独立性的定义是：

\[
P(X = x, Y = y \mid A) = P(X = x \mid A) \cdot P(Y = y \mid A)
\]

简写为

\[P(X, Y \mid A) = P(X \mid A) \cdot P(Y \mid A)\]

