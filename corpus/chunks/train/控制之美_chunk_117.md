$$
\left\{ \begin{array}{c} \overline {{{z}}} _ {1} (t) = C _ {1} \mathrm{e} ^ {\lambda_ {1} t} \\ \vdots \\ \overline {{{z}}} _ {n} (t) = C _ {n} \mathrm{e} ^ {\lambda_ {n} t} \end{array} \right. \tag {6.3.3}
$$

关于式(6.3.2)和式(6.3.3)的详细推导,请参考3.2.2节。原向量 $z(t)$ 是 $\bar{z}(t)$ 的线性组合,所以它的收敛或发散与 $\bar{z}(t)$ 一致。因此,我们可以将二维状态变量平衡点稳定判定方法沿用到更高维度的情况下,得到关于状态空间方程稳定性的两个结论:

考虑零输入系统的状态空间方程为 $\frac{\mathrm{d}z(t)}{\mathrm{d}t}=A z(t)$ :

\- 如果 $A$ 的特征值的实部都不大于 0, 它的平衡点将符合李雅普诺夫意义下的稳定性。

\- 如果 $A$ 的特征值的实部都小于0，它的平衡点将符合渐近稳定性。

上述结论为系统的控制器设计提供了思路。在闭环控制系统中，输入 $u(t)$ 是状态变量的一个函数，例如 $\pmb{u}(t) = -\pmb{K}\pmb{z}(t)$ ，其中矩阵 $\pmb{K}$ 是控制矩阵。式(6.3.1a)可以写成

$$\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) - \boldsymbol {B} \boldsymbol {K} \boldsymbol {z} (t) = (\boldsymbol {A} - \boldsymbol {B} \boldsymbol {K}) \boldsymbol {z} (t) = \boldsymbol {A} _ {\mathrm{cl}} \boldsymbol {z} (t) \tag {6.3.4}$$

其中, $A_{cl}=A-BK$ ,代表闭环控制系统的状态矩阵。根据上述分析,如果希望得到一个渐近稳定的系统,则需要设计合适的控制矩阵K,使得 $A_{cl}$ 的特征值实部都为负数。
