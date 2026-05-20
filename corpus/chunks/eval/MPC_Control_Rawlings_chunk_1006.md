# C.3.1 Outer and Inner Semicontinuity

The concepts of inner and outer semicontinuity were introduced by Rockafellar and Wets (1998, p. 144) to replace earlier definitions of lower and upper semicontinuity of set-valued functions. This section is based on the useful summary provided by Polak (1997, pp. 676-682).

Definition C.23 (Outer semicontinuous function). A set-valued function $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is said to be outer semicontinuous (osc) at $x \operatorname { i f } U ( x )$

![](image/1bf50e70826649f8c20990ee1ef02ac34ddffc420b3d7e212b80c38c0809f781.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["U(x)"] --> B["S"]
    C["U(x')"] --> D["x ⊕ δB"]
    E["x"] --> F["●"]
    G["x'"] --> H["●"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#ffc,stroke:#333
    style F fill:#cff,stroke:#333
    style G fill:#ffc,stroke:#333
    style H fill:#ffc,stroke:#333
```
</details>

(a) Outer semicontinuity.

![](image/a46d2dadc6adee6b9da142943c7ae99cf0c86e9a771012385dac50a155761027.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["U(x)"] --> B["S"]
    C["U(x')"] --> D["x ⊕ δB"]
    E["x"] --> F["●"]
    G["x'"] --> H["●"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#ffc,stroke:#333
    style F fill:#cff,stroke:#333
    style G fill:#ffc,stroke:#333
    style H fill:#cfc,stroke:#333
```
</details>

(b) Inner semicontinuity.   
Figure C.11: Outer and inner semicontinuity of $U ( \cdot )$ .

is closed and if, for every compact set S such that $U ( x ) \cap S = \emptyset$ , there exists a $\delta > 0$ such that $U ( x ^ { \prime } ) \cap S = \emptyset$ for all $ { \boldsymbol { x } } ^ { \prime } \in  { \boldsymbol { x } } \oplus \delta  { \mathcal { B } } . ^ { 4 }$ The set-valued function $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is outer semicontinuous if it is outer semicontinuous at each $\boldsymbol { x } \in \mathbb { R } ^ { n }$ .
