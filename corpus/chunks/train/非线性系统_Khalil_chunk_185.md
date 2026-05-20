![](image/b04937d14e427717858f629dc51216f930897a4405132e2b755ba179387a0383.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(b)

![](image/467f2c52211b3efe765c3e71cfe27dbfa96ec1f62c070ba3e3fd95f1da6992b7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["Block"]
    B --> C["y"]
    C --> D["+"]
    D --> E["\tilde{y}"]
    F["φ(·)"] --> C
    G["+"] --> D
```
</details>

(c)

图 6.4 $u^{T}y \geqslant \varepsilon u^{T}u$ 的图形表示。(a) $\varepsilon > 0$ (过量无源性); (b) $\varepsilon < 0$ (欠量无源性); (c) 通过输入前馈消除过量和欠量无源性  
![](image/57f63179dd421055ebd7954b8c89373199f8fe6a6b62e55a05841c73b8fc652d.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(a)

![](image/c3998f95808d46e28c814946803bc2f6e17c1953f0d19c0703d70aac78fc3493.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(b)

![](image/56aa3d4c9ccb223fe5d07c0b402cac518da2eaa90d1e08281d899dbd9fdb6a87.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["ũ"] --> B["+"]
    B --> C["u"]
    C --> D["Block"]
    D --> E["y"]
    E --> F["ρ(·)"]
    F --> G["+"]
    G --> B
```
</details>

(c)   
图 6.5 $u^{T}y \geqslant \delta y^{T}y$ 的图形表示。(a) $\delta > 0$ (过量无源性); (b) $\delta < 0$ (欠量无源性); (c) 通过输出反馈消除过量和欠量无源性
