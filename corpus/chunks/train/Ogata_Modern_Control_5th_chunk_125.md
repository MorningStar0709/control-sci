```mermaid
graph LR
    A["Q(s)"] --> B["+"]
    C["Q₁(s)"] --> B
    B --> D["1/C₁s"]
    D --> E["H₁(s)"]
```
</details>

![](image/f2061efb280516125a2f145d3e0c49a56a583ff48424d7c93f00fca52b7cd6da.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Q1(s)"] --> B["+"]
    C["Q2(s)"] --> B
    B --> D["1/(C2s)"]
    D --> E["H2(s)"]
```
</details>

![](image/ad1aff38988214ffd50bdcabdbf701fc7401da1f0b226e62723850d2b74d9aad.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Q(s)"] --> B["+"]
    B --> C["1/C1s"]
    C --> D["H1(s)"]
    D --> E["+"]
    E --> F["1/R1"]
    F --> G["Q1(s)"]
    G --> H["+"]
    H --> I["1/C2s"]
    I --> J["H2(s)"]
    J --> K["1/R2"]
    K --> L["Q2(s)"]
    L --> M["Feedback to B"]
    M --> B
```
</details>

(b)

![](image/5f5a7a3c0fbc53460c4f820a2c85ce2bbcd03bcb06a645f4b2f283c40eec5e50.jpg)

<details>
<summary>flowchart</summary>
