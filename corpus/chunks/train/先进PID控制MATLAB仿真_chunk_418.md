# 2. 有监督的 Delta 学习规则

在 Hebb 学习规则中，引入教师信号，即将 $o_{j}$ 换成希望输出 $d_{j}$ 与实际输出 $o_{j}$ 之差，就构成有监督学习的 Delta 学习规则：

$$\Delta w _ {i j} (k) = \eta \left(d _ {j} (k) - o _ {j} (k)\right) o _ {i} (k) \tag {9.2}$$
