其中，由于信号的函数结构为已知，故多项式 $d_{y}(s)$ 和 $d_{w}(s)$ 是已知的，又由于信号的非结构性特性为未知，所以多项式 $n_{y}(s)$ 和 $n_{w}(s)$ 为未知和任意。此外，对 $n_{y}(s)$ 和 $n_{w}(s)$ 的唯一的限制是应保证 $\hat{y}_0(s)$ 和 $\hat{w}(s)$ 均为严格真的有理分式函数。进而，就时间域内而言，上述复频率域关系式（5.144）和（5.145）等价于把 $y_0(t)$ 和 $w(t)$ 分别看成为是由信号模型

$$
\begin{array}{l} \dot {\boldsymbol {x}} _ {r} = A _ {r} \boldsymbol {x} _ {r} \\ \text { (5.146) } \end{array}
$$

和

$$
\begin{array}{l} \dot {\boldsymbol {x}} _ {w} = A _ {w} \boldsymbol {x} _ {w} \\ w (t) = \boldsymbol {c} _ {w} \boldsymbol {x} _ {w} \end{array} \tag {5.147}
$$

相对于各自的未知初始条件 $x_{r}(0)$ 和 $x_{w}(0)$ 所产生的。并且， $A_{r}$ 和 $A_{w}$ 的最小多项式即

分别为 $d_{\gamma}(s)$ 和 $d_{\omega}(s)$ 。

推广到向量信号的情况,那么可把参考信号 $y_{0}(t)$ 看成为是在未知的初始状态下由其模型

$$\dot {x} _ {r} = A _ {r} x _ {r} \tag {5.148}\mathbf {y} _ {0} (t) = C _ {r} \mathbf {x} _ {r}$$

所产生的。而扰动 $w(t)$ 则看成为是在未知的初始状态下由它的模型

$$\dot {x} _ {w} = A _ {w} x _ {w} \tag {5.149}\boldsymbol {w} (t) = C _ {w} \boldsymbol {x} _ {w}$$

所产生的。再令 $\phi_r(s)$ 和 $\phi_w(s)$ 分别是 $A_r$ 和 $A_w$ 的最小多项式，那么注意到跟踪问题中只需考虑 $y_0(t)$ 和 $w(t)$ 的当 $t \to \infty$ 时不趋于零的部分，所以只需考虑 $\phi_r(s)$ 和 $\phi_w(s)$ 中根均位于右半闭 $s$ 平面的部分。现表多项式 $\phi_r(s)$ 和 $\phi_w(s)$ 的位于右半闭 $s$ 平面上的根因式的最小公倍式为 $\phi(s)$ :

$$\phi (s) = s ^ {m} + \alpha_ {m - 1} s ^ {m - 1} + \dots + \alpha_ {q} s + \alpha_ {0} \tag {5.150}$$

显然 $\phi(s) = 0$ 的所有根均具有非负实部。于是，由 $\phi^{-1}(s)I_q$ 可导出 $w(t)$ 和 $y_0(t)$ 的当 $t \to \infty$ 时不趋于零的部分的共同模型，且将其和受控系统相串联，即把跟踪误差 $e$ 作为它的输入，有：

$$
\begin{array}{l} \dot {x} _ {c} = A _ {c} x _ {c} + B _ {c} e \\ y = x \end{array} \tag {5.151}
$$

其中

$$\underset {q _ {m} \times q _ {m}} {A _ {c}} = \text { block diag } \{\underbrace {\Gamma , \Gamma , \cdots , \Gamma} _ {q \text { 重 }} \} \tag {5.152}\underset {q _ {m} \times q} {B _ {c}} = \text { block diag } \{\underbrace {\beta , \beta , \cdots , \beta} _ {q \text { 重 }} \} \tag {5.153}$$

而

$$
\Gamma = \left[ \begin{array}{c c} 0 & \\ \vdots & I _ {m - 1} \\ 0 & \\ - \alpha_ {0} & - \alpha_ {1} \dots - \alpha_ {m - 1} \end{array} \right], \quad \beta = \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \tag {5.154}
$$

由式(5.151)所描述的动态系统就是在研究跟踪问题中对 $y_{0}(t)$ 和 $w(t)$ 所建立的信号模型。

无静差跟踪控制系统的综合 现考虑由受控系统(5.137)和信号模型(5.151)顺序串联组成的系统,容易导出此串联系统的状态方程为:
