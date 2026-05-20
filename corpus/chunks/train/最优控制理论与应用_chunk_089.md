若 $a > 0$ ，则上式将导致 $-1 > 0$ ，发生矛盾。若 $a < 0$ ，则 $\frac{2a - 1}{2a} > 1$ 可成立， $\pmb{K}$ 可正定。而由式(5-39)， $a < 0$ 时，不可控的状态 $x_{2}(t)$ 是稳定的，即系统满足可稳的要求，于是存在正定的最优反馈增益阵 $\pmb{K}$ 。

最优控制可计算如下：

$$
\begin{array}{l} u (t) = - \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K X} (t) = - [ 1 0 ] \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] \\ = - k _ {1 1} x _ {1} (t) - k _ {1 2} x _ {2} (t) = - x _ {1} (t) - \frac {1}{1 - a} x _ {2} (t) \tag {5-48} \\ \end{array}
$$

最优闭环系统为

$$\dot {x} _ {1} (t) = - x _ {1} (t) - \frac {a}{1 - a} x _ {2} (t) \tag {5-49}\dot {x} _ {2} (t) = a x _ {2} (t)$$

闭环系统矩阵为

$$
\boldsymbol {A} _ {\mathrm{CL}} = \left[ \boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} \right] = \left[ \begin{array}{c c} - 1 & - \frac {a}{1 - a} \\ 0 & a \end{array} \right] \tag {5-50}
$$

它的特征根为

$$\lambda_ {1} = - 1 \quad \lambda_ {2} = a \tag {5-51}$$

当 a<0 时,闭环系统也是稳定的。
