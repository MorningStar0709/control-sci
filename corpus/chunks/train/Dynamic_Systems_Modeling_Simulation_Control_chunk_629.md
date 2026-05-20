# 10.5 A closed-loop control system is shown in Fig. P10.5.

![](image/aa55b6068fd064c9f774440c0b72f4d24ffdbd4e26f699f06c49e71b059b3325.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r_t["r(t)"] --> adder["+"]
    adder --> e_t["e(t)"]
    e_t --> K1["K₁"]
    K1 --> adder
    adder --> integrator["1/(s+4)"]
    integrator --> 1_s["1/s"]
    1_s --> y_t["y(t)"]
    y_t --> K2["K₂"]
    K2 --> adder
    adder --> minus1["-"]
    minus1 --> adder
```
</details>

Figure P10.5

a. Compute the closed-loop transfer function for the overall system, $T ( s ) = Y ( s ) / R ( s )$   
b. Two gain pairs are considered: Option 1 $( K _ { 1 } = 1 5 , K _ { 2 } = 2 )$ ) and Option $2 \left( K _ { 1 } = 3 0 , K _ { 2 } = 3 \right)$ ). Which gain pair provides the greatest closed-loop damping ratio? Justify your answer.

10.6 Figure P10.6 shows a unity-feedback closed-loop system. The reference input is a ramp, $r ( t ) = 0 . 2 t .$

![](image/f076d5e86173a0b4df1ca63ff2c89cf3138588f9d954524817f206791d7d9eca.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["e(t)"]
    C --> D["Gc(s)"]
    D --> E["u(t)"]
    E --> F["3/(s² + 4s)"]
    F --> G["Output, y(t)"]
    G --> H["Feedback Loop"]
    H --> B
```
</details>

Figure P10.6

a. Compute the steady-state tracking error if the controller $G _ { C } ( s )$ is a simple proportional gain $K _ { P } = 2$   
b. Compute the steady-state tracking error if we use a PI controller with gains $K _ { P } = 3$ and $K _ { I } = 1 . 5$

10.7 A simple closed-loop PI control system is shown in Fig. P10.7.

![](image/b10e13147f6653218dccce4727b922b0a20a702ef30d665e527c084b1272e67d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["e(t)"]
    C --> D["\frac{K_P s + K_I}{s}"]
    D --> E["u(t)"]
    E --> F["\frac{1}{(s + 2)(s + 8)}"]
    F --> G["Output, y(t)"]
    G --> H["-"]
    H --> B
```
</details>

Figure P10.7

a. Show that the closed-loop system is stable for PI gains $K _ { P } = 5$ and $K _ { I } = 2 5$ .   
b. Determine “by hand” the closed-loop output y(t) at time t = 8 s if the reference input is a ramp function $r ( t ) = 1 . 4 t .$ . Use the PI gains from part (a).
