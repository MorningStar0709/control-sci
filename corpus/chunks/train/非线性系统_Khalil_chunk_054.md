# 第三种情况 多重非零特征值, ${\lambda }_{1} = {\lambda }_{2} = \lambda  \neq  0$

经坐标变换 $z = M^{-1}x$ ，系统(2.3)的形式转换为

$$\dot {z} _ {1} = \lambda z _ {1} + k z _ {2}, \quad \dot {z} _ {2} = \lambda z _ {2}$$

对于给定的初始状态 $(z_{10}, z_{20})$ ，其解由下式给出：

$$z _ {1} (t) = e ^ {\lambda t} \left(z _ {1 0} + k z _ {2 0} t\right), \quad z _ {2} (t) = e ^ {\lambda t} z _ {2 0}$$

消去 $t$ ，可得到轨线方程 $z_{1} = z_{2}\left[\frac{z_{10}}{z_{20}} +\frac{k}{\lambda}\ln \left(\frac{z_{2}}{z_{20}}\right)\right]$

图2.8所示为 $k = 0$ 时轨线的形式，图2.9为 $k = 1$ 时轨线的形式。其相图与只有一个结点的相图相似，因此当 $\lambda < 0$ 时，平衡点 $x = 0$ 称为稳定结点；当 $\lambda > 0$ 时，平衡点称为非稳定结点。但要注意图2.8和图2.9所示的结点并不具有在图2.3和图2.4中所见的渐近快慢特性。

![](image/c81e034fba570f668335c50f902cacfca955a9beab5b09b82ee06dca342b1867.jpg)

<details>
<summary>text_image</summary>

z₂
z₁
</details>

(a)

![](image/3d6e6bc4393cc736c1fecaf9eb1f2ad542db7870d5e8c8862c7582ee1dc03939.jpg)

<details>
<summary>text_image</summary>

z₂
z₁
</details>

(b)

图 2.8 k=0 时非零多重特征值情况下的相图。(a) $\lambda<0$ ;(b) $\lambda>0$   
![](image/d8465e12a1e90a17dc47ac443cc45b96fbd767b06e596aff27bbd4e5ee4174d8.jpg)

<details>
<summary>text_image</summary>

z₂
z₁
</details>

(a)

![](image/3e1004cce51866d388f80c4be76990f16e631cb04b55e915cf9fae7d25b41c71.jpg)

<details>
<summary>text_image</summary>

z₂
z₁
</details>

(b)   
图 2.9 k=1 时非零多重特征值情况下的相图。(a) $\lambda<0$ ;(b) $\lambda>0$

在讨论一个或两个特征值为零的退化情况之前,我们先总结 x=0 为孤立平衡点时系统的几个特性。我们已经看到系统显示了六种不同特性的相图,各相图对应于不同类型的平衡点:稳定结点、非稳定结点、鞍点、稳定焦点、非稳定焦点和中心。平衡点的类型完全由 A 的特征值所在的位置决定。注意系统的总体(整个相平面)特性由平衡点的类型决定,这是线性系统的特点。在下一节研究非线性系统的特性时会看到,平衡点的类型仅决定了在这一点邻域内轨线的特性。
