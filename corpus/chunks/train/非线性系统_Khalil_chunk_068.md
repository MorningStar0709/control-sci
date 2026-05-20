$$
A = \left. \frac {\partial f}{\partial x} \right| _ {x = 0} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - \varepsilon h ^ {\prime} (0) \end{array} \right]
$$

由于 $h'(0) < 0$ ，其特征值实部为正。这样，根据 Poincaré-Bendixson 准则可知在 M 内有一个闭轨道。

![](image/d41d8203334547013bb3ef605918424794abfeb044adedcf83f4a3c6102f2837.jpg)

<details>
<summary>text_image</summary>

δ(p)
r
p
</details>

图2.25 例2.9中函数 $\delta (p)$ 的图形

![](image/b0400f5148cfd6c781d86efb28251fe2337be287a5c5f7ebfaff529d57ac2da1.jpg)

<details>
<summary>text_image</summary>

x₂
A
B
C
x₁
D
E
</details>

图2.26 例2.9中形成的闭合曲线

用同样的方法可以超越 Poincaré-Bendixson 准则, 证明该闭合轨道是唯一的。注意, 由于前面讲到的对称性, 当且仅当 $\alpha(p) = p$ 时, 系统可能有一个闭轨道。由图 2.25 可见, 仅有一个 $p$ 值满足此条件, 因此只有一个闭轨道。进一步可以证明每个非平衡点的解以螺线形式趋向唯一的闭轨道。为说明这一点, 设 $p_0 > 0$ 是唯一满足 $\alpha(p) = p$ 的 $p$ 值, 考虑 $x_2$ 轴上的一点 $(0, p), p > p_0$ 。如前所述, 通过点 $(0, p)$ 的轨线与 $x_2$ 轴下半部分在点 $(0, -\alpha(p))$ 相交, 这里 $\alpha(p) < p$ 。由于对称性, 通过点 $(0, -\alpha(p))$ 的轨线将与 $x_2$ 上半轴的点 $(0, \sigma(p))$ 相交, $p_0 \leqslant \sigma(p) < p$ 。上界可由对称性得出, 而下界由于 $\sigma(p)$ 小于 $p_0$ , 所以轨线一定与闭轨道相交。映射 $p \to \sigma(p)$ 是连续的, 由初始状态解的连续性决定①。再次从 $(0, \sigma(p))$ 开始, 轨线在点 $(0, \sigma^2(p))$ 回到 $x_2$ 的上半轴, 这里 $p_0 \leqslant \sigma^2(p) < \sigma(p)$ 。由归纳法可生成一个序列 $\sigma^n(p)$ , 满足

$$p _ {0} \leqslant \sigma^ {n + 1} (p) < \sigma^ {n} (p), n = 1, 2, \dots$$

序列 $\sigma^{n}(p)$ 有一个极限为 $p_{1}\geqslant p_{0}$ 。注意，根据 $\sigma(\cdot)$ 的连续性，极限 $p_{1}$ 应满足

$$\sigma (p _ {1}) - p _ {1} = \lim _ {n \to \infty} \sigma (\sigma^ {n} (p)) - p _ {1} = p _ {1} - p _ {1} = 0$$

根据闭轨道的唯一性,一定有 $p_{1}=p_{0}$ 。这就证明了当 t 趋于无穷时,p 的轨线以螺线形式趋于唯一的闭轨道。当 $p<p_{0}$ 时也成立。

下一个结果称为 Bendixson 准则,可用于某些排除存在周期轨道的情况。

引理 2.2 (Bendixson 准则) 如果在平面上的简单连通区域 $^{②}$ D 内, 表达式 $\partial f_{1}/\partial x_{1} + \partial f_{2}/\partial x_{2}$ 不总是为零, 且符号不变, 那么系统(2.7) 在 D 内没有周期闭轨道。

证明:在系统(2.7)的任何轨道上有 $dx_{2}/dx_{1}=f_{2}/f_{1}$ ，因此在任何闭轨道 $\gamma$ 上有

$$\int_ {\gamma} f _ {2} (x _ {1}, x _ {2}) d x _ {1} - f _ {1} (x _ {1}, x _ {2}) d x _ {2} = 0$$

这就是说,与格林(Green)定理

$$\int \int_ {S} \left(\frac {\partial f _ {1}}{\partial x _ {1}} + \frac {\partial f _ {2}}{\partial x _ {2}}\right) d x _ {1} d x _ {2} = 0$$

比较， $S$ 在 $\gamma$ 内。如果在 $D$ 上 $\partial f_1 / \partial x_1 + \partial f_2 / \partial x_2 > 0$ （或 $< 0$ ），那么就不能找到一个区域 $S \subset D$ 使后面的等式成立，也就是在 $D$ 内不存在一个完整的闭轨道。

例2.10 考虑系统
