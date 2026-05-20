# Example 5.10

Consider the simple hydraulic system shown in Fig. 5.4, which consists of a single tank with constant crosssectional area A being filled with a liquid with input volumetric-flow rate $Q _ { \mathrm { i n } } .$ . Output flow through the valve is turbulent. Our objective is to derive a linear model of the hydraulic tank dynamics given a nominal input volumetric-flow rate $Q _ { \mathrm { i n } } ^ { \ast }$ .

inWe see in Fig. 5.4 that the output volumetric-flow rate through the valve is $Q _ { \mathrm { o u t } }$ . The state variable for outthis system is pressure P at the base of the tank, and atmospheric pressure at the outlet of the valve is $P _ { \mathrm { a t m } } .$ The model for this simple hydraulic system can be derived from the conservation of mass, as demonstrated in Chapter 4

$$\frac {d V}{d P} \frac {d P}{d t} = C \dot {P} = Q _ {\text { in }} - Q _ {\text { out }} \tag {5.67}$$

where $C = d V / d P$ is the fluid capacitance of the tank. This capacitance is fixed because of its constant crosssectional area. Turbulent valve flow is represented by the nonlinear equation

$$Q _ {\text { out }} = K _ {T} \sqrt {P - P _ {\text { atm }}} \tag {5.68}$$

![](image/0896c099814b42b85be32e78dfce2a7423b3d03206caf62ed4403af5f4bebbf9.jpg)

<details>
<summary>text_image</summary>

Input flow, Qin
Base pressure, P
Patm
Valve
Qout
</details>

Figure 5.4 Hydraulic tank system for Example 5.10.

Therefore, the nonlinear modeling equation for the hydraulic tank system is

$$C \dot {P} = Q _ {\text { in }} - K _ {T} \sqrt {P - P _ {\text { atm }}} \tag {5.69}$$

We begin by rewriting the nonlinear model (5.69) as a state-variable equation

$$\dot {P} = \frac {1}{C} Q _ {\mathrm{in}} - \frac {K _ {T}}{C} \sqrt {P - P _ {\mathrm{atm}}} = f (P, Q _ {\mathrm{in}}) \tag {5.70}$$

The first step is to determine the operating point $P ^ { * }$ given a nominal (constant) input $Q _ { \mathrm { i n } } ^ { \ast }$ . We can expect that over time the outflow $Q _ { \mathrm { o u t } }$ will balance the constant input flow $Q _ { \mathrm { i n } } ^ { \ast }$ . Therefore ${ \dot { P } } = 0$ and pressure reaches a constant value $P ^ { * }$ (the liquid-level height in the tank will also reach a constant value, as pressure and liquid-level height are related by the hydrostatic equation). Solving Eq. (5.69) for the constant pressure when $C { \dot { P } } = 0$ yields

$$P ^ {*} = \frac {Q _ {\text { in }} ^ {* 2}}{K _ {T} ^ {2}} + P _ {\text { atm }} \tag {5.71}$$
