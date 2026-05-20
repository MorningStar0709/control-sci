表明 $\Psi(t + T)$ 也是 $\dot{\pmb{x}} = A(t)\pmb{x}$ 的一个基本解阵。

(2) 存在一个常值矩阵 $\vec{A}$ ，使成立

$$\Psi (t + T) = \Psi (t) e ^ {A T} \tag {2.121}$$

我们来证明这一论断的正确性。首先， $\Psi(t)$ 和 $\Psi(t + T)$ 对所有 $t$ 均为非奇异，因此它们的列向量可分别构成解空间的两组基底。利用换基关系式可知，必存在一个非奇异常值矩阵 $Q$ ，使有

$$\Psi (t + T) = \Psi (t) Q \tag {2.122}$$

进而，设 $Q$ 的特征值 $\lambda_1, \lambda_2, \cdots, \lambda_n$ 为两两相异（如若不是这种情况，下面的证明过程是类同的，但形式和符号上要复杂一些），且因 $Q$ 为非奇异有 $\lambda_i \neq 0 (i = 1, 2, \cdots, n)$ ，从而存在非奇异常阵 $F$ 使成立

$$
Q = F \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \ddots & \\ & & \lambda_ {n} \end{array} \right] F ^ {- 1} = F \left[ \begin{array}{c c c} e ^ {\beta_ {1} T} & & \\ & \ddots & \\ & & e ^ {\beta_ {n} T} \end{array} \right] F ^ {- 1}
= e ^ {A T} \tag {2.123}
$$

其中

$$
\beta_ {i} = \ln \lambda_ {i} / T, \quad i = 1, 2, \dots , n \tag {2.124}
\bar {A} = F \left[ \begin{array}{c c c} \beta_ {1} & & \\ & \ddots & \\ & & \beta_ {n} \end{array} \right] F ^ {- 1} \tag {2.125}
$$

于是，由（2.122）、（2.123）和（2.125）即可导出式（2.121）。

(3) 对时变系统 (2.118)，设变换阵 $P(t)$ 和 $\dot{P}(t)$ 在 $[t_0, \infty)$ 上连续和有界，且对所有 $t \geqslant t_0$ 成立

$$\left| \det P (t) \right| > \eta > 0 \tag {2.126}$$

其中 $\eta$ 为实常数，现作变换 $x = P(t)x$ 而导出

$$
\begin{array}{l} \dot {\bar {x}} = \bar {A} (t) \bar {x} + \bar {B} (t) u \\ \therefore \quad \bar {B} (t) = 1 - \bar {B} (t). \end{array} \tag {2.127}
y = \bar {C} (t) \bar {x} + \bar {D} (t) u
$$

其中

$$
\overline {{A}} (t) = P (t) A (t) P ^ {- 1} (t) + \dot {P} (t) P ^ {- 1} (t)
\begin{array}{l} \overline {{{B}}} (t) = P (t) B (t) \\ \overline {{{B}}} (t) = P (t) B (t) \end{array} \tag {2.128}
\overline {{{C}}} (t) = C (t) P ^ {- 1} (t)\overline {{D}} (t) = D (t)
$$

则称系统 $(\overline{A}(t), \overline{B}(t), \overline{C}(t), \overline{D}(t))$ 和 $(A(t), B(t), C(t), D(t))$ 之间是李亚普诺夫（A. M. Ляпунов）意义下等价的，并称满足上述条件的变换矩阵 $P(t)$ 为李亚普诺夫变换阵。对线性时变系统作李亚普诺夫变换其稳定性保持不变，但一般的等价变换并不能保证这一点。

(4) 对 $A(\cdot)$ 为周期变化的线性时变系统 (2.118)，作变换 $\bar{x} = P(t)x$ ，其中变换矩阵取为

$$P (t) = e ^ {2 t} \Psi^ {- 1} (t) \tag {2.129}$$

则变换后的状态空间描述具有如下形式：

$$
\begin{array}{l} \dot {\bar {x}} = \bar {A} \bar {x} + P (t) B (t) u \\ v = C (t) P ^ {- 1} (t) \bar {v} + D (t) v \end{array} \tag {2.130}
$$

其中 $\overline{A}$ 是一个常阵。

考虑到 $\vec{D}(t) = D(t)$ ，而
