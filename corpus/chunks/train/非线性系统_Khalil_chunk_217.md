$$u = - \alpha y + \tilde {u} = - 0. 5 5 y + \tilde {u}\tilde {y} = (\beta - \alpha) y + \tilde {u} = 0. 4 5 y + \tilde {u}$$

因此变换后的线性系统为

$$\dot {x} = A x + B \tilde {u}, \quad \tilde {y} = C x + D \tilde {u}$$

其中 $A = \left[ \begin{array}{cc}0 & 1\\ -0.1 & -0.55 \end{array} \right],B = \left[ \begin{array}{c}0\\ 1 \end{array} \right],C = \left[ \begin{array}{ll}0.9 & 0.45 \end{array} \right],D = 1$

矩阵 P 是方程组(7.6)\~(7.8)的解。可以证明 $^{①}$

$$
\varepsilon = 0. 0 2, \quad P = \left[ \begin{array}{l l} {0. 4 9 4 6} & {0. 4 8 3 4} \\ {0. 4 8 3 4} & {1. 0 7 7 4} \end{array} \right], \quad L = \left[ \begin{array}{l l} {0. 2 9 4 6} & {- 0. 4 4 3 6} \end{array} \right], \quad W = \sqrt {2}
$$

满足方程组(7.6)\~(7.8)。因而 $V(x)=x^{T}Px$ 是系统的李雅普诺夫函数。由

$$\Omega_ {c} = \{x \in R ^ {2} \mid V (x) \leqslant c \}$$

可估计吸引区,其中 $c \leqslant \min_{|y| = 1.818} V(x) = 0.3445$ 保证了 $\Omega_{c}$ 在集合 $\{|y| \leqslant 1.818\}$ 内。取 c = 0.34 即给出估计值,如图 7.11 所示。

![](image/8bf6776e8299dcb7a3087985b5204249fd8db5a5d0b7e581652eff5ec57cd072.jpg)

<details>
<summary>contour</summary>

| Region | Value |
| --- | --- |
| y=-1.818 | -1.818 |
| y=1.818 | 1.818 |
| v(x)=0.34 | 0.34 |
</details>

图7.11 例7.4的吸引区
