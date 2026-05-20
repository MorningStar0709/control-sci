# 2.4 线性定常系统的脉冲响应矩阵

脉冲响应矩阵 考虑一个具有 p 个输入端和 q 个输出端的线性定常系统，假设系统具有零初始状态，令在 $\tau$ 时刻加于第 j 个输入端一个单位脉冲函数 $\delta(t-\tau)^{1}$ ，而令其他输入端的输入为零，则用 $g_{ij}(t-\tau)$ 表示第 i 个输出端在 t 时刻的脉冲响应。而以脉冲响应 $g_{ij}(t-\tau)$ ( $i=1,2,\cdots,q, j=1,2,\cdots,p$ ) 为元所构成的 $q \times p$ 矩阵

$$
G (t - \tau) = \left[ \begin{array}{c c c c} g _ {1 1} (t - \tau) & g _ {1 2} (t - \tau) & \dots & g _ {1 p} (t - \tau) \\ g _ {2 1} (t - \tau) & g _ {2 2} (t - \tau) & \dots & g _ {2 p} (t - \tau) \\ \vdots & \vdots & & \vdots \\ g _ {q 1} (t - \tau) & g _ {q 2} (t - \tau) & \dots & g _ {q p} (t - \tau) \end{array} \right] \tag {2.65}
$$

称为系统的脉冲响应矩阵。并且，由于系统满足因果律，且总是假定系统的输出在输入加

1) $\delta(t-\tau)$ 定义为:

$$
\delta (t - \tau) = \left\{ \begin{array}{l l} 0, & t \neq \tau \\ \infty , & t = \tau \end{array} , \int_ {- \infty} ^ {\infty} \delta (t - \tau) d t = \int_ {\tau - \varepsilon} ^ {\tau + \varepsilon} \delta (t - \tau) d t = 1 \right.
$$

其中 $s \to 0$ 。

人之前的所有瞬时为零,所以 $G(t-\tau)$ 具有性质:

$$G (t - \tau) = 0, \forall \tau \text {和} \forall t < \tau \tag {2.66}$$

当系统的输入向量 $\pmb{u}$ 的元为任意形式的时间函数时，可将其用一系列脉冲函数来逼近，即表为

$$u _ {j} \approx \sum_ {k} u _ {j} (t _ {k}) \delta (t - t _ {k}) \Delta t, \quad j = 1, 2, \dots , p \tag {2.67}$$

而相应的系统输出为

$$\mathbf {y} (t) \approx \sum_ {k} G (t - t _ {k}) u (t _ {k}) \Delta t \tag {2.68}$$

现令 $\Delta t \rightarrow 0$ ，那么上式中的近似相等就趋于精确相等，且和式可用积分代替，因而可得到根据脉冲响应矩阵来计算任意输入时的系统输出的一个基本关系式：

$$\mathbf {y} (t) = \int_ {t _ {0}} ^ {t} G (t - \tau) u (\tau) d \tau , \quad t \geqslant t _ {0} \tag {2.69}$$

进一步，如果按习惯的做法取初始时刻 $t_0 = 0$ ，那么上式还可表为：

$$\mathcal {Y} (t) = \int_ {0} ^ {t} G (t - \tau) u (\tau) d \tau , \quad t \geqslant 0 \tag {2.70}$$

对上式作自变量置换,则又可将(2.70)表示为另一形式:

$$\mathbf {y} (t) = \int_ {0} ^ {t} G (\tau) u (t - \tau) d \tau , \quad t \geqslant 0 \tag {2.71}$$

由式(2.70)和(2.71)所给出的积分关系式通常称为卷积或折积。

脉冲响应矩阵和状态空间描述 为了建立起脉冲响应矩阵和状态空间描述间的关系,考虑如下的线性定常系统:

$$\dot {x} = A x + B u, \quad x \left(t _ {0}\right) = x _ {0}, \quad t \geqslant t _ {0} \tag {2.72}\mathbf {y} = C \mathbf {x} + D \mathbf {u}$$

其中 A, B, C 和 D 分别是 $n \times n$ , $n \times p$ , $q \times n$ 和 $q \times p$ 的实值常阵。

结论 1 由(2.72)所描述的线性定常系统的脉冲响应矩阵为:

$$G (t - \tau) = C e ^ {A (t - \tau)} B + D \delta (t - \tau) \tag {2.73}$$

或将其写成更为常用的形式为:

$$G (t) = C e ^ {A t} B + D \delta (t) \tag {2.74}$$

证 利用系统(2.72)的状态方程解的表达式(2.53)和输出方程,有

$$\mathbf {y} (t) = C e ^ {A \left(t - t _ {0}\right)} \mathbf {x} _ {0} + \int_ {t _ {0}} ^ {t} C e ^ {A \left(t - \tau\right)} B \mathbf {u} (\tau) d \tau + D \mathbf {u} (t) \tag {2.75}$$
