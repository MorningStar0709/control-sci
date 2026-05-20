解 这里 $x(0), x(t_{\mathrm{f}})$ 均给定，故不需要横截条件式(3-24)。作哈密顿函数

$$H = \frac {1}{2} (x ^ {2} + u ^ {2}) + \lambda (- x + u)$$

则协态方程和控制方程为

$$
\begin{array}{l} \dot {\lambda} = - \frac {\partial H}{\partial x} = - x + \lambda \\ \frac {\partial H}{\partial u} = u + \lambda = 0 \\ \end{array}
$$

即

$$u = - \lambda$$

故可得正则方程

$$\dot {x} (t) = - x (t) - \lambda (t)\dot {\lambda} (t) = - x (t) + \lambda (t)$$

对正则方程进行拉氏变换,可得

$$s X (s) - x (0) = - X (s) - \lambda (s) \tag {3-25}s \lambda (s) - \lambda (0) = - X (s) + \lambda (s) \tag {3-26}$$

由式(3-25)可求得

$$X (s) = \frac {x (0) - \lambda (s)}{s + 1} \tag {3-27}$$

代入式 $(3-26)$ ，即得

$$(s ^ {2} - 2) \lambda (s) = (s + 1) \lambda (0) - x (0)$$

于是, 解出 $\lambda(s)$ 为

$$
\begin{array}{l} \lambda (s) = \frac {(s + 1) \lambda (0) - x (0)}{s ^ {2} - 2} \\ = \frac {s + 1}{(s + \sqrt {2}) (s - \sqrt {2})} \lambda (0) - \\ \end{array}
\frac {1}{(s + \sqrt {2}) (s - \sqrt {2})} x (0) \tag {3-28}
$$

反变换可求得

$$
\begin{array}{l} \lambda (t) = \frac {1}{2 \sqrt {2}} \left(\mathrm{e} ^ {- \sqrt {2} t} - \mathrm{e} ^ {\sqrt {2} t}\right) x (0) + \\ \frac {1}{2 \sqrt {2}} \left[ (\sqrt {2} - 1) e ^ {- \sqrt {2} t} + (\sqrt {2} + 1) e ^ {\sqrt {2} t} \right] \lambda (0) \tag {3-29} \\ \end{array}
$$

将式(3-28)代入式(3-26)可得

$$X (s) = \frac {s - 1}{(s + \sqrt {2}) (s - \sqrt {2})} x (0) - \frac {1}{(s + \sqrt {2}) (s - \sqrt {2})} \lambda (0)$$

故

$$
\begin{array}{l} x (t) = \frac {1}{2 \sqrt {2}} \left[ (\sqrt {2} + 1) e ^ {- \sqrt {2} t} + (\sqrt {2} - 1) e ^ {\sqrt {2} t} \right] x (0) + \\ \frac {1}{2 \sqrt {2}} \left[ e ^ {- \sqrt {2} t} - e ^ {\sqrt {2} t} \right] \lambda (0) \\ \end{array}
$$

由 $x(0) = 1, x(t_{\mathrm{f}}) = 0$ ，从上式可得

$$\lambda (0) = \frac {(\sqrt {2} + 1) e ^ {- \sqrt {2} t _ {\mathrm{f}}} + (\sqrt {2} - 1) e ^ {\sqrt {2} t _ {\mathrm{f}}}}{e ^ {\sqrt {2} t _ {\mathrm{f}}} - e ^ {- \sqrt {2} t _ {\mathrm{f}}}}$$

把 $\lambda(0)$ 代入(3-29)，可得 $\lambda(t)$ ，而最优控制为

$$
\begin{array}{l} u ^ {*} (t) = - \lambda (t) \\ = - \frac {1}{2 \sqrt {2}} \left\{\mathrm{e} ^ {- \sqrt {2} t} - \mathrm{e} ^ {\sqrt {2} t} + \frac {(\sqrt {2} + 1) \mathrm{e} ^ {- \sqrt {2} t _ {\mathrm{f}}} + (\sqrt {2} - 1) \mathrm{e} ^ {\sqrt {2} t _ {\mathrm{f}}}}{\mathrm{e} ^ {\sqrt {2} t _ {\mathrm{f}}} - \mathrm{e} ^ {- \sqrt {2} t _ {\mathrm{f}}}} \cdot \right. \\ \left. \left[ (\sqrt {2} - 1) e ^ {- \sqrt {2} t} + (\sqrt {2} + 1) e ^ {\sqrt {2} t} \right] \right\} \\ \end{array}
$$

例3-4 设系统的状态方程为

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t)$$

初始条件为

$$x _ {1} (0) = 1 \quad x _ {2} (0) = 1$$

终端条件为
