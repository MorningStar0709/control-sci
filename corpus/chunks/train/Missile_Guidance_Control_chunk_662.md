Missile Integration: The ballistic missile model is a 3-DOF (degrees-of-freedom) model that utilizes basic equations of motion in its missile state calculations. The model calculates acceleration as a function of aerodynamic forces, gravity, and thrust. It applies this acceleration on the appropriate directions according to missile orientation and guidance. It then computes the new position, velocity, and expended fuel mass over each integration step using a fourth-order Runge–Kutta integration method.

Calculation of Aerodynamic Forces: During integration, the missile altitude is calculated by the expression

$$H = R _ {\mathrm{mag}} - R _ {e}, \tag {6.255}$$

where

$$H = \text { missile altitude } [ \mathrm{m} ],R _ {m a g} = \text { missile } E C I \text { position vector magnitude [m], }R _ {e} = \text { radius of the Earth. }$$

The altitude H is used to reference the speed of sound C and air density ρ from 1962 standard atmosphere tables (see Appendix D for details on the atmosphere model). Mach number is then calculated according to the equation

$$M = V _ {\text { mag }} / C, \tag {6.256}$$

where

$$M = \text { missile Mach number },V _ {m a g} = \text { magnitude of missile velocity vector [m / sec] },C = \text { speed of sound } [ \mathrm{m/sec} ].$$

Next, we compute the dynamic pressure according to the equation

$$q = \frac {1}{2} \rho V _ {\text { mag }} ^ {2}, \tag {6.257}$$

where,

$$q = \text { dynamic pressure } [ \mathrm{kg/m-sec} ^ {2} ],\rho = \mathrm {air density [ kg/ m^ {3} ]}.$$

Now the coefficients of lift $C _ { L }$ and drag $C _ { D }$ must be linearly interpolated or extrapolated as functions of Mach number M. The aerodynamic forces acting on the missile body are then calculated in the body-axis frame according to the relations

$$D = - C _ {D} q S _ {r e f}, \tag {6.258a}L = C _ {L} \alpha q S _ {r e f}, \tag {6.258b}$$

where

$$D = \text { drag force in the body - axis } x \text {-direction [newtons]},L = \text { lift force in the body - axis } z \text {-direction [newtons]},\alpha = \text { angle of attack } [ \text { degrees } ],S _ {r e f} = \text { missile aerodynamic reference area } [ \mathrm{m} ^ {2} ].$$

The present model assumes no sideslip, so that the aerodynamic force acting in the body-axis Y direction is zero. These aerodynamic forces are then rotated from the body-axis coordinate frame to ECI to be used in the acceleration equations [4]

$$F _ {L D x} = L _ {x} + D _ {x},F _ {L D y} = L _ {y} + D _ {y},F _ {L D z} = L _ {z} + D _ {z}, \tag {6.259}$$
