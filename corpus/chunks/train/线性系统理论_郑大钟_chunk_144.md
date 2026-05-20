$$
\begin{array}{l} \left| y _ {i} (t) \right| = \left| \int_ {t _ {0}} ^ {t} \left[ g _ {i 1} (t, \tau) u _ {1} (\tau) + \dots + g _ {i p} (t, \tau) u _ {p} (\tau) \right] d \tau \right| \\ \leqslant \left| \int_ {t _ {0}} ^ {t _ {1}} g _ {i 1} (t, \tau) u _ {1} (\tau) d \tau \right| + \dots + \left| \int_ {t _ {0}} ^ {t _ {1}} g _ {i p} (t, \tau) u _ {p} (\tau) d \tau \right| \\ i = 1, 2, \dots , q \tag {4.9} \\ \end{array}
$$

并且有限个有界函数之和仍为有界，因而由此并利用单输入-单输出情况的结论，即可证得此结论。从而，证明完成。

结论 2 [定常情况] 对于零初始条件的线性定常系统, 表初始时刻 $t_0 = 0$ , $G(t)$ 为其脉冲响应矩阵, $\hat{G}(s)$ 为其传递函数矩阵, 则系统为 BIBO 稳定的充分必要条件是, 存在一个有限常数 $k$ , $G(t)$ 的每一个元 $g_{ij}(t)$ ( $i = 1, 2, \cdots, q$ ; $j = 1, 2, \cdots, p$ ) 均满足关系式

$$\int_ {0} ^ {\infty} \left| g _ {i j} (t) \right| d t \leqslant k < \infty \tag {4.10}$$

或者等价地，当 $\hat{G}(s)$ 为真的有理分式函数矩阵时， $\hat{G}(s)$ 的每一个元传递函数 $\hat{g}_{ij}(s)$ 的所有极点均具有负实部。

证 此结论的第一部分可由结论1直接导出。对于结论的第二部分，当 $\pmb{g}_{ij}(s)$ 为真的有理分式时，必可利用部分分式法将其展开为有限项之和，其中每一项的形式为

$$\frac {\beta_ {l}}{(s - \lambda_ {l}) ^ {\alpha_ {l}}}, \quad l = 1, 2, \dots , m \tag {4.11}$$

这里 $\lambda_{l}$ 为 $g_{ij}(s)$ 的极点， $\beta_{l}$ 和 $\alpha_{l}$ 可为零或非零常数。考虑到(4.11)所对应的拉普拉斯反变换为：

$$h _ {l r} t ^ {\alpha_ {l} - 1} e ^ {\lambda_ {l} t}, \quad l = 1, 2, \dots , m \tag {4.12}$$

其中若 $\alpha_{l}=0$ 则为 $\delta$ 函数。由此可知，由 $\hat{g}_{ij}(s)$ 取拉普拉斯反变换导出的 $g_{ij}(t)$ 是有限个 $h_{l,r}t^{\alpha_{l}-1}e^{\lambda_{l}t}$ 之和，和式中也可能包含有 $\delta$ 函数项。容易证明，当且仅当 $\lambda_{l}(l=1,2,\cdots,m)$ 均具有负实部时， $t^{\alpha_{l}-1}e^{\lambda_{l}t}$ 为绝对可积，也即 $g_{ij}(t)$ 为绝对可积。从而，系统为 BIBO 稳定。证明完成。

内部稳定性 对于线性定常系统

$$
\begin{array}{l} \dot {x} = A x + B u, \quad x (0) = x _ {0} \\ x _ {1} = C x + D u. \end{array} \tag {4.13}
y = C x + D u
$$

如果外输入 $u(t) \equiv 0$ ，初始状态 $x_{0}$ 为任意，且由 $x_{0}$ 引起的零输入响应 $\phi(t; 0, x_{0}, 0)$ 满足关系式

$$\lim _ {t \rightarrow \infty} \phi (t; 0, x _ {0}, 0) = 0 \tag {4.14}$$

则称系统是内部稳定的，或称为是渐近稳定的。对于（4.13）的线性定常系统，一个熟知的事实是，其为渐近稳定的充分必要条件是矩阵 $A$ 的所有特征值均具有负实部，即

$$\operatorname{Re} \{\lambda_ {i} (A) \} < 0, \quad i = 1, 2, \dots , n \tag {4.15}$$

其中 $n$ 为系统的维数。当矩阵 $A$ 给定后，则一旦导出其特征多项式

$$\alpha (s) \triangleq \det (s I - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {4.16}$$

那么就可利用劳斯-霍尔维茨（Routh-Hurwitz）判据 $^{①}$ 而直接由系数 $\alpha_{i}(i=0,1,\cdots,n-1)$ 来判断系统的渐近稳定性。

就一般情况而言,内部稳定性是指系统状态自由运动的稳定性,也即李亚普诺夫意义下的稳定性。有关李亚普诺夫意义下稳定性的定义和相应的结论,我们将在此后的各节中去进行系统的和详细的讨论。

内部稳定性和外部稳定性间的关系 我们只限于对线性定常系统来讨论其内部稳定性和外部稳定性间的等价关系，并可导出如下的一些推断。
