```mermaid
graph LR
    R["s"] --> |+| A["+"]
    A --> |+| B["+"]
    B --> |16/(s + 0.8)| C["1/s"]
    C --> C["s"]
    C --> |k| A
```
</details>

Figure 5–76   
Block diagram of a system.

B–5–13. Figure 5–77 shows three systems. System I is a positional servo system. System II is a positional servo system with PD control action. System III is a positional servo system with velocity feedback. Compare the unit-step, unitimpulse, and unit-ramp responses of the three systems. Which system is best with respect to the speed of response and maximum overshoot in the step response?

B–5–14. Consider the position control system shown in Figure 5–78. Write a MATLAB program to obtain a unit-step response and a unit-ramp response of the system. Plot curves $x _ { 1 } ( t )$ versus $t , x _ { 2 } ( t )$ versus $t , x _ { 3 } ( t )$ versus t, and $e ( t )$ versus t Cwhere $e ( t ) = r ( t ) - x _ { 1 } ( t ) { \big ] }$ for both the unit-step response and the unit-ramp response.

![](image/7e9dd750e3e29f11dafbc0bb165fedbce686dbe45e9a5184a13123995159957a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["5"]
    C --> D["1/(s(5s+1))"]
    D --> E["C(s)"]
    E --> F["System I"]
    F --> B
```
</details>

![](image/972db2f9423eb92bb96089f55ca066f27fa6adb71d9f4120b55f55ea0e2c9c5f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["5(1 + 0.8s)"]
    C --> D["\frac{1}{s(5s + 1)}"]
    D --> E["C_II(s)"]
    E --> F["System II"]
    F --> B
```
</details>

![](image/7d61880b1451da0e44ffab87f9db350e1adf5462bda1e5e68fd09f83b27aaa64.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> B["+"] --> C["5"] --> D["1/(5s+1)"] --> E["1/s"] --> C_III["s"]
    C --> F["0.8"] --> A
    A --> G["System III"]
    G --> H["+"]
    H --> B
    B --> I["+"]
    I --> C
    C --> J["C_III(s)"]
```
</details>

Figure 5–77 Positional servo system (System I), positional servo system with PD control action (System II), and positional servo system with velocity feedback (System III).

![](image/d762edc939ecf7efed5253eb5bf2eb9e61f86a68f84c2d5a75ace65bc7cf405e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> A["+"] --> e --> 4 --> B["+"] --> 1/s --> x3 --> 5 --> 2/(0.1s+1) --> x2 --> 1/s --> x1
    x3 --> B
    x2 --> B
    x1 --> B
    B --> A
```
</details>

Figure 5–78 Position control system.
