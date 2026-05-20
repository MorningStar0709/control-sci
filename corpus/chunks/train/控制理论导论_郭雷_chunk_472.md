$$
\left\{ \begin{array}{l} u = \alpha (\xi), \\ \dot {\xi} = f (\xi) + g _ {2} (\xi) \alpha (\xi) + \frac {1}{\gamma^ {2}} g _ {1} (\xi) \beta (\xi) + G (y - h _ {2} (\xi)), \end{array} \right. \tag {6.8.23}
$$

其中 $\alpha (\cdot)$ 由定理6.8.1给定， $x_{e} = [x^{\mathrm{T}}\xi^{\mathrm{T}}]^{\mathrm{T}}$ ，并且

$$
\beta (x) = g _ {1} (x) \frac {\partial^ {\mathbf {T}} V}{\partial x} (x),
f _ {e} (x _ {e}) = \left[ \begin{array}{c} f (x) + g _ {2} (x) \alpha (\xi) + \frac {1}{\gamma^ {2}} g _ {1} (x) \beta (\xi) \\ f (\xi) + g _ {2} (\xi) \alpha (\xi) + \frac {1}{\gamma^ {2}} g _ {1} (\xi) \beta (\xi) + G (h _ {2} (x) - h _ {2} (\xi)) \end{array} \right],

h _ {2} \left(x _ {e}\right) = \alpha (\xi) - \alpha (x), \quad E \left(x _ {e}\right) = \left[ \begin{array}{c} g _ {1} (x) \\ G k _ {2 1} (x) \end{array} \right], \quad \frac {\partial W}{\partial x _ {e}} = \left[ \begin{array}{c c} \frac {\partial W}{\partial x} & \frac {\partial W}{\partial \xi} \end{array} \right].
$$

证明 闭环系统可以描述如下:

$$
\left\{ \begin{array}{l} \dot {x} _ {e} = F (x _ {e}) + E (x _ {e}) w, \\ z = H (x _ {e}), \end{array} \right. \tag {6.8.24}
$$

其中

$$
F (x _ {e}) = f _ {e} (x _ {e}) - \left[ \begin{array}{c} - \frac {1}{\gamma^ {2}} g _ {1} (x) \beta (x) \\ 0 \end{array} \right],

E (x _ {e}) = \left[ \begin{array}{c} g _ {1} (x) \\ G k _ {2 1} (x) \end{array} \right], \qquad H (x _ {e}) = h _ {1} (x) + k _ {1 2} (x) \alpha (x).
$$

该系统具有小于 $\gamma$ 的 $L^2$ 增益的一个充分条件是系统具有 $\gamma$ -耗散性，即根据定理6.8.1, 如下Hamilton-Jacobi不等式具有半正定解 $U(x_e)$

$$\frac {\partial U}{\partial x _ {e}} F (x _ {e}) + \frac {1}{2 \gamma^ {2}} \frac {\partial U}{\partial x _ {e}} E (x _ {e}) E ^ {\mathrm{T}} (x _ {e}) \frac {\partial^ {\mathrm{T}} U}{\partial x _ {e}} + \frac {1}{2} H ^ {\mathrm{T}} (x _ {e}) H (x _ {e}) \leqslant 0, \quad \forall x _ {e}. \tag {6.8.25}$$

因此，为了证明该闭环系统具有小于 $\gamma$ 的 $L^2$ 增益，以下我们证明半正定函数

$$U (x _ {e}) = V (x) + W (x, \xi) \tag {6.8.26}$$

满足上述Hamilton-Jacobi不等式(6.8.25).令
