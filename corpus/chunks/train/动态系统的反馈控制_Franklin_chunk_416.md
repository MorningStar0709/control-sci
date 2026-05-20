# 例 7.9 热系统从能控标准形变换成模态标准形

求变换矩阵使得式(7.12)的能控形矩阵变换成式(7.14)的模态形。

解答。根据式(7.34)和式(7.35)，我们首先需要找到矩阵 $A_{c}$ 的特征矢量和特征值。取特征矢量分别为

$$
\left[ \begin{array}{c} t _ {1 1} \\ t _ {2 1} \end{array} \right], \quad \left[ \begin{array}{c} t _ {1 2} \\ t _ {2 2} \end{array} \right]
$$

用左边的特征矢量得到如下方程：

$$
\left[ \begin{array}{c c} - 7 & - 1 2 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l} t _ {1 1} \\ t _ {2 1} \end{array} \right] = p \left[ \begin{array}{l} t _ {1 1} \\ t _ {2 1} \end{array} \right] \tag {7.36a}
- 7 t _ {1 1} - 1 2 t _ {2 1} = p t _ {1 1} \tag {7.36b}t _ {1 1} = p t _ {2 1} \tag {7.36c}
$$

将式 $(7.36c)$ 代入到式 $(7.36b)$ 得到

$$- 7 p t _ {2 1} - 1 2 t _ {2 1} = p ^ {2} t _ {2 1} \tag {7.37a}p ^ {2} t _ {2 1} + 7 p t _ {2 1} + 1 2 t _ {2 1} = 0 \tag {7.37b}p ^ {2} + 7 p + 1 2 = 0 \tag {7.37c}p = - 3, - 4 \tag {7.37d}$$

我们再次发现系统的特征值(极点)是-3和-4；此外，式(7.36c)给出两个特征矢量为

$$
\left[ \begin{array}{c} - 4 t _ {2 1} \\ t _ {2 1} \end{array} \right], \quad \left[ \begin{array}{c} - 3 t _ {2 2} \\ t _ {2 2} \end{array} \right]
$$

其中： $t_{21}$ 和 $t_{22}$ 是任意非零比例因子。现在要选择两个比例因子使得式(7.14a)中 $B_{m}$ 的两个元素都是 1。利用 $B_{c}$ 表示 $B_{m}$ 的方程为 $TB_{m}=B_{c}$ ，且该方程的解为 $t_{21}=-1$ 和 $t_{22}=1$ 。因此，变换阵及其逆矩阵分别为

$$
\boldsymbol {T} = \left[ \begin{array}{c c} 4 & - 3 \\ - 1 & 1 \end{array} \right], \quad \boldsymbol {T} ^ {- 1} = \left[ \begin{array}{c c} 1 & 3 \\ 1 & 4 \end{array} \right] \tag {7.38}
$$

根据初等矩阵乘法规则，使用由式(7.38)定义的 T，则式(7.12)和式(7.14)中的矩阵具有如下关系：

$$\boldsymbol {A} _ {\mathrm{m}} = \boldsymbol {T} ^ {- 1} \boldsymbol {A} _ {\mathrm{c}} \boldsymbol {T} \quad \boldsymbol {B} _ {\mathrm{m}} = \boldsymbol {T} ^ {- 1} \boldsymbol {B} _ {\mathrm{c}}\pmb {C} _ {\mathrm{m}} = \pmb {C} _ {\mathrm{c}} \pmb {T} \qquad D _ {\mathrm{m}} = D _ {\mathrm{c}} \tag {7.39}$$

454

这些计算可以利用下面 Matlab 语句来实现：

$$
\begin{array}{l} T = [ 4 - 3; - 1 1 ]; \\ A m = \operatorname{inv} (T) ^ {*} A c ^ {*} T; \\ B m = \operatorname{inv} (T) ^ {*} B c; \\ C m = C c ^ {*} T; \\ D m = D c; \\ \end{array}
$$

下面这个例子有 5 个状态变量，对于手工计算来说，采用状态变量形式过于复杂。然而，对于说明计算机软件的优势而言，这是一个非常好的例子。我们使用的模型是基于幅值和时间比例都规定好的物理状态
