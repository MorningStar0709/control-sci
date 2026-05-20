为了用 $-\left(x_{1}^{2} + x_{2}^{4}\right) / 2$ 去控制 $|x_{2}|^{3}|u|$ 一项，把前面的不等式重写为

$$\dot {V} \leqslant - \frac {1}{2} (1 - \theta) (x _ {1} ^ {2} + x _ {2} ^ {4}) - \frac {1}{2} \theta (x _ {1} ^ {2} + x _ {2} ^ {4}) + | x _ {2} | ^ {3} | u |$$

其中 $0 < \theta < 1$ 。如果 $|x_{2}| \geqslant 2|u| / \theta$ 或 $|x_{2}| \leqslant 2|u| / \theta$ 和 $|x_{1}| \geqslant (2|u| / \theta)^{2}$ ，则

$$- \frac {1}{2} \theta (x _ {1} ^ {2} + x _ {2} ^ {4}) + | x _ {2} | ^ {3} | u | \leqslant 0$$

上述条件可表示为 $\max \{|x_1|, |x_2|\} \geqslant \max \left\{\frac{2|u|}{\theta}, \left(\frac{2|u|}{\theta}\right)^2\right\}$

利用范数 $\| x\|_{\infty} = \max \{|x_1|,|x_2|\}$ ，并定义K类函数 $\rho$ 为

$$\rho (r) = \max \left\{\frac {2 r}{\theta}, \left(\frac {2 r}{\theta}\right) ^ {2} \right\}$$

由此可知，当 $\dot{V} \leqslant -\frac{1}{2}(1 - \theta)(x_1^2 + x_2^4), \forall \| x \|_{\infty} \geqslant \rho(|u|)$

时,满足不等式(4.49)。由于 $V(x)$ 是正定的且径向无界,所以不等式(4.48)由引理4.3得出。因此系统是输入-状态稳定的。假设希望找到K类函数 $\gamma$ ,就需要找出 $\alpha_{1}$ 和 $\alpha_{2}$ 。不难看出

$$
V (x) = \frac {1}{2} x _ {1} ^ {2} + \frac {1}{4} x _ {2} ^ {4} \leqslant \frac {1}{2} \| x \| _ {\infty} ^ {2} + \frac {1}{4} \| x \| _ {\infty} ^ {4}
V (x) = \frac {1}{2} x _ {1} ^ {2} + \frac {1}{4} x _ {2} ^ {4} \geqslant \left\{ \begin{array}{l l} \frac {1}{2} | x _ {1} | ^ {2} = \frac {1}{2} \| x \| _ {\infty} ^ {2}, & | x _ {2} | \leqslant | x _ {1} | \\ \frac {1}{4} | x _ {2} | ^ {4} = \frac {1}{4} \| x \| _ {\infty} ^ {4}, & | x _ {2} | \geqslant | x _ {1} | \end{array} \right.
$$

$\mathcal{K}_{\infty}$ 类函数 $\alpha_{1}(r) = \min \left\{\frac{1}{2} r^{2},\frac{1}{4} r^{4}\right\},$ $\alpha_{2}(r) = \frac{1}{2} r^{2} + \frac{1}{4} r^{4}$

满足不等式(4.48)。于是， $\gamma(r) = \alpha_{1}^{-1}(\alpha_{2}(\rho(r)))$ ，其中

$$
\alpha_ {1} ^ {- 1} (s) = \left\{ \begin{array}{l l} (4 s) ^ {\frac {1}{4}}, & \quad s \leqslant 1 \\ \sqrt {2 s}, & \quad s \geqslant 1 \end{array} \right.
$$

函数 $\gamma$ 与 $\|x\|$ 的选择有关。我们已选择了另一个 p 范数，并得到了不同的 $\gamma$ 。

△

输入-状态稳定性概念的一个很有意义的应用表现在对级联系统

$$\dot {x} _ {1} = f _ {1} (t, x _ {1}, x _ {2}) \tag {4.51}\dot {x} _ {2} = f _ {2} (t, x _ {2}) \tag {4.52}$$

的稳定性分析中。式中 $f_{1}:[0,\infty)\times R^{n_{1}}\times R^{n_{2}}\to R^{n_{1}}$ 和 $f_{2}:[0,\infty)\times R^{n_{2}}\to R^{n_{2}}$ 是 $t$ 的分段连续函数，对 $x = \begin{bmatrix} x_1\\ x_2 \end{bmatrix}$ 是局部利普希茨的。假设

$$\dot {x} _ {1} = f _ {1} (t, x _ {1}, 0)$$

和式(4.52)都在其原点有全局一致渐近稳定平衡点,那么在什么条件下级联系统的原点 x=0 也具有同样的性质呢?下面的引理将说明,如果把 $x_{2}$ 作为输入时系统(4.51)是输入-状态稳定的,就是这种情况。
