```mermaid
graph TD
    A["\tilde{X}_1"] -->|f| B["\tilde{X}_2"]
    A -->|p₁| C["X"]
    B -->|p₂| C
```
</details>

(a)

![](image/76fd4dc58ddb1bd23db439f83ccc029af5a67f72f518830b76f18c03fb2b5b41.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["\tilde{X}_1"] -->|f^{-1}| B["\tilde{X}_2"]
    A -->|p_1| C["X"]
    B -->|p_2| C
```
</details>

(b)   
图3.4.6 泛复叠空间

(2) 如果 $(\widetilde{X}, p)$ 是 $X$ 的泛复叠空间，而 $(Y, q)$ 是一个复叠空间，那么存在一个映射 $\pi: \widetilde{X} \to Y$ ，使得 $(\widetilde{X}, \pi)$ 是 $Y$ 的一个复叠空间。并且，图3.4.7可交换。

![](image/ffa10fc28141cd743196fdcfa5bbeb09a1cdaf42094039fe272a6b12aa64fdbd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["X̃"] -->|π| B["Y"]
    A -->|p| C["X"]
    B -->|q| C
```
</details>

图3.4.7 复叠空间

例3.4.4 如图3.4.8所示，设 $p: \mathbb{R} \to S^1$ 定义为 $p: t \mapsto (\cos(2\pi t), \sin(2\pi t))$ 。选任一点 $x_0 \in S^1$ ，如 $x_0 = (1, 0)$ 。考虑邻域 $U = \widehat{Px_0Q}$ ，它是右半圆。这是一个基本邻域，因为 $p^{-1}(U) = \left\{V_k = \left(k - \frac{1}{2}, k + \frac{1}{2}\right) \mid k \in Z\right\}$ 。现在其限制 $p: V_k \to U$ 是一个同胚。因此 $p$ 是一个投影。因此可得结论： $(\mathbb{R}, p)$ 是 $S^1$ 的一个复叠空间，重数是 $\chi_0$ 。（即可数）。

因为 $\pi (\mathbb{R}) = \{0\}$ 且 $\pi (S^1)\cong Z$ ，导出的同态 $p_*$ 是 $p_*\pi (\mathbb{R}) = \{0\} <  Z.$

![](image/9e6d8a0f49243e57fcd7518a840d237e1a751790ff1139dfc627486362b085f4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+∞"] --> B["V1"]
    B --> C["V0"]
    C --> D["V-1"]
    D --> E["P"]
    E --> F["x0"]
    F --> G["Q"]
    G --> H["↓"]
```
</details>

图3.4.8 $\mathbb{R}$ 是 $S^1$ 的复叠空间
