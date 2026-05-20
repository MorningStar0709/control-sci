例2 考虑3.1节中给出的例3，即图 $3.2(b)$ 所示的电路，不难导出 $u(t) = 0$ 时电路的状态方程和输出方程为：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - \frac {\left(R _ {1} + R _ {2}\right)}{L} & \frac {R _ {2}}{L} \\ \frac {R _ {2}}{L} & - \frac {\left(R _ {1} + R _ {2}\right)}{L} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right], \quad n = 2

y = \left[ R _ {2} - R _ {2} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right]
$$

其中 $R_{1}, R_{2}$ 和 $L$ 可为任意值。于是，通过计算可得到：

$$
Q _ {o} = \left[ \begin{array}{c} C \\ C A \end{array} \right] = \left[ \begin{array}{c c} R _ {2} & - R _ {2} \\ - \frac {\left(R _ {1} R _ {2} + 2 R _ {2} ^ {2}\right)}{L} & \frac {\left(R _ {1} R _ {2} + 2 R _ {2} ^ {2}\right)}{L} \end{array} \right]
$$

显见 $\operatorname{rank} Q_{n} = 1 < n = 2$ ，因此系统为不完全能观测。

结论 3 [PBH 秩判据] 线性定常系统 (3.75) 为完全能观测的充分必要条件是, 对矩阵 A 的所有特征值 $\lambda_{i}(i=1,2,\cdots,n)$ 均成立

$$
\operatorname{rank} \left[ \begin{array}{c} C \\ \lambda_ {i} I - A \end{array} \right] = n, \quad i = 1, 2, \dots , n \tag {3.82}
$$

或等价地表为

$$
\operatorname{rank} \left[ \begin{array}{c} C \\ s I - A \end{array} \right] = n, \forall s \in \mathcal {C} \tag {3.83}
$$

也即 $(sI - A)$ 和 $C$ 是右互质的。

结论4 [PBH 特征向量判据] 线性定常系统（3.75）为完全能观测的充分必要条件是，A 没有与 C 的所有行相正交的非零右特征向量。也即对 A 的任一特征值 $\lambda_{i}$ ，使同时满足

$$A \bar {a} = \lambda_ {i} \bar {a}, \quad C \bar {a} = 0 \tag {3.84}$$

的特征向量 $\bar{a} \equiv 0$ 。

结论5[约当规范形判据] 线性定常系统(3.75)为完全能观测的充分必要条件是

(1) 当矩阵 A 的特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 为两两相异时，为由 (3.75) 导出的对角线规范形

$$
\begin{array}{l} \dot {\bar {x}} = \left[ \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \bar {x} \\ y = \bar {C} \bar {x} \end{array} \tag {3.85}
$$

中， $\overline{c}$ 不包含元素全为零的列。

(2) 当矩阵 A 的特征值为 $\lambda_{1}(\sigma_{1}\text{重}), \lambda_{2}(\sigma_{2}\text{重}), \cdots, \lambda_{l}(l\text{重})$ ，且 $(\sigma_{1} + \sigma_{2} + \cdots + \sigma_{l}) = n$ 时，为对 (3.75) 导出的约当规范形

$$
\begin{array}{l} \dot {\hat {x}} - \dot {A} \hat {x} \\ y - \hat {C} \hat {x} \end{array} \tag {3.86}
$$

其中

$$
\underset {(a \times a)} {A} = \left[ \begin{array}{c c c} J _ {1} & & \\ & J _ {2} & \\ & & \ddots \\ & & J _ {l} \end{array} \right] \quad \hat {C} _ {(a \times a)} = [ \hat {C} _ {1}, \hat {C} _ {2}, \dots , \hat {C} _ {1} ] \tag {3.87}
