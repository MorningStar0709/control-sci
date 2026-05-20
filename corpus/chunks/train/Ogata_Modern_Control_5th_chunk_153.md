Operation of this hydraulic servomotor is as follows. If input x moves the pilot valve to the right, port II is uncovered, and so high-pressure oil enters the right-hand side of the power piston. Since port I is connected to the drain port, the oil in the left-hand side of the power piston is returned to the drain. The oil flowing into the power cylinder is at high pressure; the oil flowing out from the power cylinder into the drain is at low pressure. The resulting difference in pressure on both sides of the power piston will cause it to move to the left.

Note that the rate of flow of oil $q \left( \mathrm { k g / s e c } \right)$ times dt (sec) is equal to the power-piston displacement dy (m) times the piston area $A \left( \mathbf { m } ^ { 2 } \right)$ times the density of oil $\rho \left( \mathrm { k g } / \mathrm { m } ^ { 3 } \right)$ ). Therefore,

$$A \rho d y = q d t \tag {4-30}$$

Because of the assumption that the oil flow rate $q$ is proportional to the pilot-valve displacement x, we have

$$q = K _ {1} x \tag {4-31}$$

where $K _ { 1 }$ is a positive constant. From Equations (4–30) and (4–31) we obtain

$$A \rho \frac {d y}{d t} = K _ {1} x$$

![](image/0250bf4a21e9cf17bb4d920de797d27ea25bc025516aa9fc884d6a7f9ebab7a3.jpg)

<details>
<summary>text_image</summary>

Oil
under
pressure
Pilot valve
x →
Port I
Port II
Power cylinder
y ←
</details>

Figure 4–19 Hydraulic servomotor.

The Laplace transform of this last equation, assuming a zero initial condition, gives

$$A \rho s Y (s) = K _ {1} X (s)$$

or

$$\frac {Y (s)}{X (s)} = \frac {K _ {1}}{A \rho s} = \frac {K}{s}$$

where $K = K _ { 1 } / ( A \rho )$ . Thus the hydraulic servomotor shown in Figure 4–19 acts as an integral controller.

Hydraulic Proportional Controller. It has been shown that the servomotor in Figure 4–19 acts as an integral controller. This servomotor can be modified to a proportional controller by means of a feedback link. Consider the hydraulic controller shown in Figure 4–20(a). The left-hand side of the pilot valve is joined to the left-hand side of the power piston by a link ABC. This link is a floating link rather than one moving about a fixed pivot.
