```mermaid
graph LR
    v -->|+| Sum
    Sum --> P[" P(s) "]
    P --> C[" C(s) "]
    C --> Go[" Go(s) "]
    Go --> y
    y -->|-| Sum
```
</details>

图 P11.3

![](image/16e169ee4f7d619cb8f1c8ae9a5fb036c732ec8c3e89d03e561ee2b1426dab3b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    v -->|+| A["⊕"]
    A --> B["C(s)"]
    B --> C["N(s)"]
    C --> D["⊕"]
    D --> y
    w --> D
    y -->|-| A
```
</details>

图 P11.4

11.16 给定受控系统和二次型性能指标为:

$$
\begin{array}{l} \dot {x} = \left[ \begin{array}{c c} 0 & 1 \\ 2 & - 3 \end{array} \right] x + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \\ J = \int_ {0} ^ {\infty} (x _ {1} ^ {2} + 4 x _ {2} ^ {2} + 2 u ^ {2}) d t \\ \end{array}
$$

利用复频率域法求出其最优状态反馈增益矩阵 $K^{*}$ 。
