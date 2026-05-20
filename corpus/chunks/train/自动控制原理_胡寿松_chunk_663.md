$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b} \boldsymbol {u} \tag {9-176}$$

进行 $P^{-1}$ 变换,即令

$$\boldsymbol {x} = \boldsymbol {P} ^ {- 1} \boldsymbol {z} \tag {9-177}$$

变换为

$$\dot {z} = \mathbf {P A P} ^ {- 1} z + \mathbf {P b u} \tag {9-178}$$

要求

$$
\boldsymbol {P} \boldsymbol {A} \boldsymbol {P} ^ {- 1} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right], \quad \boldsymbol {P} \boldsymbol {b} = \left[ \begin{array}{l} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \tag {9-179}
$$

下面具体推导变换矩阵 P:

设变换矩阵 $\pmb{P}$ 为

$$
\boldsymbol {P} = \left[ \begin{array}{l l l l} \boldsymbol {p} _ {1} ^ {\mathrm{T}} & \boldsymbol {p} _ {2} ^ {\mathrm{T}} & \dots & \boldsymbol {p} _ {n} ^ {\mathrm{T}} \end{array} \right] ^ {\mathrm{T}} \tag {9-180}
$$

根据 A 阵变换要求, P 应满足式(9-179), 有

$$
\left[ \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {2} \\ \vdots \\ \boldsymbol {p} _ {n - 1} \\ \boldsymbol {p} _ {n} \end{array} \right] \boldsymbol {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {2} \\ \vdots \\ \boldsymbol {p} _ {n - 1} \\ \boldsymbol {p} _ {n} \end{array} \right] \tag {9-181}
$$

展开为 $p_{1}A = p_{2}$

$$\boldsymbol {p} _ {2} \boldsymbol {A} = \boldsymbol {p} _ {3}$$

■
●
●

$$\boldsymbol {p} _ {n - 1} \boldsymbol {A} = \boldsymbol {p} _ {n}\boldsymbol {p} _ {n} \boldsymbol {A} = - a _ {0} \boldsymbol {p} _ {1} - a _ {1} \boldsymbol {p} _ {2} - \dots - a _ {n - 1} \boldsymbol {p} _ {n}$$

经整理有

$$\boldsymbol {p} _ {1} \boldsymbol {A} = \boldsymbol {p} _ {2}\boldsymbol {p} _ {2} \boldsymbol {A} = \boldsymbol {p} _ {1} \boldsymbol {A} ^ {2} = \boldsymbol {p} _ {3}$$

•
•
•

$$\boldsymbol {p} _ {n - 1} \boldsymbol {A} = \boldsymbol {p} _ {1} \boldsymbol {A} ^ {n - 1} = \boldsymbol {p} _ {n}$$

由此可得变换矩阵

$$
\boldsymbol {P} = \left[ \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {1} \boldsymbol {A} \\ \vdots \\ \boldsymbol {p} _ {1} \boldsymbol {A} ^ {n - 1} \end{array} \right] \tag {9-182}
$$

又根据 b 阵变换要求, P 应满足式(9-179), 有
