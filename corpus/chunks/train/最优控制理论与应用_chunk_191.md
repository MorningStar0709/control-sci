$$J (\boldsymbol {u}, \boldsymbol {v}) = x _ {1} ^ {2} \left(t _ {\mathrm{f}}\right) + x _ {2} ^ {2} \left(t _ {\mathrm{f}}\right) + x _ {3} ^ {2} \left(t _ {\mathrm{f}}\right) \tag {10-79}\boldsymbol {u} = \left[ u _ {1}, u _ {2} \right] ^ {\mathrm{T}}, \quad \boldsymbol {v} = \left[ v _ {1}, v _ {2} \right] ^ {\mathrm{T}}$$

对于卫星 A, 将选 u 使 J 尽可能小; 对 B, 则将选 v 使得 J 尽可能大。求解过程如下:

哈密顿函数 H, 共轭方程及其他边界条件可求得为

$$
H = \lambda_ {1} x _ {4} + \lambda_ {2} x _ {5} + \lambda_ {3} x _ {6} + \lambda_ {4} \left(2 \omega x _ {5} + T _ {\mathrm{A}} \cos u _ {1} \cos u _ {2} - T _ {\mathrm{B}} \cos v _ {1} \cos v _ {2}\right) +\lambda_ {5} \left(3 \omega^ {2} x _ {2} - 2 \omega x _ {4} + T _ {\mathrm{A}} \cos u _ {1} \sin u _ {2} - T _ {\mathrm{B}} \cos v _ {1} \sin v _ {2}\right) +\lambda_ {6} \left(- \omega^ {2} x _ {3} + T _ {\mathrm{A}} \sin u _ {1} - T _ {\mathrm{B}} \sin v _ {1}\right) \tag {10-80}
\left\{ \begin{array}{l} \dot {\lambda} _ {1} = 0 \\ \dot {\lambda} _ {2} = - 3 \omega^ {2} \lambda_ {5} \\ \dot {\lambda} _ {3} = \omega^ {2} \lambda_ {6} \\ \dot {\lambda} _ {4} = - \lambda_ {1} + 2 \omega \lambda_ {5} \\ \dot {\lambda} _ {5} = - \lambda_ {2} - 2 \omega \lambda_ {4} \\ \dot {\lambda} _ {6} = - \lambda_ {3} \end{array} \right. \tag {10-81}

\left\{ \begin{array}{l l} \lambda_ {1} (t _ {\mathrm{f}}) & = - 2 x _ {1} (t _ {\mathrm{f}}) \\ \lambda_ {2} (t _ {\mathrm{f}}) & = - 2 x _ {2} (t _ {\mathrm{f}}) \\ \lambda_ {3} (t _ {\mathrm{f}}) & = - 2 x _ {3} (t _ {\mathrm{f}}) \\ \lambda_ {4} (t _ {\mathrm{f}}) & = 0 \\ \lambda_ {5} (t _ {\mathrm{f}}) & = 0 \\ \lambda_ {6} (t _ {\mathrm{f}}) & = 0 \end{array} \right. \tag {10-82}
$$

由于 H 对 $u_{1}, u_{2}, v_{1}, v_{2}$ 连续，双方极值原理可由式(10-56)给出。因为

$$
\left\{ \begin{array}{l} \frac {\partial H}{\partial u _ {1}} = T _ {\mathrm{A}} \left(- \lambda_ {4} \sin u _ {1} \cos u _ {2} - \lambda_ {5} \sin u _ {1} \sin u _ {2} + \lambda_ {6} \cos u _ {1}\right) \\ \frac {\partial H}{\partial u _ {2}} = T _ {\mathrm{A}} \left(- \lambda_ {4} \cos u _ {1} \sin u _ {2} + \lambda_ {5} \cos u _ {1} \cos u _ {2}\right) \\ \frac {\partial H}{\partial v _ {1}} = T _ {\mathrm{B}} \left(\lambda_ {4} \sin v _ {1} \cos v _ {2} + \lambda_ {5} \sin v _ {1} \sin v _ {2} - \lambda_ {6} \cos v _ {1}\right) \\ \frac {\partial H}{\partial v _ {2}} = T _ {\mathrm{B}} \left(\lambda_ {4} \cos v _ {1} \sin v _ {2} - \lambda_ {5} \cos v _ {1} \cos v _ {2}\right) \end{array} \right. \tag {10-83}
$$

由 $\frac{\partial H}{\partial u_2} = 0$ 和 $\frac{\partial H}{\partial v_2} = 0$ 分别可得
