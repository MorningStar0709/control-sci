# 6-DOF Processing

The following computations are performed at every simulation cycle.

Compute the dynamic pressure

$$q = \frac {1}{2} \rho V ^ {2},$$

where

$$q = \text { dynamic pressure },\rho = \text { pressure in standard atmosphere },V = \text { a i r s p e e d }.$$

Compute the wing lift

$$L = C _ {L} * q * S,$$

where

$$
\begin{array}{l} L = \text { lift }, \\ C _ {L} = \text { coefficient   of   lift }, \\ S = \text { surface   area   of   the   wing. } \\ \end{array}
$$

Compute the wing drag

$$D = C _ {D} * q * S,$$

where CD = coefficient of drag.

Compute the lift acceleration

$$L _ {a} = L / w,$$

where w = weight of the airplane.

Compute the drag acceleration

$$D _ {a} = D / w.$$

Compute the thrust acceleration

$$T _ {a} = T / m,$$

where

$$
\begin{array}{l} m = \text { mass   of   the   airplane }, \\ T = \text { thrust }. \\ \end{array}
$$

Compute the body accelerations

$$
\begin{array}{l} X _ {b a} = T _ {a} * L _ {a} * \sin (\alpha) - D _ {a} * \cos (\alpha) + C m (3, 1) * g + R * V _ {b} - Q * W _ {b}, \\ Y _ {b a} = C m (3, 2) * g - R * U _ {b} + P * W _ {b}, \\ Z _ {b a} = - 1 * L _ {a} * \cos (\alpha) - D _ {a} * \sin (\alpha) + C m (3, 3) * g + Q * X _ {b} - P * V _ {b}, \\ \end{array}
$$

where

$$
\begin{array}{l} X _ {b a} = X \text {-axis body acceleration}, \\ Y _ {b a} = Y \text {-axis body acceleration}, \\ Z _ {b a} = Z \text {-axis body acceleration}, \\ P = \text { roll   rate }, \\ Q = \text { pitch   rate }, \\ R = \text { yaw   rate }, \\ g = \text { acceleration   due   to   gravity }, \\ \alpha = \text { angle   of   attack }. \\ \end{array}
$$

Compute the Earth accelerations

$$X _ {e a} = C m (1, 1) * X _ {b a} + C m (1, 2) * Y _ {b a} + C m (1, 3) * Z _ {b a},Y _ {e a} = C m (2, 1) * X _ {b a} + C m (2, 2) * Y _ {b a} + C m (2, 3) * Z _ {b a},Z _ {e a} = C m (3, 1) * X _ {b a} + C m (3, 2) * Y _ {b a} + C m (3, 3) * Z _ {b a},$$

where

$$X _ {e a} = X \text {-axis Earth acceleration},Y _ {e a} = Y \text {-axis Earth acceleration},Z _ {e a} = Z \text {-axis Earth acceleration.}$$

Compute the angular deltas

$$\Delta \theta = Q * t _ {i},\Delta \phi = P * t _ {i},\Delta \psi = R * t _ {i},$$

where

$$\Delta \theta = \text { pitch delta },\Delta \phi = \text { roll delta },\Delta \psi = \text { yaw delta },t _ {i} = \text { simulation cycle time }.$$

Compute Cn and Sn

$$C n = 1. 0 - (\Delta \theta^ {2} + \Delta \phi^ {2} + \Delta \psi^ {2}) / 8 + (\Delta \theta^ {4} + \Delta \phi^ {4} + \Delta \psi^ {4}) / 3 8 4,S _ {n} = 0. 5 - (\Delta \theta^ {2} + \Delta \phi^ {2} + \Delta \psi^ {2}) / 4 8,$$

where
