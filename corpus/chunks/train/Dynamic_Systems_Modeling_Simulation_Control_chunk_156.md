# Fluid Capacitance

The capacitance of a fluid reservoir or tank is a measure of its ability to store energy due to fluid pressure. For hydraulic systems (liquids), the fluid capacitance C is usually defined as the ratio of the change in volume V to the change in pressure P

$$C = \frac {d V}{d P} \tag {4.10}$$

Hydraulic fluid capacitance has units of $\mathrm { m } ^ { 3 } / \mathrm { P a }$ or $\mathrm { m } ^ { 5 } / \mathrm { N }$ . Figure 4.6 shows a reservoir (tank) with constant circular cross-sectional area A partially filled with a liquid. The pressure at the base of the tank is determined from the hydrostatic equation

$$P = \rho g h + P _ {\mathrm{atm}} \tag {4.11}$$

where g is the gravitational acceleration, h is the height of the liquid, and $P _ { \mathrm { a t m } }$ is the atmospheric pressure. Base pressure is the sum of the atmospheric pressure (acting at the surface) and the weight of the column of liquid (??gAh) divided by its area (A). We can compute the fluid capacitance of the tank using Eq. (4.10) by noting that volume is $V = A h$ , and hence the differential is $d V = A d h$ . Next, we can compute the differentials of both sides of the hydrostatic equation (4.11) for an incompressible fluid $( \rho = \mathrm { c o n s t a n t } )$ to yield

$$d P = \rho g d h \tag {4.12}$$

Using Eqs. (4.10), (4.12), and the differential $d V = A d h$ , the fluid capacitance of the tank is

$$C = \frac {d V}{d P} = \frac {A d h}{\rho g d h} = \frac {A}{\rho g} \tag {4.13}$$

Therefore, the fluid capacitance $d V / d P$ of a hydraulic reservoir with a constant cross-sectional area containing an incompressible fluid is a constant.

The fluid capacitance definition (4.10) can be rewritten by separating variables

$$C d P = d V \tag {4.14}$$

![](image/d89fd96d79cb1cc6ae04c02eb55a42a7e873594b7722ed8b403b514d13d2234f.jpg)

<details>
<summary>text_image</summary>

Atmospheric pressure, P_atm
Area, A
h
Pressure at base, P
</details>

Figure 4.6 Hydraulic reservoir.

Dividing both sides of Eq. (4.14) by dt yields

$$C \dot {P} = \dot {V} = Q \tag {4.15}$$

Equation (4.15) is analogous to the fundamental equation of an electrical capacitor, $C \dot { e } _ { C } = I ,$ , which states that the product of electrical capacitance and the time-rate of voltage is equal to the current flow through the capacitor. Thus, in the hydraulic tank system, pressure is analogous to electric potential (voltage) and volumetric-flow rate $Q$ is analogous to electrical current. Let us revisit Eq. (4.15) when we apply the conservation of mass to a control volume (CV) in a fluid system.
