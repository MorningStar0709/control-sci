$$\dot {x} _ {c} = x _ {c}, \quad y _ {2} = - x _ {c}$$

2）系统按可观测性的结构分解。系统按可观测性结构分解的所有结论，都对偶于系统按可控性结构分解的结果。设不可观测系统的动态方程为

$$\dot {\pmb {x}} = \pmb {A} \pmb {x} + \pmb {B} \pmb {u}, \quad \pmb {y} = \pmb {C} \pmb {x} \tag {9-201}$$

式中，x 为 n 维状态向量；u 为 p 维输入向量；y 为 q 维输出向量。系统的可观测性矩阵为

$$
\boldsymbol {V} = \left[ \begin{array}{c} \boldsymbol {C} \\ \boldsymbol {C A} \\ \vdots \\ \boldsymbol {C A} ^ {n - 1} \end{array} \right]
$$

$\operatorname{rank} V = l (l < n)$ , 在 $V$ 中任意选取 $l$ 个线性无关的行向量 $t_1, t_2, \cdots, t_l$ , 此外再选取 $n - l$ 个与之线性无关的行向量 $t_{l+1}, \cdots, t_n$ , 构成非奇异线性变换阵

$$
\boldsymbol {T} = \left[ \begin{array}{c} t _ {1} \\ \vdots \\ t _ {l} \\ \dots \\ t _ {l + 1} \\ \vdots \\ t _ {n} \end{array} \right] \tag {9-202}
$$

对式(9-201)不可观测系统进行非奇异线性变换

$$
\boldsymbol {x} = \boldsymbol {T} ^ {- 1} \left[ \begin{array}{l} \boldsymbol {x} _ {o} \\ \boldsymbol {x} _ {\delta} \end{array} \right] \tag {9-203}
$$

可得系统结构按可观测性分解的规范表达式

$$
\left[ \begin{array}{l} \dot {\boldsymbol {x}} _ {o} \\ \dot {\boldsymbol {x}} _ {o} \end{array} \right] = \mathbf {T A T} ^ {- 1} \left[ \begin{array}{l} \boldsymbol {x} _ {o} \\ \boldsymbol {x} _ {\bar {o}} \end{array} \right] + \mathbf {T B u}, \quad \boldsymbol {y} = \mathbf {C T} ^ {- 1} \left[ \begin{array}{l} \boldsymbol {x} _ {o} \\ \boldsymbol {x} _ {\bar {o}} \end{array} \right] \tag {9-204}
$$

式中， $x_{o}$ 为 l 维可观测状态子向量； $x_{\bar{o}}$ 为 n-l 维不可观测状态子向量，并且

$$
\mathbf {T A T} ^ {- 1} = \left[ \begin{array}{c c} {\hat {\mathbf {A}} _ {1 1}} & {\mathbf {0}} \\ {\dots} & {\dots} \\ {\hat {\mathbf {A}} _ {2 1}} & {\hat {\mathbf {A}} _ {2 2}} \end{array} \right] _ {n - l \text {行}}, \qquad \mathbf {T B} = \left[ \begin{array}{c} {\hat {\mathbf {B}} _ {1}} \\ {\dots} \\ {\hat {\mathbf {B}} _ {2}} \end{array} \right] _ {n - l \text {行}} ^ {l \text {行}},

\pmb {C T} ^ {- 1} = [ \begin{array}{c c c} {\hat {C} _ {1}} & {\vdots} & {\mathbf {0}} \\ {l \text {列}} & {n - l \text {列}} \end{array} ] _ {q \text {行}} \tag {9-205}
$$

展开式(9-204)，有

$$\dot {\boldsymbol {x}} _ {o} = \hat {\boldsymbol {A}} _ {1 1} \boldsymbol {x} _ {o} + \hat {\boldsymbol {B}} _ {1} \boldsymbol {u}\dot {\boldsymbol {x}} _ {\bar {o}} = \hat {\boldsymbol {A}} _ {2 1} \boldsymbol {x} _ {o} + \hat {\boldsymbol {A}} _ {2 2} \boldsymbol {x} _ {\bar {o}} + \hat {\boldsymbol {B}} _ {2} \boldsymbol {u}\mathbf {y} = \hat {\boldsymbol {C}} _ {1} \mathbf {x} _ {o}$$

可观测子系统动态方程为
