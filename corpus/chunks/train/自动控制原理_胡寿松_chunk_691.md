证明 下面以多输入 - 单输出系统为例给出定理的证明。根据对偶定理可知，若被控系统 $(\mathbf{A}, \mathbf{B}, \mathbf{c})$ 可观测，则对偶系统 $(\mathbf{A}^{\mathrm{T}}, \mathbf{c}^{\mathrm{T}}, \mathbf{B}^{\mathrm{T}})$ 可控，由状态反馈极点配置定理知 $(\mathbf{A}^{\mathrm{T}} - \mathbf{c}^{\mathrm{T}}\mathbf{h}^{\mathrm{T}})$ 的特征值可任意配置，其中 $\pmb{h}$ 为 $n \times 1$ 输出反馈向量。由于 $(\mathbf{A}^{\mathrm{T}} - \mathbf{c}^{\mathrm{T}}\mathbf{h}^{\mathrm{T}})$ 的特征值与 $(\mathbf{A}^{\mathrm{T}} - \mathbf{c}^{\mathrm{T}}\mathbf{h}^{\mathrm{T}})^{\mathrm{T}} = \mathbf{A} - \pmb{h}\mathbf{c}$ 的特征值相同，故当且仅当系统 $(\mathbf{A}, \mathbf{B}, \mathbf{c})$ 可观测时，可以任意配置 $(\mathbf{A} - \pmb{h}\mathbf{c})$ 的特征值。证毕。

为了根据期望闭环极点来设计输出反馈矩阵 $\pmb{h}$ 的参数，只需将期望的系统特征多项式与该输出反馈系统特征多项式 $|\lambda I - (A - hc)|$ 相比即可。

对于多输入-单输出被控系统来说，当采用输出至参考输入的反馈时，反馈增益矩阵 $\pmb{F}$ 为 $p\times 1$ 向量，记为 $f$ ，则

$$\boldsymbol {u} = \boldsymbol {v} - f y$$

输出反馈系统的动态方程为

$$\dot {x} = (A - B f c) x + B v, \quad y = c x$$

若令 $fc = K$ ，该输出反馈便等价为状态反馈。适当选择 $f$ ，可使特征值任意配置。但是，当比例的状态反馈变换为输出反馈时，输出反馈中必定含有输出量的各阶导数，于是 $f$ 不是常数向量，这会给物理实现带来困难，因而其应用受限。可推论，当 $f$ 是常数向量时，便不能任意配置极点。

(2) 单输入-单输出系统的极点配置算法

对于具体的可控单输入-单输出系统,求解实现希望极点配置的状态反馈向量 k 时,不必像定理 9-5 中证明那样去进行可控标准型变换,只需要运行如下简单算法。

步骤 1: 列写系统状态方程及状态反馈控制律

$$\dot {x} = A x + b u, u = v - k x$$

其中 $k = \left[k_{0} \quad k_{1} \quad \cdots \quad k_{n-1}\right]$ 。

步骤 2: 检验 $(A,b)$ 的可控性。若 rank $[b\quad Ab\quad\cdots\quad A^{n-1}b]=n$ ，则转下步。

步骤3：由要求配置的闭环极点， $\lambda_1,\lambda_2,\dots ,\lambda_n$ ，求出希望特征多项式。 $a_0^* (s) = \prod_{i = 1}^{n}(s - \lambda_i)$

步骤4：计算状态反馈系统的特征多项式。 $a_0(s) = \mathrm{det}[sI - A + bk]$

步骤5：比较多项式 $a_0^* (s)$ 与 $a_0(s)$ ，令其对应项系数相等，可确定状态反馈增益向量 $\pmb{k}$ 。

应当指出，应用极点配置方法来改善系统性能，有以下需要注意的方面：

1) 配置极点时并非离虚轴越远越好，以免造成系统带宽过大使抗扰性降低。  
2)状态反馈向量 $\pmb{k}$ 中的元素不宜过大，否则物理实现不易。  
3)闭环零点对系统动态性能影响甚大，在规定希望配置的闭环极点时，需要充分考虑闭环零

点的影响。

4) 状态反馈对系统的零点和可观测性没有影响, 只有当任意配置的极点与系统零点存在对消时, 状态反馈系统的零点和可观测性将会改变。

以上性质适用于单输入-多输出或单输出系统，但不适用于多输入-多输出系统。

例9-21 已知单输入线性定常系统的状态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 1 & - 6 & 0 \\ 0 & 1 & - 1 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] \boldsymbol {u}
$$

求状态反馈向量 k，使系统的闭环特征值为

$$\lambda_ {1} = - 2, \quad \lambda_ {2} = - 1 + j, \quad \lambda_ {3} = - 1 - j$$

解 系统的可控性判别矩阵为
