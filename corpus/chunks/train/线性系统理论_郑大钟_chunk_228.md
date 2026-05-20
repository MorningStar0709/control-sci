$$\boldsymbol {t} _ {2 1} = \bar {\boldsymbol {K}} _ {2}\boldsymbol {t} _ {1 1} \bar {A} _ {1 2} + \boldsymbol {t} _ {2 1} \bar {A} _ {2 2} = \boldsymbol {t} _ {2 1}t _ {1 2} \overline {{{A}}} _ {1 2} + t _ {2 2} \overline {{{A}}} _ {2 2} = t _ {2 3} \tag {5.362}\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet\boldsymbol {t} _ {1 m} \bar {A} _ {1 2} + \boldsymbol {t} _ {2 m} \bar {A} _ {2 2} = - \alpha_ {0} \boldsymbol {t} _ {2 1} - \alpha_ {1} \boldsymbol {t} _ {2 2} - \dots - \alpha_ {m - 1} \boldsymbol {t} _ {2 m}$$

并且上式中除最后一个等式外的其余等式还可改写为:

$$\boldsymbol {t} _ {2 1} = \bar {\boldsymbol {K}} _ {2}\boldsymbol {t} _ {2 2} = \bar {K} _ {1} \bar {A} _ {2 2} + \boldsymbol {t} _ {1 1} \bar {A} _ {1 2}\boldsymbol {t} _ {2 3} = \overline {{K}} _ {2} \overline {{A}} _ {2 2} ^ {2} + \boldsymbol {t} _ {1 1} \overline {{A}} _ {1 2} \overline {{A}} _ {2 2} + \boldsymbol {t} _ {1 2} \overline {{A}} _ {1 2} \tag {5.363}\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullett _ {2 m} = \bar {K} _ {2} \bar {A} _ {2 2} ^ {m - 1} + t _ {1 1} \bar {A} _ {1 2} \bar {A} _ {2 2} ^ {m - 2} + \dots + t _ {1, m - 2} \bar {A} _ {1 2} \bar {A} _ {2 2} + t _ {1, m - 1} \bar {A} _ {1 2}$$

现将（5.363）代入（5.362）的最后一个等式，则经过整理后可得

$$
\tilde {K} \triangleq \bar {K} _ {2} \bar {A} _ {2 2} ^ {m} + \alpha_ {m - 1} \bar {K} _ {2} \bar {A} _ {2 2} ^ {m - 1} + \dots + \alpha_ {1} \bar {K} _ {2} \bar {A} _ {2 2} + \alpha_ {0} \bar {K} _ {2}
= - \left[ t _ {1 m}, t _ {1, m - 1}, \dots , t _ {1 1} \right] \left[ \begin{array}{c c c c c} I & & & & \\ \alpha_ {m - 1} I & I & & & \\ \vdots & \alpha_ {m - 1} I & \ddots & & \\ \vdots & & \ddots & & \\ \alpha_ {1} I & \alpha_ {2} I & \dots \dots \alpha_ {m - 1} I & I \end{array} \right] \left[ \begin{array}{c} \bar {A} _ {1 2} \\ \bar {A} _ {1 2} \bar {A} _ {2 2} \\ \bar {A} _ {1 2} \bar {A} _ {2 2} ^ {3} \\ \vdots \\ - \bar {A} _ {1 2} \bar {A} _ {2 2} ^ {m - 1} \end{array} \right] \tag {5.364}
$$

上式中 $\tilde{K}$ 为 $1 \times (n - q)$ 维向量，一旦 K 给定且按函数观测器的极点配置要求选定 $\{\alpha_{i}, i = 0, 1, \cdots, m - 1\}$ 后， $\tilde{K}$ 便是已知的。此外，对任意 $\alpha_{i}$ ，式 (5.364) 的右边第二个 $mq \times mq$ 矩阵必为非奇异。从而可知，当且仅当下述 $mq \times (n - q)$ 矩阵的秩

$$
\operatorname{rank} V \triangleq \operatorname{rank} \left[ \begin{array}{c} \overline {{A}} _ {1 2} \\ \overline {{A}} _ {1 2} \overline {{A}} _ {2 2} \\ \vdots \\ \overline {{A}} _ {1 2} \dot {\overline {{A}}} _ {2 2} ^ {m - 1} \end{array} \right] = n - q \tag {5.365}
$$
