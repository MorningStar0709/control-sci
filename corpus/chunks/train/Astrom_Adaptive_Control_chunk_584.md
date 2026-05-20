To make sure that the closed-loop system is stable for small perturbations around an equilibrium of pH = 7, the gain should thus be less than 0.009. A reasonable value of the gain for operation at pH = 8 is k = 0.01, but this gain will give an unstable system at pH = 7 and is too low for a reasonable response at pH = 9. Figure 9.10 shows PI control with gain 0.01 and reset time 1. The process is started at equilibrium pH = 4. The reference value is then changed to 7, 8, and 9.

![](image/0b045989a851675a6707ea69786431c87ceb2218168294ba634011fc8fbea9a6.jpg)

<details>
<summary>line</summary>

| Time | Output pH (a) | Output pH (b) | Output pH (c) | Input u (a) | Input u (b) | Input u (c) | Concentration x (a) | Concentration x (b) | Concentration x (c) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 4 | 4 | 0.9 | 0.9 | 0.9 | -1e-4 | -1e-4 | -1e-4 |
| 2 | 8 | 8 | 8 | 1.0 | 1.0 | 1.0 | -5e-5 | -5e-5 | -5e-5 |
| 4 | 8 | 8 | 8 | 1.0 | 1.0 | 1.0 | 0 | 0 | 0 |
| 6 | 8 | 8 | 8 | 1.0 | 1.0 | 1.0 | 0 | 0 | 0 |
| 8 | 8 | 8 | 8 | 1.0 | 1.0 | 1.0 | 0 | 0 | 0 |
| 10 | 8 | 8 | 8 | 1.0 | 1.0 | 1.0 | 0 | 0 | 0 |
</details>

Figure 9.10 Output pH and control signal when the process in Example 9.8 is controlled by using a PI controller when $pH_{ref}$ is (a) 7; (b) 8; (c) 9.

The calculations and the simulation illustrate the key problems with pH control. The difficulties are compounded by the presence of time delays and flow variations. One way to get around the problem is to use the concentration x as the output rather than pH. Figure 9.11 shows a possible control scheme in which the measured pH and the reference value of pH are transformed into equivalent concentrations. This means that the variable x is computed for the

![](image/0656cb1c734daf9e7bcb65500c97d146ce018d736b2210b786e0f3cecc3e9f84.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["pH_ref"] --> B["Eq. (9.22)"]
    B --> C["x_ref"]
    C --> D["Σ"]
    D --> E["PI"]
    E --> F["u"]
    F --> G["Pump"]
    G --> H["Process"]
    H --> I["pH"]
    I --> J["pH gauge"]
    J --> K["x"]
    K --> L["Eq. (9.22)"]
    L --> M["-"]
    M --> D
```
</details>

Figure 9.11 Control configuration for the pH control problem in Example 9.8.

![](image/890e74016122754f33b88b8d7be22205460b885151d273771796678f611037c3.jpg)

<details>
<summary>line</summary>
