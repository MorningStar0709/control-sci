Clearly, for a stable plant model G(s), K(s)=0 will satisfy Inequality (10–125). However, $K ( s ) = 0$ is not the desirable transfer function for the controller. To find an acceptable transfer function for $K ( s )$ , we may add another condition—for example, that the resulting system will have robust performance such that the system output follows the input with minimum error, or another reasonable condition. In what follows we shall obtain the condition for robust performance.

![](image/c1d38a48cebf26b90e7b12a9b6de6989da19bba98b3baf28a5fb4408588d7649.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["×"] --> B["G"]
    B --> C["+"]
    C --> D["y"]
    D --> E["K"]
    E --> F["u"]
    F --> A
    C --> G["Δm"]
    G --> H["A"]
    H --> C
    style A fill:#f9f,stroke:#333
    style D fill:#ccf,stroke:#333
    style E fill:#cfc,stroke:#333
```
</details>

![](image/accce5def8c30ec1f9570517e71e0a25b815be94430fe6bd09013450c8c601ff.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["A"] -->|+| B["+"]
    B -->|y| C["K"]
    C -->|u| D["G"]
    D --> B
    B -->|Δm| E["Δm"]
    E --> A
    style A fill:#fff,stroke:#000
    style B fill:#fff,stroke:#000
    style C fill:#fff,stroke:#000
    style D fill:#fff,stroke:#000
    style E fill:#fff,stroke:#000
```
</details>

![](image/f65b8f7be85ee1da0ed750ed872c9c890f791e1eaec06610b63f3fe81ef4adf7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["A"] --> B["B"]
    B --> C["Δm"]
    C --> D["T"]
    D --> A
```
</details>

![](image/2c4004fd62b7d35fcc5891f036e56e6ffe5d4b02c85c5c01680585aa0e8fa130.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["×"] -->|u| B["G"]
    B --> C["+"]
    D["Δm"] -->|B| C
    C --> E["y"]
    F["w"] -->|A| C
    C --> G["K"]
    G --> A
    style A fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style F fill:#f9f,stroke:#333
    style G fill:#ccf,stroke:#333
```
</details>

![](image/11dd9837bafb57b0105a966bd38d9b8ab7380c573d95f59507286e59752f42e8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    w --> A
    A --> B
    B --> C
    C --> D
    D --> y
    u --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> z
    WmI --> H
    style w fill:#f9f,stroke:#333
    style x fill:#ccf,stroke:#333
    style y fill:#cfc,stroke:#333
    style z fill:#fcc,stroke:#333
    style u fill:#ffc,stroke:#333
    style v fill:#cfc,stroke:#333
    style w_mI fill:#ffc,stroke:#333
    style K fill:#cfc,stroke:#333
    style H fill:#ffc,stroke:#333
```
</details>
