where $A _ { \nu }$ is the valve area, $C _ { d }$ is the discharge coefficient, and $\rho$ is the fluid density. When spool-valve position $y > 0$ , the supply pressure $P _ { S }$ is connected to cylinder chamber $P _ { 1 }$ and Eq. (11.39) is used to compute $Q _ { 1 }$ . When $y < 0$ , the supply pressure $P _ { S }$ is connected to $P _ { 2 }$ and Eq. (11.39) is used to compute $Q _ { 2 }$ . In general, the supply pressure $P _ { S }$ is always greater than the cylinder pressure $P _ { 1 }$ or $P _ { 2 }$ , but the possibility for fluid flow from the cylinder back to the supply pressure is included by using the signum function. Volumetric flow through the spool valve between the cylinder (chamber 1 or 2) and the reservoir (drain) pressure $P _ { r }$ is also modeled by the orifice-flow equation

$$Q _ {1, 2} = - C _ {d} A _ {v} \operatorname{sgn} (P _ {1, 2} - P _ {r}) \sqrt {\frac {2}{\rho} \left| P _ {1 , 2} - P _ {r} \right|} \tag {11.40}$$

When $y < 0$ , Eq. (11.40) models flow $Q _ { 1 }$ from chamber 1 to the drain and when $y > 0$ Eq. (11.40) models flow $Q _ { 2 }$ from chamber 2 to the drain. Equation (11.40) shows that $Q _ { 1 }$ (or $Q _ { 2 } )$ is negative when $P _ { 1 }$ (or $P _ { 2 } )$ i s greater than the reservoir pressure and the fluid flows from the cylinder to the reservoir tank.

To complete the mathematical model, we must show the relationship for the electromagnetic solenoid used to position the spool valve. One common modeling method [6] is to use an underdamped, second-order transfer function to relate spool-valve position y to voltage input $e _ { \mathrm { i n } } ( t )$

$$G (s) = \frac {Y (s)}{E _ {\mathrm{in}} (s)} = \frac {K _ {v} \omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \tag {11.41}$$

Table 11.5 Parameters for the EHA
