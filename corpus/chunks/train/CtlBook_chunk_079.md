# CORRECT

Remember: dimensional agreement is a necessary but not sucient condition for correctness. If your solution fails dimensional analysis, you have denitely found an error but when it passes, there still could be

![](image/88d6330faf3efd1788407702863a4ed4be52a08caf9d364ddb3fea79c210b611.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Block M1"] --> B["Resistors B1, B2, B3, B4"]
    B --> C["Actuator X1"]
    C --> D["M2"]
    D --> E["Resistors X2, X3, X4"]
    E --> F["M3"]
    F --> G["Resistors X3, X4"]
    G --> H["M4"]
    H --> I["Actuator X5"]
    I --> J["Feedback to Block M4"]
    style A fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
    style J fill:#f9f,stroke:#333
```
</details>

Figure 2.5: A system with 4 masses and numerous springs and dampers connecting them.

another type of error.
