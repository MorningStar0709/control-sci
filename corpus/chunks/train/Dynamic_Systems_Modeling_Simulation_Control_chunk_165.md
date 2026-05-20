The definition of fluid bulk modulus, Eq. (4.1), can be used to solve for the change in density due to change in pressure, or $d \rho / d P = \rho / \beta$ . Therefore, the time-rate of density is ${ \dot { \rho } } = \rho { \dot { P } } / \beta$ and the mass-continuity equation (4.37) becomes

$$\frac {\rho \dot {P} V}{\beta} + \rho \dot {V} = \rho Q _ {\text { in }} \tag {4.39}$$

Dividing out density and rearranging Eq. (4.39) yields

$$\dot {P} = \frac {\beta}{V} (Q _ {\text { in }} - \dot {V}) \tag {4.40}$$

Equation (4.40) is the fundamental modeling equation for the time-rate of pressure for a hydraulic cylinder with a compressible fluid. The hydraulic actuator shown in Fig. 4.9 is known as a single-acting cylinder because hydraulic fluid flows to one side of the piston. If we compare Eq. (4.40) with the hydraulic capacitance equation (4.15), we see that $V / \beta$ is the fluid capacitance of a hydraulic actuator. Equation (4.40) shows that fluid flowing into the CV $( Q _ { \mathrm { i n } } > 0 )$ increases the fluid pressure while an expanding CV $( \dot { V } > 0 )$ ) decreases pressure. The instantaneous volume of the CV is V = Ax (where x is the position of the piston in Fig. 4.9), and, therefore, the time-rate of the volume is ${ \dot { V } } = A { \dot { x } }$ . It is clear that the motion of the piston (x and ẋ ) must be accounted for in the hydraulic servo equation (4.40), and consequently we must include a model of the mechanical system (piston and load). Finally, it should be noted that Eq. (4.40) is nonlinear as the coefficient 1∕V involves the inverse of the dynamic variable x.
