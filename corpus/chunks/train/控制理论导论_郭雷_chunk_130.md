$$
\boldsymbol {E} = \left[ \begin{array}{c} c _ {1} \boldsymbol {A} ^ {d _ {1}} \boldsymbol {B} \\ c _ {2} \boldsymbol {A} ^ {d _ {2}} \boldsymbol {B} \\ \vdots \\ c _ {m} \boldsymbol {A} ^ {d _ {m}} \boldsymbol {B} \end{array} \right]
$$

非奇异，其中 $c_{i}$ 表示 $\pmb{C}$ 的第 $i$ 行，而 $d_{i}$ 定义为

$$
d _ {i} = \left\{ \begin{array}{l l} n, & \text {如果} c _ {i} B = c _ {i} A B = \dots = c _ {i} A ^ {n - 1} B = 0; \\ & \min \{k: c _ {i} A ^ {k} B \neq 0, k = 0, 1, \dots , n - 1 \}, \quad \text {否则}. \end{array} \right.
$$

证明 必要性. 将 $G(s)$ 的第 $i$ 行以 $s$ 的负幂次展开,

$$
\begin{array}{l} c _ {i} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} = \frac {1}{s} c _ {i} \left[ \boldsymbol {I} - \frac {\boldsymbol {A}}{s} \right] ^ {- 1} \boldsymbol {B} \\ = \frac {1}{s} c _ {i} \left[ I + \frac {\boldsymbol {A}}{s} + \frac {\boldsymbol {A} ^ {2}}{s ^ {2}} + \dots \right] \boldsymbol {B} \\ = s ^ {- d _ {i} - 1} c _ {i} \left[ A ^ {d _ {i}} + \frac {A ^ {d _ {i} + 1}}{s} + \dots \right] B \\ = s ^ {- d _ {i} - 1} \left(c _ {i} A ^ {d _ {i}} B + c _ {i} A ^ {d _ {i} + 1} \frac {1}{s} \left[ I + \frac {A}{s} + \frac {A ^ {2}}{s ^ {2}} + \dots \right] B\right) \\ = s ^ {- d _ {i} - 1} \left(c _ {i} A ^ {d _ {i}} B + c _ {i} A ^ {d _ {i} + 1} (s I - A) ^ {- 1} B\right). \tag {1.9.4} \\ \end{array}
$$

于是有

$$\boldsymbol {G} (s) = \mathrm{diag} \left(\frac {1}{s ^ {d _ {1} + 1}}, \dots , \frac {1}{s ^ {d _ {m} + 1}}\right) \left[ \boldsymbol {E} + \boldsymbol {F} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} \right], \tag {1.9.5}$$

其中

$$
F = \left[ \begin{array}{c} c _ {1} A ^ {d _ {1} + 1} \\ c _ {2} A ^ {d _ {2} + 1} \\ \vdots \\ c _ {m} A ^ {d _ {m} + 1} \end{array} \right].
$$

由引理1.9.1得

$$
\begin{array}{l} \boldsymbol {G} _ {K L} (s) = \boldsymbol {G} (s) [ \boldsymbol {I} - \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} ]. \boldsymbol {L} \\ = \operatorname{diag} \left(\frac {1}{s ^ {d _ {1} + 1}}, \dots , \frac {1}{s ^ {d _ {m} + 1}}\right) [ \boldsymbol {E} + \boldsymbol {F} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} ] [ \boldsymbol {I} - \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} ] \boldsymbol {L}. \\ \end{array}
$$

因此 $G_{KL}(s)$ 为非奇异对角阵必导致 $\left[E + F(sI - A)^{-1}B\right]\left[I - K(sI - A + BK)^{-1}B\right]L$ 为非奇异对角阵．特别地，
