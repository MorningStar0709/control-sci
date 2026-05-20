$$J (\boldsymbol {u} (\cdot)) = \int_ {0} ^ {\infty} [ (\boldsymbol {y} - \tilde {\boldsymbol {y}}) ^ {T} Q (\boldsymbol {y} - \tilde {\boldsymbol {y}}) + \boldsymbol {u} ^ {T} R \boldsymbol {u} ] d t \tag {5.287}$$

为极小。其中，加权阵Q为正半定阵，R为正定阵。

确定跟踪问题的最优解的一个比较方便的途径是,首先将跟踪问题(5.285)—(5.287)化成为等价的一个调节问题,然后直接利用最优调节问题的有关结果并导出跟踪问题中相应的结论。为此,定义如下的增广状态和增广矩阵:

$$
\bar {x} = \left[ \begin{array}{l} x \\ z \end{array} \right], \quad \bar {A} = \left[ \begin{array}{l l} A & 0 \\ 0 & F \end{array} \right], \quad \bar {B} = \left[ \begin{array}{l} B \\ 0 \end{array} \right] \tag {5.288}
$$

和

$$
\bar {Q} = \left[ \begin{array}{c c} C ^ {T} Q C & - C ^ {T} Q H \\ - H ^ {T} Q C & H ^ {T} Q H \end{array} \right], \quad \bar {R} = R \tag {5.289}
$$

那么就可导出等价于上述跟踪问题的调节问题为：

$$\dot {\bar {x}} = \bar {A} \bar {x} + \bar {B} u, \quad \bar {x} (0) = \bar {x} _ {0}, t \geqslant 0J (\boldsymbol {u} (\cdot)) = \int_ {0} ^ {\infty} \left(\bar {\boldsymbol {x}} ^ {T} \bar {Q} \bar {\boldsymbol {x}} + \boldsymbol {u} ^ {T} \bar {R} \boldsymbol {u}\right) d t \tag {5.290}$$

并且由 $\{A, B\}$ 能控可知 $\{\overline{A}, \overline{B}\}$ 为能稳，而由 $\{A, C\}$ 和 $\{F, H\}$ 的能观测以及 $Q \geqslant 0$ 可保证 $\overline{Q}$ 为正半定， $\overline{R} = R$ 按假设显然为正定。于是，利用最优调节问题的基本结论即知，由（5.290）所描述的无限时间定常LQ调节问题的最优控制 $\pmb{u}^{*}(\cdot)$ 为：

$$\boldsymbol {u} ^ {*} (t) = - \bar {K} ^ {*} \bar {\boldsymbol {x}} ^ {*} (t), \quad \bar {K} ^ {*} = \bar {R} ^ {- 1} \bar {B} ^ {T} \bar {P} \tag {5.291}$$

最优轨线 $x^{*}(t)$ 为如下的闭环状态方程的解：

$$\dot {\bar {x}} ^ {*} = (\bar {A} - \bar {B} \bar {R} ^ {- 1} \bar {B} ^ {T} \bar {P}) \bar {x} ^ {*}, \quad \bar {x} ^ {*} (0) = \bar {x} _ {0} \tag {5.292}$$

而最优性能值为:

$$J ^ {*} = \bar {\boldsymbol {x}} _ {0} ^ {T} \bar {P} \bar {\boldsymbol {x}} _ {0}, \quad \forall \bar {\boldsymbol {x}} _ {0} \neq 0 \tag {5.293}$$

其中 $\overline{P}$ 是如下的矩阵黎卡提代数方程

$$\bar {P} \bar {A} + \bar {A} ^ {T} \bar {P} + \bar {Q} - \bar {P} \bar {B} \bar {R} ^ {- 1} \bar {B} ^ {T} \bar {P} = 0 \tag {5.294}$$

的唯一正定对称解阵。下面，从(5.291)—(5.294)出发，来进一步导出跟踪问题的最优解。为此，表 $\vec{P}$ 为分块矩阵：

$$
\bar {P} = \left[ \begin{array}{l l} P & P _ {1 2} \\ p _ {1 2} ^ {\mathrm{T}} & P _ {2 2} \end{array} \right] \tag {5.295}
$$

其中， $P$ 在维数上和 $A$ 一样为 $n \times n$ 阵。并且，利用 (5.294)、(5.288) 和 (5.289)，可以导出相对于 $P, P_{12}$ 和 $P_{22}$ 的黎卡提代数方程为：
