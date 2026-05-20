# (3) 渐近稳定性

若系统的平衡状态 $x_{e}$ 不仅具有李雅普诺夫意义下的稳定性，且有

![](image/67e3d8f9bec2dc97e7d0083893a420541e38b4f25560a36f09e3cd95a3f7f1ac.jpg)

<details>
<summary>text_image</summary>

x₂
S(ε)
ε
S(δ)
δ
x₀
xₚ
x₁
</details>

(a) 李雅普诺夫意义下的稳定性

![](image/1e0c2fa80055900a16cd8c016f6547e832d0876db7814027385ace6d84876ef3.jpg)

<details>
<summary>text_image</summary>

x₂
S(ε)
S(δ)
δ
ε
x₀
xₑ
x₁
</details>

(b) 渐近稳定性

![](image/c3e9b8942d5edbd3d297d209d5e013fdd54b9570f235ce255c40085c3b6ed9e1.jpg)

<details>
<summary>text_image</summary>

x₂
S(ε)
ε
S(δ)
δ
x₀
xₑ
x₁
</details>

(c) 不稳定性  
图 9-28 有关稳定性的平面几何表示

$$\lim _ {t \to \infty} \| x (t; x _ {0}, t _ {0}) - x _ {e} \| = 0 \tag {9-255}$$

则称此平衡状态是渐近稳定的。这时，从 $S(\delta)$ 出发的轨迹不仅不会超出 $S(\varepsilon)$ ，且当 $t \to \infty$ 时收敛于 $x_{e}$ ，其平面几何表示如图9-28(b)所示。显见经典控制理论中的稳定性定义与此处的渐近稳定性对应。

若 $\delta$ 与 $t_{0}$ 无关，且式(9-255)的极限过程与 $t_{0}$ 无关，则称平衡状态是一致渐近稳定的。
