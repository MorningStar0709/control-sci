If the current phase is a gravity turn, the pitch angle θ is set to the current guidance phase angle, and the pointing vector ${ \bf R } _ { N T }$ is calculated accordingly. Pitch θ remains at that angle until the velocity vector crosses ${ \bf R } _ { N T }$ ; that is, the angle of attack α goes from positive to negative or vice versa. Once this crossover occurs, maximum α is set to zero, so the pointing vector ${ \bf R } _ { N T }$ is calculated according to an angle of attack of zero. This results, as indicated in Section 6.5.4, in thrust acting along the direction of the unit velocity vector, and gravity pulls the velocity vector toward the center of the Earth. Hence, a gravity turn occurs. Gravity turns also occur if the maximum α is input as zero or if the total thrust equals zero, which automatically causes the maximum α to be set to zero.

Total Acceleration: The total acceleration vector in ECI coordinates is then calculated as follows:

$$A _ {x} = A _ {G x} + A _ {T} \times R _ {N T x} + F _ {L D x} / M _ {T},A _ {y} = A _ {G y} + A _ {T} \times R _ {N T y} + F _ {L D y} / M _ {T},A _ {z} = A _ {G z} + A _ {T} \times R _ {N T z} + F _ {L D z} / M _ {T}, \tag {6.267}$$

where

$$A _ {n} = \text { total acceleration in } E C I n \text {-direction}[ \mathrm{m} / \sec^ {2} ],A _ {G n} = \text { gravity acceleration in } E C I n \text {-direction}[ \mathrm{m} / \sec^ {2} ],R _ {N T n} = \text { current pointing vector in }E C I n \text {-direction [m]},F _ {L D n} = \text { aerodynamic force in } E C I n \text {-direction [newtons] },M _ {T} = \text { total missile mass } [ \mathrm{kg} ].$$
