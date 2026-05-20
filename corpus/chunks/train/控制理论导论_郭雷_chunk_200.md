# 习题 3.1

3.1.1 验证例 3.1.5 中的断言.

3.1.2 一个线性系统由三个元素 $(A, B, C)$ 确定。这里 $A \in M_n, B \in M_{n \times m}, C \in M_{p \times n}$ 。设 $T: z \mapsto Tz = x$ 为 $\mathbb{R}^n$ 上的一个线性变换，

(a) 证明经 $\pmb{T}$ 变换，系统参数在 $z$ 坐标下变为

$$\tilde {\boldsymbol {A}} = \boldsymbol {T} ^ {- 1} \boldsymbol {A} \boldsymbol {T}, \quad \tilde {\boldsymbol {B}} = \boldsymbol {T} ^ {- 1} \boldsymbol {B}, \quad \tilde {\boldsymbol {C}} = \boldsymbol {C} \boldsymbol {T};$$

(b) 证明满足上述条件的变换构成一个群.

3.1.3 记常微分方程

$$\dot {x} = f (x), \quad x \in \mathbb {R} ^ {n}$$

的解为 $e_t^f (x_0)$ .设其对所有的 $t\in \mathbb{R}$ 均成立.

(a) 说明解是一个群. 称为单参数群;

(b) 定义 $\pi : t \mapsto e_t^f(x_0)$ . 证明 $\pi : (\mathbb{R}, +) \to \{e_t^f(x_0) \mid t \in \mathbb{R}\}$ 是一个同构.

3.1.4 如果对群的每一个元素 $g \in G$ 都有 $g^2 = e$ . 则 $G$ 为 Abel 群.

3.1.5 设 $V$ 为 $\mathbb{R}^n$ 的一个子空间. $\operatorname{GL}(n, \mathbb{R})$ 是线性变换集. $A \in \operatorname{GL}(n, \mathbb{R})$ 称为 $V$ 不变的, 如果 $AV \subset V$ . 证明 $V$ 不变的线性变换集是 $\operatorname{GL}(n, \mathbb{R})$ 的子群.

3.1.6 设 $G$ 为一有限群，大小（元素个数）为 $|G|$ . 子群 $H < G$ . 证明 $|H|$ 是 $|G|$ 的因子.

3.1.7 (a) 至少找出两个 $\phi : (\mathbb{Z}_1, +) \to (\mathbb{Z}_n, +)$ 的同态；

(b) 设 $r, p, q$ 为正整数，且 $r = pq$ 。定义映射 $\phi: (\mathbb{Z}_r, +) \to (\mathbb{Z}_p, +)$ 为 $\phi(z) = z (\bmod p)$ 。证明 $\phi$ 是一个同态。找出商群： $(\mathbb{Z}_r, +)/( \mathbb{Z}_p, +)$ 。

3.1.8 刚体运动可由一个转动 $S \in \mathrm{SO}(3, \mathbb{R})$ ，和一个平动 $x \in \mathbb{R}^3$ 来描述。在运动集 $\{(S, x)\}$ 上定义一个算子来表示运动的复合。证明它使 $\{(S, x)\}$ 成为一个群。这里 $\mathrm{SO}(3, \mathbb{R}) < \mathrm{GL}(3, \mathbb{R})$ 是特殊正交群，定义为

$$\mathrm{SO} (3, \mathbb {R}) = \{\pmb {A} \in \mathrm{GL} (3, \mathbb {R}) | \det (\pmb {A}) = 1, \text {且} \pmb {A} ^ {\mathrm{T}} \pmb {A} = \pmb {I} _ {3} \}.$$

3.1.9 令 $S_{n}$ 为 $G_{n} = \{1,2,\dots ,n\}$ 上的对称群．指出任一元素 $\sigma \in S_n$ 可表示为相邻对换 $(k,k + 1)$ 的乘积.

3.1.10 证明行列式 $\operatorname{det} : \mathrm{GL}(n, \mathbb{R}) \to (\mathbb{R} \setminus \{0\}, \times)$ 是一个同态。找出它的同态核，证明

$$\operatorname{GL} (n, \mathbb {R}) / \ker (\det) \cong (\mathbb {R} \backslash \{0 \}, \times).$$
