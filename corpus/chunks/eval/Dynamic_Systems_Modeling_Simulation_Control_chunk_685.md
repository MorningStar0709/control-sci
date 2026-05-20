# Mathematical Model

The complete mathematical model consists of the electromechanical (solenoid), hydraulic, and mechanical subsystems. Figure 11.33 shows a free-body diagram of the mechanical subsystem, which consists of the piston and load mass m. Piston displacement x is positive to the left as measured from the right end of the cylinder (see Fig. 11.32). Applying Newton’s second law with a positive sign convention to the left yields

$$+ \leftarrow \sum F = P _ {1} A - P _ {2} A - b \dot {x} = m \ddot {x} \tag {11.33}$$

where $P _ { 1 }$ and $P _ { 2 }$ are the chamber pressures of the right and left sides of the cylinder, A is the area of the piston, and b is the viscous friction coefficient. Rearranging Eq. (11.33) so that all terms involving displacement x are on the left-hand side yields

$$m \ddot {x} + b \dot {x} = (P _ {1} - P _ {2}) A \tag {11.34}$$

![](image/d666b5d8a2204e045bebed78bda15dcc4df41788c37bfe792616a56ddc893874.jpg)

<details>
<summary>text_image</summary>

P₂A
m
bẋ
+x
P₁A
</details>

Figure 11.33 Free-body diagram of the mechanical subsystem.

Two pressure-rate equations are required for the two cylinder chambers

$$\dot {P} _ {1} = \frac {\beta}{V _ {1}} (Q _ {1} - \dot {V} _ {1}) \tag {11.35}\dot {P} _ {2} = \frac {\beta}{V _ {2}} (Q _ {2} - \dot {V} _ {2}) \tag {11.36}$$

where $\beta$ is the fluid bulk modulus, $Q _ { 1 }$ and $Q _ { 2 }$ are the volumetric-flow rates for chambers 1 and 2, and $V _ { 1 }$ and $V _ { 2 }$ are the volumes of cylinder chambers 1 and 2. Equations (11.35) and (11.36) are the basic pressure-rate equations derived in Chapter 4 for hydraulic systems with compressible fluids. The instantaneous volumes for cylinder chambers 1 and 2 depend on piston position x

$$V _ {1} = V _ {0} + A x \tag {11.37}V _ {2} = V _ {0} + A (L - x) \tag {11.38}$$

where $V _ { 0 }$ is the volume when $x = 0$ (piston is at the right end of the cylinder). The total stroke of the piston is L. The time rate of change of the two cylinder volumes depends on the piston velocity: ${ \dot { V } } _ { 1 } = A { \mathrm { i } }$ ẋ and $\dot { V } _ { 2 } = - A \dot { x }$ .

Volumetric flow through the spool valve between the supply pressure $P _ { S }$ and the cylinder (for either chamber 1 or 2) is modeled by the orifice-flow equation for hydraulic systems

$$Q _ {1, 2} = C _ {d} A _ {v} \operatorname{sgn} \left(P _ {S} - P _ {1, 2}\right) \sqrt {\frac {2}{\rho} \left| P _ {S} - P _ {1 , 2} \right|} \tag {11.39}$$
