g = acceleration due to gravity with components [0 0 g],

$\Omega = \mathrm { E a r t h r a t e ~ v e c t o r } ( = 7 . 2 9 1 1 5 1 \times 1 0 ^ { - 5 } \mathrm { r a d / s e c } \approx 1 5 \mathrm { d e g / h r } ) .$

This is the fundamental equation of motion, which specifies the position and velocity of the bomb at any time t. The position and velocity initial conditions must be provided to the FCC. Now let the initial position and velocity of the bomb at the time of release, $t = 0$ , be $\mathbf { R } _ { r }$ and ${ \bf V } _ { r }$ . Integrating (5.18), we obtain the following equation:

$$\mathbf {V} (t) = \mathbf {V} _ {r} + \int_ {0} ^ {t} (\mathbf {f} - \mathbf {g} - 2 \Omega \times \mathbf {V}) d \tau . \tag {5.19}$$

In order to find the position of the bomb at any time t, (5.19) must be integrated. Thus,

$$\mathbf {R} (t) = \mathbf {R} _ {r} + \mathbf {V} _ {r} t + \int_ {0} ^ {t} \int_ {0} ^ {\tau} (\mathbf {f} - \mathbf {g} - 2 \Omega \times \mathbf {V}) d \tau_ {1} d \tau , \tag {5.20}0 \leq \tau_ {1} \leq \tau ,0 \leq \tau \leq t.$$

In (5.20), if we wish to compute the bomb’s position at the time of impact (i.e., from the time of release to the final impact time), then we must substitute $t = t _ { f }$ and $\mathbf { R } ( t ) = \mathbf { R } ( t _ { f } )$ . The external forces acting on the bomb must be included in the above analysis. These forces are:

W The weight of the bomb, which acts at the center of gravity. The weight has no x-y components in the horizontal plane. Therefore, its components are [0 0 mg].

D The drag. This force originates at the center of pressure, and its direction is parallel but opposite to the direction of motion.

L This force also originates at the center of pressure, and is directed perpendicular to the direction of motion.

Assuming no other forces except that the weight and drag are acting on the bomb, the drag force is given by the equation

$$\mathbf {D} = - C _ {d} \left(\frac {1}{2} \rho V _ {a} ^ {2}\right) S [ \mathbf {V} _ {a} / V _ {a} ], \tag {5.21}$$

where

Cd = the coefficient of drag,

ρ = the density of air,

Va = the true air velocity vector,

S = the cross-sectional area of the bomb = πd2/4,

$$V _ {a} = | \mathbf {V} _ {a} |.$$

Consequently, the deceleration to the bomb is subjected is

$$\mathbf {f} = \mathbf {D} / m. \tag {5.22}$$
