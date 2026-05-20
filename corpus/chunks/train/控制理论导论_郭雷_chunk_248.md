# 3.8 分布及其积分

定义3.8.1 流形 $M$ 上的一个分布 $D$ 是 $M$ 到 $T(M)$ 的一个映射，对每一点 $x \in M, D(x)$ 为 $T_x(M)$ 的一个子空间。一个向量场 $X \in D$ 是指每一点 $x \in M$ 均有 $X(x) \in D(x)$ 。

定义 3.8.2 (1) 一个分布 D 称为对合的，如果其中的任意两个向量 $X, Y \in D$ ，其 Lie 括号

$$[ \boldsymbol {X}, \boldsymbol {Y} ] \in D, \quad \forall \boldsymbol {X}, \boldsymbol {Y} \in D; \tag {3.8.1}$$

(2) 一个子流形 $S$ 称为给定分布 $D$ 的积分流形，如果对于每一点 $x \in S$ ，它的切空间都是 $D(x)$ ，即

$$T _ {x} (S) = D (x), \quad \forall x \in S.$$

如果一个分布 $D(x)$ 有积分流形，它称为可积的.

在非线形系统的分析与控制设计中,应用微分几何方法的一个基本工具是 Frobenius 定理. 为表述这个定理我们需要一些准备.

引理3.8.1 设 $X \in V^{1}(M)$ 是一个 $C^{1}$ 向量场， $F: M \to M$ 是一个微分同胚。 $X$ 是 $F$ 不变的（即 $F_{*}(X(p)) = X(F(p))$ ，当且仅当

$$F (\phi_ {t} ^ {X} (p)) = \phi_ {t} ^ {X} (F (p)), \qquad \forall p \in M. \tag {3.8.2}$$

证明 必要性. 设 $X$ 是 $F$ 不变的. 利用链式规则, 有

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} \left(F \circ \phi_ {t} ^ {X} (p)\right) = J _ {F} \frac {\mathrm{d}}{\mathrm{d} t} \phi_ {t} ^ {X} (p) = J _ {F} X \left(\phi_ {t} ^ {X} (p)\right) = F _ {*} \left(X \left(\phi_ {t} ^ {X} (p)\right)\right) \\ = X \left(\phi_ {t} ^ {X} (p)\right). \tag {3.8.3} \\ \end{array}
$$

但 $X(\phi_t^X (p))$ 的积分曲线是 $\phi_t^X (p)$ , 从而微分方程解的唯一性保证 (3.8.2) 成立.

充分性. 设式 (3.8.3) 成立. 两边同时微分得 $F_{*}(X(\phi_{t}^{X}(p))) = X(\phi_{t}^{X}(F(p)))$ , 再令 $t = 0$ , 得 $F_{*}(X(p)) = X(F(p))$ .

引理3.8.2 设 $X$ 及 $Y$ 为 $M$ 上两个 $C^1$ 向量场. $[X, Y] = 0$ 当且仅当对任意一点 $p \in M$ 存在一个 $\delta_p > 0$ 使得

$$\phi_ {t} ^ {X} \circ \phi_ {s} ^ {Y} (p) = \phi_ {s} ^ {Y} \circ \phi_ {t} ^ {X} (p), \quad | s |, | t | < \delta_ {p}. \tag {3.8.4}$$

证明 充分性. 式 (3.8.4) 保证了 $Y$ 是 $\phi_t^X$ 不变的且 $X$ 是 $\phi_t^Y$ 不变的. 因此存在 $p$ 的一个邻域 $V$ , 使得对每一点 $q \in V$ ,

$$[ X, Y ] _ {q} = \lim _ {t \rightarrow 0} \frac {1}{t} ((\phi_ {- t} ^ {X}) _ {*} (Y (\phi_ {t} ^ {X} (q)) - Y (q))) = \lim _ {t \rightarrow 0} \frac {1}{t} (Y (q) - Y (q)) = 0.$$

必要性. 设 $[X, Y] = 0$ . 记 $q' = \phi_t^X(q)$ 且令

$$\theta_ {q} (t) = (\phi_ {- t} ^ {X}) _ {*} (Y (\phi_ {t} ^ {X} (q)).$$

则
