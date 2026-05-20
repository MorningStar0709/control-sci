$$
G (s) = \left[ \begin{array}{c c} {\left[ \begin{array}{c} 0 \\ \tilde {M} ^ {- 1} \end{array} \right]} & {\left[ \begin{array}{c} I \\ P \end{array} \right]} \\ {\tilde {M} ^ {- 1}} & P \end{array} \right] = \left[ \begin{array}{c c} A & - L Z ^ {- 1} \qquad B \\ \hline {\left[ \begin{array}{c} 0 \\ C \end{array} \right]} & {\left[ \begin{array}{c} 0 \\ Z ^ {- 1} \end{array} \right]} & {\left[ \begin{array}{c} I \\ D \end{array} \right]} \\ C & Z ^ {- 1} \qquad D \end{array} \right]

=: \quad \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & D _ {1 1} & D _ {1 2} \\ C _ {2} & D _ {2 1} & D _ {2 2} \end{array} \right].
$$

To apply the $\mathcal { H } _ { \infty }$ control formulas in Chapter 14, we need to normalize the $D _ { 1 2 }$ and $D _ { 2 1 }$ first. Note that

$$
\left[ \begin{array}{c} I \\ D \end{array} \right] = U \left[ \begin{array}{c} 0 \\ I \end{array} \right] (I + D ^ {*} D) ^ {\frac {1}{2}}, \text {where} U = \left[ \begin{array}{c c} D ^ {*} (I + D D ^ {*}) ^ {- \frac {1}{2}} & (I + D ^ {*} D) ^ {- \frac {1}{2}} \\ - (I + D D ^ {*}) ^ {- \frac {1}{2}} & D (I + D ^ {*} D) ^ {- \frac {1}{2}} \end{array} \right]
$$

![](image/e26e0977c1415981322d851db88770fe258b64aff640363db2314fa4c672c5b2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    z1 --> MtildeMtilde{M^{-1}}
    z2 --> MtildeMtilde{M^{-1}}
    y --> Khat{K}
    MtildeMtilde --> Sum((+))
    NtildeNtilde --> Sum
    Sum --> w
    style MtildeMtilde fill:#f9f,stroke:#333
    style NtildeNtilde fill:#f9f,stroke:#333
    style Khat fill:#ccf,stroke:#333
```
</details>

Figure 16.2: LFT diagram for coprime factor stabilization

and U is a unitary matrix. Let

$$
\hat {K} = (I + D ^ {*} D) ^ {- \frac {1}{2}} \tilde {K} Z
\left[ \begin{array}{c} z _ {1} \\ z _ {2} \end{array} \right] = U \left[ \begin{array}{c} \hat {z} _ {1} \\ \hat {z} _ {2} \end{array} \right].
$$

Then $\left. T _ { z w } \right. _ { \infty } = \left. U ^ { * } T _ { z w } \right. _ { \infty } = \left. T _ { \hat { z } w } \right. _ { \infty }$ and the problem becomes one of finding a controller $\tilde { K }$ so that $\| T _ { \hat { z } w } \| _ { \infty } < \gamma$ with the following generalized plant:

$$
\hat {G} = \left[ \begin{array}{c c} U ^ {*} & 0 \\ 0 & Z \end{array} \right] G \left[ \begin{array}{c c} I & 0 \\ 0 & (I + D ^ {*} D) ^ {- \frac {1}{2}} \end{array} \right]
