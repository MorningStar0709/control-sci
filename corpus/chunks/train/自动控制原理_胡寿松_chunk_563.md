# (1) 变增益线性系统的稳定性分析

为了应用描述函数分析非线性系统的稳定性,有必要研究图 8-43(a) 所示线性系统的稳定性,其中 K 为比例环节增益。设 $G(s)$ 的极点均位于 s 的左半平面,即 $P=0, G(j\omega)$ 的奈奎斯特曲线 $\Gamma_{G}$ 如图 8-43(b) 所示。闭环系统的特征方程为

![](image/adca8fd4ecc6a11509cd4c638d037e4d0aeab417abd7f1e48615696a836b05a7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r"] --> B((+))
    B --> C["e"]
    C --> D["K"]
    D --> E["G(s)"]
    E --> F["c"]
    F --> G["Feedback"]
    G --> B
```
</details>

(a)

![](image/08c10d41a9aba62aad26e740ea69acbbc1bb415369b8a6e928014aa29edb5f33.jpg)

<details>
<summary>text_image</summary>

-1/K₁ -1/K₂ G(jω)
0
j
ω
</details>

(b)   
图 8-43 可变增益的线性系统

$$1 + K G (\mathrm{j} \omega) = 0 \tag {8-82}$$

或 $G(\mathrm{j}\omega) = -\frac{1}{K} + \mathrm{j}0$ (8-83)

由奈氏判据知，当 $\Gamma_{G}$ 曲线不包围点 $\left(-\frac{1}{K},\mathrm{j}0\right)$ 时，即 $Z = P - 2N = -2N = 0$ ，系统闭环稳定；当 $\Gamma_{G}$ 曲线包围点 $\left(-\frac{1}{K},\mathrm{j}0\right)$ 时，系统不稳定；当 $\Gamma_{G}$ 曲线穿过点 $\left(-\frac{1}{K},\mathrm{j}0\right)$ 时，系统临界稳定，将产生等幅振荡。更进一步，若设 $K$ 在一定范围内可变，即有 $K_{1}\leqslant K\leqslant K_{2}$ ，则 $\left(-\frac{1}{K},\mathrm{j}0\right)$ 为复平面实轴上的一段直线，若 $\Gamma_{G}$ 曲线不包围该直线，则系统闭环稳定，而当 $\Gamma_{G}$ 包围该直线时，则系统闭环不稳定。
