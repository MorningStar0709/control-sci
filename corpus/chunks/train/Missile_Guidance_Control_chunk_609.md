![](image/cc145e9e3f22f242f9757e2be7ecbea58648e2a49e037756c5923aff4149361a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    INS["INS"] -->|a_T| A((+))
    A -->|v̇_g| B["1/s"]
    B -->|V_g| To["To control system"]
    Time["Time"] --> C["||Q|| computer"]
    C -->|V_g| D["Matrix multiplier"]
    D --> C
    C --> E["||Q|| V_g"]
    E --> A
    style INS fill:#f9f,stroke:#333
    style To fill:#ccf,stroke:#333
```
</details>

Fig. 6.25. Proposed concept for the integration of $d ( \Delta \mathbf { V } _ { g } ) / d t$ .

The cross product control relation is thus stated by the vector expression

$$\omega_ {c} = S \left[ - \left(\frac {d \mathbf {V} _ {g}}{d t}\right) \times \mathbf {V} _ {g} \right] = S \left[ \mathbf {V} _ {g} \times \left(\frac {d \mathbf {V} _ {g}}{d t}\right) \right], \tag {6.194}$$
