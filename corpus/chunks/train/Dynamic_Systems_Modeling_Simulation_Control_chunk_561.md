# Example 10.7

Figure 10.22 shows a closed-loop system for controlling the pH balance in a chemical-processing system. The pH level of a solution in a stirred reaction tank is measured by a pH meter and fed back to form the pH error. The controller $G _ { C } ( s )$ uses the pH error to determine the acid/alkaline mixture ratio u(t) of the input flow stream to the tank (if $u > 0$ the input flow is alkaline, if $u < 0$ the input flow is acidic). Use the Ziegler–Nichols tuning rules to design a PID controller that provides a good closed-loop response for a step reference pH command $r ( t ) = 9$ (alkaline) if the solution in the tank is initially neutral $\mathrm { ( p H } = 7 )$ ).

![](image/17f352bdac7dae2770b21046bc45db4a8f28039ada0f379b03b179aa94e71269.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference pH, r(t)"] --> B((+))
    B --> C["Gc(s) Controller"]
    C --> D["Gp(s) Chemical process system dynamics"]
    D --> E["Tank pH, y(t)"]
    E --> F["H(s) pH meter"]
    F --> G["-"]
    G --> B
    H["pH error, e(t)"] --> C
    I["Acid/alkaline flow rate, u(t)"] --> D
```
</details>

Figure 10.22 Closed-loop pH control of a chemical-processing system (Example 10.7).
