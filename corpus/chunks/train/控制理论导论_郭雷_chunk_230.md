# 3.5 微分流形

微分流形是非线性控制系统几何理论的基础.

定义3.5.1 设 $(M, T)$ 为一个第二可数的， $T_{2}$ (Hausdorff) 型拓扑空间。 $M$ 称为一个 $n$ 维拓扑流形，如果存在一个子集族 $A = \{A_{\lambda} \mid \lambda \in \Lambda\} \subset T$ ，使得

M1. $\cup_{\lambda \in \Lambda}A_{\lambda}\supset M;$

M2. 对任何 $U \in A$ 存在一个同胚 $\phi: U \to \phi(U) \subset \mathbb{R}^n$ , 称为坐标卡, 记作 $(U, \phi)$ , 这里 $\phi(U)$ 为 $\mathbb{R}^n$ 的开集.

如果还有以下条件：

M3. 对两个坐标卡 $(U, \phi)$ 和 $(V, \psi)$ , 如果 $U_1 \cap U_2$ 非空, 那么 $\psi \circ \phi^{-1}: \phi(U \cap V) \to \psi(U \cap V)$ 及 $\phi \circ \psi^{-1}: \psi(U \cap V) \to \phi(U \cap V)$ 两者均为 $C^r (C^\infty, C^\omega)$ 映射. 这样的两个坐标称为相容坐标卡.

M4. 如果一个坐标卡 $W$ 与 $A$ 中所有坐标卡均相容，则 $W \in A$ .

那么 $(M, T)$ 称为一个 $C^r$ (相应地，称为 $C^\infty$ , 解析) 微分流形 (图3.5.1).

注3.5.1 事实上，M1\~M3已足够确定一个微分流形。条件M4是为了某些叙述和使用上的方便。

![](image/9c9d5d403ac2bb59a7c53aa08e9e7ec20040b203b106099c7a2bd065b249f6ea.jpg)

<details>
<summary>text_image</summary>

R^n
φ
M
U
U ∩ V
V
ψ
ψ(V)
R^n
</details>

图3.5.1 微分流形

例3.5.1 (1) $\mathbb{R}^n$ 的任何一个非空开子集均为一个 $n$ 维流形；

(2) $\mathbb{R}^2$ 中的图“8”，用极坐标可定义为

$$F = \{(r, \theta) | r = | \sin (\theta) |, 0 \leqslant \theta \leqslant 2 \pi \}.$$

这不是一个流形，因为在原点 $r = 0$ 附近它不能同胚于 $\mathbb{R}^1$ 的任一开集；

(3) $S^2$ 是一个2维解析流形. 为证明这一点可取6个坐标卡为 $(U_{x+},\pi_{x+})$ , $(U_{x-},\pi_{x-})$ , $(U_{y+},\pi_{y+})$ , $(U_{y-},\pi_{y-})$ , $(U_{z+},\pi_{z+})$ , $(U_{z-},\pi_{z-})$ , 这里

$$
U _ {x +} = \{(x, y, z) \in S ^ {2} \mid x > 0 \}, \qquad \pi_ {x +} = \left\{ \begin{array}{l l} Y = y, \\ Z = z. \end{array} \right.
$$

那么 $\pi_{x+}(U_{x+})$ 是 $\mathbb{R}^2$ 上的一个开圆盘. 显见 $\pi_{x+}$ 是一个同胚, 并且 $\pi$ 和 $\pi^{-1}$ 均解析.

另外5个坐标卡可类此定义．参考例3.3.31，另一组坐标卡可定义为

$$U _ {N} = S ^ {2} \backslash \{N \}, \quad U _ {S} = S ^ {2} \backslash \{S \}.$$

然后定义 $\phi_N: U_N \to \mathbb{R}^2$ 为

$$
\left\{ \begin{array}{l} X = x / (1 - z), \\ Y = y / (1 - z), \end{array} \right.
$$

及 $\phi_S: U_S \to \mathbb{R}^2$ 为

$$
\left\{ \begin{array}{l} X = x / (1 + z), \\ Y = y / (1 + z). \end{array} \right.
$$

因此 $\{(U_N, \phi_N), (U_S, \phi_S)\}$ 确定一个 $S^2$ 上的 $C^\omega$ 结构.

例 3.5.2(Grassman 流形) 考虑 $R^{n}$ 上 k 维子空间集合。我们设法为其加上一个解析结构。首先，设 $F(k,n)$ 为 k 维子空间基底集合，即 $X \in F$ 当且仅当 $X = \{x^{1}, \cdots, x^{k}\}$ ，这里

$$\boldsymbol {x} ^ {i} = \left[ x _ {1} ^ {i}, \dots , x _ {n} ^ {i} \right] ^ {\mathrm{T}}, \quad i = 1, \dots , k,$$

且 $x^{1}, \cdots, x^{k}$ 线性无关。为方便起见，我们将每个 $X$ 等同于一个 $k \times n$ 满秩矩阵。

显见如果取 $x_{j}^{i}, i = 1, \cdots, k, j = 1, \cdots, n$ 为坐标，则 $F(k, n)$ 可以看作 $R^{k \times n}$ 的一个开集.
