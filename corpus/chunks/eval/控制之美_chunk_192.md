# 10.2.3 系统能控性的举例与分析

10.2.2节介绍了系统能控性的定义和判据，下面请看两个例子。

例10.2.1 判断系统 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = Az(t) + Bu(t)$ 的能控性，其中， $A = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix}, B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ 。

解：这是一个二维系统， $n = 2$ 。根据式(10.2.3)，可得 $\mathbf{C}_{\mathrm{o}} = [\mathbf{B}\quad \mathbf{A}\mathbf{B}] = \begin{bmatrix} 1 & 2\\ 1 & 2 \end{bmatrix}$ $\operatorname {Rank}(\mathbf{C}_{\mathrm{o}}) = 1\neq 2$ ，所以系统不能控。

例 10.2.2 判断式(10.2.1)系统(即单个小车移动) $\frac{\mathrm{d}z(t)}{\mathrm{d}t}=Az(t)+Bu(t)$ 的能控性, 其中, $A=\begin{bmatrix}0&1\\0&0\end{bmatrix},B=\begin{bmatrix}0\\1\end{bmatrix}$ 。

解：这是一个二维系统， $n = 2$ 。根据式(10.2.3)，得到 $\mathbf{C}_{\mathrm{o}} = [\mathbf{B}\quad \mathbf{A}\mathbf{B}] = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ $\operatorname {Rank}(\mathbf{C}_{\mathrm{o}}) = 2$ ，所以系统能控。

需要说明的是,系统能控只可以保证系统从初始状态 $z(t_0)$ 转移到终端状态 $z(t_1)$ , 但不能保证其移动轨迹。例如在图10.2.2所示的相平面图中, 横轴为 $z_1(t)$ , 即小车的位移, 纵轴为 $z_2(t)$ , 即小车的速度。假设在初始状态 $z(t_0)$ 时, 位移 $z_1(t_0) > 0$ 且速度 $z_2(t_0) > 0$ 。这说明此时小车在原点的右边并且向右行驶。如果终端状态在 $z(t_1)$ , 即位移 $z_1(t_1) < 0$ 且速度 $z_2(t_1) > 0$ , 这说明它在原点的左边且向右行驶。在外力(输入 $u(t)$ )的作用下, 从初始状态 $z(t_0)$ 到 $z(t_1)$ 的移动是无法通过图中的轨迹1实现的。相反, 它首先要经历一个先向右减速再加速向左的过程, 这样才可以向左移动。之后, 它需要向左减速, 最后向右加速, 才可以保证达到终端状态, 即图中轨迹2所示。

例10.2.3 判断图10.2.1(b)的两辆小车相连系统的能控性。其中, 小车质量为 $m_{1} = m_{2} = 1 \mathrm{~kg}$ , 弹簧的弹性系数为 $k = 100 \mathrm{~N} / \mathrm{m}$ , 输入 $u(t) = F(t)$ , 状态变量 $z(t) = [z_{1}(t), z_{2}(t), z_{3}(t), z_{4}(t)]^{\mathrm{T}} = \left[x_{1}(t), \frac{\mathrm{d} x_{1}(t)}{\mathrm{d} t}, x_{2}(t), \frac{\mathrm{d} x_{2}(t)}{\mathrm{d} t}\right]^{\mathrm{T}}$ 。

解：首先分析两个小车的受力情况，如图10.2.3所示。

根据牛顿第二定律,可得

$$
m _ {1} \frac {\mathrm{d} ^ {2} x _ {1} (t)}{\mathrm{d} t ^ {2}} = F (t) - k \left(x _ {1} (t) - x _ {2} (t)\right) \tag {10.2.4a}
$$

$$
m _ {2} \frac {\mathrm{d} ^ {2} x _ {2} (t)}{\mathrm{d} t ^ {2}} = k (x _ {1} (t) - x _ {2} (t)) \tag {10.2.4b}
$$

![](image/de9ed310fb885cba81f3832edc1455ec1b33b807cdf525e535b037745ce16193.jpg)

<details>
<summary>text_image</summary>

z(t₁)
z₁(t₁)<0
z₂(t₁)>0
轨迹1
z(t₀)
z₁(t₀)>0
z₂(t₀)>0
轨迹2
z₂(t)
z₁(t)
O
z₁(t)
</details>

图 10.2.2 能控性轨迹说明

![](image/2c1e1de48e02ec8cbbbe7c400c3fe7c2a1b8270925838d1244b3d3b973e4e36c.jpg)

<details>
<summary>text_image</summary>

x₂(t)
m₂
k(x₁(t)-x₂(t))
</details>
