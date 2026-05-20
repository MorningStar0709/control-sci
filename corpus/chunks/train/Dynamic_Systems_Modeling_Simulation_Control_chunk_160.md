# Modeling Hydraulic Tank Systems

As a first example of a simple fluid system, we derive the mathematical model of a hydraulic reservoir (tank) system. Because the fluid pressure in a tank is due to its weight (i.e., the hydrostatic equation (4.11)) pressure is relatively low, and, therefore, the fluid can be considered to be incompressible $( \dot { \rho } = 0 )$ ). Using Eqs. (4.19) and (4.20), the net rate of change of fluid mass is due solely to its changing volume

$$w _ {\mathrm{CV}} = \rho \dot {V} = \sum w _ {\text { in }} - \sum w _ {\text { out }} \tag {4.21}$$

We can divide Eq. (4.21) by density ?? and use input and output volumetric-flow rates instead of mass-flow rates.

$$\dot {V} = \sum Q _ {\text { in }} - \sum Q _ {\text { out }} \tag {4.22}$$

Substituting Eq. (4.15) for the left-hand side of Eq. (4.22) yields

$$C \dot {P} = \sum Q _ {\text { in }} - \sum Q _ {\text { out }} \tag {4.23}$$

Equation (4.23) is our fundamental modeling equation for a hydraulic system with incompressible flow. Note that the left side of Eq. (4.23) is $\dot { V } = ( d V / d P ) ( d P / d t )$ ) where $d V / d P = C .$ . We must apply Eq. (4.23) to each hydraulic reservoir (or CV) if we have a system of connected tanks. The following example demonstrates the modeling steps for a single-tank hydraulic system.
