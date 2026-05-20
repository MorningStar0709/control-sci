证 按设定， $X_{t}$ 为图示闭环系统矩阵 $(A - BK^{*})$ 的相应于特征值 $\mu_{t}$ 的特征向量，且注意到参考输入 $v(t) = 0$ ，则当 $x(t) = X_{t} e^{\mu_{t} t}$ 时有

$$\boldsymbol {u} ^ {*} (t) = U _ {i} e ^ {\mu_ {i} t} = - K ^ {*} X _ {i} e ^ {\mu_ {i} t} \tag {11.267}$$

由此可得:

$$U _ {i} = - K ^ {*} X _ {i} \tag {11.268}$$

另一方面，由(11.262)知 $\pmb{\alpha}^{*}$ 还需满足关系式：

$$\boldsymbol {u} ^ {*} (t) = - R ^ {- 1} B ^ {T} \lambda (t) \tag {11.269}$$

且令相应于 $x(t) = X_{i}e^{\mu_{i}t}$ 和 $\pmb{u}^{*}(t) = U_{i}e^{\mu_{i}t}$ 的 $\lambda (t)$ 为如下的形式：

$$\lambda (t) = \Lambda_ {i} e ^ {\mu_ {i} t} \tag {11.270}$$

于是将(11.270)代入(11.269)又可导出:

$$U _ {i} = - R ^ {- 1} B ^ {T} \Lambda_ {i} \tag {11.271}$$

从而，由(11.268)和(11.271)可进而得到：

$$K ^ {*} X _ {i} = R ^ {- 1} B ^ {T} \Lambda_ {i}, i = 1, 2, \dots , n \tag {11.272}$$

再因 $X_{i}$ 为 $(A - BK^{*})$ 的属于 $\mu_{i}$ 的特征向量，故依定义并考虑到所导出的(11.272)，又可有：

$$
\mu_ {i} X _ {i} = (A - B K ^ {*}) X _ {i} = A X _ {i} - B K ^ {*} X _ {i}
= A X _ {i} - B R ^ {- 1} B ^ {T} \Lambda_ {i} = (A, - B R ^ {- 1} B ^ {T}) \left[ \begin{array}{l} X _ {i} \\ \Lambda_ {i} \end{array} \right] \tag {11.273}
$$

而由(11.270)和(11.263)则有:

$$\dot {\lambda} (t) = \mu_ {i} \Lambda_ {i} e ^ {\mu_ {i} t} = - C ^ {T} C X _ {i} e ^ {\mu_ {i} t} - A ^ {T} \Lambda_ {i} e ^ {\mu_ {i} t} \tag {11.274}$$

这样，还可导出：

$$
\mu_ {i} \Lambda_ {i} = - C ^ {T} C X _ {i} - A ^ {T} \Lambda_ {i} = (- C ^ {T} C, - A ^ {T}) \left[ \begin{array}{l} X _ {i} \\ \Lambda_ {i} \end{array} \right] \tag {11.275}
$$

现把(11.273)和(11.275)联合,就可给出:

$$
\mu_ {i} \left[ \begin{array}{l} X _ {i} \\ \Lambda_ {i} \end{array} \right] = \left[ \begin{array}{c c} A & - B R ^ {- 1} B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right] \left[ \begin{array}{l} X _ {i} \\ \Lambda_ {i} \end{array} \right] = M \left[ \begin{array}{l} X _ {i} \\ \Lambda_ {i} \end{array} \right], i = 1, \dots , n \tag {11.276}
$$

这表明， $\begin{bmatrix}X_{i}\\ \Lambda_{i}\end{bmatrix}$ 为矩阵 M 的属于 $\mu_{i}$ 的特征向量。而且由于 $\{\mu_{1},\cdots,\mu_{n}\}$ 两两相异，所以 $\{X_{1},\cdots,X_{n}\}$ 必线性无关。因而，由(11.272)即可导出：

$$K ^ {*} = R ^ {- 1} B ^ {T} \left[ \Lambda_ {1}, \dots , \Lambda_ {n} \right] \left[ X _ {1}, \dots , X _ {n} \right] ^ {- 1} \tag {11.277}$$

而最优控制 $u^{*} = -K^{*}x^{*}(t)$ 。至此，，证明完成。

结论3 对于状态空间域LQ问题(11.251)和(11.252)，其最优控制律 $\pmb{u}^*$ 的频域求解算法可归纳如下：

第1步：计算矩阵

$$
M \triangleq \left[ \begin{array}{c c} A & - B R ^ {- 1} B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right]
$$

第2步：确定矩阵M的位于左半开复平面上的n个特征值 $\{\mu_{1},\cdots,\mu_{n}\}$ ，设其为两两相异的实数或共轭复数。

第3步：定出矩阵M的属于 $\mu_{i}$ 的特征向量，得到 $X_{i}$ 和 $\Lambda_{i}, i=1,2,\cdots,n$ 。
