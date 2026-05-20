# 例 7.10 利用 Matlab 找磁带驱动系统的零极点

求出下面磁带驱动控制系统(见图 3.50)矩阵的特征值。并且计算变换矩阵，将磁带驱动系统的方程从给定形式变换成模态标准形。系统矩阵分别为

$$
\mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 2 & 0 & 0 & 0 \\ - 0. 1 & - 0. 3 5 & 0. 1 & 0. 1 & 0. 7 5 \\ 0 & 0 & 0 & 2 & 0 \\ 0. 4 & 0. 4 & - 0. 4 & - 1. 4 & 0 \\ 0 & - 0. 0 3 & 0 & 0 & - 1 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{array} \right] \tag {7.40}

\boldsymbol {C} _ {2} = \left[ \begin{array}{l l l l l} 0. 0 & 0. 0 & 1. 0 & 0. 0 & 0. 0 \end{array} \right] \text {为伺服电机位置输出；}

\boldsymbol {C} _ {3} = \left[ \begin{array}{l l l l l} 0. 5 & 0. 0 & 0. 5 & 0. 0 & 0. 0 \end{array} \right] \text {为读/写磁头上的位置作为输出；}
\boldsymbol {C} _ {\mathrm{T}} = \left[ - 0. 2 \quad - 0. 2 \quad 0. 2 \quad 0. 2 \quad 0. 0 \right] \text {为电压输出。}D = 0. 0
$$

状态矢量定义为

$$
x = \left[ \begin{array}{l l} x _ {1} & (\text { 主动轮上磁带位置 }) \\ \omega_ {1} & (\text { 驱动轮速度 }) \\ x _ {3} & (\text { 磁带在磁头的位置 }) \\ \omega_ {2} & (\text { 输出速度 }) \\ i & (\text { 主动轮电动机的输入电流 }) \end{array} \right]
$$

$C_{3}$ 矩阵对应使得 $x_{3}$ （磁带在读/写磁头上的位置）作为输出，而矩阵 $C_{T}$ 对应将电压作为输出。

解答。用 Matlab 计算特征值可以使用如下语句：

$$P = \text { eig } (A)$$

455

结果为

$$
\mathbf {P} = \left[ \begin{array}{c} - 0. 6 3 7 1 + 0. 6 6 6 9 i \\ - 0. 6 3 7 1 - 0. 6 6 6 9 i \\ 0. 0 0 0 0 \\ - 0. 5 0 7 5 \\ - 0. 9 6 8 3 \end{array} \right]
$$

注意，系统除了一个极点在原点处以外，其他所有极点都在左半平面(LHP)。这意味着阶跃输入将导致一个斜坡输出，由此可知系统属于1型系统。

为了转换成模态形，我们利用 Matlab canon 函数，语句如下：

$$
\begin{array}{l} \operatorname{sysG} = \operatorname{ss} (A, B, C 3, D); \\ [ \text { sysGm }, \Pi ] = \text { canon } (\text { sysG }, ^ {\prime} \text { modal } ^ {\prime}); \\ [ A m, B m, C m, D m ] = s s d a t a (s y s G m) \\ \end{array}
$$

计算结果为

$$
\mathrm{Am} = \mathbf {A} _ {\mathrm{m}} = \left[ \begin{array}{c c c c c} - 0. 6 3 7 1 & 0. 6 6 6 9 & 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 \\ - 0. 6 6 6 9 & - 0. 6 3 7 1 & 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 \\ 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 \\ 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 & - 0. 5 0 7 5 & 0. 0 0 0 0 \\ 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 & 0. 0 0 0 0 & - 0. 9 6 8 3 \end{array} \right]
$$

注意，复极点出现在 $A_{m}$ 矩阵的左上角的 $2 \times 2$ 方阵中，实极点落在该矩阵的主对角线上。利用 canon 函数计算出其余结果分别为
