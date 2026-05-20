# Simulink Model

Figure 11.14 shows the Simulink model of the integrated solenoid actuator, which is a modified version of the solenoid model developed for Example 6.9. Figure 11.14 is slightly different from Fig. 6.28 as the armature position from the mechanical subsystem is fed back as an input to the electrical subsystem because inductance $L ( x )$ increases with x. Figure 11.15 shows the inner details of the electrical subsystem. The reader should be able to identify the back emf and electromagnetic force computations, Eqs. (11.13) and (11.15), in Fig. 11.15, as well as the summation of all voltage terms that appear in Eq. (11.9). A user-defined function Fcn divides the net voltage (from the summing junction) by the inductance $L ( x )$ in order to determine the time rate of current, ̇I. Note that inductance is simply $L ( x ) = L _ { 0 } + K x$ as we assumed that $K = d L / d x$ is constant.

![](image/19eaedf51f2a538b309beeb6794e553af57ed673ad9c12ed67764f4a9c5ff04d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Voltage input"] -->|e_in| B["e_in"]
    B --> C["x"]
    C --> D["xdot"]
    D --> E["Electrical subsystem"]
    E --> F["F_em"]
    F --> G["F_em"]
    G --> H["x"]
    H --> I["x"]
    I --> J["x"]
    J --> K["xDot"]
    K --> L["To Workspace1"]
    M["Clock"] --> N["t"]
    N --> O["To Workspace2"]
    P["x"] --> Q["x, position"]
    P --> R["x-dot, velocity"]
    S["Mechanical subsystem"] --> T["x"]
    T --> U["xDot"]
    U --> V["xDot"]
```
</details>

Figure 11.14 Simulink diagram for the solenoid actuator.

![](image/9da63db3b965ab73971a1885ad42d38cf3023827d1dd2dbe07014ee28898bf3b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Input voltage, e_in"] --> B["+"]
    C["Position, x"] --> D["x"]
    E["Position, x"] --> F["e_R"]
    G["Position, x"] --> H["R"]
    I["Position, x"] --> J["Resistance"]
    K["Position, x"] --> L["e_b"]
    M["Position, x"] --> N["K"]
    O["Position, x"] --> P["X"]
    Q["Position, x"] --> R["Product"]
    S["Position, x"] --> T["Back-emf constant dL/dx"]
    U["Input voltage, e_in"] --> V["+"]
    W["Net voltage"] --> X["u(1)/(L0 + K*u(2))"]
    X --> Y["I-dot"]
    Z["1/s"] --> AA["1/s"]
    AB["Current"] --> AC["u²"]
    AD["Math Function"] --> AE["0.5*K"]
    AF["Force constant 0.5 dL/dx"] --> AG["1"]
    AH["To Workspace"] --> AI["I"]
    AJ["Velocity, x-dot"] --> AK["3"]
    AL["xdot"] --> AM["Velocity, x-dot"]
```
</details>

Figure 11.15 Simulink diagram for the solenoid: electrical subsystem.
