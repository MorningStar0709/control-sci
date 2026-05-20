$$
\left\{ \begin{array}{l} A _ {c} = (\overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2}) + (\overline {{{B}}} _ {2} - G _ {2} \overline {{{B}}} _ {1}) F _ {c}, \\ B _ {c} = (\overline {{{A}}} _ {2 1} - G _ {2} \overline {{{A}}} _ {1 1}) + (\overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2}) G _ {2} + (\overline {{{B}}} _ {2} - G _ {2} \overline {{{B}}} _ {1}) F, \end{array} \right. \tag {1.8.23}
$$

那么方程 (1.8.17) 又可写成

$$\dot {x} _ {c} (t) = A _ {c} x _ {c} (t) + B _ {c} y (t). \tag {1.8.24}$$

由此及式 (1.8.22) 便给出动态补偿器

$$
\left\{ \begin{array}{l} \dot {x} _ {c} (t) = A _ {c} x _ {c} (t) + B _ {c} y (t), \\ u (t) = F _ {c} x _ {c} (t) + F y (t). \end{array} \right. \tag {1.8.25}
$$

这是一个 $n - m$ 阶系统. 将它代入系统 (1.6.1) 得到闭环系统为

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {\overline {{{x}}}} (t) \\ \dot {\overline {{{x}}}} _ {c} (t) \end{array} \right] = \left[ \begin{array}{c c} A + B F C & B F _ {c c} \\ B _ {c c} C & A _ {c c} \end{array} \right] \left[ \begin{array}{c} x (t) \\ x _ {c c} (t) \end{array} \right],} \\ y (t) = C x (t). \end{array} \right. \tag {1.8.26}
$$

现在，需要说明系统 (1.8.26) 是内部稳定的，从而动态补偿器 (1.8.25) 是合乎要求的。为此令

$$
\boldsymbol {P} = \left[ \begin{array}{c c} \boldsymbol {C} _ {1} & \boldsymbol {C} _ {2} \\ 0 & \boldsymbol {I} _ {n - m} \end{array} \right], \quad e (t) = \left[ \begin{array}{l l} - \boldsymbol {G} _ {2} & \boldsymbol {I} _ {n - m} \end{array} \right] \boldsymbol {P x} (t) - x _ {c} (t).
$$

由式 (1.8.13) 和式 (1.8.17) 的第一式直接计算可得

$$e (t) = \overline {{{x}}} _ {2} (t) - \overline {{{x}}} _ {2 e}.$$

对 $e(t)$ 取导数并利用式(1.8.14)和式(1.8.24)得

$$
\begin{array}{l} \dot {e} (t) = \left[ - G _ {2} \quad I _ {n - m} \right] \dot {\overline {{{x}}}} (t) - \dot {x} _ {c} (t), \\ = \left[ - G _ {2} \quad I _ {n - m} \right] \overline {{{A}}} \bar {x} (t) + \left[ - G _ {2} \quad I _ {n - m} \right] \overline {{{B}}} u (t) - A _ {c} x _ {c} (t) - B _ {c} y (t). \\ \end{array}
$$

将 $A_{c}$ 和 $B_{c}$ 的表达式(1.8.23)代入上式可以算出

$$\dot {e} (t) = (\overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2}) e (t). \tag {1.8.27}$$

对系统 (1.8.26) 作坐标变换

$$
\left[ \begin{array}{c} {\overline {{{x}}} (t)} \\ {e (t)} \end{array} \right] = \left[ \begin{array}{c c} {P} & {0} \\ {[ - G _ {2} I _ {n - m} ] P} & {- I _ {n - m}} \end{array} \right] \left[ \begin{array}{c} {x (t)} \\ {x _ {c} (t)} \end{array} \right],
$$

即

$$\overline {{{x}}} (t) = P x (t),e (t) = \left[ - G _ {2} \quad I _ {n - m} \right] x (t) - x _ {c} (t),$$

于是
