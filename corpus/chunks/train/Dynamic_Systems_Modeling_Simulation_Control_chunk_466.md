# Engineering Applications

8.18 Figure P8.18 shows the simplified, linear electrohydraulic actuator (EHA) model from Problems 5.27 and 7.31. The voltage input is a step function $e _ { \mathrm { i n } } ( t ) = 0 . 2 U ( t )$ V. The amplifier output is initially zero and the valve is initially at static equilibrium $( z = 0 )$ ).

![](image/4585e39b4c740ae7e10b37fabb1679c7977c00a3073b9e0ee3eb490582ddfafb.jpg)

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

Figure P8.18

a. Use the final-value theorem to compute the steady-state position of the spool valve.   
b. Use Laplace methods to determine the amplifier voltage response, $e _ { 0 } ( t )$ , for the step input.   
c. Use Laplace methods to determine the force response of the solenoid, f (t), for the step input $e _ { \mathrm { i n } } ( t ) =$ $0 . 2 U ( t ) { \bar { \mathbf { V } } }$ .   
d. Use Laplace methods to determine the spool-valve position, z(t), for the step input $e _ { \mathrm { i n } } ( t ) = 0 . 2 U ( t ) \ : \mathrm { V }$ . Verify the steady-state position computed in part (a).

8.19 The LC circuit shown in Fig. P8.19 (originally presented in Problems 3.25 and 7.27) is connected to an antenna and is the basic circuit component used in electrical oscillators and frequency tuners. The system parameters are $L = 3$ mH and $C = 2 0 \mu \mathrm { F }$ . At time $t = 0 ^ { - }$ the capacitor is charged and its voltage is $e _ { C } ( 0 ) = 2 . 5 \ : \mathrm { V }$ , the switch is open, and there is no current in the circuit. At time $t = 0$ the switch is closed. Use Laplace transform methods to obtain the capacitor voltage $e _ { C } ( t )$ .

![](image/46b708d49b301d06f91ce6f55d9736d8e05af69464ddc6b6cfe73afb000fdb1d.jpg)

<details>
<summary>text_image</summary>

Antenna
Switch
L
C
</details>

Figure P8.19
