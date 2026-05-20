# 2. 频域信号

频域信号 $u(j\omega)$ 可看成从 $jR \rightarrow C$ 的函数, 设 $u(j\omega)$ 为勒贝格可测函

数,则有如下定义。

定义2 对于正数 $p \in [1, +\infty)$ ，元素在 $\mathbf{jR}$ 上有定义，取值于复数域 $\mathbf{C}$ 的 $u(\cdot)$ 为勒贝格可测函数，且满足

$$\int_ {- \infty} ^ {+ \infty} | u (j \omega) | ^ {p} d \omega < + \infty$$

的空间,称 $L_{p}$ 空间。常用的 $L_{p}$ 空间有

$$
\begin{array}{l} L _ {2}: \int_ {- \infty} ^ {+ \infty} | u (j \omega) | ^ {2} d \omega <   + \infty \\ L _ {\infty}: \underset {\omega \in \mathbb {R}} {e s s \sup} | u (j \omega) | <   + \infty \\ \end{array}
$$

对于频域信号 $u(\mathrm{j}\omega)$ ，常用范数有

2 - 范数： $\| \pmb{u} \|_2 = \frac{1}{2\pi}\int_{-\infty}^{+\infty} |\pmb{u}(\mathrm{j}\omega)|^2\mathrm{d}\omega = \frac{1}{2\pi}\int_{-\infty}^{+\infty} \pmb{u}^*(\mathrm{j}\omega)\pmb{u}(\mathrm{j}\omega)\mathrm{d}\omega$

其中 $\boldsymbol{u}^{*}(j\omega)$ 是 $\boldsymbol{u}(j\omega)$ 的共轭转置。

$\infty$ - 范数： $\| u \|_{\infty} = ess \sup_{\omega \in \mathbb{R}} |u(j\omega)|$

由于实际中常遇到的频域信号都是 $\mathrm{j}\omega$ 的(真)实有理函数, 因此, 把 $L_{2}$ 和 $L_{\infty}$ 中实有理函数的全体给出专门的记号, 分别记作 $\mathbf{R}L_{2}$ 和 $\mathbf{R}L_{\infty}$ 。

即： $RL_{2}=\{u\mid u\in L_{2},u$ 为 $j\omega$ 的实有理函数（向量）

$\mathbf{R}L_{\infty}=\left\{\boldsymbol{u}\mid\boldsymbol{u}\in L_{\infty},\boldsymbol{u}\right.$ 为 $j\omega$ 的实有理函数(向量)

由定义可知, $RL_{\infty}$ 是在虚轴上无极点的真实有理函数(向量)的全体。
