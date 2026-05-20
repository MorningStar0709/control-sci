# 4. 选择操作

为了确定 $x_{i}(t)$ 是否成为下一代的成员，试验向量 $v_{i}(t+1)$ 和目标向量 $x_{i}(t)$ 对评价函数进行比较：

$$
x _ {i} (t + 1) = \left\{ \begin{array}{l} v _ {i} (t + 1), f (v _ {i 1} (t + 1), \dots , v _ {i n} (t + 1)) <   f (x _ {i 1} (t), \dots , x _ {i n} (t)) \\ x _ {i j} (t), f (v _ {i 1} (t + 1), \dots , v _ {i n} (t + 1)) \geqslant f (x _ {i 1} (t), \dots , x _ {i n} (t)) \end{array} \right. \tag {10.5}
$$

反复执行步骤 2. 至步骤 4. 操作，直至达到最大的进化代数 G。差分进化基本运算流程如图 10-1 所示。

![](image/71422ad2867c6af9a2e1eb8e408180b29891b54ca1d0a127f0228a1375bbdff3.jpg)
