$$
- \left[ \begin{array}{l l} K _ {1 1} & K _ {1 2} \\ K _ {1 2} & K _ {2 2} \end{array} \right] \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l l} K _ {1 1} & K _ {1 2} \\ K _ {1 2} & K _ {2 2} \end{array} \right] + \left[ \begin{array}{l l} K _ {1 1} & K _ {1 2} \\ K _ {1 2} & K _ {2 2} \end{array} \right] \left[ \begin{array}{l} 0 \\ K _ {V} \end{array} \right] \frac {1}{b}

\left[ \begin{array}{l l} 0 & K _ {V} \end{array} \right] \left[ \begin{array}{c c} K _ {1 1} & K _ {1 2} \\ K _ {1 2} & K _ {2 2} \end{array} \right] - \left[ \begin{array}{l l} a & 0 \\ 0 & 0 \end{array} \right] = 0
$$

由上式可得到三个方程式

$$
\left\{ \begin{array}{l} a = \frac {1}{b} K _ {\nu} ^ {2} K _ {1 2} ^ {2} \\ K _ {1 1} = \frac {1}{b} K _ {\nu} ^ {2} K _ {1 2} K _ {2 2} \\ K _ {1 2} = \frac {1}{2 b} K _ {\nu} ^ {2} K _ {2 2} ^ {2} \end{array} \right.
$$

可解得， $K_{11} = K_{V}^{\frac{1}{2}}a^{\frac{3}{4}}b^{\frac{1}{4}},K_{12} = a^{\frac{1}{2}}b^{-\frac{1}{2}}K_{V}^{-\frac{1}{2}},K_{22} = 2^{\frac{1}{2}}a^{\frac{1}{4}}b^{\frac{3}{4}}K_{V}^{-\frac{3}{2}}$

将上面求到的 $K$ 代入式(8-72)，可求得稳态增益阵为

$$\boldsymbol {L} = \left[ \sqrt {\frac {a}{b}}, \sqrt {\frac {2}{K _ {v}}} \sqrt [ 4 ]{\frac {a}{b}} \right] = \left[ L _ {1}, L _ {2} \right]$$

于是由式(8-71)得

$$u = - L _ {1} \hat {x} _ {1} - L _ {2} \hat {x} _ {2} = - \sqrt {\frac {a}{b}} \hat {x} _ {1} - \sqrt {\frac {2}{K _ {v}}} \sqrt [ 4 ]{\frac {a}{b}} \hat {x} _ {2} \tag {8-74}$$

其中，滤波值由下面的卡尔曼滤波方程决定

$$\dot {\hat {X}} = A \hat {X} + B u + K _ {c} (Z - H \hat {X}) \tag {8-75}$$

其中,稳态卡尔曼滤波增益 $K_{c}$ 为

$$\boldsymbol {K} _ {C} = \boldsymbol {P} \boldsymbol {H} ^ {\mathrm{T}} \boldsymbol {R} ^ {- 1} \tag {8-76}$$

满足下面的矩阵黎卡提代数方程

$$\boldsymbol {A} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {A} ^ {\mathrm{T}} + \boldsymbol {Q} - \boldsymbol {P} \boldsymbol {H} ^ {\mathrm{T}} \boldsymbol {R} ^ {- 1} \boldsymbol {H} \boldsymbol {P} = \mathbf {0} \tag {8-77}$$

其中

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \quad \boldsymbol {P} = \left[ \begin{array}{l l} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] \quad \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ K _ {V} \end{array} \right]

\boldsymbol {Q} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & q _ {1} \end{array} \right] \quad \boldsymbol {H} = [ 1, 0 ], \quad \boldsymbol {R} = r _ {1}, \quad \boldsymbol {K} _ {c} = \left[ \begin{array}{l} K _ {c 1} \\ K _ {c 2} \end{array} \right]
$$

由上面的值代入式(8-77)求出 $\pmb{P}$ , 将 $\pmb{P}$ 代入式(8-76)求出 $K_{c}$ , 再代入式(8-75), 可得

$$\dot {\hat {x}} _ {1} = - K _ {c 1} \hat {x} _ {1} + \hat {x} _ {2} + K _ {c 1} Z \tag {8-78}\dot {\hat {x}} _ {2} = - 2 K _ {c 2} \hat {x} _ {1} + K _ {v} u + K _ {c 2} Z \tag {8-79}$$

其中，

$$K _ {c 1} = \sqrt {2} \cdot \sqrt [ 4 ]{\frac {q _ {1}}{r _ {1}}}, K _ {c 2} = \sqrt {\frac {q _ {1}}{r _ {1}}}$$

由式(8-78)、(8-79)解出 $\hat{x}_1, \hat{x}_2$ ，代入式(8-74)即可求出所需最优控制。
