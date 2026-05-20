$$C n = n \text { th - order Maclaurin Series of } \cos (\Delta \theta / 2),S n = n \text { th - order Maclaurin Series of } \sin (\Delta \theta / 2),\Delta \theta = \text { total body angle increment in } t _ {i}.$$

Compute the Quaternions

$$A ^ {\prime} = A * C n + B * S n * \Delta \psi + C * - 1 * S n * \Delta \theta + D * S n * \Delta \phi ,B ^ {\prime} = A * - 1 * S n * \Delta \psi + B * C n + C * S n * \Delta \phi + D * S n * \Delta \theta ,C ^ {\prime} = A * S n * \Delta \theta + B * - 1 * S n * \Delta \phi + C * C n + D * S n * \Delta \psi ,D ^ {\prime} = A * - 1 * S n * \Delta \phi + B * - 1 * S n * \Delta \theta + C * - 1 * S n * \Delta \psi ,A = A ^ {\prime},B = B ^ {\prime},C = C ^ {\prime},D = D ^ {\prime}.$$

Renormalize the Quaternions

$$
\begin{array}{l} \text { Normalizer } = 0. 5 * (3. 0 - A ^ {2} - B ^ {2} - C ^ {2} - D ^ {2}), \\ A = A * \text { Normalizer }, \\ B = B * \text { Normalizer }, \\ C = C * \text { Normalizer }, \\ D = D * \text { Normalizer }. \\ \end{array}
$$

Compute the direction cosine matrix

$$
\begin{array}{l} C m (1, 1) = A ^ {2} - B ^ {2} - C ^ {2} + D ^ {2}, \\ C m (1, 2) = 2 * (A * B - C * D), \\ C m (1, 3) = 2 * (A * C + B * D), \\ C m (2, 1) = 2 * (A * B + C * D), \\ C m (2, 2) = - 1 * A ^ {2} + B ^ {2} - C ^ {2} + D ^ {2}, \\ C m (2, 3) = 2 * (B * C - A * D), \\ C m (3, 1) = 2 * (A * C - B * D), \\ C m (3, 2) = 2 * (B * C + A * D), \\ C m (3, 3) = - 1 * A ^ {2} - B ^ {2} + C ^ {2} + D ^ {2}. \\ \end{array}
$$

Compute the Earth velocities

$$
\begin{array}{l} U _ {e} = U _ {e} + X _ {e a} * t _ {i}, \\ V _ {e} = V _ {e} + Y _ {e a} * t _ {i}, \\ W _ {e} = W _ {e} + Z _ {e a} * t _ {i}. \\ \end{array}
$$

Compute the body velocities

$$
\begin{array}{l} U _ {b} = C m (1, 1) * U _ {e} + C m (2, 1) * V _ {e} + C m (3, 1) * W _ {e}, \\ V _ {b} = C m (1, 2) * U _ {e} + C m (2, 2) * V _ {e} + C m (3, 2) * W _ {e}, \\ W _ {e} = C m (1, 3) * U _ {e} + C m (2, 3) * V _ {e} + C m (3, 3) * W _ {e}. \\ \end{array}
$$

Compute the airspeed

$$V = (U _ {e} ^ {2} + V _ {e} ^ {2} + W _ {e} ^ {2}) ^ {1 / 2}.$$

Compute the Earth referenced position

$$
\begin{array}{l} U _ {e} = U _ {e} * t _ {i}, \\ V _ {e} = V _ {e} * t _ {i}, \\ W _ {e} = W _ {e} * t _ {i}. \\ \end{array}
$$

Compute the angle of attack

$$\alpha = A \tan 2 (W _ {b} / U _ {b}).$$

Compute the attitudes

$$\theta = A \sin (- 1 * C m (3, 1)),\phi = A \tan 2 (C m (3, 2) / C m (3, 3)),\psi = A \tan 2 (C m (2, 1) / C m (1, 1)).$$

Compute the sideslip angle

$$\beta = A \tan 2 (V _ {b} / U _ {b}),$$

where β is the sideslip angle.

Compute the flightpath angle

$$\gamma = A \tan 2 ((- 1 * W _ {e}) / (U _ {e} ^ {2} + V _ {e} ^ {2}) ^ {1 / 2}),$$

where γ is the flightpath angle.
