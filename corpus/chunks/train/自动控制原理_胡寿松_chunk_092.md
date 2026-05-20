# (1) 串联方框的简化(等效)

传递函数分别为 $G_{1}(s)$ 和 $G_{2}(s)$ 的两个方框，若 $G_{1}(s)$ 的输出量作为 $G_{2}(s)$ 的输入量，则 $G_{1}(s)$ 与 $G_{2}(s)$ 称为串联连接，如图2-24(a)所示(注意，两个串联连接元件的方框图应考虑负载效应)。

![](image/485908f96d9e1c90af67fba61d1c1c25b021ee57a3c1275ae290b9e64c0b6aea.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["G₁(s)"]
    B --> C["U(s)"]
    C --> D["G₂(s)"]
    D --> E["C(s)"]
```
</details>

(a)

![](image/7e3025af2286dcd567edac7ce2ff275067fc794d452fc6237f18ca7d1f6eb4ca.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["G₁(s) G₂(s)"]
    B --> C["C(s)"]
```
</details>

(b)   
图 2-24 方框串联连接及其简化

由图 2-24(a)，有

$$U (s) = G _ {1} (s) R (s), \quad C (s) = G _ {2} (s) U (s)$$

由上两式消去 $U(s)$ ，得

$$C (s) = G _ {1} (s) G _ {2} (s) R (s) = G (s) R (s) \tag {2-71}$$

式中， $G(s) = G_{1}(s)G_{2}(s)$ ，是串联方框的等效传递函数，可用图2-24(b)的方框表示。由此可知，两个方框串联连接的等效方框，等于各个方框传递函数之乘积。这个结论可推广到 $\pmb{n}$ 个串联方框情况。
