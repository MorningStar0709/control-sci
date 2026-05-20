# PROBLEMS

B–8–1. Consider the electronic PID controller shown in Figure 8–70. Determine the values of $R _ { 1 } , R _ { 2 } , R _ { 3 } , R _ { 4 } , C _ { 1 } ,$ and $C _ { 2 }$ of the controller such that the transfer function $G _ { c } ( s ) = E _ { o } ( s ) / E _ { i } ( s )$ is

$$G _ {c} (s) = 3 9. 4 2 \left(1 + \frac {1}{3 . 0 7 7 s} + 0. 7 6 9 2 s\right)= 3 0. 3 2 1 5 \frac {(s + 0 . 6 5) ^ {2}}{s}$$

![](image/869304ccb70e5b0e24978ec8ae1af4f7aaa849137cc576691f33c065a8f73987.jpg)

<details>
<summary>text_image</summary>

C1
R1
R2 C2
Ei(s)
+
-
R3
R4
E(s)
+
-
Eo(s)
</details>

Figure 8–70 Electronic PID controller.

B–8–2. Consider the system shown in Figure 8–71. Assume that disturbances D(s) enter the system as shown in the diagram. Determine parameters K, a, and b such that the response to the unit-step disturbance input and the response to the unit-step reference input satisfy the following specifications: The response to the step disturbance input should attenuate rapidly with no steady-state error, and the response to the step reference input exhibits a maximum overshoot of 20% or less and a settling time of 2 sec.

B–8–3. Show that the PID-controlled system shown in Figure 8–72(a) is equivalent to the I-PD-controlled system with feedforward control shown in Figure 8–72(b).

B–8–4. Consider the systems shown in Figures 8–73(a) and (b). The system shown in Figure 8–73(a) is the system designed in Example 8–1. The response to the unit-step reference input in the absence of the disturbance input is shown in Figure 8–10. The system shown in Figure 8–73(b) is the I-PD-controlled system using the same $K _ { p } , T _ { i } $ , and $T _ { d }$ as the system shown in Figure 8–73(a).

![](image/1852f5f586127cceb275d8ab0c0fd4ae84d208e849df22b59cba3786a4568e4c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["K(as + 1) (bs + 1)/s"]
    C --> D["+"]
    D --> E["2(s + 2)/(s + 1) (s + 10)"]
    E --> F["C(s)"]
    F --> G["Feedback"]
    G --> B
    H["D(s)"] --> D
```
</details>

Figure 8–71 Control system.

![](image/6ab1dd22d80af090fd78c6c2868161d8e159b50fddb5e36b8327ae5038a2fe78.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["Kp(1 + 1/(Tf s) + Tds)"]
    C --> D["Gp(s)"]
    D --> E["C(s)"]
    E --> F["Feedback"]
    F --> B
```
</details>

(a)

![](image/a2eada80521a13ed65e84c57677f0b01118909698c7e59ff7d1272ed97677b90.jpg)

<details>
<summary>flowchart</summary>
