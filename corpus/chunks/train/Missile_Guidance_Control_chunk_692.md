We can now write the equations of motion for the present target tracking of an incoming ballistic missile in the form

$$\frac {d ^ {2} x _ {r}}{d t ^ {2}} = - \rho V x _ {r} / 2 \beta , \tag {6.283a}\frac {d ^ {2} y _ {r}}{d t ^ {2}} = - \rho V y _ {r} / 2 \beta , \tag {6.283b}\frac {d ^ {2} z _ {r}}{d t ^ {2}} = - (\rho V z _ {r} / 2 \beta) - g _ {r}. \tag {6.283c}$$

The total gravitational acceleration can also be expressed in vector form. Assuming that the Earth is modeled as an oblate aspherical planet, then its gravity vector can be approximated by expansion into spherical harmonics as follows [11]:

$$
\mathbf {g} = - (\mu / R) ^ {2} \left[ \begin{array}{c} 1 + \frac {3}{2} J _ {2} (a / r) ^ {2} (1 - 3 \sin^ {2} \phi) \\ 0 \\ J _ {2} (a / r) ^ {2} 3 \sin \phi \cos \phi \end{array} \right],
$$

where $J _ { 2 } = 1 . 0 8 2 6 3 \times 1 0 ^ { - 3 }$ .

In the most general case of a launched ICBM, and taking into account the rotation of the Earth, the kinematic and dynamic equations describing the translational motion of the ICBM can be written in the form

$$
\frac {d \mathbf {r}}{d t} = \left(\frac {d}{d t}\right) \left[ \begin{array}{c} r \\ \lambda \\ \phi \end{array} \right] = m \left[ \begin{array}{c} V _ {r} \\ (V _ {\lambda} / r \cos \phi) - \Omega_ {e} \\ V _ {\phi} / r \end{array} \right], \tag {6.284a}

\frac {d \mathbf {V}}{d t} = \left(\frac {d}{d t}\right) \left[ \begin{array}{c} V _ {r} \\ V _ {\lambda} \\ V _ {\phi} \end{array} \right] = (1 / r) \left[ \begin{array}{c} V _ {\lambda} ^ {2} + V _ {\phi} ^ {2} \\ V _ {\lambda} (V _ {\phi} \tan \phi - V _ {r}) \\ - V _ {\lambda} ^ {2} \tan \phi - V _ {r} V _ {\phi} \end{array} \right] + \mathbf {g} + (1 / m) \Sigma \mathbf {F}, \tag {6.284b}
$$

where

Vr, Vλ, Vφ = velocity components along the indicated directions,

V = vehicle’s inertial velocity vector,

r = vehicle position vector,

m = mass of the vehicle,

φ = geodetic latitude,

λ = geodetic longitude,

g = acceleration of gravity,

F = external forces (or loads),

 = angular velocity of the Earth = 7.292115 × 10−5 rad/sec.

The dynamic pressure in the present case is taken to be

$$Q = \frac {1}{2} \rho V _ {a} ^ {2},$$

where the airpath velocity vector ${ \mathbf V } _ { a }$ is given by

$$\mathbf {V} _ {a} = \mathbf {V} - \Omega_ {e} \times \mathbf {r} - \mathbf {V} _ {w}, \tag {6.284c}$$

where $V _ { w }$ is the velocity of the atmosphere relative to the Earth.
