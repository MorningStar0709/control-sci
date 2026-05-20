$$\boldsymbol {x} (k) = \phi (k; 0, \boldsymbol {x} _ {0}, \boldsymbol {0}) + \phi (k; 0, \boldsymbol {0}, \boldsymbol {u}) \tag {2.171}$$

对于线性时变离散系统

$$\phi (k; 0, \boldsymbol {x} _ {0}, \mathbf {0}) = \Phi (k, 0) \boldsymbol {x} _ {0} \tag {2.172}\phi (k; 0, \mathbf {0}, u) = \sum_ {i = 0} ^ {k - 1} \Phi (k, i + 1) H (i) u (i) \tag {2.173}$$

对于线性定常离散系统

$$\phi (k; 0, x _ {0}, 0) = G ^ {k} x _ {0} \tag {2.174}\phi (k; 0, 0, u) = \sum_ {i = 0} ^ {k - 1} G ^ {k - i - 1} H u (i) \tag {2.175}$$

结论6 考虑线性定常离散系统(2.150)，且令 $u(k) = 0 (k = 0, 1, 2, \cdots)$ ，则系统为渐近稳定的充分必要条件是 $G$ 的所有特征值 $\mu_1, \mu_2, \cdots, \mu_n$ 的模均小于1，即

$$\left| \mu_ {i} \right| < 1, \quad i = 1, 2, \dots , n \tag {2.176}$$

证 限于对 G 的特征值 $\mu_{1}, \mu_{2}, \cdots, \mu_{n}$ 为两两相异的情况进行证明。如若不是这种情况，则证明思路类同，但推证过程要繁杂一些。

由于 $\mu_{1}, \mu_{2}, \cdots, \mu_{n}$ 为两两相异，故存在非奇异常阵 P 使成立

$$
G = P \left[ \begin{array}{c c c} \mu_ {1} & & \\ & \ddots & \\ & & \mu_ {n} \end{array} \right] P ^ {- 1} \tag {2.177}
$$

将此代入(2.174)，可得到

$$
\phi (k; 0, x _ {0}, 0) = G ^ {k} x _ {0} = P \left[ \begin{array}{c c c} \mu_ {1} ^ {k} & & \\ & \ddots & \\ & & \mu_ {n} ^ {k} \end{array} \right] P ^ {- 1} x _ {0} \tag {2.178}
$$

进而，可导出

$$
\lim _ {k \rightarrow \infty} \phi (k; 0, x _ {0}, 0)
= P \left[\begin{array}{c c c}\lim _ {k \rightarrow \infty} \mu_ {1} ^ {k}&&\\&\ddots&\\&&\lim _ {k \rightarrow \infty} \mu_ {n} ^ {k}\end{array}\right] P ^ {- 1} x _ {0} \tag {2.179}
$$

这表明，当且仅当（2.176）成立时，有

$$\lim _ {k \rightarrow \infty} \mu_ {i} ^ {k} = 0, \quad i = 1, 2, \dots , n \tag {2.180}$$

和

$$\lim _ {k \rightarrow \infty} \phi (k; 0, x _ {0}, 0) = 0 \tag {2.181}$$

也即系统为渐近稳定。于是，证明完成。

脉冲传递函数矩阵 考虑线性定常离散系统

$$
\begin{array}{r l} \boldsymbol {x} (k + 1) & = G \boldsymbol {x} (k) + H \boldsymbol {u} (k), \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \\ \boldsymbol {u} (k) & = G \boldsymbol {u} (k) + R \boldsymbol {v} (k). \end{array} \tag {2.182}
\mathbf {y} (k) = C \mathbf {x} (k) + D \mathbf {u} (k)
$$

令 $\mathcal{X}(z)$ 为 $\{x(k), k=0,1,2,\cdots,\infty\}$ 的 z 变换，即

$$\hat {x} (z) \triangleq \mathcal {Z} [ x (k) ] \triangleq \sum_ {k = 0} ^ {\infty} x (k) z ^ {- k} \tag {2.183}$$

且由此可导出
