$$
\textbf {M} = - \textbf {A}
\begin{array}{l} \boldsymbol {T} = \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \\ \boldsymbol {V} = - \boldsymbol {Q} \\ \end{array}
$$

方法三：

也可以采用 care() 函数对连续时间代数黎卡提方程求解, 其调用方法如下:

$$[ \mathrm{P}, \mathrm{E}, \mathrm{K}, \mathrm{RR} ] = \operatorname{care} (\mathrm{A}, \mathrm{B}, \mathrm{Q}, \mathrm{R}, \text {zeros} (\text {size} (\mathrm{B})), \text {eye} (\text {size} (\mathrm{A})))$$

式中输入矩阵为 A, B, Q, R，其中 $(A, B)$ 为给定的对象状态方程模型， $(Q, R)$ 分别为加权矩阵 Q 和 R；返回矩阵 P 为代数黎卡提方程的解，E 为闭环系统的零极点，K 为状态反馈矩阵，RR 是相应的留数矩阵 Res 的 Frobenius 范数（其值为：sqrt（sum（diag（Res' \* Res））），或者用 Norm（Res, 'fro'）计算）。

采用 care 函数的优点在于可以设置 P 的终值条件,例如可以在下面的程序中设置 P 的终值条件为 $[0.2;0.2]$ 。

$$[ \mathrm{P}, \mathrm{E}, \mathrm{K}, \mathrm{RR} ] = \text { care } (\mathrm{A}, \mathrm{B}, \mathrm{Q}, \mathrm{R}, [ 0. 2; 0. 2 ], \text { eye } (\text { size } (\mathrm{A})))$$

采用 lqr() 函数不能设置代数黎卡提方程的边界条件。

例12-1 线性系统为：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 5 & - 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}
$$

其目标函数是

$$
J = \frac {1}{2} \int_ {0} ^ {\infty} \left\{\boldsymbol {x} ^ {\mathrm{T}} \left[ \begin{array}{l l} 5 0 0 & 2 0 0 \\ 2 0 0 & 1 0 0 \end{array} \right] \boldsymbol {x} + \boldsymbol {u} ^ {\mathrm{T}} [ 1. 6 6 6 7 ] \boldsymbol {u} \right\} \mathrm{d} t
$$

确定最优控制。

解

方法一：

$$
\begin{array}{l} \mathrm{A} = \left[ 0 1; - 5 - 3 \right]; \\ \mathbf {B} = [ 0; 1 ]; \\ \mathrm{Q} = [ 5 0 0 2 0 0; 2 0 0 1 0 0 ]; \\ \mathrm{R} = 1. 6 6 6 7; \\ \mathbf {m y l q} \\ \mathbf {K} = \operatorname{inv} (\mathbf {R}) * \mathbf {B} ^ {\prime} * \mathbf {P} \\ \mathbf {P} \\ \end{array}
$$

E

运行结果：

$$
\begin{array}{l} \mathrm{K} = 1 3. 0 2 7 6 \quad 6. 7 4 9 6 \\ \mathrm{P} = 6 7. 9 4 0 6 \quad 2 1. 7 1 3 1 \\ \begin{array}{l l} 2 1. 7 1 3 1 & 1 1. 2 4 9 5 \end{array} \\ \mathrm{E} = - 0. 1 1 1 1 \quad 0. 2 2 2 2 \\ - 1. 1 1 1 1 - 0. 7 7 7 8 \\ \end{array}
$$

方法二：

$$
\begin{array}{l} \mathbf {A} = \left[ 0 1; - 5, - 3 \right]; \\ \mathbf {B} = [ 0; 1 ]; \\ \mathrm{Q} = [ 5 0 0 2 0 0; 2 0 0 1 0 0 ]; \\ \mathrm{R} = 1. 6 6 6 7; \\ [ \mathbf {K}, \mathbf {P}, \mathbf {E} ] = \mathrm{lqr} (\mathbf {A}, \mathbf {B}, \mathbf {Q}, \mathbf {R}) \\ \end{array}
$$

运行结果：

$$
\begin{array}{l} \mathrm{K} = 1 3. 0 2 7 6 \quad 6. 7 4 9 6 \\ \mathrm{P} = 6 7. 9 4 0 6 \quad 2 1. 7 1 3 1 \\ \begin{array}{l l} 2 1. 7 1 3 1 & 1 1. 2 4 9 5 \end{array} \\ \mathrm{E} = - 7. 2 6 9 8 \\ - 2. 4 7 9 8 \\ \end{array}
$$

方法三：
