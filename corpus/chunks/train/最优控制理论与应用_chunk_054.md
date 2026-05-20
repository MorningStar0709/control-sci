$$\dot {\lambda} _ {1} = - \frac {\partial H}{\partial x _ {1}} = - \lambda_ {3}\dot {\lambda} _ {2} = - \frac {\partial H}{\partial x _ {2}} = - \lambda_ {4}\dot {\lambda} _ {3} = - \frac {\partial H}{\partial x _ {3}} = 0\dot {\lambda} _ {4} = - \frac {\partial H}{\partial x _ {4}} = 0 \tag {3-60}$$

横截条件为

$$
\lambda \left(t _ {\mathrm{f}}\right) = \frac {\partial \phi}{\partial X \left(t _ {\mathrm{f}}\right)} + \frac {\partial G ^ {\mathrm{T}}}{\partial X \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} = \frac {\partial G ^ {\mathrm{T}}}{\partial X \left(t _ {\mathrm{f}}\right)} \boldsymbol {v}, \text {即}
\left[ \begin{array}{l} \lambda_ {1} \left(t _ {\mathrm{f}}\right) \\ \lambda_ {2} \left(t _ {\mathrm{f}}\right) \\ \lambda_ {3} \left(t _ {\mathrm{f}}\right) \\ \lambda_ {4} \left(t _ {\mathrm{f}}\right) \end{array} \right] = \frac {\partial \left[ G _ {1} , G _ {2} , G _ {3} \right]}{\partial X \left(t _ {\mathrm{f}}\right)} \left[ \begin{array}{l} v _ {1} \\ v _ {2} \\ v _ {3} \end{array} \right] = \left[ \begin{array}{l} \frac {\partial G _ {1}}{\partial x _ {1}} v _ {1} + \frac {\partial G _ {2}}{\partial x _ {1}} v _ {2} + \frac {\partial G _ {3}}{\partial x _ {1}} v _ {3} \\ \frac {\partial G _ {1}}{\partial x _ {2}} v _ {1} + \frac {\partial G _ {2}}{\partial x _ {2}} v _ {2} + \frac {\partial G _ {3}}{\partial x _ {2}} v _ {3} \\ \frac {\partial G _ {1}}{\partial x _ {3}} v _ {1} + \frac {\partial G _ {2}}{\partial x _ {3}} v _ {2} + \frac {\partial G _ {3}}{\partial x _ {3}} v _ {3} \\ \frac {\partial G _ {1}}{\partial x _ {4}} v _ {1} + \frac {\partial G _ {2}}{\partial x _ {4}} v _ {2} + \frac {\partial G _ {3}}{\partial x _ {4}} v _ {3} \end{array} \right]
$$

上式右端矩阵中 $x_{i}, i = 1,2,3,4$ 的自变量 $t_{\mathrm{f}}$ 已省略。由式(3-59)求出上式中的偏导数，可得协态的终值为

$$\lambda_ {1} \left(t _ {\mathrm{f}}\right) = v _ {1}\lambda_ {2} \left(t _ {\mathrm{f}}\right) = v _ {2}\lambda_ {3} \left(t _ {f}\right) = 0\lambda_ {4} \left(t _ {\mathrm{f}}\right) = v _ {3} \tag {3-61}$$

积分协态方程可得

$$\lambda_ {1} = - \lambda_ {3} t + c _ {1}\lambda_ {2} = - \lambda_ {4} t + c _ {2}\lambda_ {3} = \text {常数} = \lambda_ {3} \left(t _ {\mathrm{f}}\right) = 0\lambda_ {4} = \text {常数} = \lambda_ {4} \left(t _ {\mathrm{f}}\right) = v _ {3}$$

代入协态终值条件后，得 $c_{1} = v_{1}, c_{2} = v_{2} - v_{3}t_{\mathrm{f}}$ ，故

$$\lambda_ {1} = v _ {1}\lambda_ {2} = v _ {2} + v _ {3} \left(t _ {\mathrm{f}} - t\right)\lambda_ {3} = 0\lambda_ {4} = v _ {3} \tag {3-62}$$
