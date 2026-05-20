# Asea Brown Boveri (ABB) Adaptive Controller

The Asea Brown Boveri (ABB) adaptive controller was first marketed under the name Novatune. It is an adaptive controller that is incorporated as a part of ABB Master, a distributed system for process control. The system is block-oriented, which means that the process engineer creates a system by selecting and interconnecting blocks of different types. The system has blocks for conventional PID control, logic, and computation. Three different blocks, called STAR1, STAR2, and STAR3, are adaptive controllers. The adaptive controllers are self-tuning regulators based on least-squares estimation and minimum-variance control. The controllers all use the same algorithm; they differ in the controller complexity and the prior information that must be supplied in using them.

![](image/b4684d1d3e7a54d4cf5462f6c8927f1eb44c44c7f351b986e9a00eb581688a32.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["STAR1"] --> B["ON AUTO"]
    B --> C["UEXT"]
    C --> D["FB"]
    D --> E["Self-tuning adaptive regulator"]
    E --> F["REF"]
    F --> G["PY MAX MIN T"]
    H["STAR3"] --> I["ON LOAD AUTO REG- SOFT AD"]
    I --> J["UEXT"]
    J --> K["FB"]
    K --> L["REF"]
    L --> M["FF"]
    M --> N["HI"]
    N --> O["LO"]
    O --> P["DH"]
    P --> Q["DL"]
    R["PL PU PY MAX MIN T PN NA NB NC KD INT"] --> S["U"]
```
</details>

Figure 12.3 Block diagrams of the adaptive modules STAR1 and STAR3, available in the ABB adaptive controller.

The ABB adaptive controller differs from the controllers that were discussed previously in that it is not based on the PID structure. Instead, its algorithm is based on a general pulse transfer function. It also admits dead-time compensation and feedforward control. The ABB adaptive controller system may be viewed as a toolbox for solving control problems.
