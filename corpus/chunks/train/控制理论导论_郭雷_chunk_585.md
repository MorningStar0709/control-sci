证明 设能控性秩条件在 $x_0$ 点满足，那么存在 $x_0$ 的一个邻域 $U_{x_0}$ 使能控性秩条件在一切 $x \in U_{x_0}$ 满足。因此能控性秩条件满足的点的集合 $D$ 是一个开集。现在设 $D$ 不稠，那么存在一个开集 $U \neq \emptyset$ ，使得 $\operatorname{rank}(\mathcal{F}(x)) < n, x \in U$ 。设 $k$ 为 $\mathcal{F}$ 在 $U$ 上的最大秩，即 $k = \max_{x \in U} \operatorname{rank}(\mathcal{F}(x)) < n$ ，则存在其一个非空开子集 $V \subset U$ ，使得 $\operatorname{rank}(\mathcal{F}(x)) = k, x \in V$ 。根据 Frobenius 定理，对每一点 $x_0 \in V$ ，存在 $\mathcal{F}$ 的一个积分子流形 $\mathcal{I}(\mathcal{F}, x_0)$ ，它的维数为 $k$ 。显然

$$W R _ {V} (x _ {0}) \subset \mathcal {I} (\mathcal {F}, x _ {0}) \cap V,$$

这与系统在 $x_0$ 局部弱能控矛盾.

对于解析系统，弱能控可推出能控性秩条件.

命题8.1.5 设系统(8.1.1)解析且弱能控，则能控性秩条件满足，即

$$\operatorname{rank} (\mathcal {F} (x)) = n, \quad x \in M.$$

证明 设

$$\operatorname{rank} (\mathcal {F} (x)) < n, \quad \forall x \in M.$$

那么对任一点 $x_0 \in M$ 其积分子流形满足 $\dim(\mathcal{I}(\mathcal{F}, x_0)) < n$ . 但

$$W R (x _ {0}) \subset \mathcal {I} (\mathcal {F}, x _ {0}),$$

它与弱能控性矛盾．因此至少有一点 $x_0 \in M$ ，使得

$$\operatorname{rank} (\mathcal {F} (x)) = n.$$

我们断言如果系统弱能控，则对任意两点 $x, y \in M$

$$\operatorname{rank} (\mathcal {F} (x)) = \operatorname{rank} (\mathcal {F} (y)).$$

从而所需结论成立．事实上，若弱能控，则存在 $x_{0}=x, x_{1}, \cdots, x_{k}=y$ ，使得 $x_{i}$ 与 $x_{i+1}$ 由一向量场 $X \in F$ 的积分曲线相连接，即（注意下式 t 可能为负）

$$\boldsymbol {x} _ {i + 1} = \phi_ {t} ^ {X} (\boldsymbol {x} _ {i}).$$

现在对任一 $Y \in \mathcal{F}$ , 利用 Campbell-Baker-Hausdorff 公式, 有

$$\left(\phi_ {- t} ^ {X}\right) _ {*} Y \left(x _ {i + 1}\right) = \sum_ {k = 0} ^ {\infty} \mathrm{ad} _ {X} ^ {k} Y \left(x _ {i}\right) \frac {t ^ {k}}{k !}. \tag {8.1.5}$$

由于式 (8.1.5) 右边属于 $\mathcal{F}(x_i)$ 而 $Y \in \mathcal{F}$ 是任意的，因此

$$(\phi_ {- t} ^ {X}) _ {*} \mathcal {F} (x _ {i + 1}) \subset \mathcal {F} (x _ {i}).$$

由于 $(\phi_{-t}^{X})$ ，是一个微分同胚，于是

$$\operatorname{rank} (\mathcal {F} (x _ {i + 1})) \leqslant \operatorname{rank} (\mathcal {F} (x _ {i})).$$

将 $x_{i}$ 与 $x_{i + 1}$ 对换，再利用Campbell-Baker-Hausdorff公式，得到

$$\operatorname{rank} (\mathcal {F} (x _ {i})) \leqslant \operatorname{rank} (\mathcal {F} (x _ {i + 1})).$$

于是

$$\operatorname{rank} (\mathcal {F} (x)) = \dim (\mathcal {F} (x _ {1})) = \dots = \dim (\mathcal {F} (y)).$$

下面的推论直接由命题 8.1.1, 定理 8.1.1 及命题 8.1.5 可得.

推论 8.1.1 对一个形如系统 (8.1.1) 的解析系统，局部弱能控与能控性秩条件等价.

下面考虑真实的能达集. 记 $x_0 \in M$ 在时刻 $t$ 的能达集为 $R(x_0, t)$ . 显然

$$R (x _ {0}) = \bigcup_ {t \geqslant 0} R (x _ {0}, t).$$
