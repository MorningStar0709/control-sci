# 8.3 无穷远处的极点和零点

对传递函数矩阵 $G(s)$ 在无穷远处的极点和零点的研究同样是必要的。 $G(s)$ 在无穷远处的极点反映了系统的非真性，这类情况常可在分析系统的变换和计算中出现。 $G(s)$ 在无穷远处的零点则是在研究多变量系统的根轨迹的渐近行为时所不能不考虑的。但是，正如前几节中所已经指出过的， $G(s)$ 在无穷远处的极点和零点，不能直接采用 $G(s)$ 的史密斯-麦克米伦形 $M(s)$ 来定义和确定。本节中，我们通过某些修正和推广，来给出 $G(s)$ 在无穷远处的极点和零点的定义及结构指数。

无穷远处的极点和零点的定义 给定传递函数矩阵 $G(s)$ ，限于研究其在无穷远处的极点和零点，先引入变换 $s = \lambda^{-1}$ ，则 $G(s)$ 就化为 $G(\lambda^{-1})$ 。进一步，将 $G(\lambda^{-1})$ 表为以 $\lambda$ 为复变量的有理分式矩阵 $H(\lambda)$ ，则不难看出 $G(s)$ 在无穷远处的极点和零点将等同于 $H(\lambda)$ 在 $\lambda = 0$ 处的极点和零点。于是，通过对 $H(\lambda)$ 引入单模变换而导出其史密斯-麦克米伦形 $\widetilde{M}(\lambda)$ ，那么在注意到单模变换不会影响 $H(\lambda)$ 在 $\lambda = 0$ 处的行为的同时，就可对 $G(s)$ 在无穷大处的极点和零点给出如下的定义：

$G(s)$ 在无穷远处的极点 $= \widetilde{M} (\lambda)$ 中 $\tilde{\psi}_i(\lambda) = 0$ 的零根， $i = 1,2,\dots ,r_{\circ}$ (8.38)

$G(s)$ 在无穷远处的零点 $= \widetilde{M} (\lambda)$ 中 $\tilde{\varepsilon}_i(\lambda) = 0$ 的零根， $i = 1,2,\dots ,r_{\circ}$ （8.39）其中， $r = \operatorname {rank}G(s)$ ，而 $\widetilde{M} (\lambda)$ 具有如下的形式：

$$
\widetilde {M} (\lambda) = \left[ \begin{array}{c c c c} \frac {\tilde {\varepsilon} _ {1} (\lambda)}{\tilde {\psi} _ {1} (\lambda)} & & & \\ & \ddots & & 0 \\ & & \frac {\tilde {\varepsilon} _ {r} (\lambda)}{\tilde {\psi} _ {r} (\lambda)} & \\ - & 0 & & 0 \end{array} \right] \tag {8.40}
$$

并且满足整除性 $\tilde{\varepsilon}_i(\lambda) | \tilde{\varepsilon}_{i+1}(s)$ 和 $\tilde{\psi}_{i+1}(\lambda) | \tilde{\psi}_i(\lambda)$ ，以及 $\{\tilde{\varepsilon}_i(\lambda), \tilde{\psi}_i(\lambda)\}$ 为互质。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c c} \frac {s}{s - 1} & & \\ & \frac {1}{s - 1} & \\ & & (s - 1) ^ {2} \end{array} \right]
$$

令 $s = \lambda^{-1}$ ，则得到

$$
G (\lambda^ {- 1}) = \left[ \begin{array}{c c c} \frac {\lambda^ {- 1}}{\lambda^ {- 1} - 1} & & \\ & \frac {1}{\lambda^ {- 1} - 1} & \\ & & (\lambda^ {- 1} - 1) ^ {2} \end{array} \right]
$$

将其改写成以 $\lambda$ 为变量的有理分式矩阵，又有

$$
H (\lambda) = \left[ \begin{array}{c c c} \frac {- 1}{\lambda - 1} & & \\ & \frac {- \lambda}{\lambda - 1} & \\ & & \frac {(\lambda - 1) ^ {2}}{\lambda^ {2}} \end{array} \right]
$$

而其史密斯-麦克米伦形则为

$$
\widetilde {M} (\lambda) = \left[ \begin{array}{c c c} \frac {1}{\lambda^ {2} (\lambda - 1)} & & \\ & \frac {1}{\lambda - 1} & \\ & & \lambda (\lambda - 1) ^ {2} \end{array} \right]
$$

因此，根据前述定义即知， $G(s)$ 在 $s = \infty$ 处有2个极点和1个零点。

结构指数 同样，我们也可采用结构指数来统一地表征 $G(s)$ 在无穷远处的极点和零点。根据定义式(8.38)和(8.39)可以直接看出：

$G(s)$ 在 $s = \infty$ 处的结构指数 $\{\sigma_1(\infty),\dots ,\sigma_r(\infty)\}$

$$= \widetilde {M} (\lambda) \text { 在 } \lambda = 0 \text { 处的结构指数 } \{\tilde {\sigma} _ {i} (0), \dots , \tilde {\sigma} _ {r} (0) \} \tag {8.41}$$

其中， $\{\sigma_{1}(\infty,\cdots,\sigma_{r}(\infty)\}$ 中的正指数之和为 $G(s)$ 在 $\infty$ 处的零点重数， $\{\sigma_{1}(\infty),\cdots,\sigma_{r}(\infty)\}$ 中的负指数之和的绝对值为 $G(s)$ 在 $\infty$ 处极点的重数。对于本节中所讨论的例子，不难看出， $G(s)$ 在 $\infty$ 处的结构指数为： $\sigma_{1}(\infty)=-2,\quad\sigma_{2}(\infty)=0,\quad\sigma_{3}(\infty)=1;$ 因此可知， $G(s)$ 在 $\infty$ 处的极点重数为2，零点重数为1。
