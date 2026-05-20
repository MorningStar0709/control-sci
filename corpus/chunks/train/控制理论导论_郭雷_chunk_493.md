$$
\delta x (t) = \left\{ \begin{array}{l l} 0, & t \in [ t _ {0}, \bar {t} ], \\ \int_ {\bar {t}} ^ {t} \Phi (t, \sigma) \frac {\partial f}{\partial u} \Big | _ {*} h d \sigma , & t \in [ \bar {t}, \bar {t} + \varepsilon_ {1} ], \\ \int_ {\bar {t}} ^ {\bar {t} + \varepsilon_ {1}} \Phi (t, \sigma) \frac {\partial f}{\partial u} \Big | _ {*} h d \sigma , & t \in [ \bar {t} + \varepsilon_ {1}, t _ {f} ], \end{array} \right. \tag {7.1.20}
$$

其中 $\Phi(t, \sigma)$ 是变分方程 (7.1.9) 的基本解矩阵. 从方程 (7.1.20) 看到 $|\delta x(t)| = O(\varepsilon_1)$ . 因此有

$$
\left\{ \begin{array}{l l} (\delta x (t _ {f})) ^ {\mathrm{T}} \frac {\partial^ {2} k}{\partial x ^ {2}} \Big | _ {*} (\delta x (t _ {f})) = O (\varepsilon_ {1} ^ {2}), \\ (\delta x (t)) ^ {\mathrm{T}} \frac {\partial^ {2} H}{\partial x ^ {2}} \Big | _ {*} (\delta x (t)) = O (\varepsilon_ {1} ^ {2}), & t \in [ t _ {0}, t _ {f} ], \\ (\delta x (t)) ^ {\mathrm{T}} \frac {\partial^ {2} H}{\partial x \partial u} \Big | _ {*} (\delta u (t)) = O (\varepsilon_ {1}), & t \in [ t _ {0}, t _ {f} ]. \end{array} \right.
$$

由此不难得到

$$
\int_ {t _ {0}} ^ {t _ {f}} (\delta x (t)) ^ {\mathrm{T}} \frac {\partial^ {2} H}{\partial x ^ {2}} \Big | _ {*} (\delta x (t)) \mathrm{d} t = O \left(\varepsilon_ {1} ^ {2}\right),
\begin{array}{l} \int_ {t _ {0}} ^ {t _ {f}} (\delta x (t)) ^ {\mathrm{T}} \frac {\partial^ {2} H}{\partial x \partial u} \Big | _ {*} (\delta u (t)) \mathrm{d} t = \int_ {\bar {t}} ^ {\bar {t} + \varepsilon_ {1}} (\delta x (t)) ^ {\mathrm{T}} \frac {\partial^ {2} H}{\partial x \partial u} \Big | _ {*} h \mathrm{d} t \\ = \varepsilon_ {1} (\delta x (\bar {t})) ^ {\mathrm{T}} \frac {\partial^ {2} H (x ^ {*} (\bar {t}) , u ^ {*} (\bar {t}) , \psi (\bar {t}))}{\partial x \partial u} h + o (\varepsilon_ {1}), \\ \end{array}
\int_ {t _ {0}} ^ {t _ {f}} (\delta u (t)) ^ {\mathrm{T}} \frac {\partial^ {2} H}{\partial u ^ {2}} \Big | _ {*} (\delta u (t)) \mathrm{d} t = \varepsilon_ {1} h ^ {\mathrm{T}} \frac {\partial^ {2} H (x ^ {*} (\bar {t}) , u ^ {*} (\bar {t}) , \psi (\bar {t}))}{\partial u ^ {2}} h + o (\varepsilon_ {1}).
$$

利用上列三个估计式能得 $\delta^2 J_1[u]$ 的如下估计式：

$$\delta^ {2} J _ {1} [ u ] = - \varepsilon_ {1} \left[ h ^ {\mathrm{T}} \frac {\partial^ {2} H (x ^ {*} (\bar {t}) , u ^ {*} (\bar {t}) , \psi (\bar {t}))}{\partial u ^ {2}} h + o (1) \right] \geqslant 0. \quad (\varepsilon_ {1} \rightarrow 0)$$

由此即知， $\forall h\in \mathbb{R}^r$ 皆成立

$$h ^ {\mathrm{T}} \frac {\partial^ {2} H (x ^ {*} (\bar {t}) , u ^ {*} (\bar {t}) , \psi (\bar {t}))}{\partial u ^ {2}} h \leqslant 0,$$
