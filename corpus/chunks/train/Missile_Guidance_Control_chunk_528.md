Several additional kinematic elements and definitions that are frequently encountered in the astronomical literature deserve brief mention [5], [10]. For example, it is not difficult to show that the length of the radius vector from the force center to the point where the minor axis intersects the orbit exactly equals the length of the semimajor axis a. Another angle that was first introduced by Kepler is the eccentric anomaly E, which is measured from the center of the ellipse rather than from the force center. Geometric considerations show that the equation of motion may be written very simply in terms of the eccentric anomaly. That is,

$$r = a (1 - e \cos E).$$

It may be shown that

$$\cos \nu = (\cos E - e) / (1 - e \cos E), \quad \sin \nu = (1 - e ^ {2}) ^ {1 / 2} \sin E / (1 - e \cos E),$$

while the inverse relations are readily found to be

$$\cos E = (\cos \nu + e) / (1 - e \cos \nu), \quad \sin E = (1 - e ^ {2}) ^ {1 / 2} \sin \nu / (1 + e \cos \nu).$$

This form is useful in computing the relationship between time and position in orbit. For example, in terms of E, (6.38) may be written in the simple form

$$t - T = (1 / n) [ E - e \sin E ],$$

or

$$n (t - T) = E - e \sin E,$$

where n is the previously defined mean motion 2π/P . This leads to the Keplerian equation for the motion

$$n (t - T) = M = E - e \sin E, \tag {6.52}$$

where T is a constant of integration, also called the time of perihelion passage; E is the eccentric anomaly; e is the eccentricity; and M is defined as the mean anomaly [5]. The mean anomaly is the angle through which the vehicle would move at the uniform speed n, measured from the perigee. The quantity n(t − T ) is the angle that would have been described by the radius vector if it had moved uniformly with the average rate. Equation (6.52) is known as Kepler’s equation. It is transcendental in E, and the solution for this quantity cannot be expressed in a finite number of terms. Equation (6.52) is also written in the form

$$t - T = (\sqrt {a ^ {3} / \mu}) [ E - e \sin E ], \tag {6.53}$$

where we see that T is the constant of integration, and as stated above, it is the time of perihelion passage.

It is of interest now to express the total mechanical energy E in terms of the orbit elements (the reader should not confuse the use of the symbol E for energy with E for the eccentric anomaly). As stated earlier, in Section 6.2, the total energy is the sum of the kinetic and potential energies (by definition) and has the form

$$E = T + U = \frac {1}{2} m V ^ {2} - m (\mu / r) \tag {6.54}$$
