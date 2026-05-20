where $R _ { T }$ is the nonlinear (turbulent) fluid resistance (in $\mathrm { P a } { \mathrm { - s } } ^ { 2 } / \mathrm { m } ^ { 6 } )$ . Turbulent flow exists when the pressure difference $\Delta P$ across the orifice is “large” and consequently the fluid velocity is large. We can rewrite the turbulent flow equation (4.4) in terms of volumetric-flow rate Q

$$Q = K _ {T} \sqrt {\Delta P} \tag {4.5}$$

where $K _ { T } = \sqrt { 1 / R _ { T } }$ is a turbulent flow coefficient.

Most industrial hydraulic systems involve high-pressure flow through valve openings or small restrictions and hence the resulting flow is typically turbulent. Let us now develop an approximate model for turbulent hydraulic flow through an orifice or sharp-edged valve opening. Figure 4.3 shows hydraulic oil flowing through a sharp-edged orifice (such as a valve opening) with area $A _ { 0 }$ . The fluid has very high pressure $P _ { 1 }$ at station 1, which is upstream from the orifice, and lower pressure $P _ { 2 }$ at station 2, which is immediately downstream from the orifice. Let us assume that the velocity of the oil at station 1 is small and can be neglected, that is, $\nu _ { 1 } \approx 0$ . Next, we can apply Bernoulli’s equation to the fluid flow between stations 1 and 2:

![](image/8aa056960a8a32e192b391f8f7f85c41303633406ba63e0203015910d348ca79.jpg)

<details>
<summary>text_image</summary>

P₁
Supply
pressure
Velocity,
v₁ ≈ 0
P₂
Velocity,
v₂
Orifice area, A₀
</details>

Figure 4.3 Hydraulic fluid flowing through a sharp-edged orifice.

$$\frac {1}{2} \rho v _ {1} ^ {2} + P _ {1} = \frac {1}{2} \rho v _ {2} ^ {2} + P _ {2} \tag {4.6}$$

Bernoulli’s equation assumes incompressible, steady, frictionless flow and consequently the total energy is conserved along a streamline between stations 1 and 2. Assuming $\nu _ { 1 } \approx 0$ , we can solve Eq. (4.6) for the flow velocity $\nu _ { 2 }$ through the orifice

$$v _ {2} = \sqrt {\frac {2}{\rho} (P _ {1} - P _ {2})} \tag {4.7}$$

We can multiply the velocity through the orifice $\nu _ { 2 }$ by orifice area $A _ { 0 }$ to get the volumetric-flow rate through the orifice Q

$$Q = A _ {0} \sqrt {\frac {2}{\rho} (P _ {1} - P _ {2})} \tag {4.8}$$
