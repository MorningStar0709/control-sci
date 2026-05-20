# Modified z-Transforms

The problem of sampling a system with a delay can be handled by the modified z-transform defined in Definition 2.2. The modified z-transform is useful for many purposes—for example, the intersample behavior can easily be investigated using these transforms. There are extensive tables of modified z-transforms and many theorems about their properties (see the References).

(a)   
![](image/72035fe37ca486ec0e2905acf51b95ceb5c1a78a08a421bd823b984fe8b44f30.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["uc"] --> B["Multiplexer"]
    B --> C["A-D"]
    C --> D["H"]
    D --> E["D-A"]
    E --> F["G1"]
    F --> G["G2"]
    G --> H["y2"]
    H --> I["Feedback"]
    I --> B
    style A fill:#f9f,stroke:#333
    style H fill:#ccf,stroke:#333
    style G fill:#cfc,stroke:#333
```
</details>

![](image/5c7acd53bf23c2c4a2bd67d93bbd30b7e0b4969356be7d6802af8c9dc195b811.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Clock"] --> B["Hc"]
    B --> C["Σ"]
    D["y2*"] --> E["H2"]
    F["y1*"] --> G["H1"]
    G --> C
    C --> H["u*"]
    H --> I["Hold 1/s(1-e^(-sh))"]
    I --> J["G1"]
    J --> K["y1"]
    K --> L["G2"]
    L --> M["F2"]
    M --> N["F1"]
    N --> I
    style A fill:#f9f,stroke:#333
    style D fill:#ccf,stroke:#333
    style F fill:#ccf,stroke:#333
    style M fill:#cfc,stroke:#333
```
</details>

(c)   
![](image/0b40a4f7ee0c8c62da1fd4505ce14a546cc15dc9c36c7b3617edc596942c886a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["{u_c(kh)}"] --> B["H_c"]
    C["{y_2(kh)}"] --> D["H_2"]
    E["H_1"] --> F["Σ"]
    G["{u(kh)}"] --> H["\tilde{F}_1"]
    I["{y_1(kh)}"] --> J["\tilde{F}_2/\tilde{F}_1"]
    K["{y_2(kh)}"] --> L["\tilde{F}_2/\tilde{F}_1"]
    B --> M["Σ"]
    D --> M
    F --> M
    H --> M
    J --> M
    L --> M
```
</details>

Figure 7.31 Computer-controlled system with multiplexer and two feedback loops and equivalent block diagram.
