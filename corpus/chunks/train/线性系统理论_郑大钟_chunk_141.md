(i) 定出系统的能控规范形和变换阵。  
(ii) 定出系统的能观测规范形和变换阵。

3.12 给定能控的单输入定常系统

$$\dot {x} = A x + b u$$

其中 $A$ 为 $n \times n$ 常阵， $b$ 为 $n \times 1$ 常阵。现取线性非奇异变换 $\bar{x} = Px$ ，其中 $P^{-1} = [b,$

$Ab,\cdots,A^{n-1}b]$ ，试定出变换后的系统状态方程，并论证变换后系统是否仍为完全能控。

3.13 给定能控定常系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \\ 1 & 0 \end{array} \right] \boldsymbol {u}
$$

定出其旺纳姆能控规范形和龙伯格能控规范形。

3.14 定出下列系统的一个按能控性分解的规范形：

$$
\dot {x} = \left[ \begin{array}{c c} - 1 & 1 \\ 0 & 0 \end{array} \right] x + \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] u
$$

3.15 导出下列系统的能控和能观测子系统：

$$
\begin{array}{l} \dot {x} = \left[ \begin{array}{c c c c c} \lambda_ {1} & 1 & 0 & 0 & 0 \\ 0 & \lambda_ {1} & 1 & 0 & 0 \\ 0 & 0 & \lambda_ {1} & 0 & 0 \\ 0 & 0 & 0 & \lambda_ {2} & 1 \\ 0 & 0 & 0 & 0 & \lambda_ {2} \end{array} \right] x + \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ 0 \\ 1 \end{array} \right] u \\ y = [ 0 \quad 1 \quad 1 \quad 0 \quad 1 ] x \end{array}
$$

3.16 设有单变量定常系统

$$\dot {x} = A x + b u, \quad y = c x + d u$$

其中， $A, b$ 和 $\pmb{c}$ 均为非零常阵。且成立

$$c b = 0, c A b = 0, \dots , c A ^ {n - 1} b = 0$$

其中 $n = \dim(A)$ 。试论证：此系统是否是联合能控和能观测的。

3.17 定出上题中给出的系统的传递函数 $g(s)$ 。

3.18 设有单变量定常系统

$$\dot {x} = A x + b u, \quad y = c x$$

已知 $\{A, b\}$ 为能控，试问是否存在 $\mathbf{c}$ 使得 $\{A, \mathbf{c}\}$ 总是能观测的。请加以论证，并举一个例子来支持你的论证。
