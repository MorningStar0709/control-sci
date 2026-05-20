We can modify the nonlinear Simulink diagram shown in Fig. 6.13 and use the continuous equation (6.22) to model dry friction force. Figure 6.16 shows the Simulink diagram of the spool valve with the continuous dry friction force model. In this case, we have defined the dry friction force with the Fcn (or function) block from the User-Defined Functions library. The Fcn block allows the user to define any functional output equation in terms of a single input (u). To do so, the user must double-click the Fcn block and enter the desired equation in the Expression dialog box. Figure 6.16 shows Eq. (6.22) in the function block, where u is the generic symbol that represents the input to the block (velocity, ẏ , in this case). Note that the constant ?? is set to $1 0 ^ { - 4 }$ m/s. Executing the Simulink diagram in Fig. 6.16 produces a response for valve position y(t) that is essentially identical to the response shown in Fig. 6.14 for the nonlinear Simulink diagram that uses the discontinuous signum function for the dry friction force.

![](image/733d9a26bf759426d32051bf2c57089a2894294c69b3711c35fe0ec0b7b9c363.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Step force f(t)"] --> B["f(t)"]
    B --> C["+"]
    C --> D["Net force"]
    D --> E["1/0.04 Gain, 1/mass"]
    E --> F["y-ddot"]
    F --> G["1/s Integrator"]
    G --> H["y-dot"]
    H --> I["1/s Integrator1"]
    I --> J["y"]
    J --> K["To Workspace"]
    K --> L["t"]
    L --> M["Clock"]
    M --> N["To Workspace1"]
    N --> O["Dry friction function"]
    O --> P["0.4*u/sqrt(u^2 + 1e-4^2)"]
    P --> Q["7000 Gain, stiffness"]
    Q --> C
    R["16 Gain, viscous friction"] --> S["1/s Integrator"]
    S --> T["y"]
    T --> U["To Workspace"]
    U --> V["Dry friction Eq. (6.22)"]
    V --> O
```
</details>

Figure 6.16 Simulink diagram for Example 6.7: nonlinear mechanical system with continuous function for dry friction.
