Figure 11.61 shows the closed-loop step responses of the nonlinear and linearized maglev models. As before, the reference position $z _ { \mathrm { r e f } } ( t )$ is a 3-mm step function applied at time $t = 0 . 1 \ : \mathrm { s }$ . The nonlinear model response shows slightly more peak overshoot than the linearized model response but otherwise the two responses are very similar. The closed-loop response of the nonlinear maglev model (the true test for the controller design) is stable and tracks the reference command at steady state. Figure 11.62 shows that the controller voltage commands for the nonlinear and linearized models are very similar.

![](image/7f5a0f8f412095d9b9e0eee0ab66da1e93e8dad4f92188dbeb7ffb0358f8a063.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["1 e_in"] -->|Source voltage| B["+ -"]
    B --> C["1/0.018 1/L"]
    C --> D["I-dot"]
    D --> E["1/s"]
    E --> F["Coil current"]
    F --> G["1 I"]
    G --> H["5 Resistance, R"]
    H --> B
```
</details>

Figure 11.59 Nonlinear maglev system: electromagnet coil subsystem.

![](image/3a780ee0620d3b29fda5d9083a0f59127ddf74d1b98712c2c8ff63f2e03fa079.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    I["1"] -->|Current| A["×"]
    A -->|I^2| B["0.008829 K_F/m"]
    B --> C["× Product2"]
    C --> D["F_em/m"]
    D --> E["z-ddot"]
    E --> F["1/s Integrator"]
    F --> G["1/s Integrator1"]
    G --> H["Ball position, z"]
    H --> I["1 z"]
    I --> I1["9.81 Grav. accl"]
    I1 -->|g| D
    I --> I2["1/u Math function"]
    I2 -->|d - z^2| C
    I2 -->|d - z| D
    I2 -->|d - z| E
    I2 -->|d - z| F
    I2 -->|d - z| G
    I2 -->|d - z| H
```
</details>

Figure 11.60 Nonlinear maglev system: mechanical ball subsystem.

![](image/f909a22e5745a4ba77501b8af7b92b1a26d3ebc53318153b682897a3d6337c4a.jpg)

<details>
<summary>line</summary>

| Time, s | Nonlinear maglev model | Linearized maglev model | Reference step input |
| --- | --- | --- | --- |
| 0.1 | 0.0072 | 0.0072 | 0.003 |
| 0.2 | 0.003 | 0.003 | 0.003 |
| 0.3 | 0.0033 | 0.0033 | 0.003 |
| 0.4 | 0.003 | 0.003 | 0.003 |
| 0.5 | 0.003 | 0.003 | 0.003 |
| 0.6 | 0.003 | 0.003 | 0.003 |
| 0.7 | 0.003 | 0.003 | 0.003 |
| 0.8 | 0.003 | 0.003 | 0.003 |
</details>

Figure 11.61 Closed-loop step responses of the linearized and nonlinear maglev systems using the lead-plus-integral controller.

![](image/7f0913c02106e1b59c4b505e311223e39ddc0b115955cae4dfa7e34d7bb38e27.jpg)

<details>
<summary>line</summary>
