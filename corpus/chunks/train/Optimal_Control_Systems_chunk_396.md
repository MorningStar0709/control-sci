# 7.3 Fuel-Optimal Control Systems

Fuel-optimal control systems arise often in aerospace systems where the vehicles are controlled by thrusts and torques. These inputs like thrusts are due to the burning of fuel or expulsion of mass. Hence, the natural question is weather we can control the vehicle to minimize the fuel consumption. Another source of fuel-optimal control systems is nuclear reactor control systems where fuel remains within the system and not expelled out of the system like in aerospace systems.

![](image/467e225df0ab8601bb5a29b4079bea27770612149e571802dfcf503714d2c9ff.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["1/s"]
    B --> C["x_2"]
    C --> D["1/s"]
    D --> E["x_1"]
    E --> F["Phase Plane"]
    F --> G["Gain"]
    G --> H["0.5"]
    H --> I["abs(u)"]
    I --> J["Product"]
    J --> K["0.5x_2|x_2"]
    K --> L["+"]
    L --> M["z"]
    M --> N["-z"]
    N --> O["Relay"]
    O --> P["Inverter"]
    P --> Q["-1"]
    Q --> R["z"]
    R --> S["+"]
```
</details>

Figure 7.12 SIMULINK $^{©}$ Implementation of Time-Optimal Control Law

An interesting historical account is found in $[59]$ regarding fuel-optimal control as applicable to the terminal phase of the lunar landing problem $[100]$ of Apollo 11 mission, in which astronauts Neil Armstrong and Edwin Aldrin soft-landed the Lunar Excursion Module (LEM) “Eagle” on the lunar surface on July 20, 1969, while astronaut Michael Collins was in the orbit with Apollo Command Module “Columbia”.
