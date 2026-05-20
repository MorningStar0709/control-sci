![](image/df2d11d39f3f66057e40a75b4411d5d2cac5815c164e5193ef4a92eb9e9a53f9.jpg)

<details>
<summary>text_image</summary>

y
aₚ
初始视线
aₑ
</details>

图10-5 追-逃问题示意图

追逐者希望使用(其控制量决策) $a_{p}$ 使终端脱靶量 $|y(t_{\mathrm{f}})|$ 最小；而逃逸者则希望使用控制量 $a_{e}$ 使得 $|y(t_{\mathrm{f}})|$ 最大。故性能指标可选为：

$$J = \frac {1}{2} y ^ {2} \left(t _ {\mathrm{f}}\right) \tag {10-67}$$

追逐者和逃逸者的加速度都有限：

$$
\left. \begin{array}{l} \mid a _ {p} \mid \leqslant a _ {p m} \\ \mid a _ {e} \mid \leqslant a _ {e m} \end{array} \right\} \text {且} a _ {p m} > a _ {e m} \tag {10-68}
$$

下面来寻求最优对策解。首先构成哈密顿函数，令

$$\boldsymbol {x} = [ \gamma , \dot {\gamma} ] ^ {\mathrm{T}}, \boldsymbol {\lambda} ^ {\mathrm{T}} = [ \lambda_ {\gamma}, \lambda_ {\nu} ], \boldsymbol {f} (x) = [ v _ {\gamma}, \dot {v} _ {\gamma} ] ^ {\mathrm{T}},$$

则

$$H = \boldsymbol {\lambda} ^ {T} f (x) = \lambda_ {y} v _ {y} + \lambda_ {v} \left(a _ {p} - a _ {e}\right) \tag {10-69}$$

注意到这里哈密顿函数是控制量 $a_{p}$ 和 $a_{e}$ 的线性函数。

共轭方程为

$$
\left[ \begin{array}{l} \dot {\lambda} _ {y} \\ \dot {\lambda} _ {v} \end{array} \right] = - \frac {\partial H}{\partial x} = - \left[ \begin{array}{l} 0 \\ \lambda_ {y} \end{array} \right]
$$

于是，

$$
\left\{ \begin{array}{l} \dot {\lambda} _ {v} = - \lambda_ {y}, \lambda_ {v} \left(t _ {\mathrm{f}}\right) = 0 \\ \dot {\lambda} _ {y} = 0, \quad \lambda_ {y} \left(t _ {\mathrm{f}}\right) = y \left(t _ {\mathrm{f}}\right) \end{array} \right. \tag {10-70}
$$

而最优策略可由式(10-69)所示的哈密顿函数 $H$ 取极值得到，为

$$a _ {p} (t) = - a _ {p m} \operatorname{sgn} \lambda_ {v} \tag {10-71}a _ {e} (t) = - a _ {e m} \operatorname{sgn} \lambda_ {v}$$

将 $(10-70)$ 积分,得

$$\lambda_ {y} (t) = \lambda_ {y} \left(t _ {\mathrm{f}}\right) = y \left(t _ {\mathrm{f}}\right) = \text {常值} \tag {10-72}\lambda_ {v} (t) = - \left(t - t _ {\mathrm{f}}\right) \lambda_ {y} (t) = \left(t - t _ {\mathrm{f}}\right) y \left(t _ {\mathrm{f}}\right)$$

由上式,有

$$\operatorname{sgn} \lambda_ {v} (t) = \operatorname{sgn} y \left(t _ {\mathrm{f}}\right) \tag {10-73}$$

将式(10-73)代入式(10-72)和式(10-71)，并将所得的 $a_{p}$ 和 $a_{e}$ 代入运动方程(10-66)，再积分之，可得其解为：

$$y \left(t _ {\mathrm{f}}\right) = v _ {0} \left(t _ {\mathrm{f}} - t _ {0}\right) - \frac {1}{2} \left(a _ {p m} - a _ {e m}\right) \left(t _ {\mathrm{f}} - t _ {0}\right) ^ {2} \operatorname{sgn} y \left(t _ {\mathrm{f}}\right) \tag {10-74}$$

由上式右端可见,若
