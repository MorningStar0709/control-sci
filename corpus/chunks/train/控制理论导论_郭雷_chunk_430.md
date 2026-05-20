# 6.2 $H_{\infty}$ 范数的等价条件

定义 6.2.1 设 $A \in R^{n \times n}$ 为定常矩阵。若 A 的特征值的实部均为负，即 $\operatorname{Re} \lambda_{i}(A) < 0, (i = 1, 2, \cdots, n)$ ，则称该矩阵是稳定的，简称稳定阵。

根据上述定义，如果 $\{A, B, C, D\}$ 是传递函数阵 $G(s)$ 的最小实现，那么 $A$ 是稳定阵当且仅当 $G(s) \in RH_{\infty}^{r \times q}$ . 下面的定理给出了有理函数阵 $G(s)$ 的 $H_{\infty}$ 范数小于 1 的判定条件.

定理6.2.1 设 $G(s) = \{A, B, C, 0\}$ , 则下述命题等价:

(1) $A$ 是稳定阵，且 $\| G(\cdot)\|_{\infty} < 1;$

(2) 代数 Riccati 方程

$$A ^ {\mathrm{T}} X + X A + X B B ^ {\mathrm{T}} X + C ^ {\mathrm{T}} C = 0 \tag {6.2.1}$$

有半正定解 $X \geqslant 0$ ，且 $A + BB^{\mathrm{T}}X$ 是稳定阵；

(3) $A$ 是稳定阵，且如下定义的Hamilton矩阵 $\pmb{H}$ 在虚轴上无特征值：

$$
H = \left[ \begin{array}{c c} A & B B ^ {\mathrm{T}} \\ - C ^ {\mathrm{T}} C & - A ^ {\mathrm{T}} \end{array} \right]. \tag {6.2.2}
$$

证明 以下依 (1) $\Longrightarrow$ (3) $\Longrightarrow$ (2) $\Longrightarrow$ (1) 的顺序来证明该定理.

(1) $\Longrightarrow$ (3). 容易验证, Hamilton 矩阵 $H$ 是传递函数阵 $T(s) = (I - G^{\mathrm{T}}(-s)\cdot G(s))^{-1}$ 的状态空间实现的系统阵, 即

$$T (s) = \left(I - G ^ {\mathrm{T}} (- s) G (s)\right) ^ {- 1} = I + C _ {h} (s I - H) ^ {- 1} B _ {h}, \tag {6.2.3}$$

其中

$$
C _ {h} = \left[ \begin{array}{l l} 0 & B ^ {\mathrm{T}} \end{array} \right], \quad B _ {h} = \left[ \begin{array}{l} B \\ 0 \end{array} \right].
$$

由于 $A$ 是稳定阵，可以验证，在虚轴上 $(C_h, H)$ 和 $(H, B_h)$ 分别是能观测和能控的。这表明 $T(s)$ 在虚轴上无零极点相消。故 $\mathrm{j}\omega$ 是 $H$ 的特征值当且仅当 $T(s)$ 在虚轴上有极点。

若命题 (1) 成立，那么根据 $H_{\infty}$ 范数的定义有

$$I - G ^ {\mathrm{T}} (- \mathrm{j} \omega) G (\mathrm{j} \omega) > 0, \quad \forall \omega \in \mathbb {R}.$$

所以 $|I - G^{\mathrm{T}}(-\mathrm{j}\omega)G(\mathrm{j}\omega)| \neq 0, \forall \omega \in \mathbb{R}$ , 即 $T(s)$ 在虚轴上无极点, 从而命题 (3) 成立.

(3) $\Longrightarrow$ (2). 设 $A$ 是 $n \times n$ 矩阵. 由于式 (6.2.2) 定义的 Hamilton 矩阵的特征值是关于原点对称分布的 (证明参见文献 [15] 的引理 2.3.1), 所以当 $H$ 在虚轴上无特征值时, $H$ 在左、右半平面各有 $n$ 个特征值.

令 $\lambda_{1},\cdots,\lambda_{n}$ 是 H 的位于左半平面的 n 个特征值， $v_{1},\cdots,v_{n}\in R^{2n}$ 是相应的特征向量（若 $\lambda_{i}$ 重根，则取广义特征向量），则有

$$H V = V J, \qquad V = [ v _ {1} v _ {2} \dots v _ {n} ], \tag {6.2.4}$$

其中 $J \in R^{n \times n}$ 是 $\lambda_{i}(i = 1, 2, \cdots, n)$ 对应的 Jordan 标准块.

现将 $2n \times n$ 矩阵 $V$ 分块如下：

$$
V = \left[ \begin{array}{c} T _ {1} \\ T _ {2} \end{array} \right], \qquad T _ {1} \in \mathbb {R} ^ {n \times n}, T _ {2} \in \mathbb {R} ^ {n \times n}.
$$

如果 $T_{1}$ 是非奇异阵，那么由式(6.2.4)得

$$
H \left[ \begin{array}{l} I \\ X \end{array} \right] = \left[ \begin{array}{l} I \\ X \end{array} \right] T _ {1} J T _ {1} ^ {- 1}, \quad X = T _ {2} T _ {1} ^ {- 1}.
$$
