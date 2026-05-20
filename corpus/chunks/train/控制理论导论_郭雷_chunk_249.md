$$
\begin{array}{l} \dot {\theta} _ {q} (t) = \lim _ {\Delta t \rightarrow 0} \frac {1}{\Delta t} \left[ \right.\left(\phi_ {- t + \Delta t} ^ {X} (q)\right) _ {*} \left( \right.Y \left(\phi_ {\Delta t} ^ {X} \left(q ^ {\prime}\right)\right) - \left(\phi_ {- t} ^ {X}\right) _ {*} \left(Y \left(q ^ {\prime}\right)\right)\left. \right]\left. \right. \\ = \left(\phi_ {- t} ^ {X}\right) _ {*} \left(\lim _ {\Delta t \rightarrow 0} \frac {1}{\Delta t} \left(\phi_ {- \Delta t} ^ {X}\right) _ {*} \left(Y \left(\phi_ {\Delta t} ^ {X} \left(q ^ {\prime}\right)\right) - Y \left(q ^ {\prime}\right)\right)\right. \\ = \left(\phi_ {- t} ^ {X}\right) _ {*} ([ X, Y ] _ {q ^ {\prime}}) = 0. \\ \end{array}
$$

从而 $\theta_q(t)$ 对 $t < \delta$ 及 $q \in V$ 是定常的，因此 $Y$ 是 $\phi_t^X$ 不变的。由引理3.8.1即得式(3.8.4).

定理3.8.1(Frobenius定理) 一个分布 $D$ 是可积的，当且仅当它是对合的且有定常维数.

证明 必要性. 设 $D$ 在 $p$ 点邻域可积, 那么存在 $D$ 的一个积分流形 $S$ 通过 $p$ 使得 $T_{p}(S) = D(p)$ . 因为 $S$ 是一个子流形, 所以存在局部坐标系 $(U, x)$ 使 $p \in U$ 且

$$S = \{x \in U \mid x _ {k + 1} = \dots = x _ {n} = 0 \}.$$

于是可知

$$D = \operatorname{span} \left\{\frac {\partial}{\partial x _ {1}}, \dots , \frac {\partial}{\partial x _ {k}} \right\}.$$

由此可见必要性成立.

充分性. 设 $\dim(D)=k$ . 对一给定点 $p\in M$ , 存在 p 的一个邻域 V, 及 V 上的一组基 $X_{1},\cdots,X_{k}$ 使得

$$D (q) = \operatorname{span} \left\{X _ {1} (q), \dots , X _ {k} (q) \right\}, \quad q \in V.$$

不失一般性，我们可假定矩阵的顶部 $k \times k$ 子块，记作 $Q(q)$ ，是非奇异的。然后定义

$$
\boldsymbol {Y} (q) = (\boldsymbol {Q} (q)) ^ {- 1} \left(X _ {1} (q), \dots , X _ {k} (q)\right) \stackrel {\text { def }} {=} \left(Y _ {1} (q), \dots , Y _ {k} (q)\right) = \left[ \begin{array}{c} I _ {k} \\ * \end{array} \right].
$$

因为 $D$ 是对合的，所以

$$\left[ Y _ {i}, Y _ {j} \right] = \sum_ {s = 1} ^ {k} c _ {s} (q) Y _ {s}. \tag {3.8.5}$$

利用公式 (3.8.4), 有

$$
[ Y _ {i}, Y _ {j} ] = \left[ \begin{array}{c} 0 \\ * \end{array} \right]. \tag {3.8.6}
$$

将式 (3.8.5) 与式 (3.8.6) 比较，可知

$$[ Y _ {i}, Y _ {j} ] = 0, \qquad 0 \leqslant i, j \leqslant k.$$

即 $(Y_{1},\cdots,Y_{k})$ 为D的一组可交换基. 再选择 $Y_{k+1},\cdots,Y_{n}$ 使得 $Y_{1}(q),\cdots,Y_{n}(q)$ 为 $T_{q}^{\prime}(M)$ 的一组基， $q\in V$ . 于是可以找一个小 $\delta>0$ 定义映射

$$\Phi \left(y _ {1}, \dots , y _ {n}\right) = \phi_ {y _ {1}} ^ {Y _ {1}} \dots \phi_ {y _ {n}} ^ {Y _ {n}} (p), \quad | y _ {i} | < \delta , i = 1, \dots , n. \tag {3.8.7}$$

因为 Jacobi 矩阵 $J_{\Phi}(0) = I_n$ 非奇异，故 $\Phi$ 定义了一个从 $0 \in \mathbb{R}^n$ 邻域到 $p \in M$ 邻域的微分同胚。由定义
