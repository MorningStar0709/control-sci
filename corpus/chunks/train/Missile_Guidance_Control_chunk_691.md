# 6.9.2 Missile Tracking Equations of Motion

Let us assume an ECEF (earth-centered earth-fixed) coordinate system, in which the positive x-axis passes through the prime meridian at the equator, the positive y-axis passes through the 90◦ east meridian at the equator, and the positive z-axis passes through the North Pole. The target missile’s equations of motion can be expressed as (assuming that only drag and gravity forces are acting on the body) [13]

$$m \mathbf {A} = m \mathbf {A} _ {d} + m \mathbf {A} _ {\mathbf {g}}, \tag {6.278}$$

where

A = total acceleration of the body (i.e., target),

Ad = acceleration due to drag forces,

A = gravitational acceleration,

m = mass of the body (target).

The drag force will be taken to be

$$\mathbf {F} _ {d} = m \mathbf {A} _ {d} = - [ m \rho V / 2 \beta ] \mathbf {V}, \tag {6.279}$$

where

$$V = \text { target velocity } (= (x ^ {2} + y ^ {2} + z ^ {2}) ^ {1 / 2})),$$

β = ballistic coefficient $= m C _ { d } S$ , where $C _ { d }$ is the coefficient of drag and S is the reference area,

ρ = atmospheric density at the target position $( \rho = \rho ( h ) )$ .

Note that the height h required in $\rho = \rho _ { } ( h )$ is obtained as the distance between the target and the point of intersection of the reference ellipsoid and the line passing through the target and normal to the reference ellipsoid. A good approximation to this is

$$h \approx r - R _ {\phi} = r - [ a ^ {2} (1 - e ^ {2}) / (1 - e ^ {2} \cos^ {2} \phi) ] ^ {1 / 2},$$

where

r = distance from the center of the Earth to the target,

a = equatorial radius of the Earth,

e = eccentricity,

φ = geodetic latitude.

From (6.278) the total acceleration can be written in vector form as

$$\mathbf {A} = (\rho V / 2 \beta) \mathbf {V} + \mathbf {A} _ {g}; \tag {6.280}$$

$\mathbf { A } _ { g }$ can be expressed as

$$\mathbf {A} _ {g} = g _ {r} \mathbf {1} _ {r} + g _ {z} \mathbf {1} _ {z}, \tag {6.281}$$

where

$$g _ {r} = - (\mu / r ^ {2}) [ 1 + J (a / r) ^ {2} (1 - 5 \sin^ {2} \phi) ], \tag {6.282a}g _ {z} = (2 \mu / r ^ {2}) J (a / r) ^ {2} \sin \phi . \tag {6.282b}$$

In 6.282, the various parameters are

µ = GM (= 3.9860322 × 105km3 /sec2) = universal gravitational constant,

J = dimensionless coefficient $( \approx 1 . 6 2 4 \times 1 0 ^ { - 3 } )$ ,

a = equatorial radius (= 6, 378.135 km),

$\phi$ = geodetic latitude,

$g _ { o }$ = acceleration of gravity at the surface of the $\mathrm { E a r t h } = 9 . 7 9 8 3 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ ,

r = distance from the center of the Earth to the target.
