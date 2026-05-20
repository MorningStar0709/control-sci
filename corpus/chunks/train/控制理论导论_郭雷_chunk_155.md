由此可见，求解方程 (2.3.11) 和方程 (2.3.12) 的初值问题归结为求得状态转移矩阵 $\mathbf{e}^{\mathbf{A}t}$ .

求状态转移矩阵的方法有多种 [15]. 例如关系式 (2.3.13) 就是其中的一种. 但最常见的是将微分方程的系数矩阵 $A$ 变换成具有某种“简单”形式的矩阵, 使得对应于这种简单形式矩阵的状态转移矩阵易于求得. 然后再变换回原矩阵而得到它的状态转移矩阵 [8],[11].

为了解状态转移矩阵的构成并便于引用，下面列出一些简单情形下的表达式：

(1) $\pmb{A}$ 的特征值皆为实数且两两不相同的情况。这时 $\mathbf{e}^{\mathbf{A}t}$ 具有下列形式：

$$
\mathrm{e} ^ {A t} = S ^ {- 1} \left[ \begin{array}{c c c c} \mathrm{e} ^ {\lambda_ {1} t} & & & \\ & \mathrm{e} ^ {\lambda_ {2} t} & & \\ & & \ddots & \\ & & & \mathrm{e} ^ {\lambda_ {n} t} \end{array} \right] S,
$$

其中 $S = [h_{1}, h_{2}, \cdots, h_{n}]^{-1}$ ， $Ah_{i} = \lambda_{i}h_{i}, i = 1, 2, \cdots, n;$

(2) $A$ 的两两不相同的特征值中有复共轭成双的情况。为简单起见，设 $A$ 仅有一对复共轭成双的特征值。不妨认为 $\lambda_1 = \alpha_1 + \mathrm{j}\beta_1, \lambda_2 = \alpha_1 - \mathrm{j}\beta_1$ 。这时 $\mathbf{e}^{At}$ 的具体形式为

$$
\mathrm{e} ^ {\boldsymbol {A} t} = \boldsymbol {S} ^ {- 1} \left[ \begin{array}{c c c c} \mathrm{e} ^ {\boldsymbol {A} _ {1, 2} t} & & & \\ & \mathrm{e} ^ {\lambda_ {3} t} & & \\ & & \ddots & \\ & & & \mathrm{e} ^ {\lambda_ {n} t} \end{array} \right] \boldsymbol {S},

e ^ {A _ {1, 2} t} = \left[ \begin{array}{l l} e ^ {\alpha_ {1} t} \cos \beta_ {1} t & e ^ {\alpha_ {1} t} \sin \beta_ {1} t \\ - e ^ {\alpha_ {1} t} \sin \beta_ {1} t & e ^ {\alpha_ {1} t} \cos \beta_ {1} t \end{array} \right],
$$

其中 $S = [\xi_{1}, \eta_{1}, h_{3}, \cdots, h_{n}]^{-1}$ ， $Ah_{i} = \lambda_{i}h_{i}, i = 1, 2, \cdots, n, h_{1,2} = \xi_{1} \pm j\eta_{1};$

(3) $\pmb{A}$ 有实的重特征值的情况. 这时 $\mathbf{e}^{\mathbf{A}t}$ 的形式如下:

$$
\mathbf {e} ^ {\boldsymbol {A} t} = \boldsymbol {S} ^ {- 1} \left[ \begin{array}{c c c c} \mathrm{e} ^ {J _ {1} t} & & & \\ & \mathrm{e} ^ {J _ {2} t} & & \\ & & \ddots & \\ & & & \mathrm{e} ^ {J _ {l} t} \end{array} \right] \boldsymbol {S}, \tag {2.3.15}

\mathrm{e} ^ {J _ {k} t} = \left[ \begin{array}{c c c c} \mathrm{e} ^ {T _ {k 1} t} & & & \\ & \mathrm{e} ^ {T _ {k 2} t} & & \\ & & \ddots & \\ & & & \mathrm{e} ^ {T _ {k m _ {k}} t} \end{array} \right],
$$

这里 $k=1,2,\cdots,l,p=1,2,\cdots,m_{k},e^{T_{kp}t}$ 为 $n_{kp}\times n_{kp}$ 矩阵，

$$
\mathrm{e} ^ {T _ {k p} t} = \left[ \begin{array}{c c c c} \mathrm{e} ^ {\lambda_ {k} t} & t \mathrm{e} ^ {\lambda_ {k} t} & \dots & \frac {t ^ {n _ {k p} - 1}}{(n _ {k p} - 1) !} \mathrm{e} ^ {\lambda_ {k} t} \\ & \mathrm{e} ^ {\lambda_ {k} t} & \dots & \frac {t ^ {n _ {k p} - 2}}{(n _ {k p} - 2) !} \mathrm{e} ^ {\lambda_ {k} t} \\ & & \ddots & \vdots \\ & & & \mathrm{e} ^ {\lambda_ {k} t} \end{array} \right],
$$
