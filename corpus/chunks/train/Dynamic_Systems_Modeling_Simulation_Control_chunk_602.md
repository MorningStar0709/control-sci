Suppose we choose to implement a PD controller with an open-loop zero at s = −4 that is preceded by a low-pass filter with corner frequency $\omega _ { c } = 1 5 \mathrm { r a d / s }$ . Figure 10.46a shows this controller structure with the unity-gain low-pass filter $G _ { \mathrm { L P } } ( s )$ and PD controller $G _ { C } ( s )$ in series. The product of the low-pass filter and PD controller is

$$G _ {\mathrm{LP}} (s) G _ {C} (s) = \frac {1 5}{s + 1 5} K (s + 4) \tag {10.52}$$

We can factor the low-pass filter’s numerator gain (=15) into the arbitrary control gain $K _ { 1 } = 1 5 K$ to yield

$$G _ {\mathrm{LF}} (s) = \frac {K _ {1} (s + 4)}{s + 1 5} \tag {10.53}$$

The controller presented by Eq. (10.53) and shown in Fig. 10.46b is called a lead controller or lead filter. The name arises from the fact that this transfer function adds phase lead at low frequencies. Figure 10.47 shows the Bode diagram for the following PD and lead controllers:

$$
\begin{array}{l l} \text {PD controller:} & 0. 2 5 (s + 4) \\ \text {Lead controller:} & \frac {3 . 7 5 (s + 4)}{s + 1 5} \end{array}
$$

![](image/125d75cb4e05b4e961d746fb55af502a355e726f0d9710690e0c9d2c9931ca67.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference input, r(t)"] --> B((+))
    B --> C["Error, e(t)"]
    C --> D["15/(s + 15) Low-pass filter"]
    D --> E["Filtered error, e_F(t)"]
    E --> F["G_C(s) PID controller"]
    F --> G["Control signal, u(t)"]
    G --> H["G_P(s) Plant"]
    H --> I["Output, y(t)"]
    I --> J["Feedback to B"]
    J --> B
```
</details>

Figure 10.45 PID controller with low-pass filter 15/(s + 15).

![](image/9ce11e4af84862414c06cf1806c00efedb2d523b6887d18709eac454b326d9d7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Error, e(t)"] --> B["15/(s + 15)"]
    B --> C["Filtered error, e_F(t)"]
    C --> D["K(s + 4)"]
    D --> E["Control signal, u(t)"]
    F["Unity-gain low-pass filter"] --> B
    G["PD controller"] --> D
```
</details>

![](image/2e0b2e0cd85d041370fdfa6d5259c1eec8f438ef2ce1525b579dda741f3dca74.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Error, e(t)"] --> B["Lead controller (b)"]
    C["Equivalent"] --> B
    B --> D["Control signal, u(t)"]
```
</details>

Figure 10.46 Equivalent controllers: (a) low-pass filter + PD controller and (b) lead controller.   
![](image/0e597ab7a385778f176f81b807c4ed49f51247993f62fcd0f9de244a1ef00515.jpg)

<details>
<summary>line</summary>
