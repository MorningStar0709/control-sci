where $K _ { T }$ is a turbulent flow coefficient and $\Delta P = P - P _ { \mathrm { a t m } }$ . Substituting Eq. (4.28) into the continuity equation (4.24) yields

$$C \dot {P} + K _ {T} \sqrt {P - P _ {\mathrm{atm}}} = Q _ {\text { in }} \tag {4.29}$$

Equation (4.29) is the mathematic model of the hydraulic tank system with turbulent flow through the valve. The system is modeling by a single first-order nonlinear ODE as we have a single fluid capacitance that can store energy.

(c) We want to write the linear and nonlinear mathematical models (4.27) and (4.29) in terms of liquid height h instead of base pressure P. Pressure and height are related by the hydrostatic equation (4.11)

$$P = \rho g h + P _ {\mathrm{atm}} \tag {4.30}$$

The time derivative of hydrostatic pressure (4.30) is

$$\dot {P} = \rho g \dot {h} \tag {4.31}$$

Next, we substitute Eq. (4.31) for $\dot { P }$ and $\operatorname { E q . }$ . (4.30) for $P - P _ { \mathrm { a t m } }$ in the linear hydraulic tank model (4.27) to yield

$$R _ {L} C \rho g \dot {h} + \rho g h = R _ {L} Q _ {\text { in }} \tag {4.32}$$

Finally, we can divide all terms in Eq. (4.32) by $\rho g$

$$R _ {L} C \dot {h} + h = \frac {R _ {L}}{\rho g} Q _ {\text { in }} \tag {4.33}$$

Equation (4.33) is the mathematical model of the hydraulic tank with laminar valve flow where liquid height h is the dynamic variable. Equations (4.27) and (4.33) are equivalent dynamic models of the hydraulic tank with laminar flow through the valve.

We can obtain the nonlinear (turbulent flow) model in terms of liquid height h by substituting Eqs. (4.30) and (4.31) for $P - P _ { \mathrm { a t m } }$ and $\dot { P }$ in the nonlinear hydraulic tank model (4.29) to yield

$$C \rho g \dot {h} + K _ {T} \sqrt {\rho g h} = Q _ {\text { in }} \tag {4.34}$$

Equation (4.34) is the mathematical model of the hydraulic tank with turbulent valve flow where liquid height h is the dynamic variable. The reader should note that if we substitute fluid capacitance $C = A / ( \rho g )$ ) in Eq. (4.34), the first left-hand side term is clearly the time-rate of volume $( A { \dot { h } } = { \dot { V } } )$ and exhibits a dimensional match with $Q _ { \mathrm { i n } }$ and $Q _ { \mathrm { o u t } } = K _ { T } \sqrt { \Delta P } .$ . Equations (4.29) and (4.34) are equivalent dynamic models of the hydraulic tank with turbulent valve flow.
