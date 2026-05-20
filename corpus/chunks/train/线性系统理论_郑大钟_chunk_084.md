考虑到 $\omega_{s}=2\pi/T$ ，则（2.134）可化为对采样周期 T 加以限制的一个不等式：

$$T < \pi / \omega_ {e} \tag {2.135}$$

![](image/dd3ece01454d977e11b01f45c469447febc6b7ee4f18d4c17abb52cfda616bfb.jpg)  
图 2.3 连续信号的幅频谱及其上限频率

![](image/34a758507f7cda97761492844d9932a9eeb842ebf4e600721647f78258e3316e.jpg)  
图 2.4 零阶保持的示意图

③ 保持器是零阶的，即把离散信号转换为连续信号是按零阶保持方式来实现的。零阶保持的示意图见图2.4。零阶保持的特点是：保持器输出 $u_{j}(t)$ 的值在采样瞬时等于离散信号 $u_{j}(k)$ 的值，而在两个采样瞬时之间则保持为常值且等于前一采样瞬时上的值。

基本结论 在上述三点基本假设的前提下，我们现在来给出并证明线性连续系统的时间离散化问题的两个基本结论。

结论1 给定线性连续时变系统

$$\dot {\boldsymbol {x}} = A (t) \boldsymbol {x} + B (t) \boldsymbol {u}, \quad t \in [ t _ {0}, t _ {a} ]\mathbf {y} = C (t) \mathbf {x} + D (t) \mathbf {u}, \quad \mathbf {x} \left(t _ {0}\right) = \mathbf {x} _ {0} \tag {2.136}$$

则其在基本假设下的时间离散化模型为：

$$\boldsymbol {x} (k + 1) = G (k) \boldsymbol {x} (k) + H (k) \boldsymbol {u} (k), \quad k = 0, 1, \dots , l\mathbf {y} (k) = C (k) \mathbf {x} (k) + D (k) \mathbf {u} (k), \quad \mathbf {x} (0) = \mathbf {x} _ {0} \tag {2.137}$$

并且，两者的系数矩阵间存在如下的关系式：

$$G (k) = \Phi ((k + 1) T, k T) \triangleq \Phi (k + 1, k)H (k) = \int_ {k T} ^ {(k + 1) T} \Phi ((k + 1) T, \tau) B (\tau) d \tau \tag {2.138}C (k) = [ C (t) ] _ {t = k T}D (k) = [ D (t) ] _ {t = k T}$$

其中， $T$ 为采样周期， $l = (t_{a} - t_{0}) / T$ ， $\Phi (\cdot ,\cdot)$ 是连续系统（2.136）的状态转移矩阵， $x(k) = [x(t)]_{t = kT},u(k) = [u(t)]_{t = kT},y(k) = [y(t)]_{t = kT}\circ$

证 前已导出,线性连续时变系统(2.136)的状态运动表达式为:

$$\boldsymbol {x} (t) = \Phi (t, t _ {0}) \boldsymbol {x} _ {0} + \int_ {t _ {0}} ^ {t} \Phi (t, \tau) B (\tau) \boldsymbol {u} (\tau) d \tau \tag {2.139}$$

上式中，令 $t = (k + 1)T$ ，而表 $\pmb{\iota_0}$ 对应为 $k = 0$ ，可得到：

$$
\begin{array}{l} \boldsymbol {x} (k + 1) = \Phi (k + 1, 0) \boldsymbol {x} _ {0} + \int_ {0} ^ {(k + 1) T} \Phi ((k + 1) T, \tau) B (\tau) \boldsymbol {u} (\tau) d \tau \\ = \Phi (k + 1, k) \left[ \Phi (k, 0) x _ {0} + \int_ {0} ^ {k T} \Phi (k T, \tau) B (\tau) u (\tau) d \tau \right] \\ \end{array}
+ \left[ \int_ {k T} ^ {(k + 1) T} \Phi ((k + 1) T, \tau) B (\tau) d \tau \right] u (k)= G (k) \boldsymbol {x} (k) + H (k) \boldsymbol {u} (k) \tag {2.140}
$$

再对输出方程加以离散化，即令 $t = kT$ ，又可得到：

$$\mathbf {y} (k) = C (k) \mathbf {x} (k) + D (k) \mathbf {u} (k) \tag {2.141}$$

从而，就完成了证明。

结论 2 给定线性连续定常系统

$$
\begin{array}{l} \dot {x} = A x + B u, \quad x (0) = x _ {0}, t \geqslant 0 \\ y = C x + D x \end{array} \tag {2.142}
\mathbf {y} = C \mathbf {x} + D \mathbf {u}
$$

则其在基本假设下的时间离散化模型为：
