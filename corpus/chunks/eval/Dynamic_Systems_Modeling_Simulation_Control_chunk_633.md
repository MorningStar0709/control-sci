# 10.17 Figure P10.17 shows a closed-loop system with a PID controller.

![](image/1de93b6c88f62b56f7e193b7919dc7b526cb84872957d4e7b27f0ebf643fce66.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["e(t)"]
    C --> D["Gc(s)"]
    D --> E["u(t)"]
    E --> F["\frac{0.00027}{s^3 + 0.17s^2 + 0.008s + 0.0001}"]
    F --> G["Output, y(t)"]
    G --> H["-"]
    H --> B
    I["PID controller"] --> D
```
</details>

Figure P10.17

a. Use the Ziegler–Nichols reaction-curve method to select the PID control gains. Use MATLAB and Simulink as needed.   
b. Use Simulink to simulate the closed-loop response to a unit-step input, $r ( t ) = U ( t )$ , with the PID controller obtained in part (a). Plot y(t).   
c. Use the Simulink model from part (b) and vary the PID gains in an attempt to decrease the overshoot while maintaining a fast closed-loop response (use the Ziegler–Nichols gains from part (a) as the starting point). Plot the closed-loop response y(t) for an improved PID control scheme along with the output y(t) obtained in part (b) using the Ziegler–Nichols gains.

10.18 Repeat all parts of Problem 10.17 using the Ziegler–Nichols ultimate-gain method to design the PID controller.

10.19 Figure P10.19 shows the mechanical position-control system from Examples 10.6, 10.8, 10.12, and 10.13. The open-loop pole of the lead controller is $p _ { L }$ . The actuator gain is $K _ { A } = 2 \mathrm { N } / \mathrm { V } .$ .

![](image/dea90ed15e7a851c0fde8aa224fe48ab9656f03e3859001980ef0c1a51593163.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference position, x_ref(t)"] --> B((+))
    B --> C["Position error, x_e(t)"]
    C --> D["K(s + 3) / (s + p_L)"]
    D --> E["Lead controller"]
    E --> F["Actuator voltage, e_in(t)"]
    F --> G["K_A"]
    G --> H["Actuator gain (N/V)"]
    H --> I["Force, f(t)"]
    I --> J["Mechanical system dynamics"]
    J --> K["Position, x(t)"]
    K --> L["-"]
    L --> B
```
</details>

Figure P10.19

a. Use MATLAB to create the root-locus plots for four different lead controllers: $p _ { L } = 4 , 1 5 , 2 5 .$ , and 30.   
b. Interpret the four root-locus plots (and their corresponding closed-loop responses) for these four lead controllers. Compare these four root-locus plots to the results from Example 10.12 (PD controller) and Example 10.13 (lead controller). What conclusions can you draw regarding the open-loop pole location of the lead controller?
