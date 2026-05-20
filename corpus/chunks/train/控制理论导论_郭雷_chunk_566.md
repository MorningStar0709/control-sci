$$
\begin{array}{l} \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u ^ {*} (x, t), v) + l (x, u ^ {*} (x, t), v) \\ \leqslant \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u ^ {*} (x, t), v ^ {*} (x, t)) + l (x, u ^ {*} (x, t), v ^ {*} (x, t)) = 0 \\ \leqslant \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u, v ^ {*} (x, t)) + l (x, u, v ^ {*} (x, t)). \\ \end{array}
$$

因此

$$
\left\{ \begin{array}{l l} \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u ^ {*} (x, t), v ^ {*} (x, t)) + l (x, u ^ {*} (x, t), v ^ {*} (x, t)) = 0, \\ J ^ {*} (x (t _ {f}), t _ {f}) = 0, & \forall (x, t) \in \mathbb {R} ^ {n} \times [ 0, t _ {f} ], \end{array} \right. \tag {7.4.45}

\left\{ \begin{array}{l} \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u ^ {*} (x, t), v) + l (x, u ^ {*} (x, t), v) \leqslant 0, \\ J ^ {*} (x \left(t _ {f}\right), t _ {f}) = 0, \quad \forall v \in \mathbb {V} _ {r _ {2}}, (x, t) \in \mathbb {R} ^ {n} \times [ 0, t _ {f} ], \end{array} \right. \tag {7.4.46}

\left\{ \begin{array}{l} \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u, v ^ {*} (x, t)) + l (x, u, v ^ {*} (x, t)) \geqslant 0, \\ J ^ {*} (x \left(t _ {f}\right), t _ {f}) = 0, \quad \forall u \in \mathbb {U} _ {r _ {1}}, (x, t) \in \mathbb {R} ^ {n} \times [ 0, t _ {f} ]. \end{array} \right. \tag {7.4.47}
$$

将 $(u^{*}(x,t),v^{*}(x,t))$ 代入式(7.4.8)得到闭环系统

$$\dot {x} = f (x, u ^ {*} (x, t), v ^ {*} (x, t)). \tag {7.4.48}$$

注意到， $\forall x_0 \in \mathbb{R}^n$ ，式 (7.4.48) 以 $x(0) = x_0$ 为初态的轨线在 $[t_0, t_f]$ 上存在唯一，记之为 $x^*(t)$ . 令

$$u ^ {*} (t) \stackrel {\text { def }} {=} u ^ {*} (x ^ {*} (t), t), \quad v ^ {*} (t) \stackrel {\text { def }} {=} v ^ {*} (x ^ {*} (t), t). \tag {7.4.49}$$

易知， $(u^{*}(t),v^{*}(t))\in \mathcal{W}_{[0,t_{f}]}$ 显然， $\forall t\in [0,t_f]$ 有

$$
\left\{ \begin{array}{l} {\dot {x} ^ {*} (t) = f (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)),} \\ {x (0) = x _ {0}.} \end{array} \right. \tag {7.4.50}
$$

将 $(x^{*}(t), u^{*}(t), v^{*}(t))$ 代入式 (7.4.45) 得

$$
\left\{ \begin{array}{l} \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)) + l (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)) = 0, \\ J ^ {*} (x ^ {*} (t _ {f}), t _ {f}) = 0, \forall t \in [ 0, t _ {f} ]. \end{array} \right.
$$

从 0 到 $t_{f}$ 积分上式并考虑到终值条件，容易得到
