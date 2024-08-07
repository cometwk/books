### 七、什么是贝叶斯过滤器？

垃圾邮件是一种令人头痛的顽症，困扰着所有的互联网用户。正确识别垃圾邮件的技术难度非常大。传统的垃圾邮件过滤方法，主要有"关键词法"和"校验码法"等。前者的过滤依据是特定的词语；后者则是计算邮件文本的校验码，再与已知的垃圾邮件进行对比。它们的识别效果都不理想，而且很容易规避。

2002 年，Paul Graham 提出使用"贝叶斯推断"过滤垃圾邮件。他说，这样做的效果，好得不可思议。1000 封垃圾邮件可以过滤掉 995 封，且没有一个误判。另外，这种过滤器还具有自我学习的功能，会根据新收到的邮件，不断调整。收到的垃圾邮件越多，它的准确率就越高。

### 八、建立历史资料库

贝叶斯过滤器是一种统计学过滤器，建立在已有的统计结果之上。所以，我们必须预先提供两组已经识别好的邮件，一组是正常邮件，另一组是垃圾邮件。我们用这两组邮件，对过滤器进行"训练"。这两组邮件的规模越大，训练效果就越好。Paul Graham 使用的邮件规模，是正常邮件和垃圾邮件各 4000 封。

"训练"过程很简单。首先，解析所有邮件，提取每一个词。然后，计算每个词语在正常邮件和垃圾邮件中的出现频率。比如，我们假定"sex"这个词，在 4000 封垃圾邮件中，有 200 封包含这个词，那么它的出现频率就是 5%；而在 4000 封正常邮件中，只有 2 封包含这个词，那么出现频率就是 0.05%。（【注释】如果某个词只出现在垃圾邮件中，Paul Graham 就假定，它在正常邮件的出现频率是 1%，反之亦然。这样做是为了避免概率为 0。随着邮件数量的增加，计算结果会自动调整。）有了这个初步的统计结果，过滤器就可以投入使用了。

### 九、贝叶斯过滤器的使用过程

现在，我们收到了一封新邮件。在未经统计分析之前，我们假定它是垃圾邮件的概率为 50%。（【注释】有研究表明，用户收到的电子邮件中，80%是垃圾邮件。但是，这里仍然假定垃圾邮件的"先验概率"为 50%。）我们用 S 表示垃圾邮件（spam），H 表示正常邮件（healthy）。因此，P(S)和 P(H)的先验概率，都是 50%。

$$P(S) = P(H) = 0.5$$

然后，对这封邮件进行解析，发现其中包含了 sex 这个词，请问这封邮件属于垃圾邮件的概率有多高？我们用 W 表示"sex"这个词，那么问题就变成了如何计算 P(S|W)的值，即在某个词语（W）已经存在的条件下，垃圾邮件（S）的概率有多大。根据条件概率公式，马上可以写出

$$ P(S|W) = \frac{P(W|S) \cdot P(S)}{P(W|S) \cdot P(S) + P(W|H) \cdot P(H)} $$

公式中，P(W|S)和 P(W|H)的含义是，这个词语在垃圾邮件和正常邮件中，分别出现的概率。这两个值可以从历史资料库中得到，对 sex 这个词来说，上文假定它们分别等于 5%和 0.05%。另外，P(S)和 P(H)的值，前面说过都等于 50%。所以，马上可以计算 P(S|W)的值：

$$ P(S|W) = \frac{0.05 \times 0.5}{0.05 \times 0.5 + 0.0005 \times 0.5} = \frac{0.025}{0.025 + 0.00025} = \frac{0.025}{0.02525} \approx 0.99 $$

因此，这封新邮件是垃圾邮件的概率等于 99%。这说明，sex 这个词的推断能力很强，将 50%的"先验概率"一下子提高到了 99%的"后验概率"。

### 十、联合概率的计算

做完上面一步，请问我们能否得出结论，这封新邮件就是垃圾邮件？回答是不能。因为一封邮件包含很多词语，一些词语（比如 sex）说这是垃圾邮件，另一些说这不是。你怎么知道以哪个词为准？

Paul Graham 的做法是，选出这封信中 P(S|W)最高的 15 个词，计算它们的联合概率。（【注释】如果有的词是第一次出现，无法计算 P(S|W)，Paul Graham 就假定这个值等于 0.4。因为垃圾邮件用的往往都是某些固定的词语，所以如果你从来没见过某个词，它多半是一个正常的词。）

所谓联合概率，就是指在多个事件发生的情况下，另一个事件发生概率有多大。比如，已知 W1 和 W2 是两个不同的词语，它们都出现在某封电子邮件之中，那么这封邮件是垃圾邮件的概率，就是联合概率。

**问题**

概率论中: 事件 W1, W2 同时发生, 叫联合事件 joint event

$$
\begin{align*}
S & \quad 垃圾邮件\\
H & \quad 正常邮件\\
(W_1 \cap W_2) & \quad 联合事件\\
P(W1,W2) & \quad \text{联合事件的概率} \\
P(S|W_1,W_2) & \quad \text{条件概率: 当 W 同时出现时是垃圾邮件的概率} \\
\end{align*}
$$

那么当单词 $W_1,W_2$ 同时出现的情况下，垃圾邮件的概率为 $P(S|W1, W2)$。

---

**已知数据**

回顾上一小节中，

- 根据数据统计，已知单词 W 在垃圾邮件和正常邮件中的概率值， 即:
  - $ P(W|S)$ 值已知
- 再根据条件概率，已知在某个词语（W）已经存在的条件下，垃圾邮件（S）的概率值, 即:
  - $ P(S|W) $ 值已知
- 故根据统计，可得到 $ P(S|W_1) , P(S|W_2) $ 的值

**定理引用**

1. 根据条件概率公式:

$$
\begin{align}
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
\end{align}
$$

2. 根据全概率定理:

$$
\begin{align}
P(W) = P(W|S)P(S) + P(W|H)P(H)
\end{align}
$$

3. 根据[条件独立性的定义](./spam_3.md), 
若 $ X \perp Y \mid A $ ， 则:
$$
\begin{align}
P(X, Y \mid A) = P(X \mid A) \cdot P(Y \mid A)
\end{align}
$$


**计算**

开始计算垃圾邮件概率 $P(S|W1, W2)$


根据 $(1)$ :

$$ 
\begin{align}
P(S|W1, W2) = \frac{P(W_1,W_2|S)P(S)}{P(W1, W2)} 
\end{align}  
$$

根据 $(2)$ :

$$
P(W_1, W_2) = P(W_1, W_2|S)P(S) + P(W_1, W_2|H)P(H) 
$$


根据 $(3)$ :

假定: 所有事件都是独立事件, 即 W1,W2 独立（【注释】严格地说，这个假定不成立，但是这里可以忽略）.

> 即: 在条件 $S$ 下, $W_1, W_2$ 独立


$$
P(W_1, W_2|S) = P(W_1|S)  P(W_2|S)
$$

上述2式带入 $(4)$ 
得:

$$
\begin{align*}
P(S|W1, W2) 
&= \frac{P(W_1,W_2|S)P(S)}{P(W1, W2)} \\ 
&= \frac{ P(W_1,W_2|S)  P(S)} {P(W_1, W_2|S)P(S) + P(W_1, W_2|H)P(H) } \\ 
&= \frac{ P(W_1|S)  P(W_2|S)  P(S)} {P(W_1|S)P(W_2|S)P(S) + P(W_1|H)P(W_2|H)P(H) } \\ 
\end{align*}
$$


结论:

$$
\begin{align}
P(S|W1, W2) 
&= \frac{ P(W_1|S)  P(W_2|S) } {P(W_1|S)P(W_2|S) + P(W_1|H)P(W_2|H) } \\ 
\end{align}
$$

这就是所谓的 **朴素贝叶斯推断** 算法。
等式的右边都是已知的数据，所以可以计算出 $P(S|W1, W2)$ 的值。


## Paul Graham 的结果

为了得到跟 Paul Graham 一样的结果，
还要根据结论 $(5)$ , 继续计算。

为了简化计算，
假设垃圾邮件的先验概率 $$ P(S) = P(H) = 0.5 $$
这不是问题，先验不太重要，后验能改进结果。

既然 $P(S) = P(H)$ 这点很重要，因为这样可以简化计算。

$$
\begin{align*}
P(S|W1, W2) 
&= \frac{ P(W_1|S)  P(W_2|S)  P(S)} {P(W_1|S)P(W_2|S)P(S) + P(W_1|H)P(W_2|H)P(H) } \\ 
\end{align*}
$$

上式，乘以因子 $$ \frac {\frac {P(S)} {P(W_1)P(W_2)}} {\frac {P(S)} {P(W_1)P(W_2)}} $$ 后，再按
$ \frac {P(W_i|S)P(S)} {P(W_i)} = P(S|W_i)$ 排列整齐， 

得:

$$
\begin{align*}
& P(S|W1, W2)  \\
& = \frac{ P(W_1|S)  P(W_2|S)  P(S) } {P(W_1|S)P(W_2|S)P(S) + P(W_1|H)P(W_2|H)P(H) } \cdot \frac {\frac {P(S)} {P(W_1)P(W_2)}} {\frac {P(S)} {P(W_1)P(W_2)}}\\ 
& = \frac { 
  \frac {P(W_1|S)P(S)} {P(W_1)} \cdot 
  \frac {P(W_2|S)P(S)} {P(W_2)} 
  } {
  \frac {P(W_1|S)P(S)} {P(W_1)} \cdot 
  \frac {P(W_2|S)P(S)} {P(W_2)} + 
  \frac {P(W_1|H)P(H)} {P(W_1)} \cdot 
  \frac {P(W_2|H)P(S)} {P(W_2)}  
  } \\
& = \frac { 
    P(S|W_1) \cdot P(S|W_2)
  } {
     P(S|W_1) \cdot P(S|W_2) +
     P(H|W_1) \cdot 
  \frac {P(W_2|H)P(S)} {P(W_2)}  
  } \\
& = \frac { 
    P_1 \cdot P_2
  } {
    P_1 \cdot P_2 +
    (1-P_1) \cdot (1 - P_2)
  }
\end{align*}
$$

注意，其中:
- 替换
$$ \frac {P(W_2|H)P(S)} {P(W_2)} = \frac {P(W_2|H)P(H)} {P(W_2)}  = P(H|W_2) $$
- 一封邮件，不管条件如何, 要么是垃圾邮件, 要么是正常邮件, 即:
$$  1 = P(S|W_1) + P(H|W_1)$$
- 再设 $$P_1 = P(S|W_1)$$
  那么 $$ 1 - P_1 = P(H|W_1)$$


### 十一、最终的计算公式

既然W1已经出现，那么要么出现在垃圾邮件中, 要么出现在正常邮件中，即:
$$ P(W_1|S) + P(W_1|H) =1 $$
$$ P(W_1|H) = 1 - P(W_1|S) $$


将上面的公式扩展到 15 个词的情况，就得到了最终的概率计算公式：

$$ P(S|W_1, W_2, \dots, W_{15}) = \frac{P1 \cdot P2 \cdot \dots \cdot P_{15}}{P1 \cdot P2 \cdot \dots \cdot P_{15} + (1 - P1) \cdot (1 - P2) \cdot \dots \cdot (1 - P_{15})} $$

一封邮件是不是垃圾邮件，就用这个式子进行计算。这时我们还需要一个用于比较的门槛值。Paul Graham 的门槛值是 0.9，概率大于 0.9，表示 15 个词联合认定，这封邮件有 90%以上的可能属于垃圾邮件；概率小于 0.9，就表示是正常邮件。有了这个公式以后，一封正常的信件即使出现 sex 这个词，也不会被认定为垃圾邮件了。
