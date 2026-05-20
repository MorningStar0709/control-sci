\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1} (t), x _ {2} (t)) - z _ {3} (t) + b u _ {0} \Rightarrow \left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = b u _ {0} \\ y = x _ {1} \end{array} \right. \\ y = x _ {1} \end{array} \right. \tag {4.3.14}
$$

或

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + b \frac {u _ {0} - z _ {3} (t)}{b} \Rightarrow \\ y = x _ {1} \end{array} \right.

\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1} (t), x _ {2} (t)) - z _ {3} (t) + u _ {0} \Rightarrow \left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = u _ {0} \\ y = x _ {1} \end{array} \right. \\ y = x _ {1} \end{array} \right. \tag {4.3.15}
$$

即原来的非线性控制系统(4.3.2)变成线性的积分器串联型控制系统.

对非线性控制系统(4.3.2)用扩张状态观测器(4.3.5)估计的结果来把控制量取成(4.3.13)的形式,使原非线性控制系统(4.3.2)变成线性控制系统(4.3.14)或(4.3.15)的过程,称为动态补偿线性化过程(用系统输出y来改造系统输入u的过程).

这样,无论对象(4.3.2)是确定性的还是不确定性的,线性的还是非线性的,时变的还是时不变的,经过式(4.3.10)形式的补偿,均可以把系统化成(4.3.13)或(4.3.14)形式的积分器串联型被控制系统.这样,扩张状态观测器和(4.3.12)形式的补偿办法给予我们一种可能性,用统一的方式来处理确定性和不确定性,线性和非线性,时变和时不变等控制系统的控制问题.

例1 设有系统

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = a \operatorname{sign} (\sin (\omega t)) + 3 \cos \left(\frac {t}{2}\right) \\ y = x _ {1} \end{array} \right. \tag {4.3.16}
$$

式中， $a = 1, w = 1.0$ . 假定系统中函数 $3\cos \left(\frac{t}{2}\right)$ 是已知的输入. 我们想用离散型扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = | e | ^ {\frac {1}{2}} \operatorname{sign} (e), \mathrm{fe} _ {1} = | e | ^ {\frac {1}{4}} \operatorname{sign} (e) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe} + 3 \cos \left(\frac {t}{2}\right)\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {4.3.17}
$$

进行状态和被扩张的状态 $x_{3}(t) = \operatorname{asign}(\sin (\omega t))$ 的实时估计的数值仿真结果如图4.3.2所示.这里，状态变量 $x_{1}(t),x_{2}(t)$ 和其估计值 $z_{1}(t),z_{2}(t)$ 的差别已看不出来了，但被扩张的状态和其估计 $z_{3}(t)$ 的差别是可以从图4.3.2中看得出来.在这里参数取了如下值：

$$h = 0. 0 1, \delta = h, \beta_ {0 1} = 1 0 0, \beta_ {0 2} = 3 0 0, \beta_ {0 3} = 1 0 0 0.$$

![](image/114ad871be55d759505888080dc6e9d3cbaf68797c8f487f23e51be346fa6cce.jpg)

<details>
<summary>line</summary>
