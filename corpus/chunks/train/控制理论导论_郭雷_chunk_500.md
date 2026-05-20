$$
\begin{array}{l} \Delta J _ {1} [ u ] = J _ {1} \left[ u ^ {*} + \Delta u \right] - J _ {1} \left[ u ^ {*} \right] \\ = k \left(x ^ {*} \left(t _ {f}\right) + \Delta x \left(t _ {f}\right)\right) - k \left(x ^ {*} \left(t _ {f}\right)\right) + \psi^ {\mathrm{T}} \left(t _ {f}\right) \cdot \Delta x \left(t _ {f}\right) - \int_ {t _ {0}} ^ {t _ {f}} \dot {\psi} ^ {\mathrm{T}} (t) \Delta x (t) \mathrm{d} t \\ - \int_ {t _ {0}} ^ {t _ {f}} \left[ H (x ^ {*} (t) + \Delta x (t), u ^ {*} (t) + \Delta u (t), \psi (t)) - H (x ^ {*} (t), u ^ {*} (t), \psi (t)) \right] d t. \\ \end{array}
$$

易知

$$
\begin{array}{l} k \left(x ^ {*} \left(t _ {f}\right) + \Delta x \left(t _ {f}\right)\right) - k \left(x ^ {*} \left(t _ {f}\right)\right) = \frac {\partial k \left(x ^ {*} \left(t _ {f}\right)\right)}{\partial x} \Delta x \left(t _ {f}\right) + o \left(\left| \Delta x \left(t _ {f}\right) \right|\right) \\ H \left(x ^ {*} (t) + \Delta x (t), u ^ {*} (t) + \Delta u (t), \psi (t)\right) - H \left(x ^ {*} (t), u ^ {*} (t), \psi (t)\right) \\ = H \left(x ^ {*} (t) + \Delta x (t), u ^ {*} (t) + \Delta u (t), \psi (t)\right) - H \left(x ^ {*} (t), u ^ {*} (t) + \Delta u (t), \psi (t)\right) \\ + H \left(x ^ {*} (t), u ^ {*} (t) + \Delta u (t), \psi (t)\right) - H \left(x ^ {*} (t), u ^ {*} (t), \psi (t)\right) \\ = \left(\frac {\partial H \left(x ^ {*} (t) , u ^ {*} (t) + \Delta u (t) , \psi (t)\right) - H \left(x ^ {*} (t) , u ^ {*} (t) , \psi (t)\right)}{\partial x} \right. \\ \left. + \frac {\partial H \left(x ^ {*} (t) , u ^ {*} (t) , \psi (t)\right)}{\partial x}\right) \Delta x (t) + \left[ H \left(x ^ {*} (t), u ^ {*} (t) + \Delta u (t), \psi (t)\right) \right. \\ \left. - H \left(x ^ {*} (t), u ^ {*} (t), \psi (t)\right) \right] + o \left(\left| \Delta x (t) \right|\right). \\ \end{array}
$$

由此可得

$$
\begin{array}{l} \Delta J _ {1} [ u ] = \left(\frac {\partial k (x ^ {*} (t _ {f}))}{\partial x} + \psi^ {T} (t _ {f})\right) \Delta x (t _ {f}) - \int_ {t _ {0}} ^ {t _ {f}} \left(\dot {\psi} ^ {T} (t) + \frac {\partial H}{\partial x} | _ {*}\right) \Delta x (t) d t \\ - \int_ {t _ {0}} ^ {t _ {f}} \frac {\partial (H (x ^ {*} (t) , u ^ {*} (t) + \Delta u (t) , \psi (t)) - H (x ^ {*} (t) , u ^ {*} (t) , \psi (t)))}{\partial x} \Delta x (t) \mathrm{d} t \\ - \int_ {t _ {0}} ^ {t _ {f}} \left(H (x ^ {*} (t), u ^ {*} (t) + \Delta u (t), \psi (t)) - H (x ^ {*} (t), u ^ {*} (t), \psi (t))\right) d t \\ + \int_ {t _ {0}} ^ {t _ {f}} o (| \Delta x (t) |) \mathrm{d} t + o (| \Delta x (t _ {f}) |). \\ \end{array}
$$

今选择 Lagrange 乘子向量值函数 $\psi(t)$ 为下列终值问题:
