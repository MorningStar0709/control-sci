性质 3. 微分方程 (2.5.1) 的非封闭的轨线 $L: x = x(t; x_0)$ 与任一无切线段 $\ell_u$ 之交点，在 $\ell_u$ 上的排列顺序和时间增加的顺序一致，即对轨线 $x = x(t; x_0)$ ，若把它与 $\ell_u$ 的交点 $x(t_k; x_0)$ 按 $t_k$ 增加顺序排列： $0 = t_0 < t_1 < t_2 < \cdots < t_k < t_{k+1} < \cdots$ ，并记 $P_k = x(t_k; x_0)$ ，则在线段 $\overline{P_k P_{k+1}}$ 上，轨线 $L$ 不再与 $\ell_u$ 相交。

事实上，如果在线段 $\overline{P_kP_{k + 1}}$ 上，轨线与 $\ell_u$ 还有交点，那么这个交点所对应的时刻 $\tilde{t}$ ，或者有 $\tilde{t} < t_k$ ，或者有 $\tilde{t} > t_{k + 1}$ 。但这都是不可能的。因为例如 $\tilde{t} > t_{k + 1}$ ，这时轨线 $L$ 自时刻 $t_{k + 1}$ 进入区域（由直线段 $\overline{P_kP_{k + 1}}$ 和对应于参数 $t \in [t_k, t_{k + 1}]$ 的轨线段 $L_{t_k t_{k + 1}}$ 围成）后，再也不能走出去。当然也就不会再与 $\overline{P_kP_{k + 2}}$ 相交。同样当 $\tilde{t} < t_k$ 时，轨线也不会再与 $\overline{P_kP_{k + 1}}$ 相交，如图2.5.3所示。

![](image/2e90b4c1084a4f07d7ab28dd55ee826d62cb4dec0d800109958fedf3edc79fd2.jpg)

<details>
<summary>text_image</summary>

l_u
P_k
P_{k+1}
L
</details>

图2.5.3

定理 2.5.1 $^{[12]}$ 假设 $f(x)$ 在区域 $\Omega_{2}$ 内连续可微. 对于 $\Omega_{2}$ 内的微分方程 (2.5.1) 的任一常点 $x_{0}$ , 总存在 $x_{0}$ 的一个领域 $K_{\varepsilon}(x_{0})$ 及定义在闭邻域 $\overline{K}_{\varepsilon}(x_{0})$ 上的拓扑变换 g, 使 $g(\overline{V}_{\varepsilon}(x_{0})) = \overline{R}, \overline{R}$ 为 $R^{2}$ 中一个闭长方形区域, 并且 g 把 $K_{\varepsilon}(x_{0})$ 上微分方程 (2.5.1) 的轨线变换为 $\overline{R}$ 中的平行直线.

此结论对 $n$ 维流形上的非零向量场都对，称为立方流，证明见文献[3].

与常点相比，奇点有更丰富的内容，这里将进一步讨论它.

研究如下形式的二阶非线微分方程：

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x + \bar {f} (x), \tag {2.5.2}$$

这里 $x \in \mathbb{R}^2$ ; $A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \frac{\partial f}{\partial x}(0)$ 为 $2 \times 2$ 常值矩阵, $\bar{f}(x)$ 为连续可微函数,且 $\bar{f}(x) = o(|x|)$ .

定义2.5.4 称 $x = 0$ 为微分方程(2.5.1)的一次奇点，如果 $\operatorname{det} A \neq 0$ ；称 $x = 0$ 为微分方程(2.5.1)的高次奇点，如果 $\operatorname{det} A = 0$ ，且 $x = 0$ 是微分方程(2.5.1)的孤立奇点。

首先给出线性齐次微分方程的一次奇点及其分类. 相应于非线性微分方程 (2.5.1) 的一次近似微分方程为

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x \tag {2.5.3}$$

易知，当 $\operatorname{det} A \neq 0$ 时， $x = 0$ 是其唯一的奇点.

记 $\pmb{A}$ 的Jordan标准型为 $A = SAS^{-1}$ , $\pmb{S}$ 为可逆方阵. 设 $y = Sx$ , 则有

$$\frac {\mathrm{d} y}{\mathrm{d} t} = \Lambda y. \tag {2.5.4}$$

(1) $\pmb{A} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$ , $\lambda_1, \lambda_2$ 为 $\pmb{A}$ 的两个互不相同的实特征值.

当 $\lambda_1, \lambda_2$ 同为负，不妨认为 $\lambda_1 < \lambda_2 < 0$ 时，式(2.5.4)的解为
