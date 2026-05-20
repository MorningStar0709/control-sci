B–6–27. Consider the system shown in Figure 6–117. Plot the root loci as the value of k varies from 0 to q.What value of k will give a damping ratio of the dominant closed-loop poles equal to 0.5? Find the static velocity error constant of the system with this value of k.

![](image/85db4942ef64cdf0ad78f8e5fbd1e2cc1c2a81971f8733b7e70532dcccd15189.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["s + 1.4 / (s + 5)"]
    B --> C["+"]
    C --> D["10 / (s(s + 1))"]
    D --> E["ks / (s + 10)"]
    E --> F["Feedback to A"]
    F --> G["Output"]
```
</details>

B–6–28. Consider the system shown in Figure 6–118. Assuming that the value of gain K varies from 0 to q, plot the root loci when $K _ { h } = 0 . 1 , 0 . 3$ and 0.5.,

Compare unit-step responses of the system for the following three cases:

(1) $K = 1 0 , \qquad K _ { h } = 0 . 1$   
(2) $K = 1 0 , \qquad K _ { h } = 0 . 3$   
(3) $K = 1 0 , \qquad K _ { h } = 0 . 5$

![](image/f529b0bb3bd1c3da925caa7857d78b751e876196b228471b42603c1291127a24.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum1
    Sum1 --> |+| Sum2
    Sum2 --> |K/(s+1)| A["1/s"]
    A --> C["s"]
    C --> |K_h| Sum1
    Sum1 --> m
```
</details>

Figure 6–118 Control syste

![](image/4c83e7bfbe03ff004dd6c22996116786b77398d85674109de2f4a450f114d967.jpg)

<details>
<summary>text_image</summary>

7
</details>
