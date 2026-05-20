B–7–32. Referring to the closed-loop system shown in Figure 7–166, design a lead compensator $G _ { c } ( s )$ such that the phase margin is $4 5 ^ { \circ }$ , gain margin is not less than 8 dB, and the static velocity error constant $K _ { v }$ is $4 . 0 \ \mathrm { s e c } ^ { - 1 }$ . Plot unit-step and unit-ramp response curves of the compensated system with MATLAB.

![](image/53bcacdb32a8152fd441263d7c33802d0c0e72b40aebb8deca9296d3bfd9305c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["K/(s(0.1s+1)(s+1))"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> A
```
</details>

Figure 7–166

Closed-loop system.

B–7–33. Consider the system shown in Figure 7–167. It is desired to design a compensator such that the static velocity error constant is 4 sec–1, phase margin is $5 0 ^ { \circ }$ , and gain margin is 8 dB or more. Plot the unit-step and unitramp response curves of the compensated system with MATLAB.

![](image/63ea842c48a4c7d30f255b32b9715571f520378acb09b0c926a9c8a1e1e29738.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> +
    + --> Gc["Gc(s)"]
    Gc --> Hydraulic["1/s"]
    Hydraulic --> Aircraft["Aircraft (2s + 0.1)/(s² + 0.1s + 4)"]
    Aircraft --> C
    C --> Rate["Rate gyro"]
    Rate --> +
    + --> +
    + --> -
    - --> +
    - --> -
    - --> -
    - --> -
```
</details>

Figure 7–167

Control system.

B–7–34. Consider the system shown in Figure 7–168. Design a lag–lead compensator such that the static velocity error constant $K _ { v }$ is 20 sec–1, phase margin is $6 0 ^ { \circ }$ , and gain margin is not less than 8 dB. Plot the unit-step and unitramp response curves of the compensated system with MATLAB.

![](image/f8a070b8e8e7da10b78ca558310e674f64d1dad480381465cd23a18e7f0f3e8e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["1/(s(s+1)(s+5))"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> A
```
</details>

Figure 7–168

Control system.

![](image/0f9d37b682a3f387fa09040551faf3e7a4c8c145605a016e13ccf7b7e1021092.jpg)

<details>
<summary>text_image</summary>

8
</details>
