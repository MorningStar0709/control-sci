B–4–10. Consider the liquid-level control system shown in Figure 4–52. The inlet valve is controlled by a hydraulic integral controller. Assume that the steady-state inflow rate is $\bar { Q }$ and steady-state outflow rate is also $\dot { \bar { Q } } .$ the steady-state, head is $\bar { H }$ steady-state pilot valve displacement is, $\dot { \bar { X } } = 0 .$ , and steady-state valve position is $\bar { Y }$ We assume that the set. point corresponds to the steady-state head The setH R . point is fixed. Assume also that the disturbance inflow rate $q _ { d } ,$ which is a small quantity, is applied to the water tank at $t = 0$ .This disturbance causes the head to change from $\bar { H }$ to $\bar { H } + h$ This change results in a change in the outflow rate. by $q _ { o }$ . Through the hydraulic controller, the change in head causes a change in the inflow rate from $\bar { Q }$ to $\bar { Q } + q _ { i }$ (The. integral controller tends to keep the head constant as much as possible in the presence of disturbances.) We assume that all changes are of small quantities.

We assume that the velocity of the power piston (valve) is proportional to pilot-valve displacement x, or

$$\frac {d y}{d t} = K _ {1} x$$

where $K _ { 1 }$ is a positive constant. We also assume that the change in the inflow rate $q _ { i }$ is negatively proportional to the change in the valve opening y, or

$$q _ {i} = - K _ {v} y$$

where $K _ { v }$ is a positive constant.

Assuming the following numerical values for the system,

$$C = 2 \mathrm{m} ^ {2}, \quad R = 0. 5 \sec / \mathrm{m} ^ {2}, \quad K _ {v} = 1 \mathrm{m} ^ {2} / \seca = 0. 2 5 \mathrm{m}, \quad b = 0. 7 5 \mathrm{m}, \quad K _ {1} = 4 \sec^ {- 1}$$

obtain the transfer function $H ( s ) / Q _ { d } ( s )$ .

![](image/67c2582006d153aab5a2800ad7bdc9fbd5a450e62f4cd91ba0a6a60c901db70c.jpg)

<details>
<summary>text_image</summary>

a
b
x
h
\bar{Y} + y
\bar{Q} + q_i
q_d
\bar{H} + h
C (Capacitance)
R
\bar{Q} + q_o
(Resistance)
</details>

Figure 4–52 Liquid-level control system.

B–4–11. Consider the controller shown in Figure 4–53.The input is the air pressure $p _ { i }$ measured from some steady-state reference pressure $\bar { P }$ and the output is the displacement y of the power piston. Obtain the transfer function $Y ( s ) / P _ { i } ( s )$ .

![](image/92165b14e0dbdb2c50d19cda81f35207a4f2733dda2deaf286678c38cbe92517.jpg)

<details>
<summary>text_image</summary>

Air p_i (Input)
Bellows
x
a
a
k
b
b
y (Output)
</details>

Figure 4–53   
Controller.
