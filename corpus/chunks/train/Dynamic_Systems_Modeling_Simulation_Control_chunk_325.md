<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1"] --> B["+"]
    C["F_em"] --> D["+"]
    B --> E["Net force"]
    D --> F["Net force"]
    E --> G["1/m"]
    F --> H["1/Mass"]
    G --> I["x-ddot"]
    H --> J["1/s"]
    I --> K["Integrator"]
    J --> L["Integrator1"]
    K --> M["x"]
    L --> N["x"]
    M --> O["2"]
    N --> P["2"]
    Q["Viscous friction force"] --> R["b"]
    S["Dry friction force"] --> T["F_dry"]
    U["Dry force"] --> V["k"]
    W["Spring force"] --> X["Spring constant"]
    Y["x-dot"] --> Z["Sign"]
    AA["x-dot"] --> AB["xDot"]
    AC["xDot"] --> AD["1/s"]
    AE["xDot"] --> AF["1/s"]
```
</details>

Figure 6.26 Simulink diagram for Example 6.9: mechanical subsystem.

![](image/c2a4b7905b59489095c0d72ca4c5db482f0e984a5bd48ba2d6b9c34f647b7d13.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["1\nF_em"] --> B["In1\nMechanical subsystem"]
    B --> C["Out1\nx"]
    B --> D["Out2\nxdot"]
```
</details>

Figure 6.27 Simulink subsystem for Example 6.9: mechanical subsystem.

![](image/7fdbd3bed97b8ce377d652335aa2547b53484220e346f18e1b20d8fbcb771694.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["10-V Step at t = 0.05 s"] -->|Voltage input| B["e_in"]
    B --> C["F_em"]
    C --> D["F_em"]
    D --> E["x"]
    E --> F["Position"]
    F --> G["x"]
    G --> H["To Workspace1"]
    H --> I["xdot"]
    I --> J["t"]
    J --> K["To Workspace2"]
    K --> L["Clock"]
    L --> M["Electrical subsystem"]
    M --> N["xdot"]
    N --> O["Mechanical subsystem"]
    O --> P["x"]
    P --> Q["Velocity"]
    Q --> R["x"]
    R --> S["To Workspace1"]
```
</details>

Figure 6.28 Simulink diagram for Example 6.9: integrated solenoid actuator system.

We can now simulate the integrated system. Table 6.1 presents the numerical values of the system parameters for the solenoid actuator. All integrators in the subsystem models are initialized with values of zero. MATLAB M-file 6.3 sets the required parameters and executes the Simulink model integrated\_EMA.mdl (Fig. 6.28) using the sim command (note that “EMA” denotes “electromagnetic actuator”). This M-file also plots the desired dynamic variables, current I(t) and armature–valve position x(t) (note that the M-file converts position to units of millimeters for the plot).

Table 6.1 System Parameters for the Solenoid Actuator (Example 6.9)
