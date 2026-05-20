$$\lambda_ {1} (1) = \frac {\partial \phi}{\partial x _ {1} (1)} = \frac {\partial J}{\partial x _ {1} (1)} = 0 \tag {7-60}\lambda_ {2} (1) = \frac {\partial J}{\partial x _ {2} (1)} = 1 \quad \therefore c = 1 \tag {7-61}$$

故协态方程化为

$$\dot {\lambda} _ {1} = - (1 + u) \quad \lambda_ {1} (1) = 0 \tag {7-62}\lambda_ {2} (t) = 1 \tag {7-63}$$

(1) K=0 时的计算

选 $u^0 (t) = 0$ ，代入状态方程和协态方程(7-54）、(7-55)、(7-62)和(7-63)，可求得 $\dot{x}_1 = 0, \dot{x}_2 = x_1, \dot{\lambda}_1 = -\lambda_2, \lambda_2 = 1$ 。积分可得

$$x _ {1} ^ {0} (t) = \frac {1}{2}, \quad x _ {2} ^ {0} (t) = \frac {1}{2} t, \quad \lambda_ {1} ^ {0} (t) = - t + 1$$

梯度向量

$$
\begin{array}{l} \boldsymbol {g} ^ {0} (t) = \left(\frac {\partial H}{\partial u}\right) _ {0} = \left(\lambda_ {1} + \lambda_ {2} x _ {1} + \lambda_ {2} + \lambda_ {2} u\right) _ {0} \\ = \lambda_ {1} ^ {0} + \lambda_ {2} ^ {0} x _ {1} ^ {0} + \lambda_ {2} ^ {0} = - t + 1 + \frac {1}{2} + 1 = \frac {5}{2} - t \\ \end{array}
$$

共轭梯度 $P^{0} = -g^{0} = t - \frac{5}{2}$ 。

(2) K = 1 时

$u^{1}(t) = u^{0}(t) + \alpha^{0}P^{0} = \alpha^{0}\left(t - \frac{5}{2}\right),\alpha^{0}$ 用一维寻优来决定。将 $u^{1}$ 代入状态方程(7-54)、(7-55)和协态方程(7-62)、(7-63)，得

$$\dot {x} _ {1} (t) = \alpha^ {0} \left(t - \frac {5}{2}\right)\dot {x} _ {2} (t) = \left[ 1 + \alpha^ {0} \left(t - \frac {5}{2}\right) \right] x _ {1} ^ {0} + \alpha^ {0} \left(t - \frac {5}{2}\right) + \frac {1}{2} \left[ \alpha^ {0} \left(t - \frac {5}{2}\right) \right] ^ {2}$$

积分得

$$
\begin{array}{l} x _ {1} ^ {1} (t) = \alpha^ {0} \left(\frac {t ^ {2}}{2} - \frac {5}{2} t\right) + \frac {1}{2} \\ x _ {2} ^ {1} (t) = \frac {t}{2} + \alpha^ {0} \left(\frac {t ^ {3}}{6} - \frac {t ^ {2}}{2} - \frac {1 5}{4} t\right) + (\alpha^ {0}) ^ {2} \left(\frac {t ^ {4}}{8} - \frac {1 3}{1 2} t ^ {3} + \frac {1 5}{8} t ^ {2} + \frac {2 5}{8} t\right) \\ J = x _ {2} (1) = \frac {1}{2} - \frac {4 9}{1 2} \alpha^ {0} + \frac {9 7}{2 4} (\alpha^ {0}) ^ {2} \\ \frac {\partial J}{\partial \alpha^ {0}} = - \frac {4 9}{1 2} + \frac {9 7}{1 2} \alpha^ {0} = 0 \\ \end{array}
$$

可求得 $\alpha^0$ 的最优值为

$$\alpha^ {0} = \frac {4 9}{9 7}$$

于是

$$u ^ {1} (t) = \frac {4 9}{9 7} \left(t - \frac {5}{2}\right)$$

由式(7-62)

$$\dot {\lambda} _ {1} = - \left[ 1 + \frac {4 9}{9 7} \left(t - \frac {5}{2}\right) \right]$$

积分上式可得
