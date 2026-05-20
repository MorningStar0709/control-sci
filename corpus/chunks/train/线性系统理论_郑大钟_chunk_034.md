图 1.2 动力学系统结构示意图

和输入-输出描述不同,状态空间描述中把系统动态过程的描述考虑为一个更为细致的过程: 输入引起系统状态的变化,而状态和输入则决定了输出的变化。

输入引起状态的变化是一个运动的过程，数学上必须采用微分方程或差分方程来表征，并且称这个数学方程为系统的状态方程。就连续动态过程而言，考虑最为一般的情况，则其状态方程为如下的一个一阶非线性时变微分方程组：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = f _ {1} \left(x _ {1}, \dots , x _ {n}; u _ {1}, \dots , u _ {p}; t\right) \\ \dots \dots \\ \dot {x} _ {n} = f _ {n} \left(x _ {1}, \dots , x _ {n}; u _ {1}, \dots , u _ {p}; t\right) \end{array} \quad t \geqslant t _ {0} \right. \tag {1.10}
$$

进而，在引入向量表示的基础上，还可将状态方程简洁地表为向量方程的形式：

$$\dot {x} = f (x, u, t), \quad t \geqslant t _ {0} \tag {1.11}$$

其中

$$
\boldsymbol {x} = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {n} \end{array} \right], u = \left[ \begin{array}{c} u _ {1} \\ \vdots \\ u _ {p} \end{array} \right], f (\boldsymbol {x}, u, t) = \left[ \begin{array}{c} f _ {1} (\boldsymbol {x}, u, t) \\ \vdots \\ f _ {n} (\boldsymbol {x}, u, t) \end{array} \right] \tag {1.12}
$$

状态和输入决定输出的变化是一个变量间的转换过程，描述这种转换过程的数学表达式为变换方程，并且称其为系统的输出方程或量测方程。最为一般情况下，一个连续动力学系统的输出方程具有如下的形式：

$$
\left\{ \begin{array}{l} y _ {1} = g _ {1} \left(x _ {1}, \dots , x _ {n}; u _ {1}, \dots , u _ {p}; t\right) \\ \dots \dots \\ y _ {q} = g _ {q} \left(x _ {1}, \dots , x _ {n}; u _ {1}, \dots , u _ {p}; t\right) \end{array} \right. \tag {1.13}
$$

或表为向量方程的形式则为

$$y = g (x, u, t) \tag {1.14}$$

其中

$$
\mathcal {Y} = \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {q} \end{array} \right], \quad g (x, u, t) = \left[ \begin{array}{c} g _ {1} (x, u, t) \\ \vdots \\ g _ {q} (x, u, t) \end{array} \right] \tag {1.15}
$$

系统的状态空间描述由状态方程和输出方程所组成。由于采用向量方程的形式，当状态变量、输入变量和输出变量的数目增加时，并不增加状态空间描述在表达形式上的复杂性。特别是，如果限于考虑线性的连续动态过程，那么此时在系统的状态方程和输出方程中，向量函数 $f(x, u, t)$ 和 $g(x, u, t)$ 将都具有线性的关系，从而线性系统的状态空间描述可表为如下一般形式：

$$
\left\{ \begin{array}{l l} \dot {x} = A (t) x + B (t) u, & t \geqslant t _ {0} \\ y = C (t) x + D (t) u \end{array} \right. \tag {1.16}
$$

其中，各个系数矩阵分别为

$$
A (t) = \left[ \begin{array}{c c c} a _ {1 1} (t) & \dots & a _ {1 n} (t) \\ \vdots & & \vdots \\ a _ {n 1} (t) & \dots & a _ {n n} (t) \end{array} \right], B (t) = \left[ \begin{array}{c c c} b _ {1 1} (t) & \dots & b _ {1 p} (t) \\ \vdots & & \vdots \\ b _ {n 1} (t) & \dots & b _ {n p} (t) \end{array} \right]

C (t) = \left[ \begin{array}{c c c} c _ {1 1} (t) & \dots & c _ {1 n} (t) \\ \vdots & & \vdots \\ c _ {q 1} (t) & \dots & c _ {q n} (t) \end{array} \right], D (t) = \left[ \begin{array}{c c c} d _ {1 1} (t) & \dots & d _ {1 p} (t) \\ \vdots & & \vdots \\ d _ {q 1} (t) & \dots & d _ {q p} (t) \end{array} \right]
$$
