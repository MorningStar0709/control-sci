<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Specifications"] --> B["Design calculation"]
    B --> C["Controller"]
    C --> D["Process"]
    D --> E["Measured output signal"]
    F["Controller parameters"] --> B
    G["Command signal"] --> C
    H["Process parameters"] --> B
    I["Control signal"] --> D
    J["Parameter estimation"] --> B
    K["Control parameter"] --> B
    L["Process"] --> D
```
</details>

Figure 6.6 Block diagram of an adaptive controller obtained by combining a parameter estimator with a design calculation.

approach is in fact the technique predominantly used in process control. Its success depends largely on the experience and skill of the designer.

An adaptive system, which is obtained by combining a parameter estimator with a design procedure, is shown in Fig. 6.6.
