First, write a MATLAB program such that the nested loops in the program start with the highest values of K and a and step toward the lowest and the computation stops when a successful set of K and a is found for the first time.

Next, write a MATLAB program that will find all possible sets of K and a that will satisfy the given specifications.

Among multiple sets of K and a that satisfy the given specifications, determine the best choice.Then, plot the unitstep response curves of the system with the best choice of K and a.

B–8–13. Consider the two-degrees-of-freedom control system shown in Figure 8–80. The plant $G _ { p } ( s )$ is given by

$$G _ {p} (s) = \frac {3 (s + 5)}{s (s + 1) \left(s ^ {2} + 4 s + 1 3\right)}$$

Design controllers $G _ { c 1 } ( s )$ and $G _ { c 2 } ( s )$ such that the response to the unit-step disturbance input should have small amplitude and settle to zero quickly (in approximately 2 sec). The response to the unit-step reference input should be such that the maximum overshoot is 25% (or less) and the settling time is 2 sec. Also, the steady-state errors in the response to the ramp and acceleration reference inputs should be zero.

![](image/b1f2d638d59d137e810dbca8213073eaf1ee3e6e88a7935f0d17ea494f157055.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum
    Sum --> Gc["Gc(s)"]
    Gc --> |1.2 / (0.3s + 1)(s + 1)(1.2s + 1)| C["s"]
    C --> |feedback| Sum
    PID["PID controller"] --> Sum
```
</details>

Figure 8–79   
Control system.

![](image/107e071cb784ce497420455346d01ec21b86730cf7b1dd15bb9b147fedec2824.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["R(s)"] --> |+| Sum1["+"]
    Sum1 --> Gc1["Gc1(s)"]
    Gc1 --> |+| Sum2["+"]
    Sum2 --> U["U(s)"]
    U --> |+| Sum3["+"]
    Sum3 --> Gp["Gp(s)"]
    Gp --> Y["Y(s)"]
    Y --> |B(s)| Sum1
    D["D(s)"] --> |+| Sum2
    D --> |+| Sum3
```
</details>

Figure 8–80   
Two-degrees-of-freedom control system.

B–8–14. Consider the system shown in Figure 8–81. The plant $G _ { p } ( s )$ is given by

$$G _ {p} (s) = \frac {2 (s + 1)}{s (s + 3) (s + 5)}$$
