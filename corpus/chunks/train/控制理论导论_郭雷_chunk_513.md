$$
\left\{ \begin{array}{l} \psi^ {\mathrm{T}} (t) = - \frac {\partial J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial x}, \\ \psi_ {n + 1} (t) = \frac {\partial J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial t}. \end{array} \right. \tag {7.1.70}
$$

从式 (7.1.63) 可得

$$
\left\{ \begin{array}{l l} { \frac {\partial J ^ {*} (0 , t _ {f} ^ {*})}{\partial x} = \mu^ {\mathrm{T}} \quad (\text {待定常向量}),} \\ { \frac {\partial J ^ {*} (0 , t _ {f} ^ {*})}{\partial t} = - \psi_ {n + 1} (t _ {f} ^ {*}) = 0.} \end{array} \right. \tag {7.1.71}
$$

利用方程 (7.1.69), 对方程 (7.1.70) 中的 $\psi(t)$ 求导得到

$$
\begin{array}{l} \dot {\psi} ^ {T} (t) = - \frac {\partial^ {2} J ^ {*} (x ^ {*} (t) , t)}{\partial t \partial x} - \frac {\partial^ {2} J ^ {*} (x ^ {*} (t) , t)}{\partial x ^ {2}} \cdot f (x ^ {*} (t), u ^ {*} (t)) \\ = \frac {\partial}{\partial x} \left[ - \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} - \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \cdot f (x ^ {*} (t), u ^ {*} (t)) \right] \\ + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \cdot \frac {\partial f (x ^ {*} (t) , u ^ {*} (t))}{\partial x} \\ = - \psi^ {T} (t) \frac {\partial f \left(x ^ {*} (t) , x ^ {*} (t)\right)}{\partial x} + \frac {\partial l \left(x ^ {*} (t) , u ^ {*} (t)\right)}{\partial x}. \\ \end{array}
$$

由于方程 (7.1.69) 和 $f, l$ 不显含 $t$ , 故对方程 (7.1.70) 中的 $\psi_{n+1}(t)$ 求导即得

$$
\begin{array}{l} \dot {\psi} _ {n + 1} (t) = - \frac {\partial^ {2} J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial t ^ {2}} - \frac {\partial^ {2} J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial x \partial t} \cdot f \left(x ^ {*} (t), u ^ {*} (t)\right) \\ = - \frac {\partial}{\partial t} \left[ \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \cdot f (x ^ {*} (t), u ^ {*} (t)) \right] \\ + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \frac {\partial f (x ^ {*} (t) , u ^ {*} (t))}{\partial t} \\ = - \frac {\partial}{\partial t} \left[ \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \cdot f (x ^ {*} (t), u ^ {*} (t)) \right] \\ = - \frac {\partial l \left(x ^ {*} (t) , u ^ {*} (t)\right)}{\partial t} = 0. \\ \end{array}
$$

因此 $\psi(t), \psi_{n+1}(t)$ 满足

$$
\left\{ \begin{array}{l} \dot {\psi} ^ {T} (t) = \frac {\partial l (x ^ {*} (t) , u ^ {*} (t))}{\partial x} - \psi^ {T} (t) \frac {\partial f (x ^ {*} (t) , u ^ {*} (t))}{\partial x}, \\ \dot {\psi} _ {n + 1} (t) = 0. \end{array} \right. \tag {7.1.72}
$$
