$$
\boldsymbol {A} ^ {- 1} = \left[ \begin{array}{c c} \boldsymbol {A} _ {1 1} ^ {- 1} + \boldsymbol {A} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2} \widetilde {\boldsymbol {A}} _ {2 2} ^ {- 1} \boldsymbol {A} _ {2 1} \boldsymbol {A} _ {1 1} ^ {- 1} & - \boldsymbol {A} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2} \widetilde {\boldsymbol {A}} _ {2 2} ^ {- 1} \\ - \widetilde {\boldsymbol {A}} _ {2 2} ^ {- 1} \boldsymbol {A} _ {2 1} \boldsymbol {A} _ {1 1} ^ {- 1} & \widetilde {\boldsymbol {A}} _ {2 2} ^ {- 1} \end{array} \right] \tag {1.1.6}
$$

或

$$
\boldsymbol {A} ^ {- 1} = \left[ \begin{array}{c c} \tilde {\boldsymbol {A}} _ {1 1} ^ {- 1} & - \tilde {\boldsymbol {A}} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2} \boldsymbol {A} _ {2 2} ^ {- 1} \\ - \boldsymbol {A} _ {2 2} ^ {- 1} \boldsymbol {A} _ {2 1} \tilde {\boldsymbol {A}} _ {1 1} ^ {- 1} & \boldsymbol {A} _ {2 2} ^ {- 1} \boldsymbol {A} _ {2 1} \tilde {\boldsymbol {A}} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2} \boldsymbol {A} _ {2 2} ^ {- 1} + \boldsymbol {A} _ {2 2} ^ {- 1} \end{array} \right], \tag {1.1.7}
$$

其中 $\widetilde{A}_{22} = A_{22} - A_{21}A_{11}^{-1}A_{12},\widetilde{A}_{11} = A_{11} - A_{12}A_{22}^{-1}A_{21}$

比较式 (1.1.6) 和式 (1.1.7) 得

$$\left(\boldsymbol {A} _ {1 1} - \boldsymbol {A} _ {1 2} \boldsymbol {A} _ {2 2} ^ {- 1} \boldsymbol {A} _ {2 1}\right) ^ {- 1} = \boldsymbol {A} _ {1 1} ^ {- 1} + \boldsymbol {A} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2} \left(\boldsymbol {A} _ {2 2} - \boldsymbol {A} _ {2 1} \boldsymbol {A} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2}\right) ^ {- 1} \boldsymbol {A} _ {2 1} \boldsymbol {A} _ {1 1} ^ {- 1}. \tag {1.1.8}$$

矩阵函数 设 $f(s)$ 是变量 $s$ 的函数, $\mathbf{X} \in \mathbb{C}^{n \times n}$ . 令 $s = \mathbf{X}$ , 得矩阵函数 $f(\mathbf{X})$ . 当 $f(s)$ 在 $s_0$ 附近解析时, $f(\mathbf{X})$ 可以展成一致收敛的幂级数

$$f (\boldsymbol {X}) = \sum_ {i = 0} ^ {\infty} p _ {i} (\boldsymbol {X} - s _ {0} \boldsymbol {I}) ^ {i}.$$

设 $f(s) = \sum_{i=0}^{\infty} p_i s^i$ , 当 $|s| < \rho$ ( $\rho$ 为收敛半径) 幂级数是收敛的, 那么对矩阵幂级数来说, 当 $X$ 的所有特征值的模都小于 $\rho$ 时, $\sum_{i=0}^{\infty} p_i X^i$ 收敛. 当 $X$ 有一个特征值的模大于 $\rho$ 时, $\sum_{i=0}^{\infty} p_i X^i$ 就发散.

由上述结果，易知

$$\sum_ {i = 0} ^ {\infty} \frac {1}{i !} X ^ {i}$$

对任意方阵 X 均收敛，把极限记为 $e^{X}$ ，即

$$\mathrm{e} ^ {X} \stackrel {\text { def }} {=} \sum_ {i = 0} ^ {\infty} \frac {1}{i !} X ^ {i}.$$

同样可定义

$$\ln (I + X) \stackrel {\mathrm{def}} {=} X - \frac {X ^ {2}}{2} + \frac {X ^ {3}}{3} + \dots$$

当 $X$ 的所有特征值的模都小于1时，该幂级数方阵收敛，而幂级数
