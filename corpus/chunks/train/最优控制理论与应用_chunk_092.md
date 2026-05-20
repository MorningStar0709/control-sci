$$
\begin{array}{l} \boldsymbol {X} (k + 1) = \boldsymbol {A} (k) \boldsymbol {X} (k) + \boldsymbol {B} (k) \boldsymbol {U} (k) \\ = \boldsymbol {A} (k) \boldsymbol {X} (k) - \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {X} (k + 1) \\ \end{array}
$$

所以

$$\boldsymbol {X} (k + 1) = [ \boldsymbol {I} + \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) ] ^ {- 1} \boldsymbol {A} (k) \boldsymbol {X} (k)$$

把上式代入式(5-59)并消去等式两端的 $X(k)$ , 可得 $K(k)$ 必须满足下面的黎卡提矩阵差分方程

$$
\begin{array}{l} \boldsymbol {K} (k) = \boldsymbol {Q} (k) + \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) [ \boldsymbol {I} + \\ \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) ] ^ {- 1} \boldsymbol {A} (k) \tag {5-60} \\ \end{array}
$$

对上式方括号部分应用矩阵求逆引理。

$$(A + B C) ^ {- 1} = A ^ {- 1} - A ^ {- 1} B (I + C A ^ {- 1} B) ^ {- 1} C A ^ {- 1}$$

令 $\mathbf{A} = \mathbf{I},\mathbf{B} = \mathbf{B}(k),\mathbf{C} = \mathbf{R}^{-1}(k)\mathbf{B}^{\mathrm{T}}(k)\mathbf{K}(k + 1)$

可得矩阵黎卡提差分方程的另一形式

$$\boldsymbol {K} (k) = \boldsymbol {Q} (k) + \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) - \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {B} (k) [ \boldsymbol {R} (k) +\boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {B} (k) ] ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) \tag {5-61}$$

黎卡提方程的终端条件为

$$\boldsymbol {K} (N) = \boldsymbol {P} (N) \tag {5-62}$$

从 k=N 开始反向递推计算式(5-60)即可决定 $K(k)$ 。 $K(k)$ 求出后，下面来决定 $U(k)$ 。由式(5-55)得

$$
\begin{array}{l} \boldsymbol {\lambda} (k + 1) = \left(\boldsymbol {A} ^ {\mathrm{T}} (k)\right) ^ {- 1} [ \boldsymbol {\lambda} (k) - \boldsymbol {Q} (k) \boldsymbol {X} (k) ] \\ = \boldsymbol {A} ^ {- T} (k) [ \boldsymbol {K} (k) - \boldsymbol {Q} (k) ] \boldsymbol {X} (k) \\ \end{array}
$$

因而由(5-57)得

$$\boldsymbol {U} (k) = - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {A} ^ {- \mathrm{T}} (k) [ \boldsymbol {K} (k) - \boldsymbol {Q} (k) ] \boldsymbol {X} (k) \tag {5-63}$$

式(5-63)可化为另一形式,将式(5-60)代入式(5-63)并利用式(5-61)得
