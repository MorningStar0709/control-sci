由 $\Omega_{c} = \{V(x)\leqslant c\}$ 估计吸引区很简单，但通常也是保守的。根据LaSall定理(定理4.4)，如果可以证明 $\Omega$ 是正不变集，就可以研究任意紧集 $\Omega \subset D$ 。这就要求研究 $\Omega$ 边界处的向量场，以保证始于 $\Omega$ 的轨线不会离开其内，下面的例题将说明这一思想。

例8.10 考虑系统 $\dot{x}_1 = x_2$

$$\dot {x} _ {2} = - 4 \left(x _ {1} + x _ {2}\right) - h \left(x _ {1} + x _ {2}\right)$$

其中 $h: R \rightarrow R$ 是局部利普希茨函数, 满足

$$h (0) = 0; \quad u h (u) \geqslant 0, \forall | u | \leqslant 1$$

考虑以二次函数

$$
V (x) = x ^ {\mathrm{T}} \left[ \begin{array}{l l} 2 & 1 \\ 1 & 1 \end{array} \right] x = 2 x _ {1} ^ {2} + 2 x _ {1} x _ {2} + x _ {2} ^ {2}
$$

作为备选李雅普诺夫函数①,其导数 $\dot{V}(x)$ 为

$$
\begin{array}{l} \dot {V} (x) = \left(4 x _ {1} + 2 x _ {2}\right) \dot {x} _ {1} + 2 \left(x _ {1} + x _ {2}\right) \dot {x} _ {2} \\ = - 2 x _ {1} ^ {2} - 6 \left(x _ {1} + x _ {2}\right) ^ {2} - 2 \left(x _ {1} + x _ {2}\right) h \left(x _ {1} + x _ {2}\right) \\ \leqslant - 2 x _ {1} ^ {2} - 6 \left(x _ {1} + x _ {2}\right) ^ {2}, \forall | x _ {1} + x _ {2} | \leqslant 1 \\ = - x ^ {\mathrm{T}} \left[ \begin{array}{l l} 8 & 6 \\ 6 & 6 \end{array} \right] x \\ \end{array}
$$

因此 $\dot{V}(x)$ 在集合

$$G = \{x \in R ^ {2} \mid | x _ {1} + x _ {2} | \leqslant 1 \}$$

内是负定的,所以原点是渐近稳定的。为了估算 $R_{A}$ ，首先估算 $\Omega_{c}=\{V(x)\leqslant c\},\Omega_{c}\subset G$ 时c>0的最大值为

$$c = \min _ {| x _ {1} + x _ {2} | = 1} x ^ {\mathrm{T}} P x = \frac {1}{b ^ {\mathrm{T}} P ^ {- 1} b} = 1$$

其中 $b^{\mathrm{T}} = [11]$ 。因此当 $c = 1$ 时 $\Omega_{c}$ 是 $R_{A}$ 的估计区域（见图8.5）。在本例中不必局限于估计 $\Omega_{c}$ 即可得到更准确的 $R_{A}$ 的估计值，这一过程的关键是观察 $G$ 内的轨线不能通过边界 $|x_1 + x_2| = 1$ 的某一部分而离开，通过检测边界处的向量场可以看出这一点，也可以由下面的分析看出。设

![](image/403fe046277b60e763fa9d17f6c9a86f433781bdb60ba8d2a4744696c85f3403.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| -3 | 4 |
| 0 | 0 |
| 3 | -4 |
</details>

图8.5 例8.10吸引区的估计

$$\sigma = x _ {1} + x _ {2}$$

使 $G$ 的边界由 $\sigma = 1$ 和 $\sigma = -1$ 给出。 $\sigma^2$ 沿系统轨线的导数为

$$\frac {d}{d t} \sigma^ {2} = 2 \sigma (\dot {x} _ {1} + \dot {x} _ {2}) = 2 \sigma x _ {2} - 8 \sigma^ {2} - 2 \sigma h (\sigma) \leqslant 2 \sigma x _ {2} - 8 \sigma^ {2}, \forall | \sigma | \leqslant 1$$

在边界 $\sigma=1$ 上,有

$$\frac {d}{d t} \sigma^ {2} \leqslant 2 x _ {2} - 8 \leqslant 0, \forall x _ {2} \leqslant 4$$

这就是说,对于 $x_{2} \leqslant 4$ , 当轨线到达边界 $\sigma = 1$ 上任意一点时, 就不会移动到集合 G 之外, 因为在这些点上 $\sigma^{2}$ 是非增的。同样, 在边界 $\sigma = -1$ 上, 有

$$\frac {d}{d t} \sigma^ {2} \leqslant - 2 x _ {2} - 8 \leqslant 0, \forall x _ {2} \geqslant - 4$$
