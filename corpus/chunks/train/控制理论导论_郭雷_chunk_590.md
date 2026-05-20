现在式 (8.1.22) 表明 $\sum_{i=1}^{s} \lambda_i = 0$ , 因此式 (8.1.21) 表明 $V \in \mathcal{F}_0(x_0)$ . 但是 $V \in T_{x_0}(M)$ 是任选的, 这说明 $T_{x_0}(M) \subset \mathcal{F}_0(x_0)$ . 因此

$$\operatorname{rank} \left(\mathcal {F} _ {0} \left(x _ {0}\right)\right) = n.$$

反之，设有式(8.1.19).那么对 $V\in T_{x_0}(M)$ 它可表示为

$$V = \left(\sum_ {i = 1} ^ {s} \lambda_ {i} X _ {i} + Y\right) (x _ {0}),$$

这里 $X_{i}\in F,Y\in \mathcal{F}^{\prime}$ ，且 $\sum_{i = 1}^{s}\lambda_{i} = 0.$ 于是

$$(0 \oplus V) = \left(\sum_ {i = 1} ^ {s} \lambda_ {i} \left(\frac {\partial}{\partial t} \oplus X _ {i}\right) + 0 \oplus Y\right) (0, x _ {0}) \in \hat {\mathcal {F}} (0, x _ {0}). \tag {8.1.23}$$

选择任一 $X \in F$ , 根据定义,

$$\left(\frac {\partial}{\partial t} \oplus X\right) (0, x _ {0}) \in \hat {F} (0, x _ {0}) \subset \hat {\mathcal {F}} (0, x _ {0}). \tag {8.1.24}$$

特别地，设 $V = X$ ，那么由式(8.1.21)和式(8.1.24)可知

$$\frac {\partial}{\partial t} \oplus 0 \in \hat {\mathcal {F}} (0, x _ {0}). \tag {8.1.25}$$

于是式 (8.1.23) 和式 (8.1.25) 表明 $\hat{\mathcal{F}}(0, x_0)$ 包括在 $T_{(0, x_0)}(\mathbb{R} \times M)$ 的一切向量场. 因此

$$\operatorname{rank} (\hat {\mathcal {F}} (0, x _ {0})) = n + 1.$$

最后，我们证明 (3). 设 $y \in R(x_0, T)$ ，则存在 $X_1, \cdots, X_m \in F$ ，及 $t = (t_1, \cdots, t_m) \in \mathbb{R}_+^m, \|t\| = T$ ，使得

$$y = \phi_ {t _ {1}} ^ {X _ {1}} \dots \phi_ {t _ {m}} ^ {X _ {m}} (x _ {0}).$$

选择一序列 $\{s_k\} \subset (0, t_m)$ 使得

$$\lim _ {k \rightarrow \infty} s _ {k} = 0.$$

利用定理8.1.2, 对每个 $s_k$ 我们可找到一个内点 $x_k \in R(x_0, s_k)$ . 令

$$t ^ {k} = \left(t _ {1}, \dots , t _ {m - 1}, t _ {m} - s _ {k}\right),$$

然后我们可构造一序列 $\{y_k\} \subset M$ 使得

$$y _ {k} = \phi_ {t _ {1}} ^ {X _ {1}} \dots \phi_ {t _ {m} - s _ {k}} ^ {X _ {m}} (x _ {k}) := e (t ^ {k}, x _ {k}) \in R (x _ {0}, T).$$

由于 $x_{k}$ 是 $R(x_0,s_k)$ 的内点，且 $z\mapsto \varphi (t^k,z)$ 是一个微分同胚，故 $y_{k}$ 是 $R(x_0,T)$ 的一个内点．令 $k\to \infty$ ，则 $t^k\rightarrow t$ 于是由连续性可知

$$\lim _ {k \rightarrow \infty} y _ {k} = y.$$

几种能控性的关系可小结如下：

(1) 能控性秩条件 (在 $x_0$ 点) $\Longrightarrow$ 弱能控 (在 $x_0$ 点);  
(2) 弱能控 $\Longrightarrow$ 能控性秩条件在一开稠集上成立;  
(3) 弱能控 + 解析 $\Longrightarrow$ 能控性秩条件;  
(4) 能控性秩条件 (在 $x_0$ 点) $\Longrightarrow$ 能接近 (在 $x_0$ 点);  
(5) 能接近 (在 $x_0$ 点) + 解析 $\Longrightarrow$ 能控性秩条件 (在 $x_0$ 点);  
(6) 强能控秩条件 (在 $x_0$ 点) $\Longrightarrow$ 强能接近 (在 $x_0$ 点);  
(7) 强能接近 (在 $x_0$ 点) + 解析 $\Longrightarrow$ 强能控秩条件 (在 $x_0$ 点).

定义8.1.7 给定一个向量场 $X$ 。一个分布 $\mathcal{D}$ 称为 $X$ 不变的，如果

$$\operatorname{ad} _ {X} Y \in \mathcal {D}, \quad \forall Y \in \mathcal {D},$$

类似，一个Lie代数 $L$ 称为 $X$ 不变的，如果

$$\operatorname{ad} _ {X} Y \in L, \quad \forall Y \in L.$$

给定两个向量场集合 $F$ 和 $G$ , 包含 $G$ 且 $F$ 不变的最小分布记作 $\langle F|G\rangle$ . 最小的包含 $G$ 且 $F$ 不变的对合分布记作 $[F|G]$ . 当一个 Lie 代数被当作分布时我们使用相同的记号. 事实上, 当我们讨论能控或强能控 Lie 代数的维数时, 它们均被当作分布.

下面讨论仿射非线性系统 (8.1.2). 依定义有

命题 8.1.6 对仿射非线性系统 (8.1.2), 能控 Lie 代数是由 $\{f, g_{1}, \cdots, g_{m}\}$ 生成的 Lie 代数, 即

$$\mathcal {F} = \{f, g _ {1}, \dots , g _ {m} \} _ {L A}.$$

强能控 Lie 代数是包含 $\{g_{1},\cdots,g_{m}\}$ 且 f 不变的最小 Lie 代数，即

$$\mathcal {F} _ {0} = [ f \mid g _ {1}, \dots , g _ {m} ].$$
