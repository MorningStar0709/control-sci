定义3.5.4 设 $M, N$ 为两个微分流形. $\pi: M \to N$ 为一个同胚. 如果 $\pi$ 及 $\pi^{-1}$ 均为 $C^r (C^\infty, C^\omega)$ , 那么 $M, N$ 称为 $C^r$ (相应地称为 $C^\infty$ , 或 $C^\omega$ ) 微分同胚, $\pi$ 称为一个 $C^r$ (相应地 $C^\infty$ , 或 $C^\omega$ ) 微分同胚映射.

设 $x \in M$ 。如果存在一个邻域 $U \ni x$ 及邻域 $V \in y = \pi(x)$ 使得 $\pi: U \to V$ 为一微分同胚，则 $M$ 和 $N$ 称为在 $x$ 点局部微分同胚，而 $\pi$ 则称为局部微分同胚映射。

例3.5.3 考虑一个开圆盘

$$D = \{(x, y) \in \mathbb {R} ^ {2} \mid x ^ {2} + y ^ {2} < r \}$$

和一个椭圆盘

$$E = \left\{(x, y) \in \mathbb {R} ^ {2} \mid \frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} < r ^ {2} \right\},$$

它们是 $C^\omega$ 微分同胚的．一个微分同胚映射 $F:D\to E,$ 可定义如下：

$$F _ {1} (x, y) = (a / r) x, \quad F _ {2} (x, y) = (b / r) y.$$

同一个映射也可当作边界到边界的映射，即 $F: \partial D \to \partial E$ 。于是可知圆周与椭圆周也是解析微分同胚的。

$\mathbb{R}$ 不可能与 $\partial D$ 微分同胚，因为微分同胚是一个同胚，但 $\mathbb{R}$ 与 $\partial D$ 不可能同胚，因为它们有不同的基本群。（ $\partial D$ 的基本群是 $Z$ ，而 $\mathbb{R}$ 的基本群是 $\{e\}$ .）

它们可以局部微分同胚. 事实上, $\mathbb{R}$ 是 $\partial D$ 的复叠空间.

定义3.5.5 设 $M, N$ 为两个微分流形， $\dim(M) = m \geqslant n = \dim(N)$ 且 $F: N \to M$ 是一个一对一的光滑映射。那么 $F: N \to \tilde{N} = F(N)$ 给出 $N$ 和 $\tilde{N}$ 之间的一个一一对应。

(1) 当 $\widetilde{N}$ 带有 $N$ 的拓扑时它称为 $M$ 的一个嵌入子流形；  
(2) 如果 $\tilde{N}$ 是一个嵌入子流形，并且当 $\tilde{N}$ 带有作为 $M$ 的子空间的诱导拓扑时， $F: N \to \tilde{N}$ 是一个同胚，则 $\tilde{N}$ 称为浸入子流形；  
(3) 如果 $H \subset M$ 且对每一点 $p \in H$ 存在一个局部坐标卡 $(U, \phi)$ 使得

$$
\left\{ \begin{array}{l} {\phi (p) = 0,} \\ {\phi (U) = \{x \in \mathbb {R} ^ {n} \mid | x _ {i} | <   \varepsilon \},} \\ {\phi (N \cap U) = \{x \in \phi (U), \mid x _ {n + 1} = \dots = x _ {m} = 0 \},} \end{array} \right. \tag {3.5.3}
$$

那么 $N$ 称为 $M$ 的一个正规子流形. 坐标系 (3.5.3) 称为 $N$ 的平整坐标.

例3.5.4 (1) 考虑一个映射 $F: \mathbb{R} \to \mathbb{R}^2$ 定义为

$$F (t) = \left(2 \cos \left(t - \frac {\pi}{2}\right), \sin \left(2 \left(t - \frac {\pi}{2}\right)\right)\right).$$

$F$ 的象是一个“8”字． $F$ 是嵌入，因为 $\operatorname {rank}(F) = 1$ .但 $F$ 不是一对一的.事实上，当 $t$ 走过 $2\pi ,F(t)$ 走出一个“8”字．因此其象不是一个嵌入子流形.（图3.5.2(a))

![](image/bd4c172de8a2f5c22d9243df3acb044c78c8359f0ab08052710af8e5a8de017f.jpg)

<details>
<summary>text_image</summary>

y
1 x
</details>

(a)

![](image/35167b7fb7c739c61c36eabe87e557b539418c8a3ae16409a16f0b0cd2adbc20.jpg)

<details>
<summary>text_image</summary>

y
1 x
</details>

(b)   
图 3.5.2 嵌入，浸入子流形

(2) 设 $g(\cdot): \mathbb{R} \to (-\pi, \pi)$ 定义为 $g(t) = 2\arctan(t)$ . 定义 $F: \mathbb{R} \to \mathbb{R}^2$ 为
