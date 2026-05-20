$$
G (s) = \left[ \begin{array}{c c c} \frac {1}{(s + 1)} & \frac {1}{(s + 2) (s + 1)} & \frac {1}{(s + 1) (s + 4)} \\ \frac {(s + 2)}{(s + 3)} & \frac {1}{(s + 3)} & \frac {(s + 2)}{(s + 3) (s + 4)} \end{array} \right]
$$

容易判断， $\operatorname{rank} G(s) = 1$ ，因此其右零空间的维数为 $\dim(Q_r) = 2$ 。现找出 $Q_r$ 的一个多项式基为

$$
\boldsymbol {f} _ {1} (s) = \left[ \begin{array}{c} - 1 \\ s + 2 \\ 0 \end{array} \right], \quad \boldsymbol {f} _ {2} (s) = \left[ \begin{array}{c} 0 \\ - (s + 2) \\ s + 4 \end{array} \right]
$$

且可以判断：由于

$$
F (s) = \left[ f _ {1} (s), f _ {2} (s) \right] = \left[ \begin{array}{c c} - 1 & 0 \\ s + 2 & - (s + 2) \\ 0 & s + 4 \end{array} \right]
$$

中不存在使其降秩的 $s$ 值，因此 $F(s)$ 是不可简约的；再因为 $F(s)$ 可表为

$$
F (s) = \left[ \begin{array}{l l} 0 & 0 \\ 1 & - 1 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{l l} s & 0 \\ 0 & s \end{array} \right] + \left[ \begin{array}{c c} - 1 & 0 \\ 2 & - 2 \\ 0 & 4 \end{array} \right] = F _ {h c} H _ {c} (s) + F _ {l c} (s)
$$

且其列次系数阵 $F_{bc}$ 为满列秩，所以 $F(s)$ 又是列既约的。这样，根据上述推论即知，上面构造的多项式基 $\{f_1(s), f_2(s)\}$ 必为 $G(s)$ 的右零空间 $\Omega_r$ 的一个最小多项式基，其最小指数为 $\{1,1\}$ 。
