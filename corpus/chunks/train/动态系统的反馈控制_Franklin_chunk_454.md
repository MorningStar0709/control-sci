# 例 7.25 摆的降阶估计器设计

为摆设计一个降阶估计器，其误差极点为 $-10\omega_{0}$ 。

解答。系统方程为

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ - \omega_ {0} ^ {2} & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right]
$$

分块后的矩阵为

$$
\left[ \begin{array}{c c} A _ {\mathrm{aa}} & A _ {\mathrm{ab}} \\ A _ {\mathrm{ba}} & A _ {\mathrm{bb}} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \omega_ {0} ^ {2} & 0 \end{array} \right]

\left[ \begin{array}{c} B _ {\mathrm{a}} \\ \boldsymbol {B} _ {\mathrm{b}} \end{array} \right] = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

由式 $(7.155)$ 得到由L表示的特征方程：

$$s - (0 - L) = 0$$

将上式的特征方程与期望方程

$$\alpha_ {\mathrm{e}} (s) = s + 1 0 \omega_ {0} = 0$$

相比较得

$$L = 1 0 \omega_ {0}$$

根据式 $(7.158)$ 得估计器方程为

$$\dot {x} _ {\mathrm{c}} = - 1 0 \omega_ {0} \hat {x} _ {2} - \omega_ {0} ^ {2} y + u$$

并且由式(7.157)得状态估计为

$$\hat {x} _ {2} = x _ {\mathrm{c}} + 1 0 \omega_ {0} y$$

使用先前例题中给出的控制律。图 7.33 给出了 $\omega_{0}=1$ 时，被控对象初始条件为$x_{0}=[1.0\quad0.0]^{T}$ 和估计器初始条件为 $x_{c0}=0$ 的曲线。该响应曲线可由 Matlab 中的 impulse 或 initial 函数得到。注意观察该初始条件响应曲线与图 7.30 所示的全阶估计器的响应曲线的相似之处。

使用如下的 Matlab 语句得到降阶估计器的增益：

$$\mathrm{Lt} = \text { acker } (\mathrm{Abb} ^ {\prime}, \mathrm{Aab} ^ {\prime}, \mathrm{pe}),\mathrm{Lt} = \text { place } (\mathrm{Abb} ^ {\prime}, \mathrm{Aab} ^ {\prime}, \mathrm{pe}),L = L t ^ {\prime}.$$

降阶估计器的存在条件与全阶估计器的存在条件相同，即可以证明 $(A_{bb}, A_{ab})$ 的可观测性与 $(A, C)$ 的可观测性相同。
