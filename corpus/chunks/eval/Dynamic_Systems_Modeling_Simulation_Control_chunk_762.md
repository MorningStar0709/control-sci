subgraph "Time-domain signals"
        J["+20 step"] --> K["+"]
        L["-20 step applied at t=1"] --> K
        K --> M["u"]
        M --> N["+"]
        N --> O["1/4 Gain, 1/4"]
        O --> P["1/s Integrator1"]
        P --> Q["z-dot"]
        Q --> R["1/s Integrator2"]
        R --> S["z"]
        S --> T["To Workspace"]
        U["0.5 Gain, 0.5"] --> V["x Product"]
        W["0.6 Gain, 0.6"] --> V
        V --> W
        X["10 Gain, 10"] --> Y["Gain, 10"]
    end

subgraph "Output Time"
        Z["Clock"] --> AA["t To Workspace2"]
    end
```
</details>

Figure C.13 Creating a subsystem for Eq. (C.12) (Example C.4).

![](image/0c0b56eb8f78178e50b346432313bca3ae0666271a25cc47fd80f466b93f7c24.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+20 step"] --> B["+"]
    C["-20 step applied at t=1"] --> B
    B --> D["u"]
    D --> E["z"]
    E --> F["To Workspace"]
    G["z-dot subsystem Eq. (C.12)"] --> H["y"]
    I["z-dot subsystem Eq. (C.13)"] --> J["y"]
    K["t"] --> L["Clock"]
    M["To Workspace1"] --> N["y"]
    O["To Workspace"] --> P["z"]
```
</details>

Figure C.14 Simulink model using subsystems (Example C.4).

![](image/19e029f8d7e8798936d50453a6ea591464663d6cfe3a1876643584982b481219.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1"] --> B["+"]
    B --> C["1/4"]
    C --> D["z-dot"]
    D --> E["1/s"]
    E --> F["1/s"]
    F --> G["1/z"]
    G --> H["10"]
    H --> I["Gain, 10"]
    I --> J["Product"]
    J --> K["z-dot*2"]
    K --> L["Gain, 0.5"]
    L --> M["+"]
    M --> B
```
</details>

Figure C.15 Block-diagram details of the z-ddot subsystem (Example C.4).

the inner model. Figure C.15 shows a screen shot of the dialog box that appears upon double clicking the z-ddot subsystem in Fig. C.14. This dialog box presents the subsystem’s inner block-diagram details for representing Eq. (C.13).
