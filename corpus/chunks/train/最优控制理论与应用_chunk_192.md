$$\tan u _ {2} = \frac {\lambda_ {5}}{\lambda_ {4}}, \tan v _ {2} = \frac {\lambda_ {5}}{\lambda_ {4}}$$

由此可得

$$u _ {2} = v _ {2} \text {或} u _ {2} = v _ {2} + \pi \tag {10-84}$$

由 $\frac{\partial H}{\partial u_1} = 0$ 和 $\frac{\partial H}{\partial v_1} = 0$ 可分别求得

$$
\begin{array}{l} \tan u _ {1} = \frac {\lambda_ {6}}{\lambda_ {4} \cos u _ {2} + \lambda_ {5} \sin u _ {2}} \\ \tan v _ {1} = \frac {\lambda_ {6}}{\lambda_ {4} \cos v _ {2} + \lambda_ {5} \sin v _ {2}} \\ \end{array}
$$

考虑到式(10-84)，又可得

$$u _ {1} = v _ {1} \text {或} u _ {1} = - v _ {1} \tag {10-85}$$

下面来验证哈密顿函数 H 对 u、v 的二阶导数的符号

$$
\left\{ \begin{array}{l} \frac {\partial^ {2} H}{\partial u _ {1} ^ {2}} = - T _ {\mathrm{A}} \left(\lambda_ {4} \cos u _ {1} \cos u _ {2} + \lambda_ {5} \cos u _ {1} \sin u _ {2} + \lambda_ {6} \sin u _ {1}\right) \\ \frac {\partial^ {2} H}{\partial u _ {2} ^ {2}} = - T _ {\mathrm{A}} \left(\lambda_ {4} \cos u _ {1} \cos u _ {2} + \lambda_ {5} \cos u _ {1} \sin u _ {2}\right) \\ \frac {\partial^ {2} H}{\partial v _ {1} ^ {2}} = T _ {\mathrm{B}} \left(\lambda_ {4} \cos v _ {1} \cos v _ {2} + \lambda_ {5} \cos v _ {1} \sin v _ {2} + \lambda_ {6} \sin v _ {1}\right) \\ \frac {\partial^ {2} H}{\partial v _ {2} ^ {2}} = T _ {\mathrm{B}} \left(\lambda_ {4} \cos v _ {1} \cos v _ {2} + \lambda_ {5} \cos v _ {1} \sin v _ {2}\right) \end{array} \right. \tag {10-86}
$$

当 $u_{1} = v_{1}, u_{2} = v_{2}$ 时，只要

$$
\left\{ \begin{array}{l} \lambda_ {4} \cos u _ {1} \cos u _ {2} + \lambda_ {5} \cos u _ {1} \sin u _ {2} > 0 \\ \lambda_ {4} \cos u _ {1} \cos u _ {2} + \lambda_ {5} \cos u _ {1} \sin u _ {2} + \lambda_ {6} \sin u _ {1} > 0 \end{array} \right. \tag {10-87}
$$

就给出

$$\frac {\partial^ {2} H}{\partial u _ {1} ^ {2}} < 0, \frac {\partial^ {2} H}{\partial u _ {2} ^ {2}} < 0, \frac {\partial^ {2} H}{\partial v _ {1} ^ {2}} > 0, \frac {\partial^ {2} H}{\partial v _ {2} ^ {2}} > 0$$

即满足鞍点条件,所以在满足条件(10-84)时

$$u _ {1} ^ {*} = v _ {1} ^ {*}, u _ {2} ^ {*} = v _ {2} ^ {*}$$

即为双方极值原理的最优策略。

当 $u_{2} = v_{2} + \pi, u_{1} = -v_{1}$ 时，可得到

$$\frac {\partial^ {2} H}{\partial u _ {1} ^ {2}} = T _ {\mathrm{A}} \left(\lambda_ {4} \cos v _ {1} \cos v _ {2} + \lambda_ {5} \cos v _ {1} \sin v _ {2} + \lambda_ {6} \sin v _ {1}\right)\frac {\partial^ {2} H}{\partial v _ {1} ^ {2}} = T _ {\mathrm{B}} \left(\lambda_ {4} \cos v _ {1} \cos v _ {2} + \lambda_ {5} \cos v _ {1} \sin v _ {2} + \lambda_ {6} \sin v _ {1}\right)$$

二者具有相同符号,故不满足双方极值原理。
