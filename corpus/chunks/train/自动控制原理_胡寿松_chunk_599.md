$$\dot {x} _ {1} = \dot {x} _ {2} + R \frac {\mathrm{d} i}{\mathrm{d} t} = \frac {1}{R C} \left(x _ {1} - x _ {2}\right) + \frac {R}{L} (- x _ {1} + e)\dot {x} _ {2} = \frac {1}{C} i = \frac {1}{R C} \left(x _ {1} - x _ {2}\right)y = x _ {2}$$

其向量-矩阵形式为

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} \frac {1}{R C} - \frac {R}{L} & - \frac {1}{R C} \\ \frac {1}{R C} & - \frac {1}{R C} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} \frac {R}{L} \\ 0 \end{array} \right] e

y = \left[ \begin{array}{l l} 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

由上可见,系统的状态空间表达式不具有唯一性。选取不同的状态变量,便会有不同的状态空间表达式,但它们都描述了同一系统。可以推断,描述同一系统的不同状态空间表达式之间一定存在着某种线性变换关系。现研究本例题中两组状态变量之间的关系。

设 $x_{1} = i, x_{2} = \frac{1}{C}\int i\mathrm{d}t, \overline{x}_{1} = i, \overline{x}_{2} = \int i\mathrm{d}t$ ，则有

$$x _ {1} = \overline {{{{x}}}} _ {1}, \quad x _ {2} = \frac {1}{C} \overline {{{{x}}}} _ {2}$$

其相应的向量-矩阵形式为

$$\boldsymbol {x} = \boldsymbol {P x}$$

其中 $\pmb{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}, \quad \pmb{x} = \begin{bmatrix} \overline{x}_1 \\ \overline{x}_2 \end{bmatrix}, \quad \pmb{P} = \begin{bmatrix} 1 & 0 \\ 0 & \frac{1}{C} \end{bmatrix}$

以上说明只要令 $x = Px, P$ 为非奇异变换矩阵，便可将 $x_{1}, x_{2}$ 变换为 $\overline{x}_{1}, \overline{x}_{2}$ 。若取任意的非奇异变换阵 $P$ ，便可变换出无穷多组状态变量，这就说明状态变量的选择不具有唯一性。对于图9-4所示RLC网络来说，由于电容端电压和电感电流容易测量，通常选择这些物理量作为状态变量。
