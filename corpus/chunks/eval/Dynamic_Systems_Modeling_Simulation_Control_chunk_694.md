Let us define $\Delta P = P _ { 1 } - P _ { 2 }$ as the differential pressure across the piston $( \Delta P > 0$ because fluid is flowing from chamber 2 to the reservoir). Substituting $P _ { 2 } = P _ { 1 } - \Delta P$ into Eq. (11.45) and solving for the supply pressure yields

$$P _ {S} = P _ {1} + P _ {1} - \Delta P - P _ {r} \tag {11.46}$$

Usually, the reservoir pressure $P _ { r }$ is much less than the other pressures and can be neglected. With this assumption, we obtain the following expression for cylinder pressure $P _ { 1 }$ from Eq. (11.46)

$$P _ {1} = \frac {P _ {S} + \Delta P}{2} \tag {11.47}$$

Substituting Eq. (11.47) for pressure $P _ { 1 }$ in Eq. (11.43) yields the following expression for flow rate $Q _ { 1 }$

$$Q _ {1} = C _ {d} A _ {v} \sqrt {\frac {2}{\rho} \left(P _ {S} - \frac {P _ {S} + \Delta P}{2}\right)}$$

Applying simple algebra and substituting $A _ { \nu } = h y$ yields

$$Q _ {1} = C _ {d} h y \sqrt {\frac {P _ {S} - \Delta P}{\rho}} = f (y, \Delta P) \tag {11.48}$$

Equation (11.48) is a nonlinear function of valve position y and differential pressure $\Delta P$ . We can linearize flow rate about the reference states $y ^ { * }$ and $\Delta P ^ { * }$

$$\delta Q _ {1} = \left. \frac {\partial f}{\partial y} \right| _ {*} \delta y + \left. \frac {\partial f}{\partial (\Delta P)} \right| _ {*} \delta (\Delta P) \tag {11.49}$$

where the partial derivatives of Eq. (11.48) are

$$\left. \frac {\partial f}{\partial y} \right| _ {*} = C _ {d} h \sqrt {\frac {P _ {S} - \Delta P}{\rho}} \Bigg | _ {*} \tag {11.50}\left. \frac {\partial f}{\partial (\Delta P)} \right| _ {*} = \left. \frac {- C _ {d} h y}{2 \rho} \left(\frac {P _ {S} - \Delta P}{\rho}\right) ^ {- \frac {1}{2}} \right| _ {*} \tag {11.51}$$

We select the reference (or nominal) states as $y ^ { * } = 0$ and $\Delta P ^ { * } = 0$ (no flow), and consequently the partial derivatives evaluated at the operating point are

$$\left. \frac {\partial f}{\partial y} \right| _ {*} = C _ {d} h \sqrt {\frac {P _ {S}}{\rho}}\left. \frac {\partial f}{\partial (\Delta P)} \right| _ {*} = 0$$

Hence, the linear flow equation (11.49) becomes

$$\delta Q _ {1} = C _ {d} h \sqrt {\frac {P _ {S}}{\rho}} \delta y \tag {11.52}$$

The reader should note that the perturbation variables are relative to the reference values

$$\delta Q _ {1} = Q _ {1} - Q _ {1} ^ {*} \tag {11.53}\delta y = y - y ^ {*} \tag {11.54}$$
