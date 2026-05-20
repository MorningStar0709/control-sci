<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+"] --> B["1/0.5 Gain, 1/0.5"]
    B --> C["1/s Integrator"]
    C --> D["y"]
    D --> E["To Workspace1"]
    F["0.6 Gain, 0.6"] --> G["Sign"]
    G --> C
    H["1.4 Gain, 1.4"] --> I["z"]
    I --> J["+20 step"]
    J --> K["+"]
    K --> L["u"]
    L --> M["+/-"]
    M --> N["1/4 Gain, 1/4"]
    N --> O["1/s Integrator1"]
    O --> P["z-dot"]
    P --> Q["1/s Integrator2"]
    Q --> R["z"]
    R --> S["To Workspace"]
    T["0.5 Gain, 0.5"] --> U["× Product"]
    U --> V["z-dot^2"]
    V --> W["+20 step applied at t=1"]
    W --> X["+"]
    X --> Y["u"]
    Y --> Z["+/-"]
    Z --> AA["1/4 Gain, 1/4"]
    AA --> AB["1/s Integrator1"]
    AB --> AC["z-dot"]
    AC --> AD["1/s Integrator2"]
    AD --> AE["z"]
    AE --> AF["To Workspace2"]
    AG["10 Gain, 10"] --> AH["+"]
    AH --> AI["u"]
    AI --> AJ["+/-"]
    AJ --> AK["1/4 Gain, 1/4"]
    AK --> AL["1/s Integrator1"]
    AL --> AM["z-dot"]
    AM --> AN["1/s Integrator2"]
    AN --> AO["z"]
    AO --> AP["To Workspace2"]
    AQ["Clock"] --> AR["t"]
```
</details>

Figure C.11 Simulink model of nonlinear Eqs. (C.12) and (C.13) (Example C.4).

Figure C.11 shows that the signal ż is the first and second input to the Product block, which creates $\dot { z } ^ { 2 }$ as the output. The reader should be able to verify that the signal paths in Fig. C.11 correctly represent the system equations (C.12) and (C.13).

The desired input function is a rectangular pulse of 20 that lasts for 1 s. One way to create this input signal is to sum together two step functions: the first step has a constant value of 20 and “steps $\mathsf { u p } ^ { \mathsf { , , } }$ at time $t = 0 ,$ , and the second step has a constant value of −20 and “steps down” at time t = 1 s. Of course when they are summed together we get a pulse function with value 20 for $0 < t < 1$ s and zero input for $t \geq 1 \mathrm { s }$ . Figure C.11 shows the summation of the two Step blocks from the Sources library. The desired initial values, final values, and step times can be set in the dialog boxes of each Step block.
