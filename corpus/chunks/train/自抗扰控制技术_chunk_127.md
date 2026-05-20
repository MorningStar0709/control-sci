# 3.6 三阶线性最速控制系统的开关曲面

三阶线性控制系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = u, | u | \leqslant r \end{array} \right. \tag {3.6.1}
$$

在三维状态空间中，以原点为终点的最速轨线可分为如下五种形式：控制取 $u = +r$ 或 $u = -r$ 不开关直接进入原点的轨线；控制先取 $u = +r$ ，走一段开关一次，然后取 $u = -r$ 来进入原点的轨线和控制先取 $u = -r$ ，走一段开关一次，然后取 $u = +r$ 来进入原点的轨线；控制先取 $u = +r$ ，走一段，开关一次后取 $u = -r$ 再走一段，再开关一次后取 $u = +r$ 来最后进入原点的轨线；控制先取 $u = -r$ ，走一段开关一次后取 $u = +r$ ，再走一段，再开关一次，然后取 $u = -r$ 来最后进入原点的轨线。在所有的最速轨线上，控制量的绝对值始终取最大值 $|u| = r$ ，并且在到达原点之前的整个过程中，控制量最多开关两次。控制量最多开关一次的所有最速轨线将在三维状态空间中编织出一个二维曲面，这个曲面是在整个状态空间中最速控制综合函数 $u(x_1, x_2, x_3)$ 取 $+r$ 和 $-r$ 的分界面，被称为“开关曲面”。因此要确定此开关曲面，将采用从原点出发积分倒退方程

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = - x _ {3} \\ \dot {x} _ {3} = - u \end{array} \right. \tag {3.6.2}
$$

的办法来确定.

下面就用倒退积分的办法确定这个三维空间中的开关曲面.

先取 $u = +r$ ，从原点出发积分倒退方程，得

$$
\left\{ \begin{array}{l} x _ {3} (\tau) = - r \tau \\ x _ {2} (\tau) = r \frac {\tau^ {2}}{2} \\ x _ {1} (\tau) = - r \frac {\tau^ {3}}{6} \end{array} \right.
$$

开关一次后取 u = -r，以上式表示的点为初值倒退积分，得

$$
\left\{ \begin{array}{l} x _ {3} = - r \tau + r (t - \tau) = r t - 2 r \tau \\ x _ {2} = r \frac {\tau^ {2}}{2} - r \frac {(t - \tau) ^ {2}}{2} + r \tau (t - \tau) \\ x _ {1} = - r \frac {\tau^ {3}}{6} - r \frac {\tau^ {2}}{2} (t - \tau) + r \frac {(t - \tau) ^ {3}}{6} - r \tau \frac {(t - \tau) ^ {2}}{2} \end{array} \right. \tag {3.6.3}
$$

从式(3.6.3)第1式解出 $t - \tau = \tau +\frac{x_3}{r}$ ，把它代到第2式，得

$$2 \frac {x _ {2}}{r} = \tau^ {2} + 2 \tau \left(\tau + \frac {x _ {3}}{r}\right) - \left(\tau + \frac {x _ {3}}{r}\right) ^ {2} = 2 \tau^ {2} - \frac {x _ {3} ^ {2}}{r ^ {2}}$$

由此

$$\tau = \pm \frac {1}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}}, x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0$$

由于 $\tau \geqslant 0$ ，这里的符号“±”只能取“+”，从而有

$$
\left\{ \begin{array}{l} \tau = \frac {1}{\sqrt {\tau}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}}, x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0 \\ t = 2 \tau + \frac {x _ {3}}{r} = \frac {2}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + \frac {x _ {3}}{r} \\ t - \tau = \tau + \frac {x _ {3}}{r} = \frac {1}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + \frac {x _ {3}}{r} \end{array} \right. \tag {3.6.4}
$$

把式 $(3.6.3)$ 中第3式整理成

$$6 \frac {x _ {1}}{r} = - \tau^ {3} - 3 \tau^ {2} (t - \tau) + (t - \tau) ^ {3} - 3 \tau (t - \tau) ^ {2}6 \frac {x _ {1}}{r} = - (\tau + t - \tau) ^ {3} + 2 (t - \tau) ^ {3} = - t ^ {3} + 2 (t - \tau) ^ {3} \tag {3.6.5}$$

把 $\tau$ 和 $t$ 的表达式(式3.6.4中第2式和第3式)代进去,最后得
