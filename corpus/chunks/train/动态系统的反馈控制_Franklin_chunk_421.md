这些方程再次表明，传递函数的极点是系统矩阵 A 的特征值。行列式式(7.55)为特征值 $p_{i}$ 的多项式，称为特征方程。例 7.9 中，我们计算了一个能控标准形的特殊矩阵相应的特征值和特征矢量。计算此系统的极点还有另外一个方法，即求解特征式(7.55)。对于式(7.12a)和式(7.12b)所描述的系统，根据式(7.55)求解下式找到系统的极点：

$$
\det (s \boldsymbol {I} - \boldsymbol {A}) = 0 \tag {7.56a}
\det \left[ \begin{array}{c c} s + 7 & 1 2 \\ - 1 & s \end{array} \right] = 0 \tag {7.56b}
s (s + 7) + 1 2 = (s + 3) (s + 4) = 0 \tag {7.56c}
$$

这再次验证了系统的极点是矩阵 A 的特征值。

由系统理论的观点，我们也可以通过状态描述矩阵 A, B, C 和 D 求出系统的零点。从这个角度而言，零点就是广义频率 s 的一个值，该值使得系统存在一个非零输入和状态时仍然可以得到零输出。如果输入在零频率 $z_{i}$ 下是指数形式，即

$$u (t) = u _ {0} \mathrm{e} ^ {z _ {\mathrm{i}} t} \tag {7.57}$$

那么输出是恒为零的，即

$$y (t) \equiv 0 \tag {7.58}$$

式 $(7.57)$ 和式 $(7.58)$ 的状态空间描述将变为

$$u = u _ {0} \mathrm{e} ^ {z _ {1} t}, \quad x (t) = x _ {0} \mathrm{e} ^ {z _ {1} t}, \quad y (t) \equiv 0 \tag {7.59}$$

因此

$$\boldsymbol {x} = z _ {\mathrm{i}} \mathrm{e} ^ {z _ {\mathrm{i}} t} \boldsymbol {x} _ {0} = \boldsymbol {A} \mathrm{e} ^ {z _ {\mathrm{i}} t} \boldsymbol {x} _ {0} + \boldsymbol {B} u _ {0} \mathrm{e} ^ {z _ {\mathrm{i}} t} \tag {7.60}$$

或

$$
\left[ z _ {i} \boldsymbol {I} - \boldsymbol {A} - \boldsymbol {B} \right] \left[ \begin{array}{l} x _ {0} \\ u _ {0} \end{array} \right] = 0 \tag {7.61}
$$

及

$$y = \mathbf {C} x + D u = \mathbf {C} \mathrm{e} ^ {z _ {\mathrm{i}} t} \mathbf {x} _ {0} + D u _ {0} \mathrm{e} ^ {z _ {\mathrm{i}} t} \equiv 0 \tag {7.62}$$

联立式(7.61)和式(7.62)，我们得到

$$
\left[ \begin{array}{c c} z _ {i} I - A & - B \\ C & D \end{array} \right] \left[ \begin{array}{l} x _ {0} \\ u _ {0} \end{array} \right] = \left[ \begin{array}{l} 0 \\ 0 \end{array} \right] \tag {7.63}
$$

由式(7.63)，我们可以得到，状态空间形式的系统的零点就是使式(7.63)具有非平凡解 $z_{i}$ 的某个值。对于单输入单输出情况，矩阵是方阵，对于式(7.63)的解等价于如下方程的解

$$
\det \left[ \begin{array}{c c} z _ {\mathrm{i}} I - A & - B \\ C & D \end{array} \right] = 0 \tag {7.64}
$$
