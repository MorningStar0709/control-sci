10.10 给定 $G(s) = R(s)P^{-1}(s)Q(s) + W(s)$ 为 $q \times q$ 有理分式矩阵, 其中

$$\det W (s) \not \equiv 0 _ {\circ}$$

再设 $G(s)$ 为可逆，且表 $G^{-1}(s) = \widetilde{R}(s)\widetilde{P}^{-1}(s)\widetilde{Q}(s) + \widetilde{W}(s)$ ，其中

$$\widetilde {W} = W ^ {- 1}, \widetilde {Q} = Q W ^ {- 1}, \widetilde {R} = - W ^ {- 1} R, \widetilde {P} = P + Q W ^ {- 1} R _ {\circ}$$

试证明： $\{\widetilde{P}(s),\widetilde{Q}(s),\widetilde{R}(s),\widetilde{W}(s)\}$ 为不可简约的，当且仅当 $\{P(s),Q(s),R(s),W(s)\}$ 为不可简约。

10.11 确定下列 PMD 的极点和传输零点:

$$
\left[ \begin{array}{c c} s ^ {2} + 2 s + 1 & 2 \\ 0 & s + 1 \end{array} \right] \hat {\zeta} (s) = \left[ \begin{array}{c c} s + 2 & s \\ 1 & s + 3 \end{array} \right] \hat {u} (s)

\hat {\mathbf {y}} (s) = \left[ \begin{array}{c c} s + 1 & 1 \\ 2 & s \end{array} \right] \hat {\boldsymbol {\zeta}} (s)
$$

10.12 确定下列 PMD 的输入解耦零点和输出解耦零点:

$$
\left[ \begin{array}{c c} s ^ {2} + 2 s + 1 & 3 \\ 0 & s + 1 \end{array} \right] \hat {\zeta} (s) = \left[ \begin{array}{c c} s + 2 & s \\ 0 & s + 1 \end{array} \right] \hat {\boldsymbol {u}} (s)

\hat {\mathbf {y}} (s) = \left[ \begin{array}{c c} s + 1 & 2 \\ 0 & s \end{array} \right] \hat {\zeta} (s)
$$

10.13 试判断下列两个系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 是否为严格系统等价：

$$
S _ {1} (s) = \left[ \begin{array}{c c c} s + 1 & s ^ {3} & 0 \\ 0 & s + 1 & 1 \\ - 1 & 0 & 0 \end{array} \right], \quad S _ {2} (s) = \left[ \begin{array}{c c c} s + 1 & - 1 & - 3 \\ 0 & s + 1 & 1 \\ - 1 & 0 & 2 - s \end{array} \right]
$$

(提示：可通过行和列的初等运算来判断。)

10.14 对于受控系统

$$P (s) \hat {r} _ {2} (s) = Q (s) \hat {u} (s)\hat {\mathcal {Y}} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {\boldsymbol {u}} (s)$$

取 $\hat{\boldsymbol{u}}(s)$ 为反馈控制律 $\hat{\boldsymbol{u}}(s)=\hat{\boldsymbol{v}}(s)-F(s)\hat{\boldsymbol{y}}(s)$ ，由此组成闭环系统，而 $\hat{\boldsymbol{v}}(s)$ 为参考输入。试证明：闭环系统的系统矩阵为

$$
\left[ \begin{array}{c c c c} P (s) & Q (s) & 0 & 0 \\ - R (s) & W (s) & I & 0 \\ 0 & - I & F (s) & I \\ \hline 0 & 0 & - I & 0 \end{array} \right]
$$

10.15 对于上题中的闭环系统，试证明：当 $\{P(s), Q(s), R(s), W(s)\}$ 为不可简约时，闭环系统矩阵必是不可简约的。
