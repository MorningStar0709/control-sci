$$
\boldsymbol {F} = \left[ \begin{array}{c} c _ {1} \Delta_ {1} (\boldsymbol {A}) \\ c _ {2} \Delta_ {2} (\boldsymbol {A}) \\ \vdots \\ c _ {m} \Delta_ {m} (\boldsymbol {A}) \end{array} \right].
$$

证明 用 $g_{i}(s)$ 表示 $G(s)$ 的第 $i$ 行，并对所有 $k \geqslant d_{i} + 2$ 令 $\alpha_{ik} = 0$ ，则由式 (1.9.4) 和 $d_{i}$ 的定义得

$$
\begin{array}{l} \Delta_ {i} (s) \mathbf {g} _ {i} (s) = \left[ s ^ {d _ {i} + 1} + \alpha_ {i 1} s ^ {d _ {i}} + \dots + \alpha_ {i (d _ {i} + 1)} \right] s ^ {- d _ {i} - 1} c _ {i} \left[ A ^ {d _ {i}} + \frac {A ^ {d _ {i} + 1}}{s} + \dots \right] B \\ = c _ {i} \boldsymbol {A} ^ {d _ {i}} \boldsymbol {B} + \left[ c _ {i} \boldsymbol {A} ^ {d _ {i} + 1} + \alpha_ {i 1} c _ {i} \boldsymbol {A} ^ {d _ {i}} \right] \boldsymbol {B} s ^ {- 1} \\ + \left[ c _ {i} A ^ {d _ {i} + 2} + \alpha_ {i 1} c _ {i} A ^ {d _ {i} + 1} + \alpha_ {i 2} c _ {i} A ^ {d _ {i}} \right] B s ^ {- 2} + \dots \\ + \left[ c _ {i} A ^ {d _ {i} + k} + \alpha_ {i 1} c _ {i} A ^ {d _ {i} + k - 1} + \dots + \alpha_ {i k} c _ {i} A ^ {d _ {i}} \right] B s ^ {- k} + \dots \\ = c _ {i} \boldsymbol {A} ^ {d _ {i}} \boldsymbol {B} + c _ {i} \left(\boldsymbol {A} ^ {d _ {i} + 1} + \alpha_ {i 1} \boldsymbol {A} ^ {d _ {i}} + \dots + \alpha_ {i (d _ {i} + 1)} \boldsymbol {I}\right) \boldsymbol {B} s ^ {- 1} \\ + c _ {i} \left(\boldsymbol {A} ^ {d _ {i} + 1} + \alpha_ {i 1} \boldsymbol {A} ^ {d _ {i}} + \dots + \alpha_ {i (d _ {i} + 1)} \boldsymbol {I}\right) \boldsymbol {A B s} ^ {- 2} + \dots \\ + c _ {i} \left(\boldsymbol {A} ^ {d _ {i} + 1} + \alpha_ {i 1} \boldsymbol {A} ^ {d _ {i}} + \dots + \alpha_ {i (d _ {i} + 1)} \boldsymbol {I}\right) \boldsymbol {A} ^ {k - 1} \boldsymbol {B} s ^ {- k} + \dots \\ = c _ {i} \boldsymbol {A} ^ {d _ {i}} \boldsymbol {B} + c _ {i} \Delta_ {i} (\boldsymbol {A}) \frac {1}{s} \left(I + \frac {\boldsymbol {A}}{s} + \frac {\boldsymbol {A} ^ {2}}{s ^ {2}} + \dots\right) \boldsymbol {B} \\ = c _ {i} A ^ {d _ {i}} B + c _ {i} \Delta_ {i} (A) (s I - A) ^ {- 1} B. \\ \end{array}
$$

所以有

$$\boldsymbol {G} (s) = \operatorname{diag} \left(\frac {1}{\Delta_ {1} (s)}, \dots , \frac {1}{\Delta_ {m} (s)}\right) [ \boldsymbol {E} + \boldsymbol {F} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} ].$$

进而由式 (1.9.8) 得
