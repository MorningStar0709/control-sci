极小。式中， $\hat{z}=1(t)$ 为理想输出。

解 本例为无限时间定常输出跟踪系统问题,可按如下步骤求解:

1）系统状态空间建模。由于传递函数

$$G (s) = \frac {Y (s)}{U (s)} = \frac {4}{s ^ {2}}$$

可得 $\dot{x}_1(t) = x_2(t),\quad \dot{x}_2(t) = 4u(t),\quad y(t) = x_1(t)$

于是 $\pmb {A} = \left[ \begin{array}{ll}0 & 1\\ 0 & 0 \end{array} \right],\qquad \pmb {b} = \left[ \begin{array}{ll}0\\ 4 \end{array} \right],\qquad \pmb {c} = [10]$

检验 $G(s) = c(sI - A)^{-1}b = \frac{4}{s^2}$

2）检验可控性与可观性。性能指标又可表示为

$$J = \frac {1}{2} \int_ {0} ^ {\infty} \left\{2 [ \hat {z} - y (t) ] ^ {2} + 2 u ^ {2} (t) \right\} d t$$

故有 $r = q = 2, \quad c^{\mathrm{T}}qc = \begin{bmatrix} 2 & 0 \\ 0 & 0 \end{bmatrix}$

因为 $\operatorname{rank}[\pmb{b}\pmb{A}\pmb{b}] = \operatorname{rank}\begin{bmatrix} 0 & 4 \\ 4 & 0 \end{bmatrix} = 2$

$$
\operatorname{rank} \left[ \begin{array}{l} c \\ c A \end{array} \right] = \operatorname{rank} \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] = 2
$$

故 $\{A,b\}$ 可控， $\{A,c\}$ 可观。

3) 解里卡蒂方程。令

$\hat{P}=\begin{bmatrix}P_{11}&P_{12}\\ P_{12}&P_{22}\end{bmatrix},$ 由式(10-134)得

$$- 8 P _ {1 2} ^ {2} + 2 = 0P _ {1 1} - 8 P _ {1 2} P _ {2 2} = 02 P _ {1 2} - 8 P _ {2 2} ^ {2} = 0$$

联立解出

$$
\hat {\boldsymbol {P}} = \left[ \begin{array}{c c} \sqrt {2} & \frac {1}{2} \\ \frac {1}{2} & \frac {\sqrt {2}}{4} \end{array} \right] > \mathbf {0}
$$

4）求伴随常向量。

$$
\hat {\boldsymbol {g}} = (\hat {\boldsymbol {P b r}} ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} - \boldsymbol {A} ^ {\mathrm{T}}) ^ {- 1} \boldsymbol {c} ^ {\mathrm{T}} q \hat {\boldsymbol {z}} = \left[ \begin{array}{l} \sqrt {2} \\ \frac {1}{2} \end{array} \right]
$$

5) 确定近似最优控制。

$$
\begin{array}{l} \hat {u} ^ {*} (t) = - r ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} \hat {\boldsymbol {P}} \boldsymbol {x} (t) + r ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} \hat {\boldsymbol {g}} \\ = - x _ {1} (t) - \frac {\sqrt {2}}{2} x _ {2} (t) + 1 \\ = - y (t) - \frac {\sqrt {2}}{2} \dot {y} (t) + 1 \\ \end{array}
$$

6）检验闭环输出跟踪系统的稳定性。闭环系统的系统矩阵为

$$
\bar {\boldsymbol {A}} = (\boldsymbol {A} - \boldsymbol {b r} ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} \hat {\boldsymbol {P}}) = \left[ \begin{array}{c c} 0 & 1 \\ - 4 & - 2 \sqrt {2} \end{array} \right]
$$

特征方程 $\operatorname{det}(\lambda I - \overline{A}) = \lambda^2 + 2\sqrt{2}\lambda + 4 = 0$

解得特征值 $\lambda_{1} = -\sqrt{2} +\mathrm{j}\sqrt{2},\quad \lambda_{2} = -\sqrt{2} -\mathrm{j}\sqrt{2}$

故闭环输出跟踪系统渐近稳定。
