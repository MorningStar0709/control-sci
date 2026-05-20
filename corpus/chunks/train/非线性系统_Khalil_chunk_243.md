二次函数 $V(x) = x^{\mathrm{T}}Px$ 是系统在原点某邻域内的李雅普诺夫函数。由于我们的目的是估算吸引区，所以必须在原点附近确定一个定义域，在其内 $\dot{V}(x)$ 是负定的，并确定常数 $c > 0$ ，使得 $\Omega_{c} = \{V(x)\leqslant c\}$ 是 $D$ 的一个子集。我们对所确定集合中最大的 $\Omega_{c}$ 感兴趣，即常数 $c$ 的最大值。注意，我们不必考虑检测在 $D$ 内 $V(x)$ 的正定性，因为 $V(x)$ 对于所有 $x$ 均是正定的，且是径向无界的，因此对于任意 $c > 0,\Omega_c$ 是有界的。 $V(x)$ 沿系统轨线的导数为

$$\dot {V} (x) = - (x _ {1} ^ {2} + x _ {2} ^ {2}) - (x _ {1} ^ {3} x _ {2} - 2 x _ {1} ^ {2} x _ {2} ^ {2})$$

$\dot{V}(x)$ 的右边可写为两项之和。第一项 $-\| x \|_2^2$ 为线性化部分 $Ax$ 作用的结果，而第二项为非线性部分 $g(x) = f(x) - Ax$ 作用的结果。因为

$$\frac {\| g (x) \| _ {2}}{\| x \| _ {2}} \to 0 \quad \text {当} \| x \| _ {2} \to 0$$

可知存在一个开球 $D = \{x\in R^2\mid \| x\| _2 < r\}$ ，使 $\dot{V} (x)$ 在 $D$ 内是负定的。一旦我们找到这样一个球，通过选择

$$c < \min _ {\| x \| _ {2} = r} V (x) = \lambda_ {\min} (P) r ^ {2}$$

即可确定 $\Omega_{c} \subset D$ 。这样, 为了扩大吸引区的估计值, 需要找到一个最大的开球, 在其内 $\dot{V}(x)$ 是负定的。我们有

$$\dot {V} (x) \leqslant - \| x \| _ {2} ^ {2} + | x _ {1} | | x _ {1} x _ {2} | | x _ {1} - 2 x _ {2} | \leqslant - \| x \| _ {2} ^ {2} + \frac {\sqrt {5}}{2} \| x \| _ {2} ^ {4}$$

其中用到 $|x_1| \leqslant \| x \|_2, |x_1x_2| \leqslant \| x \|_2^2 / 2$ 和 $|x_1 - 2x_2| \leqslant \sqrt{5} \| x \|_2$ 。这样 $\dot{V}(x)$ 在由$r^{2}=2/\sqrt{5}=0.8944$ 给出半径的球D上是负定的。在这个二阶系统例子中，可以通过在极坐标系中寻找球D求出不太保守的 $\Omega_{c}$ 的估计值。取

$$x _ {1} = \rho \cos \theta , x _ {2} = \rho \sin \theta$$

得 $\dot{V} = -\rho^{2} + \rho^{4}\cos^{2}\theta \sin \theta (2\sin \theta -\cos \theta)$

$$\leqslant - \rho^ {2} + \rho^ {4} | \cos^ {2} \theta \sin \theta | \cdot | 2 \sin \theta - \cos \theta |\leqslant - \rho^ {2} + \rho^ {4} \times 0. 3 8 4 9 \times 2. 2 3 6 1\leqslant - \rho^ {2} + 0. 8 6 1 \rho^ {4} < 0, \text {当} \rho^ {2} < \frac {1}{0 . 8 6 1}$$

利用上面的方程及 $\lambda_{\min}(P) \geqslant 0.69$ ，选取

$$c = 0. 8 < \frac {0 . 6 9}{0 . 8 6 1} = 0. 8 0 1$$

则当 c=0.8 时的集合 $\Omega_{c}$ 为吸引区的一个估计。逐渐增大 c，直到确定出使 $V(x)=c$ 在 $\{\dot{V}(x)<0\}$ 内的最大 c 值，画出 $\dot{V}(x)=0$ 和 $V(x)=c$ 的周线，可得到不太保守（即更大）的估计区域，如图 8.4(a) 所示，其中确定了 c=2.25。图 8.4(b) 是该估计区域与边界为极限环的吸引区的比较。

![](image/fa25e9af6618fb12236f1a6aae7aa955bd534ab6224759a3ae7c74e94f19788d.jpg)

<details>
<summary>text_image</summary>

x₂
x₁
</details>

(a)

![](image/f170eacdf6696a9a01bb088495e11079c12280e9ddacdca8bf6251bfadc8f998.jpg)

<details>
<summary>contour</summary>

| x1 | x2 |
| --- | --- |
| -2 | 0 |
| 0 | 2 |
| 2 | 0 |
| -2 | -2 |
| 0 | -1 |
| 2 | 1 |
</details>

(b)   
图 8.4 (a) 例 8.9 的周线 $\dot{V}(x)=0$ (长划线), $V(x)=0.8$ (点划线), $V(x)=2.25$ (实线); (b) 吸引区与其估计值的比较
