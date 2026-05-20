下面，我们进而介绍确定矩阵指数函数 $e^{At}$ 的一些常用计算方法，并举例说明它们的应用。

方法 1: 直接利用定义关系式:

$$e ^ {A t} = I + A t + \frac {1}{2 !} A ^ {2} t ^ {2} + \frac {1}{3 !} A ^ {3} t ^ {3} + \dots \tag {2.31}$$

通常,由这一方法只能得到 $e^{At}$ 的数值结果,一般难以获得其函数表达式。当运用计算机进行计算时,这种方法具有编程方便和计算简单的优点。

方法 2: 如果系统矩阵 A 的 n 个特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 为两两相异，则在定出使 A 实现对角线化

$$
A = P \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \ddots & \\ & & \lambda_ {n} \end{array} \right] P ^ {- t} \tag {2.32}
$$

的变换阵 $P$ 及其逆 $P^{-1}$ 后，即有

$$
e ^ {A t} = P \left[ \begin{array}{c c c} e ^ {\lambda_ {1} t} & & \\ & \ddots & \\ & & e ^ {\lambda_ {n} t} \end{array} \right] P ^ {- 1} \tag {2.33}
$$

此关系式的正确性已在(2.20)中作了证明。

对于系统矩阵 $A$ 包含重特征值的情况，原理上也可给出类同于(2.33)的关系式，但其形式要复杂得多。为不致符号过于繁杂，不妨考虑一个具体的例子。设 $A$ 具有相异特征值 $\lambda_{1}$ （三重）和 $\lambda_{2}$ （二重），且可找到变换阵 $Q$ 和 $Q^{-1}$ ，使其实现约当形化：

$$
A = Q \left[ \begin{array}{c c c c c} - \lambda_ {1} & 1 & 0 & 0 & 0 \\ 0 & \lambda_ {1} & 1 & 0 & 0 \\ 0 & 0 & \lambda_ {1} & 0 & 0 \\ \hline 0 & 0 & 0 & \lambda_ {2} & 1 \\ - 0 & 0 & 0 & 0 & \lambda_ {2} \end{array} \right] Q ^ {- 1} \tag {2.34}
$$

则相应的矩阵指数函数为：

$$
e ^ {A t} = Q \left[ \begin{array}{c c c c c} e ^ {\lambda_ {1} t} & t e ^ {\lambda_ {1} t} & t ^ {2} e ^ {\lambda_ {1} t} / 2! & 0 & 0 \\ 0 & e ^ {\lambda_ {1} t} & t e ^ {\lambda_ {1} t} & 0 & 0 \\ 0 & 0 & e ^ {\lambda_ {1} t} & 0 & 0 \\ \hline 0 & 0 & 0 & e ^ {\lambda_ {2} t} & t e ^ {\lambda_ {2} t} \\ 0 & 0 & 0 & 0 & e ^ {\lambda_ {2} t} \end{array} \right] Q ^ {- 1} \tag {2.35}
$$

方法 3: 把 $e^{At}$ 表为 $A^{k}(k=0,1,\cdots,n-1)$ 的一个多项式, 即

$$e ^ {A t} = a _ {0} (t) I + a _ {1} (t) A + \dots + a _ {n - 1} (t) A ^ {n - 1} \tag {2.36}$$

其中，对于 $A$ 的特征值 $\lambda_1, \lambda_2, \cdots, \lambda_n$ 为两两相异的情况， $\alpha_0(t), \alpha_1(t), \cdots, \alpha_{n-1}(t)$ 可按下式计算：

$$
\left[ \begin{array}{c} \alpha_ {0} (t) \\ \alpha_ {1} (t) \\ \vdots \\ \alpha_ {n - 1} (t) \end{array} \right] = \left[ \begin{array}{l l l l l} 1 & \lambda_ {1} & \lambda_ {1} ^ {2} & \dots & \lambda_ {1} ^ {n - 1} \\ 1 & \lambda_ {2} & \lambda_ {2} ^ {2} & \dots & \lambda_ {2} ^ {n - 1} \\ \vdots & \vdots & \vdots & & \\ 1 & \lambda_ {n} & \lambda_ {n} ^ {2} & \dots & \lambda_ {n} ^ {n - 1} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} e ^ {\lambda_ {1} t} \\ e ^ {\lambda_ {2} t} \\ \vdots \\ e ^ {\lambda_ {n} t} \end{array} \right] \tag {2.37}
$$

对于 A 包含重特征值的情况,例如其特征值为 $\lambda_{1}$ (三重), $\lambda_{2}$ (二重), $\lambda_{3}, \cdots, \lambda_{n-3}$ 时, $\alpha_{0}(t), \alpha_{1}(t), \cdots, \alpha_{n-1}(t)$ 可按下式计算:
