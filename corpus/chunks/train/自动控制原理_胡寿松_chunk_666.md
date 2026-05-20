3) 取 $V_{1}^{-1}$ 的第 n 行 $v_{n}^{T}$ ，并按下列规则构造变换矩阵 P:

$$
\boldsymbol {P} = \left[ \begin{array}{c} \boldsymbol {v} _ {n} ^ {\mathrm{T}} \\ \boldsymbol {v} _ {n} ^ {\mathrm{T}} \boldsymbol {A} ^ {\mathrm{T}} \\ \vdots \\ \boldsymbol {v} _ {n} ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}}) ^ {n - 1} \end{array} \right]
$$

4) 求 $\pmb{P}$ 的逆阵 $P^{-1}$ , 并引入 $P^{-1}$ 变换, 即 $z = P^{-1}z$ , 变换后动态方程为

$$\dot {\overline {{{z}}}} = \boldsymbol {P} \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} ^ {- 1} \overline {{{z}}} + \boldsymbol {P} \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {v}, \quad \overline {{{w}}} = \boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {P} ^ {- 1} \overline {{{z}}}$$

5）对对偶系统再利用对偶原理，便可获得原系统的可观测标准型，结果为

$$\dot {\overline {{{x}}}} = \left(\boldsymbol {P} \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} ^ {- 1}\right) ^ {\mathrm{T}} \overline {{{x}}} + \left(\boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {P} ^ {- 1}\right) ^ {\mathrm{T}} u = \boldsymbol {P} ^ {- \mathrm{T}} \boldsymbol {A} \boldsymbol {P} ^ {\mathrm{T}} \overline {{{x}}} + \boldsymbol {P} ^ {- \mathrm{T}} \boldsymbol {b u}\bar {y} = \left(\boldsymbol {P} \boldsymbol {c} ^ {\mathrm{T}}\right) ^ {\mathrm{T}} \bar {\boldsymbol {x}} = \boldsymbol {c} \boldsymbol {P} ^ {\mathrm{T}} \bar {\boldsymbol {x}}$$

与原系统动态方程相比较, 可知将原系统化为可观测标准型需要进行 $P^{T}$ 变换, 即令

$$\boldsymbol {x} = \boldsymbol {P} ^ {\mathrm{T}} \overline {{\boldsymbol {x}}} \tag {9-190}$$

其中

$$
\boldsymbol {P} ^ {\mathrm{T}} = \left[ \begin{array}{l l l l} \boldsymbol {v} _ {n} & \boldsymbol {A} \boldsymbol {v} _ {n} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {v} _ {n} \end{array} \right] \tag {9-191}
$$

$v_{n}$ 为原系统可观测性矩阵的逆阵中第 n 行的转置。
