# 3.10 张量场

张量的本质是多线性映射。流形上的多线性映射给了拓扑空间丰富的几何结构，如 Riemann 几何、辛几何、外微分等。它们在现代控制理论的许多分支，如非线性控制，分布参数系统等的研究中起着重要作用。

设 V 为一个 n 维向量空间. 一个映射 $\phi: \underbrace{V \times \cdots \times V}_{k} \rightarrow R$ 称为多线性映射, 如果它满足

(1)

$$\phi (X _ {1}, \dots , c X _ {r}, \dots , X _ {k}) = c \phi (X _ {1}, \dots , X _ {r}, \dots , X _ {k});$$

(2)

$$\phi \left(X _ {1}, \dots , Y _ {r} + Z _ {r}, \dots , X _ {k}\right) = \phi \left(X _ {1}, \dots , Y _ {r}, \dots , X _ {k}\right) + \phi \left(X _ {1}, \dots , Z _ {r}, \dots , X _ {k}\right).$$

设 $\{e_{1},\cdots,e_{n}\}$ 为 V 的一组基. V 的对偶空间记作 $V^{*}$ . $V^{*}$ 的一组基 $\{d^{1},\cdots,d^{n}\}$ 称为 $\{e_{i}\}$ 的对偶基，如果它满足

$$
d ^ {i} (e _ {j}) = \left\{ \begin{array}{l l} 1, & \quad i = j, \\ 0, & \quad i \neq j. \end{array} \right.
$$

定义 3.10.1 一个多线性映射 $\phi: \underbrace{V \times \cdots \times V}_{r} \times \underbrace{V^{*} \times \cdots \times V^{*}}_{s} \to \mathbb{R}$ 称为 $V$ 上的张量，这里 $r$ 称为协变阶， $s$ 称为逆变阶。 $\phi$ 简称为一个 $(r, s)$ 张量。所有 $(r, s)$ 张量的集合记作 $\mathcal{T}_s^r(V)$ 。

记

$$\gamma_ {j _ {1}, \dots , j _ {s}} ^ {i _ {1}, \dots , i _ {r}} = \phi (e _ {i _ {1}}, \dots , e _ {i _ {r}}, d ^ {j _ {1}}, \dots , d ^ {j _ {s}}), \quad 1 \leqslant i _ {1}, \dots , i _ {r} \leqslant r, 1 \leqslant j _ {1}, \dots , j _ {s} \leqslant s.$$

我们构造 $\phi$ 的结构矩阵如下：

$$
\Gamma = \left[ \begin{array}{c c c c c c c} \gamma_ {1 1 \dots 1} ^ {1 1 \dots 1} & \dots & \gamma_ {1 1 \dots 1} ^ {1 1 \dots n} & \dots & \gamma_ {1 1 \dots 1} ^ {n n \dots 1} & \dots & \gamma_ {1 1 \dots 1} ^ {n n \dots n} \\ \vdots & & \vdots & & \vdots & & \vdots \\ \gamma_ {1 1 \dots n} ^ {1 1 \dots 1} & \dots & \gamma_ {1 1 \dots n} ^ {1 1 \dots n} & \dots & \gamma_ {1 1 \dots n} ^ {n n \dots 1} & \dots & \gamma_ {1 1 \dots n} ^ {n n \dots n} \\ \vdots & & \vdots & & \vdots & & \vdots \\ \gamma_ {n n \dots 1} ^ {1 1 \dots 1} & \dots & \gamma_ {n n \dots 1} ^ {1 1 \dots n} & \dots & \gamma_ {n n \dots 1} ^ {n n \dots 1} & \dots & \gamma_ {n n \dots 1} ^ {n n \dots n} \\ \vdots & & \vdots & & \vdots & & \vdots \\ \gamma_ {n n \dots n} ^ {1 1 \dots 1} & \dots & \gamma_ {n n \dots n} ^ {1 1 \dots n} & \dots & \gamma_ {n n \dots n} ^ {n n \dots 1} & \dots & \gamma_ {n n \dots n} ^ {n n \dots n} \end{array} \right]. (3. 1 0. 1)
$$

记向量 $X \in V$ 为一列向量 $X = [a_{1}, \cdots, a_{n}]^{T}$ ，即 $X = \sum_{i=1}^{n} a_{i} e_{i}$ 。同样，一个余向量 $\omega \in V^{*}$ 为一个行向量 $\omega = (b_{1}, \cdots, b_{n})$ ，即 $\omega = \sum_{i=1}^{n} b_{id}^{i}$ 。那么可以用下式计算张量值：
