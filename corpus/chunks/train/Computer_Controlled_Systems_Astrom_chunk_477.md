# Input-Output Methods

Multirate systems can also be investigated by input-output analysis. First, observe as before that the system is periodic with period h if the ratios of the sampling periods are rational numbers. The values of the system variables at times that are synchronized to the period can then be described as a time-invariant dynamic system. Ordinary operator or transfer-function methods for linear systems can then be used. The procedure for analyzing a system can be described as follows: A block diagram of the system including all subsystems and all samplers is first drawn. The period h is determined. All samplers appearing in the system then have periods h/m, where m is an integer. A trick called switch decomposition is then used to convert samplers with rate h/m to a combination of samplers with period h. The system can then be analyzed using the methods described in Sec. 7.8.

(a)   
![](image/58a46c43d65a062df9dc87ea12fc5f89a610f547483ff49d30bb96cda0653481.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Input"] --> B["Σ"]
    B --> C["e^sh/2"]
    C --> D["Output"]
    B --> E["h"]
    E --> B
    D --> F["h"]
    F --> C
```
</details>

(b)   
![](image/8fcc8336ee4fc2af31776e104ab5f3450326bea849088144ffdd9fe0ea048d9a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["e^{sh/m}"] -->|h| B["e^{-sh/m}"]
    C["e^{2sh/m}"] -->|h| D["e^{-2sh/m}"]
    E["..."] --> F["..."]
    G["e^{s(m-1)h/m}"] -->|h| H["e^{-s(m-1)h/m}"]
    B --> I["Σ"]
    D --> I
    H --> I
    I --> J["h"]
    style I fill:#f9f,stroke:#333
```
</details>

Figure 7.33 Representation of samplers with periods (a) h/2 and (b) h/m by switch decomposition.
