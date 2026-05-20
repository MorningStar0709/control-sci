a. Accurately sketch the temperature response T(t) if the container is a cardboard “to-go” cup with $R = 0 . 2 5 ^ { \circ } \mathrm { C - s / J } .$ .   
b. Accurately sketch the temperature response T(t) if the container is a thermos with $R = 5 . 5 ^ { \circ } \mathrm { C - s / J }$

7.31 Figure P7.31 shows the simplified, linear electrohydraulic actuator (EHA) model from Problem 5.27 in Chapter 5. The voltage input is a step function $e _ { \mathrm { i n } } ( t ) = 0 . 2 U ( t ) \mathrm { V } .$ . The amplifier output is initially zero and the valve is initially at static equilibrium $( z = 0 )$ .

![](image/30be822d3451ecb65a49efa1649bbffe996d68aa9512525425e55a917a2f1515.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input voltage, e_in(t)"] --> B["Power amplifier"]
    B --> C["Solenoid"]
    C --> D["Spool valve"]
    D --> E["Valve position, z (m)"]
    B -->|e_0| C
    C -->|Force, f (N)| D
```
</details>

Figure P7.31

a. Accurately sketch the response of the power amplifier output.   
b. Compute the steady-state position of the spool valve.   
c. Accurately sketch the response of the spool-valve position z(t). Label all important response characteristics on your sketch. Verify your sketch of z(t) with a simulation of the EHA valve response using MATLAB or Simulink. Plot z(t) from the simulation, and discuss the similarities and differences between the approximate sketch of valve position and the simulation result.

7.32 An engineer wants to develop a simple model for a DC motor, which is available in the lab with sensors to measure input voltage and shaft speed of the motor. With the motor initially at rest, she applies a constant 2-V input voltage and measures the following motor response characteristics: (a) the steady-state angular velocity of the motor is 85 rad/s, (b) the time to reach steady-state speed is 0.6 s, (c) the angular velocity response shows an exponential rise from zero to the steady-state speed without overshoot. Derive an appropriate transfer function for the DC motor based on the experimental data. Verify the engineer’s experimental results with a simulation of your model using MATLAB or Simulink.
