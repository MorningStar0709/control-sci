# 8.4.1 比例微分控制

将例 8.3.2 中所描述的系统表达为单位反馈控制系统的标准形式, 如图 8.4.1 所示, 它同时也是一个比例控制系统。

![](image/aec99e5b91f3bb685115a1b2a648816b7018b06b5deb574d7ef141f98b27def5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["E(s)"]
    C --> D["K"]
    D --> E["U(s)"]
    E --> F["G(s)=1/(s+1)(s+3)"]
    F --> G["X(s)"]
    G --> H["Feedback"]
    H --> B
```
</details>

图 8.4.1 比例控制的系统框图

绘制闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹, $G(s) = \frac{1}{(s + 1)(s + 3)}$ 有 $n = 2$ 个极点, 分别是 $s_{\mathrm{p}1} = -1$ 和 $s_{\mathrm{p}2} = -3$ , 有 $m = 0$ 个零点。根据规则5, 根轨迹有 $n - m = 2$ 条分支指向无穷。根据规则6, 其渐近线与实轴的交点为

$$
\sigma_ {\mathrm{a}} = \frac {\sum s _ {\mathrm{pn}} - \sum s _ {\mathrm{zm}}}{n - m} = \frac {- 1 - 3}{2 - 0} = - 2 \tag {8.4.1a}
$$

夹角为

$$
\theta = \frac {2 q + 1}{n - m} \pi = \frac {2 q + 1}{2 - 0} \pi , \quad q = 0, 1
$$

$$
\Rightarrow \left\{ \begin{array}{l} \theta_ {1} = \frac {1}{2} \pi \\ \theta_ {2} = \frac {3}{2} \pi = - \frac {1}{2} \pi \end{array} \right. \tag {8.4.1b}
$$

其根轨迹如图 8.4.2(a) 所示, 如例 8.3.2 所分析的, s = -2 - j 在其根轨迹上。

![](image/79e3378f3ffa4a8663c20a086447d5e7058942ae7959de5e33382a483862f7c7.jpg)

<details>
<summary>text_image</summary>

渐近线
Im
s_p2
-3
-2
-1
O
Re
s_p1
</details>

(a) $G(s)=\frac{1}{(s+1)(s+3)}$ 的根轨迹

![](image/6bfb6b7784fb47382cc9bebc3cf4ba7d8a8f3f5a7ba5cc3486e26ce0c43a6bc9.jpg)

<details>
<summary>text_image</summary>

Im
scl_p3
scl_p2
scl_p1
-3
-2
-1
O
Re
scl_p4
</details>

(b) 闭环传递函数极点  
图 8.4.2 系统的根轨迹及闭环传递函数极点分布

进一步分析系统的时间响应, 当增益 K 比较小的时候, 闭环传递函数有两个小于零的实数极点。例如当 K=0.5 时, 闭环传递函数所对应的两个实数根为 $s_{cl\_p1}=-1.29$ 和 $s_{cl\_p2}=-2.71$ [如图 8.4.2(b) 所示, 可以通过 $1+KG(s)=0$ 求解]。当单位阶跃 $(r(t)=1$ , 拉普拉斯变换为 $R(s)=\frac{1}{s}$ 作用在系统上时, 其输出 $x(t)$ 为

$$
x (t) = 1 + C _ {1} \mathrm{e} ^ {s _ {\mathrm{cl} - \mathrm{pl}} t} + C _ {2} \mathrm{e} ^ {s _ {\mathrm{cl} - \mathrm{pl}} t} = 1 + C _ {1} \mathrm{e} ^ {- 1. 2 9 t} + C _ {2} \mathrm{e} ^ {- 2. 7 1 t} \tag {8.4.2}
$$

其中， $C_1$ 和 $C_2$ 是两个常数，读者可以自行计算（参考第5章），然而这里我们并不需要 $C_1$ 和 $C_2$ 的精确数据就可以分析系统。式(8.4.2)由三部分相加而成，其中，1是一个常数，来自参考输入 $R(s) = \frac{1}{s}$ ，而另外两项都会随着时间的增加趋于0。同时，因为 $|s_{\mathrm{cl\_p1}}| < |s_{\mathrm{cl\_p2}}|$ ，所以 $C_1\mathrm{e}^{-1.29t}$ 的收敛速度要慢于 $C_2\mathrm{e}^{-2.71t}$ 。因此，它们相加后的结果 $x(t)$ 的收敛速度是由 $C_1\mathrm{e}^{-1.29t}$ 决定的，所以 $s_{\mathrm{cl\_p1}} = -1.29$ 称为主导极点（Dominant Pole），主导极点更靠近虚轴。
