其中，实现的维数 $\dim(A) = \deg \det D(s)$ 。则 $\{D(s), N(s)\}$ 的右互质等价于 $\{A, C\}$ 的能观测。相应地，对于左 MFD $D_L^{-1}(s)N_L(s)$ ，则 $\{D_L(s), N_L(s)\}$ 的左互质，等价于其维数为 $\deg \det D_L(s)$ 的能观测类实现 $(\overline{A}, \overline{B}, \overline{C}, \overline{E}(p))$ 的 $\{\overline{A}, \overline{B}\}$ 的能控。

推论3 考虑系统的状态空间描述 $(A, B, C, E(p))$ ，那么注意到其传递函数矩阵为

$$G (s) = C (s I - A) ^ {- 1} B + E (s) \tag {10.74}$$

就可根据前述结论推断： $\{A, B\}$ 能控等价于 $\{sI - A, B\}$ 的左互质，而 $\{A, C\}$ 能观测则等价于 $\{sI - A, C\}$ 的右互质。而这正是 PBH 秩判据给出的结论。

推论4 如果限于考虑单输入-单输出系统，则由于其传递函数 $g(s)$ 可表为

$$g (s) = \boldsymbol {r} (s) P ^ {- 1} (s) \boldsymbol {q} (s) + w (s) = \frac {\boldsymbol {r} (s) H (s) \boldsymbol {q} (s)}{\phi (s)} + w (s) \tag {10.75}$$

其中 $\phi(s)$ 为 $P(s)$ 的最小多项式，所以这时 $\{P(s), q(s)\}$ 的左互质即等同于 $\phi(s)$ 和 $H(s)q(s)$ 不包含相消因子，而 $\{P(s), r(s)\}$ 的右互质则等同于 $\phi(s)$ 和 $r(s)H(s)$ 不包含相消因子。当 $\{P(s), r(s)\}$ 和 $\{P(s), q(s)\}$ 同时为互质时，就等同于 $g(s)$ 的严格真部分中不包含“零点-极点对消”现象。
