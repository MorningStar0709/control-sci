$$
\boldsymbol {K} (t) = \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] \tag {5-21}
$$

为简单起见，上式右端省略了自变量 $t$ 。把上面的 $\pmb{A},\pmb{B},\pmb{Q},\pmb{R}$ 和 $\pmb {K}(t)$ 代入黎卡提方程式(5-14)，可得

$$
\left[ \begin{array}{l l} \dot {k} _ {1 1} & \dot {k} _ {1 2} \\ \dot {k} _ {1 2} & \dot {k} _ {2 2} \end{array} \right] = - \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] +

\left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] [ 0 \quad 1 ] \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] - \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right]

= \left[ \begin{array}{c c} - 1 + k _ {1 2} ^ {2}, & - k _ {1 1} + k _ {1 2} k _ {2 2} \\ - k _ {1 1} + k _ {2 2} k _ {1 2}, & - 2 k _ {1 2} + k _ {2 2} ^ {2} \end{array} \right] \tag {5-22}
$$

令上式等号左右端的对应元相等,得

$$\dot {k} _ {1 1} = - 1 + k _ {1 2} ^ {2}\dot {k} _ {1 2} = - k _ {1 1} + k _ {1 2} k _ {2 2} \tag {5-23}\dot {k} _ {2 2} = - 2 k _ {1 2} + k _ {2 2} ^ {2}$$

这是一组非线性微分方程。由边界条件

$$\boldsymbol {K} (t _ {\mathrm{f}}) = \boldsymbol {P} = \mathbf {0} \tag {5-24}$$

得

$$k _ {1 1} \left(t _ {\mathrm{f}}\right) = k _ {1 2} \left(t _ {\mathrm{f}}\right) = k _ {2 2} \left(t _ {\mathrm{f}}\right) = 0 \tag {5-25}$$

由 $t_{\mathrm{f}}$ 到 $t_0$ 逆时间积分上面的非线性微分方程组，即可求得 $k_{11}(t)$ ， $k_{12}(t), k_{22}(t)$ 。于是最优控制为

$$
\begin{array}{l} u (t) = - \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} (t) \boldsymbol {X} (t) = - 1 \cdot [ 0 \quad 1 ] \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] \\ = - k _ {1 2} (t) x _ {1} (t) - k _ {2 2} (t) x _ {2} (t) \tag {5-26} \\ \end{array}
$$

$k_{12}(t)$ 、 $k_{22}(t)$ 、 $x_{1}(t)$ 、 $x_{2}(t)$ 和 $u(t)$ 随时间变化的曲线可求出，如图5-3(a)、(b)、(c)所示。

![](image/38bf7ae3a59e188e45afdde87e87489964250f72b129a71e49ad3b7841ebbba2.jpg)

<details>
<summary>line</summary>

| t | k₂₂(t) | k₁₂(t) |
| --- | --- | --- |
| √2 | 1 | 1 |
| t_f | 0 | 0 |
</details>

(a)

![](image/fd96be3af5d757ba23f739f6e5a641c5529a94decbabd1c38274387d7309e1cd.jpg)

<details>
<summary>text_image</summary>

1
x₁(t)
O
x₂(t)
t
t_f
</details>

(b)
