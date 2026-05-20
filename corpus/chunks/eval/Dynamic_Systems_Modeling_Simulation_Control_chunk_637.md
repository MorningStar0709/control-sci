```mermaid
graph LR
    A["Reference position input (m), x_ref(t)"] --> B((+))
    B --> C["G_C(s)"]
    C --> D["Controller"]
    D --> E["K_V"]
    E --> F["Solenoid-valve gain"]
    F --> G["Pneumatic servo"]
    G --> H["Piston position (m), x(t)"]
    H --> I["-"]
    I --> B
    J["Voltage, e_in(t)"] --> E
    K["Valve position (m), u(t)"] --> F
```
</details>

Figure P10.24

10.25 A simplified version of the Space Shuttle’s Flare and Shallow Glide Slope normal acceleration command channel is shown in Fig. P10.25. The input is a flight-path angle command, $\gamma _ { C }$ (in rad), and the output is an incremental normal acceleration command, $\Delta n _ { Z }$ (in units of $^ { \ast } g ^ { \prime \prime } )$ . Note that dividing the flight-path angle error $\gamma _ { e }$ by time constant ?? produces the approximate angular rate d??/dt, which is then multiplied by velocity V to produce normal acceleration. Earth gravity acceleration is $\dot { g } = 3 2 . 2 \mathrm { f t } / \mathrm { s } ^ { 2 }$ , and the Shuttle’s velocity is V = 420 ft/s during the Flare and Shallow Glide Slope phase.

![](image/e175f8e4c6a0d6fd3b52bcfd74842c9d760bd017fe393fe59011752324012635.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Flight-path angle command (rad), γ_C"] --> B["+"]
    B --> C["γ_e"]
    C --> D["1/τ"]
    D --> E["dγ/dt (rad/s)"]
    E --> F["V/g"]
    F --> G["Δn_Z"]
    G --> H["Incremental normal acceleration (g's)"]
    H --> I["1/s"]
    I --> J["-"]
    J --> B
```
</details>

Figure P10.25

Use Simulink to simulate the closed-loop response to a step-input flight-path angle command $\gamma _ { C } ( t ) =$ 0.09U(t) rad. Adjust the time constant ?? so that the incremental normal acceleration $\Delta n _ { Z } ( t )$ shows a peak value equal to 0.4 g. Plot $\Delta n _ { Z } ( t )$ for the best design value for ?? and describe the closed-loop response for the incremental normal acceleration. Relate the time constant ?? to the settling time.
