where $\rho$ is the air density, $\beta$ is the ballistic coefficient, and ${ \bf v } _ { r }$ is the velocity relative to the (rotating) atmosphere:

$$
\mathbf {v} _ {r} = \mathbf {v} - \omega_ {E A} \left[ \begin{array}{c} - y \\ x \\ 0 \end{array} \right], \tag {11}
$$

where $\omega _ { E A }$ is the angular velocity of the Earth’s atmosphere. The angular velocity $\omega _ { E A }$ can be made zero even if the Earth is rotating to eliminate wind effects if desired (note that the period of rotation of the atmosphere relative to the Earth is one month at a height of 500 mb and 2–3 weeks in the highest levels of the atmosphere). The density $\rho$ is that of the 1959 ARDC standard atmosphere, corrupted by random perturbations. The altitude used for the density calculations is

$$h = r - R (\theta), \tag {12}$$

where

$$R (\theta) = (1 - f) R _ {e} / \left[ (1 - f) ^ {2} \sin^ {2} \theta + \cos^ {2} \theta \right] ^ {1 / 2}, \tag {13}$$

and $f$ is the flattening of the Earth given by the expression

$$f = (R _ {e} - R _ {p}) / R _ {e}, \tag {14}$$

where $R _ { p }$ is the Earth’s polar radius. The air density is computed from the model atmosphere given by the symbol $\rho _ { m }$ , so that the true density $\rho$ is given by

$$\rho = \rho_ {m} \exp (n _ {d}), \tag {15}$$

where $n _ { d }$ is a dimensionless “density noise.” The form of the equation ensures that $\rho$ will never be negative. When $n _ { d }$ is small, it represents a fractional change of the density from the nominal (i.e., model) value.
