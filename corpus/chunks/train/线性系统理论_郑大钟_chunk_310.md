# 8.5 传递函数矩阵的零空间

传递函数矩阵的结构特性的另一表征就是它的奇异性。在直观上，这种奇异性表现为传递函数矩阵的非方和非满秩。但是，采用零空间的概念，将可对传递函数矩阵的奇异性进行更深刻的描述。

零空间 给定 $q \times p$ 的传递函数矩阵 $G(s)$ ，设 $G(s)$ 是非方的且为非满秩，则一定存在非零的 $p \times 1$ 和 $1 \times q$ 的有理分式向量 $f(s)$ 和 $h(s)$ ，使成立

$$G (s) \boldsymbol {f} (s) = 0 \tag {8.69}$$

和

$$\boldsymbol {h} (s) G (s) = \mathbf {0} \tag {8.70}$$

由此， $G(s)$ 的右零空间就定义为由满足(8.69)的所有非零向量 $\pmb{f}(s)$ 在有理分式域上构成的一个向量空间，表之为

$$\mathcal {Q} _ {r} = \{f (s) | f (s) \in \mathscr {R} ^ {p \times 1} (s), G (s) f (s) = 0 \} \tag {8.71}$$

而满足(8.70)的所有非零向量 $h(s)$ 的集合在有理分式域上构成的向量空间，则称之为 $G(s)$ 的左零空间，表示为

$$\mathcal {Q} _ {1} = \left\{\boldsymbol {h} (s) \mid \boldsymbol {h} (s) \in \mathcal {R} ^ {1 \times q} (s), \boldsymbol {h} (s) G (s) = 0 \right\} \tag {8.72}$$

零空间的基本属性 从零空间的定义出发,不难导出如下的一些推论。

(1) 令 $\operatorname{rank} G(s) = r, 0 \leqslant r \leqslant \min\{p, q\}$ ，则 $G(s)$ 的零空间的维数满足下列关系式：

$$\dim (\Omega_ {r}) = p - r \tag {8.73}\dim (\Omega_ {1}) = q - r \tag {8.74}$$

(2) $G(s)$ 的右零空间 $\Omega$ ，上的任一向量 $f(s)$ 都正交于 $G(s)$ 的所有行有理分式向量， $G(s)$ 的左零空间 $\Omega$ ，上的任一向量 $h(s)$ 都正交于 $G(s)$ 的所有列有理分式向量。

(3) 如果 $q \times p$ 的传递函数矩阵 $G(s)$ 为列满秩，即 $\operatorname{rank} G(s) = p$ ，则 $G(s)$ 的右零空间 $\Omega_r$ 为空的，如果 $G(s)$ 为行满秩，即 $\operatorname{rank} G(s) = q$ ，则 $G(s)$ 的左零空间 $\Omega_t$ 为空的。

(4) $G(s)$ 的右零空间 $\Omega_{t}$ 和左零空间 $\Omega_{t}$ 同时为空的充分必要条件，是传递函数矩阵 $G(s)$ 为方的且为非奇异，即 $\operatorname{det} G(s) \neq 0$ 。

(5) $G(s)$ 的零空间上的向量, 一般为有理分式向量, 但其中也包含有多项式向量。
