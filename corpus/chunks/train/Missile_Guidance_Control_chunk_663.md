where

$$F _ {L D n} = \text { aerodynamic force in } E C I n \text {-direction [newtons]},L _ {n} = \text { lift force in ECI } n \text {-direction [newtons] },D _ {n} = \text { drag force in ECI } n \text {-direction[newtons] }.$$

Acceleration due to Gravity Potential gravity is calculated by (see also (6.232))

$$g _ {p} = - g _ {c} / R _ {\text { mag }} ^ {3}, \tag {6.260}$$

where

$$g _ {p} = \text { potential gravity } [ 1 / \sec^ {2} ],g _ {c} = \text { universal gravitational constant (also known as } \mu)= 3. 9 8 6 \times 1 0 ^ {1 4} [ \mathrm{m} ^ {3} / \sec^ {2} ].$$

Acceleration due to gravity is calculated in ECI coordinates according to

$$A _ {g x} = g _ {p} R _ {x},A _ {g y} = g _ {p} R _ {y},A _ {g z} = g _ {p} R _ {z}, \tag {6.261}$$

where

$$A _ {g n} = \text { acceleration of gravity in } E C I n \text {-direction} [ \mathrm{m/sec} ^ {2} ],R _ {n} = \text { missile position in } E C I n \text {-direction} [ m ].$$

Acceleration due to Thrust: Vacuum thrust is input as a function of the missile flight section. The ballistic missile model tracks the total amount of fuel that is available, setting the thrust to zero when all the current-stage fuel has been expended. However, if fuel is available, the total thrust is calculated from the expression

$$T = T _ {v} - A _ {N E} P, \tag {6.262}$$

where

$$T = \text { total thrust } [ \text { newtons } ],T _ {v} = \text { vacuum thrust [newtons] },A _ {N E} = \text { nozzle exit area } [ \mathrm{m} ^ {2} ],P = \text { atmospheric pressure } [ \text { newtons } / \mathrm{m} ^ {2} ].$$

The second term in (6.262) is the thrust that is canceled out by atmospheric pressure working against the vacuum thrust on the engine exit area plane. Thrust acceleration magnitude is then calculated according to (see (6.215))

$$A _ {T} = T / M _ {T}, \tag {6.263}$$

where

$$A _ {T} = \text { thrust acceleration } [ \mathrm{m/sec} ^ {2} ],T = \text { total thrust } [ \text { newtons } ],M _ {T} = \text { total missile mass } [ \mathrm{kg} ].$$
