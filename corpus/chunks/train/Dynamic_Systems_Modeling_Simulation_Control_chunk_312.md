# Nonlinear system simulation

Figure 6.17 shows a single tank with constant cross-sectional area A. It is being filled with water with input volumetric-flow rate $Q _ { \mathrm { i n } } .$ The output volumetric flow $Q _ { \mathrm { o u t } }$ is modeled by turbulent flow through the valve to atmospheric pressure $P _ { \mathrm { a t m } }$ . The nonlinear modeling equation for the hydraulic tank system is

$$C \dot {P} = Q _ {\text { in }} - K _ {T} \sqrt {P - P _ {\text { atm }}} \tag {6.23}$$

where C is the capacitance of the tank, P is the pressure at the base of the tank, and $K _ { T }$ is a turbulent flow coefficient.

We develop the nonlinear simulation first, using the following numerical parameters: cross-sectional area of the tank $A = \dot { 1 } . 9 6 2 \mathrm { m } ^ { 2 }$ , water density $\rho = 1 0 0 0 \mathrm { k g } / \mathrm { m } ^ { 3 }$ , turbulent flow coefficient $K _ { T } = 4 ( 1 0 ^ { - 4 } ) \mathrm { m } ^ { 3 . 5 } / \mathrm { k g } ^ { 0 . 5 }$ , and atmospheric pressure $P _ { \mathrm { a t m } } = 1 . 0 1 3 3 ( 1 0 ^ { 5 } ) \mathrm { N } / \mathrm { m } ^ { 2 }$ . Therefore, fluid capacitance is $C = \overset { \cdot } { A } / \rho g = 2 ( 1 0 ^ { - 4 } ) \mathrm { m ^ { 4 }  – s ^ { 2 } / k g }$ .

![](image/c9558d8644be03cfa6a4128f966675a8125aad7abfbf9ae1c2c2febcd777228e.jpg)

<details>
<summary>text_image</summary>

Input flow,
Qin
Base pressure, P
Patm
Valve
Qout
</details>

Figure 6.17 Hydraulic tank system for Example 6.8.

The Simulink diagram consists of a single integrator block that integrates the nonlinear state-variable equation for tank pressure P, which is obtained from Eq. (6.23)

$$\dot {P} = \frac {1}{C} \left(Q _ {\mathrm{in}} - K _ {T} \sqrt {P - P _ {\mathrm{atm}}}\right) \tag {6.24}$$
