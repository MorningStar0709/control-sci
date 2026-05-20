$$
\frac {\mathrm{d} x}{\mathrm{d} t} = \left[ \begin{array}{l l} 1 & 1 \\ - 1 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} - x _ {1} (x _ {1} ^ {2} + x _ {2} ^ {2}) \\ - x _ {2} (x _ {1} ^ {2} + x _ {2} ^ {2}) \end{array} \right]. \tag {2.5.14}
$$

由于 $\operatorname{det} A = \operatorname{det}\left[ \begin{array}{cc} 1 & 1 \\ -1 & 1 \end{array} \right] = 2$ , 并且 $A$ 的两个复共轭特征值为 $1 \pm j$ , 根据定理 2.5.2 知方程 (2.5.14) 的轨线在一次奇点 $x = 0$ 附近的分布是不稳定焦点型的.

现引入极坐标

$$
\left\{ \begin{array}{l} x _ {1} = \rho \cos \theta , \\ x _ {2} = \rho \sin \theta , \end{array} \right. \tag {2.5.15}
$$

其中 $\rho = \sqrt{x_1^2 + x_2^2},\tan \theta = x_2 / x_1,\forall x_1\neq 0.$ 在此坐标变换下，微分方程(2.5.14)变换为

$$
\left\{ \begin{array}{l} \dot {\rho} = \rho (1 - \rho^ {2}), \\ \dot {\theta} = - 1. \end{array} \right. \tag {2.5.16}
$$

易知非线性微分方程 (2.5.16) 的以 $(\rho_0, \theta_0)$ 为初值的解为

$$
\left\{ \begin{array}{l} \rho = \rho (t; \rho_ {0}, \theta_ {0}) = \frac {1}{\sqrt {1 + k _ {0} \mathrm{e} ^ {- 2 t}}}, \\ \theta = \theta (t; \rho_ {0}, \theta_ {0}) = - t + \theta_ {0}, \end{array} \right. \tag {2.5.17}
$$

其中 $k_{0} = (1 - \rho_{0}^{2}) / \rho_{0}^{2},\rho_{0}^{2} = x_{10}^{2} + x_{20}^{2},\theta_{0} = \arctan (x_{20} / x_{10}),x_{10}\neq 0.$ 由此不难得到非线性微分方程(2.5.14)的以 $x_0 = [x_{10},x_{20}]^{\mathrm{T}}$ 为初值的解为

$$
\left\{ \begin{array}{l} x _ {1} = x _ {1} (t; x _ {0}) = \frac {\cos (t + \theta_ {0})}{\sqrt {1 + k _ {0} \mathrm{e} ^ {- 2 t}}}, \\ x _ {2} = x _ {2} (t; x _ {0}) = \frac {- \sin (t + \theta_ {0})}{\sqrt {1 + k _ {0} \mathrm{e} ^ {- 2 t}}}. \end{array} \right. \tag {2.5.18}
$$

从方程 (2.5.18) 看出，当 $k_0 > 0$ ，即 $x_{10}^2 + x_{20}^2 < 1$ 时，随着 $t \to +\infty$ ，微分方程 (2.5.14) 的从单位圆内部出发的轨线趋于单位圆周；当 $k_0 < 0$ ，即 $x_{10}^2 + x_{20}^2 > 1$ 时，随着 $t \to +\infty$ ，微分方程 (2.5.14) 的从单位圆外部出发的轨线也趋于单位圆周；又当 $k_0 < 0, t \to \ln(-k_0)^{1/2}$ 时， $\mathrm{e}^{-2t} \to -1/k_0$ 。从式 (2.5.18) 知， $x(t; x_0)$ 趋于无穷远点，但轨线的径向 $\frac{x_2(t; x_0)}{x_1(t; x_0)} = -\tan(t + \theta_0)$ 趋于 $-\tan[\ln(-k_0)^{1/2} + \theta_0]$ .

不难验证闭曲线 (即单位圆周)

$$
\left\{ \begin{array}{l} x _ {1} = x _ {1} (t; x _ {0}) = \cos t \\ x _ {2} = x _ {2} (t; x _ {0}) = \sin t \end{array} \right. \tag {2.5.19}
$$

也是微分方程(2.5.14)的轨线. 由此看到, 方程(2.5.14)的轨线分布是: 方程(2.5.14)有唯一的不稳定的焦点型奇点和唯一的封闭轨线 单位圆周, 其余的轨线按顺时针方向盘旋式地趋于单位圆周.

例2.5.3 考察非线性二阶向量微分方程
