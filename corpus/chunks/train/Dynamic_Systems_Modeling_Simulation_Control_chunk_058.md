# Example 2.2

The mechanical system shown in Fig. 2.11a is composed of a single mass m, a spring k, and a damper b. The vertical position of the mass is x, which is measured from the undeflected position of the spring.

Figure 2.11b shows the FBD of mass m, which includes the spring force, damper force, and gravitational force mg. Summing all external forces with downward as the positive sign convention (see Fig. 2.11a) and applying Newton’s second law, we obtain

$$+ \downarrow \sum F = - k x - b \dot {x} + m g = m \ddot {x}$$

Rearranging this equation with all dynamic variables on the left-hand side, we have

$$m \ddot {x} + b \dot {x} + k x = m g \tag {2.22}$$

![](image/60a98dcefed96fe6c17b0eeb5d23e382bd639d4eef796d039791059d95669a8a.jpg)

<details>
<summary>text_image</summary>

k
b
m
x
Undeflected
spring position
</details>

(a)

![](image/9d815f639c043c261a381fbb2c976ffe6afd42954fee6c2fd5c00dfbbdfd2947.jpg)

<details>
<summary>text_image</summary>

kx
bx
m
mg
</details>

(b)   
Figure 2.11 (a) Vertical mass–spring–damper system for Example 2.2 and (b) free-body diagram.

Equation (2.22) is the mathematical model of the vertical mass–spring–damper system for the case when displacement x is measured from the undeflected spring position. Note that the gravitational force mg appears on the right-hand side as an input to the mechanical system model.

We can rederive the mathematical model so that the gravitational force mg does not explicitly appear in the ODE. To begin, consider the case when the vertical mechanical system in Fig. 2.11a is at rest in static equilibrium, that is, ẍ = ẋ = 0. Therefore, from the mathematical model (2.22) we obtain kx = mg and the spring force balances the gravitational force. Define the static deflection of the spring as

$$d = \frac {m g}{k} \tag {2.23}$$

Next, define z as the position of the mass relative to its static deflection, so that the total deflection is $x = d + z .$ . In other words, when $z = 0$ , the mass is at its static deflection position, or x = d. We can compute the first and second time derivatives of $x = d + z$ to obtain ẋ = ḋ + ż and $\ddot { x } = \ddot { d } + \ddot { z }$ , which simplifies to ẋ = ż and ẍ = z̈ because the static deflection d is constant. Finally, we can substitute $\ddot { x } = \ddot { z } , \dot { x } = \dot { z } .$ , and $x = d + z$ into the mathematical model (2.22) to obtain

$$m \ddot {z} + b \dot {z} + k (d + z) = m g$$
