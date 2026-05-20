<details>
<summary>line</summary>

| t (sec) | x² |
| --- | --- |
| 0 | 0.05 |
| 2 | -0.03 |
| 4 | 0.01 |
| 6 | 0.005 |
| 8 | 0.002 |
| 10 | 0.001 |
</details>

![](image/06ae8ac90dacbe276716b5f2437e42fcf2b4fa53452fd4e529bbaf3788e0cd0d.jpg)

<details>
<summary>line</summary>

| t (sec) | x3 |
| --- | --- |
| 0 | 0.0 |
| 2 | 0.5 |
| 4 | 0.9 |
| 6 | 1.0 |
| 8 | 1.0 |
| 10 | 1.0 |
</details>

![](image/1ce7f9a8dcfc8276959e71610623ddd8d7827eef0ea026fbe7fa1b842137996a.jpg)

<details>
<summary>line</summary>

| t (sec) | x4 |
| --- | --- |
| 0 | 0.0000 |
| 1 | 0.2500 |
| 2 | 0.3500 |
| 3 | 0.3000 |
| 4 | 0.2000 |
| 5 | 0.1000 |
| 6 | 0.0500 |
| 7 | 0.0200 |
| 8 | 0.0100 |
| 9 | 0.0050 |
| 10 | 0.0025 |
</details>

![](image/411f17c5cb7cb7ff88c30491ecd8ebba7034a38e71b942d2220fb535a38cfcff.jpg)

<details>
<summary>line</summary>

| t (sec) | x5 |
| --- | --- |
| 0 | 0 |
| 2 | 2 |
| 4 | 2.5 |
| 6 | 2.7 |
| 8 | 2.7 |
| 10 | 2.7 |
</details>

Figure 10–55   
Response curves to a unit-step input.

![](image/0dc5c4c39527715ea65671dc500c6953487bfc7e793572bc7b43fd09856b84ec.jpg)

<details>
<summary>line</summary>

| t (sec) | Cart Position x₃ |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.1 |
| 2 | 0.4 |
| 3 | 0.7 |
| 4 | 0.9 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

Figure 10–56   
Cart position versus t curve.

A–10–18. Consider the stability of a system with unstructured additive uncertainty as shown in Figure 10–57(a). Define

$\widetilde { G }$ true plant dynamics=

G=model of plant dynamics

$\Delta _ { a }$ = unstructured additive uncertainty

![](image/c11155d267b10da608c6e68d19169679e2dd6472c578be33f313b29fab68b57f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+"] --> B["G"]
    B --> C["-"]
    C --> D["K"]
    D --> E["y"]
    E --> F["u"]
    F --> C
    C --> G["Δa"]
    G --> H["A"]
    H --> I["+"]
    I --> J["B"]
    J --> C
```
</details>

(a)

![](image/3dc63926146d47cdbbe906ffa855057a1749e8130e9f0b71aafca0b5175c7d6f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["A"] --> G["+"]
    G --> K["K"]
    K --> B["B"]
    B --> G
    G -->|y| G
    G -->|u| K
    K -->|Δa| B
```
</details>

(b)

![](image/103418596124008153c42fdef7e5ba82a430078a2a3a59748f168627907aba62.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["A"] --> B["B"]
    B --> C["Δa"]
    C --> D["Ta"]
    D --> A
```
</details>

(c)

![](image/bfd7bc76389cf831673e6b5ee8fb9ce3b905b5af1b01d8a007c464bcebaaccaf.jpg)

<details>
<summary>flowchart</summary>
