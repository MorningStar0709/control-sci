In the present analysis we assume that the load reactive forces are small, so that the leakage flow rate and oil compressibility can be ignored.

Referring to Figure $4 \mathrm { - } 1 7 ( \mathrm { a } )$ , we see that the rate of flow of oil q times dt is equal to the power-piston displacement $d y$ times the piston area A times the density of oil $\rho .$ Thus, we obtain

$$A \rho d y = q d t$$

Notice that for a given flow rate q the larger the piston area A is, the lower will be the velocity $d y / d t$ . Hence, if the piston area A is made smaller, the other variables remaining constant, the velocity $d y / d t$ will become higher. Also, an increased flow rate q will cause an increased velocity of the power piston and will make the response time shorter.

Equation (4–27) can now be written as

$$\Delta P = \frac {1}{K _ {2}} \left(K _ {1} x - A \rho \frac {d y}{d t}\right)$$

The force developed by the power piston is equal to the pressure difference $\Delta P$ times the piston area A or

Force developed by the power piston $= A \Delta P$

$$= \frac {A}{K _ {2}} \left(K _ {1} x - A \rho \frac {d y}{d t}\right)$$

![](image/9fdeacaab176cbb40c9bc42db04bee7470a6612b485423c593c251e9f686d6cc.jpg)

<details>
<summary>text_image</summary>

x = 2x₁
x = x₁
x = 0
x = -x₁
x = -2x₁
q
0
ΔP
</details>

Figure 4–18 Characteristic curves of the linearized hydraulic servomotor.

For a given maximum force, if the pressure difference is sufficiently high, the piston area, or the volume of oil in the cylinder, can be made small. Consequently, to minimize the weight of the controller, we must make the supply pressure sufficiently high.

Assume that the power piston moves a load consisting of a mass and viscous friction. Then the force developed by the power piston is applied to the load mass and friction, and we obtain

$$m \ddot {y} + b \dot {y} = \frac {A}{K _ {2}} \left(K _ {1} x - A \rho \dot {y}\right)$$

or

$$m \ddot {y} + \left(b + \frac {A ^ {2} \rho}{K _ {2}}\right) \dot {y} = \frac {A K _ {1}}{K _ {2}} x \tag {4-28}$$

where m is the mass of the load and b is the viscous-friction coefficient.

Assuming that the pilot-valve displacement x is the input and the power-piston displacement y is the output, we find that the transfer function for the hydraulic servomotor is, from Equation (4–28),
