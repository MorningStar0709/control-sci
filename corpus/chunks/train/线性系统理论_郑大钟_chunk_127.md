$$
\overline {{A}} _ {c} = T ^ {- 1} A T = \left[ \begin{array}{l l l l} \overline {{A}} _ {1 1} & \overline {{A}} _ {1 2} & \dots & \overline {{A}} _ {1 l} \\ & \overline {{A}} _ {2 2} & & \vdots \\ & & \ddots & \overline {{A}} _ {l l} \end{array} \right] \tag {3.193}

\overline { { A } } _ { i i } \left( v _ { i \times v _ { i } } \right) = \left[ \begin{array} { c c c c c } 0 & 1 & \cdots & & \\ \vdots & & \ddots & \ddots & \\ 0 & & & & 1 \\ \hdashline \alpha _ { i 1 } & \alpha _ { i 2 } & \cdots & \alpha _ { i v _ { i } } \end{array} \right] , i = 1 , 2 , \cdots , l \tag {3.194}

\overline {{{A}}} _ {i j} = \left[ \begin{array}{c c c c} \gamma_ {j 1 i} & 0 & \dots & 0 \\ \vdots & \vdots & & \vdots \\ \gamma_ {j v _ {i} i} & 0 & \dots & 0 \end{array} \right], j = i + 1, \dots , l \tag {3.195}

\bar {B} _ {\varepsilon_ {(n \times p)}} = T ^ {- 1} B = \underbrace {\left[ \begin{array}{c c c c c c c c c} 0 & & & & * & \cdots & * \\ \vdots & & & & & & & \\ 0 & & & & & & & \\ 1 & & & & \vdots & & \vdots \\ - & \ddots & & & \vdots & & \vdots \\ & & 0 & & \vdots & & \vdots \\ & & \vdots & & \vdots & & \vdots \\ & & 0 & & \vdots & & \vdots \\ & & 1 & & * & \cdots & * \\ l \end{array} \right]} _ {p - l} \Bigg \} v _ {l} \tag {3.196}
\overline {{C}} _ {e} = C T (\text {无特殊形式}) \tag {3.197}
$$

且式(3.196)中用“\*”表示的元为可能的非零元。

证 利用(3.191)和(3.183)—(3.190)，并考虑到 $T\bar{A}_{c}=AT$ 和 $T\bar{B}_{c}=B$ ，即可证得(3.193)—(3.196)。具体推证过程和单输入-单输出情形相类似，故略去。证明完成。

再来讨论旺纳姆能观测规范形。利用能控性和能观测性间的对偶关系，即可导出如下的结论。

结论 2 考虑完全能观测的多输入-多输出线性定常系统（3.178），则其旺纳姆能观测规范形在形式上对偶于旺纳姆能控规范形，即有：

$$\Sigma_ {o W}: \quad \dot {\bar {x}} ^ {o} = \bar {A} _ {o} \bar {x} ^ {o} + \bar {B} _ {o} u \tag {3.198}\mathbf {y} = \bar {C} _ {o} \bar {\mathbf {x}} ^ {o}$$

其中

$$
\bar {A} _ {o} = \left[ \begin{array}{c c c c} A _ {1 1} & & & \\ A _ {2 1} & A _ {2 2} & & \\ \vdots & & \ddots & \\ A _ {m 1} & \dots \dots & A _ {m m} \end{array} \right] \tag {3.199}

\begin{array}{l} A _ {i i} = \left[ \begin{array}{c c c c c} 0 & \dots & 0 & \beta_ {i 1} \\ \hline 1 & & & & \beta_ {i 2} \\ & \ddots & & & \vdots \\ & & \ddots & & \beta_ {i \zeta_ {i}} \\ & & & 1 & \end{array} \right], i = 1, 2, \dots , m (3.200) \\ A _ {i j} = \left[ \begin{array}{c c c} \rho_ {i 1 j} & \dots & \rho_ {i \zeta_ {i} j} \\ 0 & \dots & 0 \\ \vdots & & \vdots \\ 0 & \dots & 0 \end{array} \right], j = 1, 2, \dots , i - 1 (3.201) \\ \overline {{C}} _ {o} = \left[ \begin{array}{c c c c c c c c c} 0 & \dots & 0 & 1 & & & & \\ \hline & & & & \ddots & & & \\ & & & & & \boxed {0} & \dots & 0 & 1 \\ \hline * & & & \dots \dots & & & & * \\ \vdots & & & & & & & \vdots \\ \vdots & & & & & & & \vdots \\ * & & & \dots \dots & & & * \end{array} \right] (3.202) \\ \end{array}
$$
