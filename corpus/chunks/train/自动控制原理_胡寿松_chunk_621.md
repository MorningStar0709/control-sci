$$
(s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} = \left[ \begin{array}{c c} s & - 1 \\ 0 & s + 2 \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s (s + 2)} \\ 0 & \frac {1}{s + 2} \end{array} \right]

\boldsymbol {G} (s) = \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s (s + 2)} \\ 0 & \frac {1}{s + 2} \end{array} \right] \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s (s + 2)} \\ 0 & \frac {1}{s + 2} \end{array} \right]
$$

![](image/98cb964f928d2bd034d1f18b6d9b7a07b3ff3347e9eb8c5f00fdc2ecc02a6bc1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    U["s"] --> A["+"]
    E["s"] --> G["s"]
    G["s"] --> Y["s"]
    Y["s"] --> H["s"]
    H["s"] --> Z["s"]
    Z["s"] --> A
```
</details>
