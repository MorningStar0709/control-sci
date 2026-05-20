图 7.7 式(7.9)的能控标准形对应的框图

当积分器的输出是状态变量时，积分器的输入是该状态变量的导数。例如，在图 7.7 中第一个状态变量满足的方程为

$$\dot {x} _ {1} = - 7 x _ {1} - 1 2 x _ {2} + u$$

继续使用上述方法，我们得到

$$\dot {x} _ {2} = x _ {1}y = x _ {1} + 2 x _ {2}$$

这三个方程可以重写成矩阵形式，即

$$\dot {x} = A _ {\mathrm{c}} x + B _ {\mathrm{c}} u \tag {7.10}y = C _ {c} x \tag {7.11}$$

其中：

$$
\mathbf {A} _ {\mathrm{c}} = \left[ \begin{array}{c c} - 7 & - 1 2 \\ 1 & 0 \end{array} \right], \qquad \mathbf {B} _ {\mathrm{c}} = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \tag {7.12a}

C _ {\mathrm{c}} = \left[ \begin{array}{l l} 1 & 2 \end{array} \right], \qquad D _ {\mathrm{c}} = 0 \tag {7.12b}
$$

其中：下标 c 代表能控标准形。

关于这个形式有两个重要特点：一个是传递函数的分子多项式 $b(s)$ 的系数 1 和 2 出现在矩阵 $C_{c}$ 中；另一个是（除了首项）分母多项式 $a(s)$ 的系数 7 和 12（符号取反）作为矩阵 $A_{c}$ 的第一行出现。根据这个结论，我们可以通过观察写出任意系统的能控标准形的状态矩阵，前提是该系统的传递函数是分子分母多项式的比值的形式。如果 $b(s)=b_{1}s^{n-1}+b_{2}s^{n-2}+\cdots+b_{n}$ 和 $a(s)=s^{n}+a_{1}s^{n-1}+a_{2}s^{n-2}+\cdots+a_{n}$ ，则求状态矩阵的 Matlab 语句如下。

$$
\begin{array}{l} \text { num } = b = [ b _ {1} \quad b _ {2} \quad \dots \quad b _ {n} ] \\ \text { den } = a = [ 1 \quad a _ {1} \quad a _ {2} \quad \dots \quad a _ {n} ] \\ [ A _ {c}, \quad B _ {c}, \quad C _ {c}, \quad D _ {c} ] = t f 2 s s (\text { num }, \text { den }). \end{array}
$$

将 tf2ss 理解为传递函数到状态空间，程序运行的结果为

$$
\boldsymbol {A} _ {\mathrm{c}} = \left[ \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & \dots & - a _ {\mathrm{n}} \\ 1 & 0 & \dots & \dots & 0 \\ 0 & 1 & 0 & \dots & 0 \\ \dots & & \ddots & 0 & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right], \quad \boldsymbol {B} _ {\mathrm{c}} = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{array} \right] \tag {7.13a}

\boldsymbol {C} _ {\mathrm{c}} = \left[ \begin{array}{l l l l l} b _ {1} & b _ {2} & \dots & \dots & b _ {\mathrm{n}} \end{array} \right], \quad D _ {\mathrm{c}} = 0 \tag {7.13b}
$$

图 7.7 所示的框图及相应矩阵式(7.12)不是传递函数 $G(s)$ 的唯一表达形式。根据 $G(s)$ 的部分分式展开表达式画出的框图如图 7.8 所示。利用前面介绍的同样方法，图中标出了状态变量，我们可以直接根据框图确定矩阵为

$$\dot {z} = A _ {\mathrm{m}} z + B _ {\mathrm{m}} uy = C _ {\mathrm{m}} z + D _ {\mathrm{m}} u$$

其中：

$$
\mathbf {A} _ {\mathrm{m}} = \left[ \begin{array}{c c} - 4 & 0 \\ 0 & - 3 \end{array} \right], \quad \mathbf {B} _ {\mathrm{m}} = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \tag {7.14a}
\mathbf {C} _ {\mathrm{m}} = \left[ 2 - 1 \right], \quad D _ {\mathrm{m}} = 0 \tag {7.14b}
$$

下标 m 表示模态标准形。该名字来源于传递函数的极点常被称为系统的标准模态。这种形式的矩阵有一个重要的特点，就是系统的极点（此处为 -4 和 -3）是 $A_{m}$ 矩阵的对角线上的元素，而其余各项，即部分分式展开式的分子项（此处为 2 和 -1）出现在 $C_{m}$ 矩阵中。
