$$0 = \mathrm{e} ^ {\boldsymbol {A} t _ {1}} x _ {0} + \int_ {t _ {0}} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} (t _ {1} - \tau)} \boldsymbol {B} u (\tau) \mathrm{d} \tau . \tag {1.3.5}$$

由命题1.2.1知，存在连续函数 $\alpha_{k}(t)$ ，使得

$$\mathrm{e} ^ {- A \tau} = \sum_ {k = 0} ^ {n - 1} \alpha_ {k} (\tau) A ^ {k}.$$

将它代入式 (1.3.5) 并记 $z_{k} = -\int_{0}^{t_{1}} \alpha_{k}(\tau) u(\tau) \mathrm{d}\tau$ ，则得

$$\pmb {x} _ {0} = - \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {t _ {1}} \alpha_ {k} (\tau) \pmb {A} ^ {k} \pmb {B} u (\tau) \mathrm{d} \tau = \sum_ {k = 0} ^ {n - 1} \pmb {A} ^ {k} \pmb {B} z _ {k}, \tag {1.3.6}$$

或者

$$
\boldsymbol {x} _ {0} = \boldsymbol {Q} _ {c} \left[ \begin{array}{c} z _ {0} \\ z _ {1} \\ \vdots \\ z _ {n - 1} \end{array} \right]. \tag {1.3.7}
$$

这说明代数方程 (1.3.7) 对任意的 $x_0$ 都有解，因此必有 $\operatorname{rank} Q_c = n$ .

推论 1.3.1 已知定常线性系统 $(A, B)$ . 如果 A 的最小多项式是 k 次的, $k \leqslant n$ , 那么系统 $(A, B)$ 能控的充要条件是

$$\operatorname{rank} [ B, A B, \dots , A ^ {k - 1} B ] = n.$$

推论1.3.2 设定常线性系统 $(A, B)$ 是单输入的，那么它能控的充要条件是

$$\det Q _ {c} \neq 0.$$

定理1.3.3 定常线性系统 $(A, B)$ 能控的充要条件是，对每个 $s \in \sigma(A)$ 都有

$$\operatorname{rank} [ \boldsymbol {A} - s \boldsymbol {I} _ {n}, \quad \boldsymbol {B} ] = n \tag {1.3.8}$$

其中 $\sigma(A)$ 表示 A 的特征值集合.

证明 必要性. 设系统 $(A, B)$ 能控. 若对某 $s_0 \in \sigma(A)$ 有

$$\operatorname{rank} [ \boldsymbol {A} - s _ {0} \boldsymbol {I} _ {n}, \quad \boldsymbol {B} ] < n,$$

则必有非零向量 $z$ （它可能是复的），使得 $z^{\mathrm{T}}[A - s_0I_n,B] = 0$ 。于是有 $z^{\mathrm{T}}(A - s_0I_n) = 0$ 和 $z^{\mathrm{T}}B = 0$ 。这说明 $z^{\mathrm{T}}$ 是 $\pmb{A}$ 的对应于特征值 $s_0$ 的右特征向量，它与矩阵 $\pmb{B}$ 的每个列向量直交，从而有

$$\boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {A} ^ {k} \boldsymbol {B} = 0, \quad k = 0, 1, \dots , n - 1. \tag {1.3.9}$$

于是 $z^{\mathrm{T}}Q_{c} = 0$ 。因为 $z^{\mathrm{T}} \neq 0$ ，所以 $\operatorname{rank} Q_{c} < n$ 。而这与系统 $(A, B)$ 能控矛盾。这个矛盾表明式 (1.3.8) 对一切 $s \in \sigma(A)$ 成立。

充分性．假设式(1.3.8)成立，而系统 $(A,B)$ 不能控，那么必存在非零向量 $z$ 使得 $z^{\mathrm{T}}Q_{c} = 0$ ，即

$$\boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {A} ^ {k} \boldsymbol {B} = 0, \quad k = 0, 1, \dots , n - 1. \tag {1.3.10}$$

显然， $z^{\mathrm{T}}A^{k}(k=0,1,\cdots,n-1)$ 都是B的左零空间的元。于是可以断定，存在一个最小的整数 $k,0\leqslant k<n-1$ ，使得向量 $z^{\mathrm{T}},z^{\mathrm{T}}A,\cdots,z^{\mathrm{T}}A^{k}$ 行线性独立。这时有不全为零的实常数 $\alpha_{0},\alpha_{1},\cdots,\alpha_{k-1}$ ，使得
