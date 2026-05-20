由控制方程 $\frac{\partial H}{\partial U} = \frac{\partial H}{\partial\theta} = 0$ ，得

$$\lambda_ {1} a \sin \theta - \lambda_ {2} a \cos \theta = 0$$

即

$$\tan \theta = \frac {\lambda_ {2}}{\lambda_ {1}} = - v _ {1} - v _ {2} \left(t _ {\mathrm{f}} - t\right) \tag {3-63}$$

为了确定最优程序 $\theta(t)$ ，还需确定拉格朗日未定常数 $v_{1}, v_{2}$ 。下面来积分状态方程式(3-58)，为此将自变量 t 变成 $\theta$ 。由式(3-63)得

$$\frac {\mathrm{d} \tan \theta}{\mathrm{d} \theta} \cdot \frac {\mathrm{d} \theta}{\mathrm{d} t} = \sec^ {2} \theta \frac {\mathrm{d} \theta}{\mathrm{d} t} = v _ {2} \quad \frac {\mathrm{d} \theta}{\mathrm{d} t} = \frac {v _ {2}}{\sec^ {2} \theta}$$

将上面关系代入状态方程,即得

$$\frac {\mathrm{d} x _ {1}}{\mathrm{d} \theta} = a \cos \theta \frac {\mathrm{d} t}{\mathrm{d} \theta} = \frac {a}{v _ {2} \cos \theta}\frac {\mathrm{d} x _ {2}}{\mathrm{d} \theta} = a \sin \theta \frac {\mathrm{d} t}{\mathrm{d} \theta} = \frac {a}{v _ {2}} \cdot \frac {\sin \theta}{\cos^ {2} \theta}$$

积分上面两式得

$$x _ {1} = \frac {a}{v _ {2}} \ln (\sec \theta + \tan \theta) + c _ {3}x _ {2} = \frac {a}{v _ {2}} \sec \theta + c _ {3}$$

由初始条件 $x_{1}(0) = 0, x_{2}(0) = 0, \theta(0) = \theta_{0}$ 可求得

$$x _ {1} = \frac {a}{v _ {2}} \ln \frac {\tan \theta + \sec \theta}{\tan \theta_ {0} + \sec \theta_ {0}} \tag {3-64}x _ {2} = \frac {a}{v _ {2}} (\sec \theta - \sec \theta_ {0}) \tag {3-65}$$

将上面的 $x_{1}$ 和 $x_{2}$ 代入状态方程式(3-58)的后两式，积分并经较复杂运算可得

$$x _ {3} = \frac {a}{v _ {2} ^ {2}} \left(\sec \theta_ {0} - \sec \theta + \tan \theta \ln \frac {\tan \theta + \sec \theta}{\tan \theta_ {0} + \sec \theta_ {0}}\right) \tag {3-66}x _ {4} = \frac {a}{2 v _ {2} ^ {2}} \left[ (\tan \theta_ {0} - \tan \theta) \sec \theta_ {0} - (\sec \theta_ {0} - \sec \theta) \tan \theta + \right.\left. \ln \frac {\tan \theta + \sec \theta}{\tan \theta_ {0} + \sec \theta_ {0}} \right] \tag {3-67}$$

由终端条件 $x_{2}(t_{\mathrm{f}}) = 0$ 和式(3-65)可得 $\sec \theta (t_{\mathrm{f}}) = \sec \theta_0$ ，故

$$\theta_ {\mathrm{f}} \stackrel {\triangle} {=} \theta \left(t _ {\mathrm{f}}\right) = 2 \pi - \theta_ {0} \tag {3-68}$$

（注：另一解为 $\theta_{\mathrm{f}} = \theta_0$ ，但这时由式(3-67)可得出 $x_{4}(t_{\mathrm{f}}) = 0$ 与给定终端条件 $x_{4}(t_{\mathrm{f}}) = h_{\mathrm{f}}\neq 0$ 不符，故略去 $\theta_{\mathrm{f}} = 0$ 的解）

由式(3-63)得

$$\tan \theta = \tan \theta_ {0} + v _ {2} t\tan \theta_ {f} = \tan \theta_ {0} + v _ {2} t _ {f}v _ {2} t _ {\mathrm{f}} = - 2 \tan \theta_ {0}$$

故

$$v _ {2} = - \frac {2 \tan \theta_ {0}}{t _ {\mathrm{f}}} \tag {3-69}$$

于是
