# EXAMPLE PROBLEMS AND SOLUTIONS

A–4–1. In the liquid-level system of Figure 4–27 assume that the outflow rate $Q \mathrm { m } ^ { 3 } /$ sec through the outflow valve is related to the head H m by

$$Q = K \sqrt {H} = 0. 0 1 \sqrt {H}$$

Assume also that when the inflow rate Q is 0.015 m3 sec the head stays constant. For $t < 0$ the system is at steady state $\left( Q _ { i } = 0 . 0 1 5 \mathrm { m } ^ { 3 } / \mathrm { s e c } \right)$ . $\mathbf { A } \mathfrak { t } t = 0$ the inflow valve is closed and so there is no inflow for $t \geq 0 ,$ . Find the time necessary to empty the tank to half the original head. The capacitance C of the tank is $2 \mathrm { m } ^ { 2 } .$ .

Solution. When the head is stationary, the inflow rate equals the outflow rate. Thus head $H _ { o }$ at $t = 0$ is obtained from

$$0. 0 1 5 = 0. 0 1 \sqrt {H _ {o}}$$

or

$$H _ {o} = 2. 2 5 \mathrm{m}$$

The equation for the system for $t > 0$ is

$$- C d H = Q d t$$

or

$$\frac {d H}{d t} = - \frac {Q}{C} = \frac {- 0 . 0 1 \sqrt {H}}{2}$$

Hence

$$\frac {d H}{\sqrt {H}} = - 0. 0 0 5 d t$$

Assume that, at $t = t _ { 1 } , H = 1 . 1 2 5$ m. Integrating both sides of this last equation, we obtain

$$\int_ {2. 2 5} ^ {1. 1 2 5} \frac {d H}{\sqrt {H}} = \int_ {0} ^ {t _ {1}} (- 0. 0 0 5) d t = - 0. 0 0 5 t _ {1}$$

It follows that

$$2 \sqrt {H} \left| _ {2. 2 5} ^ {1. 1 2 5} = 2 \sqrt {1 . 1 2 5} - 2 \sqrt {2 . 2 5} = - 0. 0 0 5 t _ {1} \right.$$

or

$$t _ {1} = 1 7 5. 7$$

Thus, the head becomes half the original value (2.25 m) in 175.7 sec.

![](image/11614908cdddb5b07454acffa77deb87dc69e5d4407f9e7e601159d3fe5ad291.jpg)

<details>
<summary>text_image</summary>

Q_i →
Capacitance C
H
→ Q
</details>

Figure 4–27 Liquid-level system.

A–4–2. Consider the liquid-level system shown in Figure 4–28. In the system, $\textstyle { \bar { Q } } _ { 1 }$ and ${ \bar { Q } } _ { 2 }$ are steady-state inflow rates and $\boldsymbol { \bar { H } } _ { 1 }$ and $\textstyle { \overline { { H } } } _ { 2 }$ are steady-state heads.The quantities $q _ { i 1 } , q _ { i 2 } , h _ { 1 } , h _ { 2 } , q _ { 1 }$ , and $q _ { o }$ are considered small. Obtain a state-space representation for the system when $h _ { 1 }$ and $h _ { 2 }$ are the outputs and $q _ { i 1 }$ and $q _ { i 2 }$ are the inputs.

Solution. The equations for the system are

$$C _ {1} d h _ {1} = \left(q _ {i 1} - q _ {1}\right) d t \tag {4-32}\frac {h _ {1} - h _ {2}}{R _ {1}} = q _ {1} \tag {4-33}C _ {2} d h _ {2} = \left(q _ {1} + q _ {i 2} - q _ {o}\right) d t \tag {4-34}\frac {h _ {2}}{R _ {2}} = q _ {o} \tag {4-35}$$

Elimination of $q _ { 1 }$ from Equation (4–32) using Equation (4–33) results in
