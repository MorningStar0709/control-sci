# 6.3 线性相关和线性无关

有理分式域 $\mathcal{R}(s)$ 上的一个线性空间中的 p 个多项式向量 $q_{1}(s), q_{2}(s), \cdots, q_{p}(s)$ 称为是线性相关的，当且仅当存在一组不全为零的多项式 $\alpha_{1}(s), \alpha_{2}(s), \cdots, \alpha_{p}(s)$ ，使成立

$$\alpha_ {1} (s) \boldsymbol {q} _ {1} (s) + \alpha_ {2} (s) \boldsymbol {q} _ {2} (s) + \dots + \alpha_ {p} (s) \boldsymbol {q} _ {p} (s) = 0 \tag {6.2}$$

如果仅当 $\alpha_{1}(s)=0,\alpha_{2}(s)=0,\cdots,\alpha_{p}(s)=0$ 时式(6.2)才成立，则称 $q_{1}(s),q_{2}(s),\cdots,q_{p}(s)$ 是线性无关的。

例 给定两个多项式行向量 $q_{1}(s)$ 和 $q_{2}(s)$ 如下：

$$\boldsymbol {q} _ {1} (s) = [ s + 2, s - 1 ], \quad \boldsymbol {q} _ {2} (s) = [ s ^ {2} + 3 s + 2, s ^ {2} - 1 ]$$

现选取标量多项式 $\alpha_{1}(s) = s + 1$ 和 $\alpha_{2}(s) = -1$ ，使有

$$
\begin{array}{l} \alpha_ {1} (s) \boldsymbol {q} _ {1} (s) + \alpha_ {2} (s) \boldsymbol {q} _ {2} (s) \\ = [ s ^ {2} + 3 s + 2, s ^ {2} - 1 ] - [ s ^ {2} + 3 s + 2, s ^ {2} - 1 ] = [ 0, 0 ] \\ \end{array}
$$

因此，按定义，多项式向量 $q_{1}(s)$ 和 $q_{2}(s)$ 是线性相关的。

进一步,如果引进如下的表示法:

$$
\begin{array}{l} \alpha_ {1} (s) \boldsymbol {q} _ {1} (s) + \alpha_ {2} (s) \boldsymbol {q} _ {2} (s) + \dots + \alpha_ {p} (s) \boldsymbol {q} _ {p} (s) \\ = \left[ \begin{array}{l l} \boldsymbol {q} _ {1} (s) & \boldsymbol {q} _ {2} (s) \dots \boldsymbol {q} _ {p} (s) \end{array} \right] \left[ \begin{array}{c} \alpha_ {1} (s) \\ \alpha_ {2} (s) \\ \vdots \\ \alpha_ {p} (s) \end{array} \right] \\ = \left[ q _ {1} (s) q _ {2} (s) \dots q _ {p} (s) \right] a (s) \tag {6.3} \\ \end{array}
$$

则上面给出的多项式向量组为线性相关和线性无关的定义也可用另一种方式来表述。称多项式向量组 $q_{1}(s)$ , $q_{2}(s)$ , $\cdots$ , $q_{p}(s)$ 为线性相关，当且仅当存在 p 维多项式向量 $\alpha(s) \neq 0$ ，使成立

$$[ \boldsymbol {q} _ {1} (s) \quad \boldsymbol {q} _ {2} (s) \dots \boldsymbol {q} _ {p} (s) ] \boldsymbol {\alpha} (s) = 0 \tag {6.4}$$

反之，如果仅当 $\boldsymbol{a}(s)=0$ 时上式才成立，则称多项式向量组 $\boldsymbol{q}_{1}(s),\boldsymbol{q}_{2}(s),\cdots,\boldsymbol{q}_{p}(s)$ 是线性无关的。

由式(6.4)出发，可以很容易把多项式矩阵的奇异和非奇异的概念与多项式向量组的线性相关和线性无关的概念联系起来。给定一个方多项式矩阵 $Q(s)$ ，则 $Q(s)$ 为奇异当且仅当其列(行)多项式向量为线性相关，而 $Q(s)$ 为非奇异当且仅当其列(行)向量为线性无关。反之，如果给定 p 个 p 维列(行)多项式向量 $q_{1}(s), q_{2}(s), \cdots, q_{p}(s)$ ，则它们的线性无关等同于由它们组成的方多项式矩阵为非奇异，而它们的线性相关则等同于相应的方多项式矩阵为奇异。

还需指出，多项式向量组的线性相关或线性无关，不仅依赖于这组向量本身，而且通常还依赖于引入的标量 $\alpha_{1}(s), \alpha_{2}(s), \cdots, \alpha_{p}(s)$ 所取值的域。向量组 $q_{1}(s), q_{2}(s), \cdots, q_{p}(s)$ 在 $(\mathcal{R}^{p}(s), \mathcal{R}(s))$ 上是线性相关的，并不意味着它们在 $(\mathcal{R}^{p}(s), \mathcal{R})$ 上也是线性相关的。事实上，在前面列举的例子中， $q_{1}(s)$ 和 $q_{2}(s)$ 在 $(\mathcal{R}^{2}(s), \mathcal{R}(s))$ 上是线性相关的，但在 $(\mathcal{R}^{2}(s), \mathcal{R})$ 上它们则是线性无关的。指出这一点，对于正确理解多项式向量组的线性相关和线性无关的含义，无疑是会有帮助的。
