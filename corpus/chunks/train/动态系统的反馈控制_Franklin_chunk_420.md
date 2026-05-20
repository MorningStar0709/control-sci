# 例7.11 由状态描述得到的热系统传递函数

用式(7.45)求出由式(7.12a)和式(7.12b)所描述热系统的传递函数。

解答。系统的状态变量描述矩阵分别为

$$
\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c} - 7 & - 1 2 \\ 1 & 0 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \\ \boldsymbol {C} = \left[ \begin{array}{l l} 1 & 2 \end{array} \right], \quad D = 0 \\ \end{array}
$$

根据式 $(7.45)$ 计算传递函数，我们有

$$
s \boldsymbol {I} - \boldsymbol {A} = \left[ \begin{array}{c c} s + 7 & 1 2 \\ - 1 & s \end{array} \right]
$$

计算

$$
(s \mathbf {I} - \mathbf {A}) ^ {- 1} = \frac {\left[ \begin{array}{c c} s & - 1 2 \\ 1 & s + 7 \end{array} \right]}{s (s + 7) + 1 2} \tag {7.46}
$$

然后，将式 $(7.46)$ 代入到式 $(7.45)$ ，得到

$$
\begin{array}{l} G (s) = \frac {[ 1 - 2 ] \left[ \begin{array}{c c} s & - 1 2 \\ 1 & s + 7 \end{array} \right] \left[ \begin{array}{l} 1 \\ 0 \end{array} \right]}{s (s + 7) + 1 2} (7.47) \\ = \frac {[ 1 - 2 ] \left[ \begin{array}{l} s \\ 1 \end{array} \right]}{s (s + 7) + 1 2} (7.48) \\ = \frac {(s + 2)}{(s + 3) (s + 4)} (7.49) \\ \end{array}
$$

这些结果也可以由如下的 Matlab 语句得到：

$$[ \text { num }, \text { den } ] = \text { ss2tf } (A, B, C, D)$$

并且通过执行上述语句得到 num=[0 1 2] 和 den=[1 7 12]，这与上面手工计算的结果是一致的。

因为式(7.45)给出的传递函数是由一般状态空间描述矩阵 A、B、C 和 D 表示的，所

457

458

以，可以依据这些矩阵表示出系统的零点和极点。我们早就看出将状态矩阵变换为对角形式，极点会作为特征值出现在 A 矩阵的主对角线上。现在从系统理论的观点，考察系统暂态响应中所涉及的零极点的情况。

由第3章可知，传递函数 $G(s)$ 的一个极点是广义频率 $s$ 的一个值，使得如果 $s = p_{i}$ ，那么系统在没有强迫函数 $u$ 的情况下，可以按照 $K_{i}e^{p_{i}t}$ 对某个初始状态响应。本文中，称 $p_{i}$ 为系统的自然频率或者自然模态。如果我们取状态空间式(7.18a)和式(7.18b)，且将强迫函数 $u$ 设置为0，则有

$$\dot {x} = A x \tag {7.50}$$

如果假设某个(仍然未知)初始条件为

$$\boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {7.51}$$

并且假定整个状态运动行为根据同一自然频率进行的，那么状态就可以表示为 $X(t)=\mathrm{e}^{\beta_{1}t}x_{0}$ ，由式(7.50)可得：

$$\dot {\boldsymbol {x}} (t) = p _ {i} \mathrm{e} ^ {p _ {i} t} \boldsymbol {x} _ {0} = \boldsymbol {A x} = \boldsymbol {A} \mathrm{e} ^ {p _ {i} t} \boldsymbol {x} _ {0} \tag {7.52}$$

或者

$$\boldsymbol {A} \boldsymbol {x} _ {0} = p _ {\mathrm{i}} \boldsymbol {x} _ {0} \tag {7.53}$$

式 $(7.53)$ 可以改写为

$$(p _ {i} \boldsymbol {I} - \boldsymbol {A}) \boldsymbol {x} _ {0} = 0 \tag {7.54}$$

式(7.53)和式(7.54)构成了我们在式(7.35)中遇到的特征矢量/特征值的问题，在式(7.35)中，矩阵A的特征值 $p_{i}$ ，对应的特征矢量为 $x_{0}$ 。如果我们仅仅对特征值感兴趣，那么可以利用非零矢量 $x_{0}$ ，当且仅当下式成立时，式(7.54)才有解：

$$\det (p _ {i} \boldsymbol {I} - \boldsymbol {A}) = 0 \tag {7.55}$$
