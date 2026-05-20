$$
P = \left[ \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right], P ^ {- 1} = \left[ \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 1 & 0 \end{array} \right]
$$

从而，可定出

$$
\overline {{{A}}} = P ^ {- 1} A P = \left[ \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 1 \end{array} \right], \quad \overline {{{b}}} = P ^ {- 1} b = \left[ \begin{array}{l} 2 \\ 5 \\ 2 \end{array} \right]
$$

也即给定状态方程的对角线规范形为

$$
\left[ \begin{array}{l} \dot {\overline {{x}}} _ {1} \\ \dot {\overline {{x}}} _ {2} \\ \dot {\overline {{x}}} _ {3} \end{array} \right] = \left[ \begin{array}{l l l} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 1 \end{array} \right] \left[ \begin{array}{l} \overline {{x}} _ {1} \\ \overline {{x}} _ {2} \\ \overline {{x}} _ {3} \end{array} \right] + \left[ \begin{array}{l} 2 \\ 5 \\ 2 \end{array} \right] u
$$

下面,对上述结论作几点讨论:

(1) 由 (1.55) 可以看出, 在对角线规范形下, 各个状态变量间实现了完全解耦, 可表成为 $n$ 个独立的状态变量方程。

(2) 如果在 (1.53) 中, 系统矩阵 $A$ 具有形式

$$
A = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ 0 & & & 1 & \\ \hline - a _ {0} & - a _ {1} \dots & - a _ {n - 1} \end{array} \right] \tag {1.59}
$$

且其特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 两两不相等，则此时化状态方程为对角线规范形的变换阵可按下述方式组成：

$$
P = \left[ \begin{array}{c c c} 1 & \dots & 1 \\ \lambda_ {1} & \dots & \lambda_ {n} \\ \vdots & & \vdots \\ \lambda_ {1} ^ {n - 1} & \dots & \lambda_ {n} ^ {n - 1} \end{array} \right] \tag {1.60}
$$

这一推论的正确性可直接利用关系式 $Av_{i} = \lambda_{i}v_{i}$ 来证明，具体推证过程略去。

(3) 当特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 中包含复数特征值时，上述变换阵 P 和对角线规范形 (1.55) 中的系数矩阵 $\overline{A}$ 及 $\overline{B}$ 都将为复数阵。尽管这种处理和形式是没有实际物理含义的，但它不会影响对系统结构特性的分析。

约当规范形 如果系统的特征值为非互异，则其状态方程一般不能变换为对角线规范形，但可构造特定的变换阵使之化为准对角线规范形，即约当（Jordan）规范形。下面，就约当规范形及其变换阵等有关概念，逐点进行讨论。

(1) 约当规范形 给定系统的状态方程(1.53)，设其特征值为 $\lambda_{1}(\sigma_{1}\text{重}), \lambda_{2}(\sigma_{2}\text{重}), \cdots, \lambda_{l}(\sigma_{l}\text{重}), (\sigma_{1} + \sigma_{2} + \cdots + \sigma_{l}) = n$ ，则存在可逆变换阵 Q，通过引入变换 $\hat{x} = Q^{-1}x$ ，可使状态方程(1.53)化为如下的约当规范形：

$$
\dot {\hat {x}} = Q ^ {- 1} A Q \hat {x} + Q ^ {- 1} B u = \left[ \begin{array}{c c c} J _ {1} & & \\ & \ddots & \\ & & J _ {t} \end{array} \right] \hat {x} + \hat {B} u \tag {1.61}
$$

其中， $\hat{B}=Q^{-1}B,\ J_{i}$ 为 $\sigma_{i}\times\sigma_{i}$ 阵且具有形式

$$
J _ {i} = \left[ \begin{array}{c c c} J _ {j i} & & \\ & \ddots & \\ & & J _ {j e _ {i}} \end{array} \right], i = 1, 2, \dots , l \tag {1.62}
$$

$J_{ik}$ 称为相应于特征值 $\lambda_{i}$ 的约当小块且具有形式
