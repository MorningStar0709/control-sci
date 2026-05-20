$$\Sigma : \quad \dot {\bar {x}} = \overline {{A}} \bar {x} + \overline {{B}} u \tag {1.113}\mathbf {y} = \bar {C} \bar {\mathbf {x}} + \bar {D} \mathbf {u}$$

则两种表达式(1.112)和(1.113)之间成立如下的关系式:

$$\overline {{A}} = P A P ^ {- 1}, \overline {{B}} = P B, \overline {{C}} = C P ^ {- 1}, \overline {{D}} = D \tag {1.114}$$

证 利用 $\pmb{x} = P\pmb{x}$ ，即可导出

$$
\begin{array}{l} \dot {\bar {x}} = P \dot {x} = P (A x + B a) \\ = P A P ^ {- 1} \bar {x} + P B u = \bar {A} \bar {x} + \bar {B} u \tag {1.115} \\ \end{array}
\mathbf {y} = C \mathbf {x} + D \mathbf {u} = C P ^ {- 1} \bar {\mathbf {x}} + D \mathbf {u} = \bar {C} \bar {\mathbf {x}} + \bar {D} \mathbf {u} \tag {1.116}
$$

于是，证明完成。

结论2 考虑由(1.112)和(1.113)所给出的状态空间描述 $\Sigma$ 和 $\Sigma$ ，则两者具有相同的特征值，也即成立

$$\lambda_ {i} (A) = \lambda_ {i} (\overline {{{A}}}), \quad i = 1, 2, \dots , n \tag {1.117}$$

证 利用 $\widetilde{A} = PAP^{-1}$ ，就可导出

$$
\begin{array}{l} \overline {{A}} = P A P ^ {- 1}, \text {就可导出} \\ 0 = \det (\lambda_ {i} I - \overline {{A}}) = \det (\lambda_ {i} I - P A P ^ {- 1}) = \det P (\lambda_ {i} I - A) P ^ {- 1} \end{array}
= \det (\lambda_ {i} I - A) \det P \det P ^ {- 1} = \det (\lambda_ {i} I - A) \tag {1.118}
$$

表明 $\lambda_{i}$ 同时为 $\overline{A}$ 和 A 的特征值，即 (1.117) 成立。于是，证明完成。

结论 3 考虑线性时变系统

$$\Sigma : \quad \dot {x} = A (t) x + B (t) u \tag {1.119}\mathbf {y} = C (t) \mathbf {x} + D (t) \mathbf {u}$$

引入变换 $\bar{x} = P(t)x, P(t)$ 可逆且连续可微，再令变换后的状态空间描述为：

$$
\begin{array}{l} \begin{array}{l} \Sigma ; \quad \dot {\bar {x}} = \bar {A} (t) \bar {x} + \bar {B} (t) u \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array} \tag {1.120} \\ y = \bar {C} (t) \bar {x} + \bar {D} (t) u \\ \end{array}
$$

则两种表达式(1.119)和(1.120)之间成立如下的关系式:

$$
\begin{array}{l} \bar {A} (t) = \dot {P} (t) P ^ {- 1} (t) + P (t) A (t) P ^ {- 1} (t) \\ \overline {{B}} (t) = P (t) B (t), \overline {{C}} (t) = C (t) P ^ {- 1} (t), \overline {{D}} (t) = D (t) \tag {1.121} \\ \end{array}
$$

其中 $\dot{P}(t)\triangleq dP(t)/dt$ 。

证 利用 $\pmb{x} = P(t)\pmb{x}$ 和 $x = P^{-1}(t)\pmb{x}$ ，即可导出

$$
\begin{array}{l} \dot {\bar {x}} = \dot {P} (t) x + P (t) \dot {x} = \dot {P} (t) P ^ {- 1} (t) \bar {x} + P (t) [ A (t) x + B (t) u ] \\ = [ \hat {P} (t) P ^ {- 1} (t) + P (t) A (t) P ^ {- 1} (t) ] \bar {x} + P (t) B (t) u \\ - \bar {A} (t) \bar {x} + \bar {B} (t) u (1.122) \\ y = C (t) P ^ {- 1} (t) \bar {x} + D (t) u = \bar {C} (t) \bar {x} + \bar {D} (t) u (1.123) \\ \end{array}
$$

于是，证明完成。

下面，对上述导出的几点结论进行如下的几点讨论：

(1) 如果两个状态空间描述之间存在 (1.114) 或 (1.121) 的关系, 则称它们是代数等

价的，也即它们具有相同的一些代数特性。

（2）同一系统采用不同的状态变量组所导出的两个状态空间描述之间，必然是代数等价的。  
（3）对于线性定常的情况，可以做到使两个代数等价的状态空间描述化为相同的对角线规范形或约当规范形。  
（4）由于坐标系的选择带有人为的性质，而系统的特性具有客观性，因此系统在坐标变换下的不变量和不变属性反映了其固有的特性。例如，特征值在坐标变换下保持不变，反映了系统的稳定性这一固有特性。
