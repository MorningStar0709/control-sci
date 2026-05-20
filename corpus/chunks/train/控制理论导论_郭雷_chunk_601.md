证明 $\mathcal{F}_0\cap \mathcal{H}^\perp$ 的对合性是显见的，因为由定义可知两个对合分布的交一定对合．至于 $\mathcal{F}_0\bigcup \mathcal{H}^\perp$ ，因为 $\mathcal{H}^{\perp}$ 对 $F$ 不变，它对 $\mathcal{F}$ 也不变，特别是对 $\mathcal{F}_0$ 也不变.对合性显见.

下面的引理在一些文献中称为广义 Frobenius 定理 [24].

引理 8.2.5 设分布族 $\Delta_{1} \subset \Delta_{2} \subset \cdots \subset \Delta_{k}$ 是对合且在 $x_{0}$ 的一个邻域 U 上的维数为 $d_{1} < d_{2} < \cdots < d_{k}$ ，则存在一个局部坐标卡 $(V, z)$ ， $x_{0} \in V \subset U$

$$z = \{z _ {1} ^ {1}, \dots , z _ {d _ {1}} ^ {1}, z _ {1} ^ {2}, \dots , z _ {d _ {2} - d _ {1}} ^ {2}, \dots , z _ {1} ^ {k}, \dots , z _ {d _ {k} - d _ {k - 1}} ^ {k}, z ^ {k + 1} \},$$

使得

$$\Delta_ {s} = \left\{\frac {\partial}{\partial z _ {j} ^ {i}} \mid i \leqslant s, j = 1, \dots , d _ {s} - d _ {s - 1} \right\}, \quad 1 \leqslant s \leqslant k. \tag {8.2.17}$$

证明 我们用数学归纳法证明. 因为 $D_{1}$ 是对合, 故存在一个平整坐标卡 $(U, z)$ 使式 (8.2.17) 对 $s = 1$ 成立. 设命题对 $i \leqslant s$ 成立. 设 $p_{s} := d_{s} - d_{s-1}$ , 及 $d_{0} = 0$ , 则可找到 $p_{s+1}$ 向量场 $\{X_{1}, \cdots, X_{p_{s+1}}\}$ 使得

$$
\text { span } \left\{\left[ \begin{array}{c} I _ {p _ {1}} \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \end{array} \right], \left[ \begin{array}{c} 0 \\ I _ {p _ {2}} \\ \vdots \\ 0 \\ \vdots \\ 0 \end{array} \right], \left[ \begin{array}{c} 0 \\ 0 \\ \vdots \\ I _ {p _ {s}} \\ \vdots \\ 0 \end{array} \right], [ X _ {1} \dots X _ {p _ {s + 1}} ] \right\} = \Delta_ {s + 1}.
$$

于是在

$$[ X _ {1} \dots X _ {p _ {s + 1}} ]$$

的最后 $n - d_s$ 行中至少有一个 $p_{s+1} \times p_{s+1}$ 的子式非奇异。不失一般性设其最后 $p_{s+1}$ 子块线性无关，记这一个子块为 $T$ ，且定义

$$
\left[ \begin{array}{l l l} Y _ {1} & \dots & Y _ {p _ {s + 1}} \end{array} \right] = \left[ \begin{array}{l l l} X _ {1} & \dots & X _ {p _ {s + 1}} \end{array} \right] T ^ {- 1} = \left[ \begin{array}{c} * \\ I _ {p _ {s + 1}} \end{array} \right],
$$

则 $Y_{1},\cdots,Y_{p_{s+1}}$ 可交换. (参考 Frobenius 定理的证明) 设 $V_{i}, i=1,\cdots,n$ 为一线性无关向量场集合，这里 $d_{s}$ 个向量场为 $\frac{\partial}{\partial z_{j}^{i}}, i=1,\cdots,s, j=1,\cdots,p_{i}$ ，且

$$V _ {d _ {s} + j} = Y _ {j}, \quad j = 1, \dots , p _ {s + 1}.$$

构造一个从零点邻域 $W \subset \mathbb{R}^n$ 到 $U$ 的一个微分同胚

$$\varphi (t) := \phi_ {t _ {1}} ^ {V _ {1}} \dots \phi_ {t _ {n}} ^ {V _ {n}} (x _ {0}).$$

那么 $(\varphi(W), t)$ 为 $x_0$ 的一个局部坐标卡，且在这个局部坐标卡下式 (8.2.17) 对 $s + 1$ 成立。（具体细节可参考 Frobenius 定理的证明。）

利用引理8.2.4和引理8.2.5，设 $x_0 \in M$ 为 $\mathcal{F}_0, \mathcal{F}_0 \cap \mathcal{H}^\perp, \mathcal{F}_0 \cup \mathcal{H}^\perp$ 的正则点，那么我们可找到一个局部坐标卡 $(V, z), V \subset U$ 及 $z = (z^1, z^2, z^3, z^4)$ 使得
