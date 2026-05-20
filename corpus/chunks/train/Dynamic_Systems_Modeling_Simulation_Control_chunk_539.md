# Example 10.1

Figure 10.5 shows the block diagram of the DC motor from Example 5.17. Derive the closed-loop transfer function T(s) that relates angular velocity ??(t) to source voltage $e _ { \mathrm { i n } } ( t )$ .

The DC motor consists of an armature circuit (RL circuit) and a mechanical rotor with friction b and inertia J. The feedback signal in Fig. 10.5 is the “back-emf ” voltage $e _ { b }$ that is induced by the angular velocity of the rotor windings. Hence, the DC motor shown in Fig. 10.5 is not a feedback control system; rather, it is an electromechanical system that possesses natural voltage feedback due to Faraday’s laws of induction. However, the DC motor shown in Fig. 10.5 is a closed-loop system and therefore we can determine its closed-loop transfer function using Eq. (10.4), where the forward transfer function G(s) is of the product of the three blocks in the forward path

$$G (s) = \frac {K _ {m}}{(L s + R) (J s + b)}$$

The feedback transfer function H(s) is the back-emf gain $K _ { b }$ . Using Eq. (10.4) and the definitions of G(s) and H(s), the closed-loop transfer function is

$$T (s) = \frac {G (s)}{1 + G (s) H (s)} = \frac {\frac {K _ {m}}{(L s + R) (J s + b)}}{1 + \frac {K _ {m} K _ {b}}{(L s + R) (J s + b)}} \tag {10.5}$$

![](image/fc84342e5af6fe3a4a82b7556a5426c5c7d56ccd89c6865c61662fc64578fb67.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Source voltage, e_in(t)"] --> B((+))
    B --> C["Armature circuit"]
    C --> D["Current, I"]
    D --> E["K_m"]
    E --> F["Motor torque, T_m"]
    F --> G["Mechanical rotor"]
    G --> H["Angular velocity, ω"]
    H --> I["G(s)"]
    I --> J["Back-emf constant"]
    J --> K["K_b"]
    K --> L["Back emf = K_bω"]
    L --> M["-"]
    M --> B
```
</details>

Figure 10.5 Block diagram of a DC motor (Example 10.1).

![](image/772beb414971907dcc726d1eb7ec0ae58dc382143d3731a440fda98a0a66ee20.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Source voltage, e_in(t)"] --> B["\frac{K_m}{(Ls + R)(Js + b) + K_m K_b}"]
    B --> C["Angular velocity, ω"]
```
</details>

Closed-loop transfer function T(s)   
Figure 10.6 Closed-loop transfer function representation of the DC motor (Example 10.1).

Multiplying the numerator and denominator in Eq. (10.5) by (Ls + R)(Js + b) in order to clear fractions we obtain

$$T (s) = \frac {K _ {m}}{(L s + R) (J s + b) + K _ {m} K _ {b}} \tag {10.6}$$
