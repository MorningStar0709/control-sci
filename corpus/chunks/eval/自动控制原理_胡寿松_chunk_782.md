$$\frac {\partial H}{\partial u} = u + \lambda_ {2} = 0, \quad u (t) = - \lambda_ {2} (t) = c _ {1} t - c _ {2}$$

由状态方程

$$\dot {x} _ {2} = u = c _ {1} t - c _ {2}, \quad x _ {2} (t) = \frac {1}{2} c _ {1} t ^ {2} - c _ {2} t + c _ {3}\dot {x} _ {1} = x _ {2} = \frac {1}{2} c _ {1} t ^ {2} - c _ {2} t + c _ {3}, \quad x _ {1} (t) = \frac {1}{6} c _ {1} t ^ {3} - \frac {1}{2} c _ {2} t ^ {2} + c _ {3} t + c _ {4}$$

根据已知初态 $x_{1}(0) = x_{2}(0) = 0$ ，求出

$$c _ {3} = c _ {4} = 0$$

再由目标集条件 $x_{1}(1) + x_{2}(1) - 1 = 0$ ，求得

$$4 c _ {1} - 9 c _ {2} = 6$$

根据横截条件

$$\lambda_ {1} (1) = \frac {\partial \psi}{\partial x _ {1} (1)} \gamma = \gamma , \quad \lambda_ {2} (1) = \frac {\partial \psi}{\partial x _ {2} (1)} \gamma = \gamma$$

得到 $\lambda_1(1) = \lambda_2(1)$ ，故有 $c_{1} = \frac{1}{2} c_{2}$ 。于是解出

$$c _ {1} = - \frac {3}{7}, \quad c _ {2} = - \frac {6}{7}$$

从而，本例最优解为

$$u ^ {*} (t) = - \frac {3}{7} (t - 2)x _ {1} ^ {*} (t) = - \frac {1}{1 4} t ^ {2} (t - 6)x _ {2} ^ {*} (t) = - \frac {3}{1 4} t (t - 4)$$
