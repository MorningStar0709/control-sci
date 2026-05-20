# Example 3.19 (dc Servo)

Repeat Example 3.16 but with the output $y = \omega$ ( $C = \begin{bmatrix} 0 & 1 & 0 \end{bmatrix}$ ). Display the canonical decomposition. (For simplicity, use only the input $v$ .)

Solution The steps are as in Example 3.16, up to

$$
C T = \left[ \begin{array}{c c c} 0 & 1 & -. 2 0 6 2 \end{array} \right].
$$

Figure 3.14 displays the canonical decomposition.

![](image/ec3b6c6ebec1b549eeb6f74dad6646ec381c6acae3c3bf09cb9c3d63284e8e75.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1.6667"] --> B["1/s"]
    C["4.6588"] --> D["1/(s + 2.474)"]
    E["22.5971"] --> F["1/(s + 21.526)"]
    G["-0.2062"] --> H["+"]
    H --> I["y"]
    J["v"] --> C
    K["Controllable/Unobservable"] --> A
    K --> C
    K --> E
    L["Controllable/Observable"] --> H
```
</details>

Figure 3.14 Canonical decomposition of the dc servo

![](image/7eb719546e13e148a1580486ab75716505c447918abd30cfc299a1866c381d44.jpg)
