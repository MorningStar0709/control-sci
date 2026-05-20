# 分布函数和特征函数

反过来，如果给出了 $\xi$ 的特征函数 $\phi(\lambda)$ ，则可用下面的反演公式，求出 $\xi$ 的分布函数 $F$ 。设 $b > a$ 为 $F(\cdot)$ 的连续点，那么

$$F (b) - F (a) = \lim _ {c \rightarrow \infty} \frac {1}{2 \pi} \int_ {- c} ^ {c} \frac {\mathrm{e} ^ {- \mathrm{i} \lambda a} - \mathrm{e} ^ {- \mathrm{i} \lambda b}}{\mathrm{i} \lambda} \phi (\lambda) \mathrm{d} \lambda . \tag {4.1.11}$$

因此分布函数和特征函数相互一一对应.

设 $F_{n}(\cdot)$ 及 $F(\cdot)$ 都是分布函数. 如果在 $F(\cdot)$ 的所有连续点 $x$ 上都有 $F_{n}(x) \underset{n \to \infty}{\longrightarrow} F(x)$ , 那么称 $F_{n}(\cdot)$ 弱收敛到 $F(\cdot)$ , 或相应的随机变量依分布收敛, 记作 $F_{n} \underset{n \to \infty}{\overset{w}{\longrightarrow}} F$ .

定理 4.1.1 设 $F_{n} \xrightarrow{w} F$ ，则相应的特征函数也收敛 $\phi_{n}(n) \xrightarrow[n\to\infty]{\phi(\lambda)}, \forall \lambda \in \mathbb{R}^{1}$ 。反之，若特征函数 $\phi_{n}(\lambda)$ 收敛到某一函数 $\phi(\lambda), \phi(\lambda)$ 在 $\lambda = 0$ 处连续，那么和 $\phi_{n}$ 相应的分布函数 $F_{n}$ 必弱收敛到某一分布函数 F，并且 $\phi(\lambda)$ 是 F 的特征函数。

定理 4.1.2 (Bochner-Khinchin) 设 $\phi(\lambda)$ 对 $\lambda \in R^{1}$ 连续， $\phi(0) = 1$ ，则 $\phi(\lambda)$ 为特征函数的充分必要条件是 $\phi(\lambda)$ 非负定，即对任意实数 $\lambda_{1}, \cdots, \lambda_{n}$ 及任意复数 $z_{1}, \cdots, z_{n}, n = 1, 2, \cdots$ 都有

$$\sum_ {i, j = 1} ^ {n} \phi (\lambda_ {i} - \lambda_ {j}) z _ {i} \overline {{{{z}}}} _ {j} \geqslant 0.$$

定理 4.1.3 (Polya) 设 $\phi(\lambda)$ 为连续偶函数， $\phi(\lambda) \geqslant 0, \phi(0) = 1$ ，当 $\lambda \to \infty$ 时 $\phi(\lambda) \to 0$ ，且 $\phi(\lambda)$ 在 $\lambda \in (0, \infty)$ 上为凸函数，那么 $\phi(\lambda)$ 为特征函数。

例 4.1.9 $\phi(\lambda)=\mathrm{e}^{-|\lambda|}$ 是特征函数.

例4.1.10 $\phi (\lambda) = \left\{ \begin{array}{ll}1 - |\lambda |, & |\lambda |\leqslant 1,\\ 0, & |t| > 1, \end{array} \right.$

是特征函数.

对随机向量 $\pmb{\xi} \in R^{l}$ 也可定义特征函数，设 $\lambda \in \mathbb{R}^{l}, \xi$ 的特征函数 $\phi(\lambda)$ 定义为

$$\phi (\lambda) \stackrel {\text { def }} {=} E \mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} \xi} \tag {4.1.12}$$

随机向量的特征函数和分布函数也是相互一一对应的.

与由式 (4.1.6) 定义的正态密度相应的特征函数为
