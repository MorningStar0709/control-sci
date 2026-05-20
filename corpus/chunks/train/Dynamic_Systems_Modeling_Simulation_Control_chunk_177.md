# Modeling Pneumatic Systems

Mathematical models of pneumatic systems can be derived by applying the conservation of mass and the CV approach demonstrated in Section 4.2. The derivation is only slightly different from the steps we applied to the hydraulic system with a compressible fluid. To begin, recall the mass-continuity equation (4.19) for a CV, which is repeated here

$$w _ {\mathrm{CV}} = \sum w _ {\text { in }} - \sum w _ {\text { out }} \tag {4.69}$$

The total mass of the gas in the CV at any instant is $m _ { \mathrm { C V } } = \rho V$ , and, therefore, its time derivative is

$$w _ {\mathrm{CV}} = \dot {m} _ {\mathrm{CV}} = \dot {\rho} V + \rho \dot {V} \tag {4.70}$$

We used the fluid bulk modulus to define the density change $\dot { \rho }$ for a hydraulic system with a compressible fluid. For pneumatic systems we find $\dot { \rho }$ by taking the time derivative of the polytropic gas expansion process (4.62)

$$\dot {P} = a n \rho^ {n - 1} \dot {\rho} = \frac {n}{\rho} a \rho^ {n} \dot {\rho} \tag {4.71}$$

Substituting the polytropic process model $P = a \rho ^ { n }$ in Eq. (4.71) yields an expression for the time derivative of density

$$\dot {\rho} = \frac {\rho}{n P} \dot {P} \tag {4.72}$$

Substituting Eq. (4.72) into the mass-flow rate equation (4.70) and using the ideal gas law to replace density $( \rho = P / R T )$ we obtain

$$w _ {\mathrm{CV}} = \frac {V}{n R T} \dot {P} + \frac {P}{R T} \dot {V} = \sum w _ {\text { in }} - \sum w _ {\text { out }} \tag {4.73}$$

Because we are interested in the pressure variation of the pneumatic system, we solve Eq. (4.73) for the time-rate of pressure to obtain

$$\dot {P} = \frac {n R T}{V} \left(w _ {\text { net }} - \frac {P}{R T} \dot {V}\right) \tag {4.74}$$
