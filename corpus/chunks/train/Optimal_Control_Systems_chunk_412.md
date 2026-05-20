# 7.5 Energy-Optimal Control Systems

In minimum-energy (energy-optimal) systems with constraints, we often formulate the performance measure as the energy of an electrical (or mechanical) system. For example, if $u(t)$ is the voltage input to a field circuit in a typical constant armature-current, field controlled positional control system, with negligible field inductance and a unit field resistance, the total energy to the field circuit is (power is $u^{2}(t)/R_{f}$ , where, $R_{f}=1$ is the field resistance)

$$J = \int_ {t _ {0}} ^ {t _ {f}} u ^ {2} (t) d t \tag {7.5.1}$$

and the field voltage $u(t)$ is constrained by $|u(t)| \leq 110$ . This section is based on [6, 89].

![](image/a0f258f411e3e2b2b986dcfbb8a005ba5ac77f9d0f3fc133b1590cb17ef12aa1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["PLANT"] --> B["Velocity"]
    B --> C["Position"]
    C --> D["Phase Plane"]
    D --> E["Gain1"]
    E --> F["Product"]
    F --> G["Gain2"]
    G --> H["Gain3"]
    H --> I["Epsilon = 1/Gain3"]
    I --> J["Sign1"]
    J --> K["+"]
    K --> L["Sign2"]
    L --> M["-"]
    M --> N["Dead Zone"]
    N --> O["Relay with Dead Zone"]
    O --> P["Sign3"]
    P --> Q["+"]
    Q --> R["0.5x_2|x_21"]
    R --> S["Gain2"]
    S --> T["0.5"]
    T --> U["Gain3"]
    U --> V["Epsilon = 1/Gain3"]
    V --> W["+"]
    W --> X["0.5x_2|x_21"]
    X --> Y["Gain2"]
    Y --> Z["0.5"]
    Z --> AA["Gain3"]
    AA --> AB["Epsilon = 1/Gain3"]
```
</details>

Figure 7.29 SIMULINK $^{©}$ Implementation of Fuel-Optimal Control Law
