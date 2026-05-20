现在考虑复合备选李雅普诺夫函数

$$\nu (x, y) = (1 - d) V (x) + d W (x, y), \quad 0 < d < 1 \tag {11.42}$$

其中常数 d 待选。计算 $\nu$ 沿整个系统(11.35)\~(11.36)的轨线的导数, 得

$$
\begin{array}{l} \dot {\nu} = (1 - d) \frac {\partial V}{\partial x} f (x, y + h (x)) + \frac {d}{\varepsilon} \frac {\partial W}{\partial y} g (x, y + h (x)) \\ - d \frac {\partial W}{\partial y} \frac {\partial h}{\partial x} f (x, y + h (x)) + d \frac {\partial W}{\partial x} f (x, y + h (x)) \\ = (1 - d) \frac {\partial V}{\partial x} f (x, h (x)) + \frac {d}{\varepsilon} \frac {\partial W}{\partial y} g (x, y + h (x)) \\ + (1 - d) \frac {\partial V}{\partial x} [ f (x, y + h (x)) - f (x, h (x)) ] \\ + d \left[ \frac {\partial W}{\partial x} - \frac {\partial W}{\partial y} \frac {\partial h}{\partial x} \right] f (x, y + h (x)) \\ \end{array}
$$

这里已经把导数 $\dot{\nu}$ 表示成四项之和。前两项是 V 和 W 沿降阶系统和边界层系统的轨线的导数。根据不等式(11.39)和不等式(11.40)，这两项关于 x 和 y 都是负定的。其他两项表示慢动态和快动态互联的影响，当 $\varepsilon=0$ 时可以忽略。一般来说，这两项是无限的，前一项

$$\frac {\partial V}{\partial x} [ f (x, y + h (x)) - f (x, h (x)) ]$$

表示降价系统(11.35)与降阶系统(11.37)偏差的影响。另一项

$$\left[ \frac {\partial W}{\partial x} - \frac {\partial W}{\partial y} \frac {\partial h}{\partial x} \right] f (x, y + h (x))$$

表示方程(11.36)与边界层系统(11.38)的偏差,以及在边界层分析中冻结x的效应。假设这些扰动项满足

$$\frac {\partial V}{\partial x} [ f (x, y + h (x)) - f (x, h (x)) ] \leqslant \beta_ {1} \psi_ {1} (x) \psi_ {2} (y) \tag {11.43}$$

和 $\left[\frac{\partial W}{\partial x} -\frac{\partial W}{\partial y}\frac{\partial h}{\partial x}\right]f(x,y + h(x))\leqslant \beta_{2}\psi_{1}(x)\psi_{2}(y) + \gamma \psi_{2}^{2}(y)$ (11.44)

其中 $\beta_{1},\beta_{2}$ 和 $\gamma$ 是非负常数。运用不等式(11.39)、不等式(11.40)、不等式(11.43)和不等式(11.44)得 $i_{n} < -\frac{d}{(1 - d)\alpha_{1}y^{2}(x)} = \frac{d}{\alpha_{2}y^{2}(y)} + (1 - d)\beta_{1}y / (x)y / 2(y)$

$$
\begin{array}{l} \dot {\nu} \leqslant - (1 - d) \alpha_ {1} \psi_ {1} ^ {2} (x) - \frac {d}{\varepsilon} \alpha_ {2} \psi_ {2} ^ {2} (y) + (1 - d) \beta_ {1} \psi_ {1} (x) \psi_ {2} (y) \\ + d \beta_ {2} \psi_ {1} (x) \psi_ {2} (y) + d \gamma \psi_ {2} ^ {2} (y) \\ = - \psi^ {T} (x, y) \Lambda \psi (x, y) \\ \end{array}
$$

其中 $\psi (x,y) = \left[ \begin{array}{l}\psi_{1}(x)\\ \psi_{2}(y) \end{array} \right]$

且 $\Lambda = \left[ \begin{array}{cc}(1 - d)\alpha_{1} & -\frac{1}{2} (1 - d)\beta_{1} - \frac{1}{2} d\beta_{2}\\ -\frac{1}{2} (1 - d)\beta_{1} - \frac{1}{2} d\beta_{2} & d((\alpha_{2} / \varepsilon) - \gamma) \end{array} \right]$
