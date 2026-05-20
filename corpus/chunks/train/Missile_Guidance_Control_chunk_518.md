The differential equation represented by (6.18) is called the harmonic equation; its solution is well known. The complementary solution of (6.18) is the general solution of

$$d ^ {2} u / d \theta^ {2} + u = 0.$$

That is,

$$u _ {c} = A \sin \theta + B \cos \theta ,$$

or

$$u _ {c} = C _ {1} \cos (\theta - C _ {2}), \tag {6.19}$$

where $C _ { 1 }$ and $C _ { 2 }$ are constants of integration. The particular solution is readily found to be $u _ { p } = \mu / h ^ { 2 }$ .

Then the complete solution of (6.18) is

$$u = u _ {c} + u _ {p} = C _ {1} \cos (\theta - C _ {2}) + \mu / h ^ {2} = (\mu / h ^ {2}) / [ 1 + C _ {1} \cos (\theta - C _ {2}) ],$$

or

$$r = (h ^ {2} / \mu) / [ 1 + C _ {1} \cos (\theta - C _ {2}) ]. \tag {6.20}$$

This is the polar form of an ellipse with origin at one focus. In terms of Figure 6.3, the constant $C _ { 1 }$ is identified with the eccentricity $e ,$ and the constant $C _ { 2 }$ identified with $\omega .$ . Therefore, we can write (6.20) as

$$r = (h ^ {2} / \mu) / [ 1 + e \cos (\theta - \omega) ], \tag {6.21}$$

where e and ω are constants of integration. The initial conditions on the motion are the burnout conditions of the ballistic missile or orbital vehicle (or the burnout conditions of the retrorocket in the case of reentry). These conditions must, of course, exist at a point of zero aerodynamic forces. A statement of the initial conditions that appears natural from an engineering point of view is

$$
\begin{array}{l} \text { at   } t = 0: \quad \theta = 0, \\ \frac {d \theta}{d t} = \frac {d \theta_ {i}}{d t}, \\ r = r _ {i}, \\ \frac {d r}{d t} = \frac {d r _ {i}}{d t}. \\ \end{array}
$$

Note that the polar angle θ has been set equal to zero at the initial conditions. This puts no restrictions on the solution, since the effect of having $\theta = \theta _ { i }$ rather than $\theta = 0$ is simply to rotate the reference for measurement of the polar angle. The astronomical solution uses a slightly different choice of $\theta _ { i }$ .

From Figure 6.3 we note that the semilatus rectum $p$ is given by

$$p = b ^ {2} / a = a (1 - e ^ {2}), \tag {6.22a}$$

or we can write

$$p = h ^ {2} / \mu , \tag {6.22b}$$

so that $h ^ { 2 } = p \mu = \mu a ( 1 - e ^ { 2 } )$ . Again, we remark in reference to (6.21) that this is the general equation of a conic section, which may be (see also Appendix G)

(i) an ellipse if $e < 1$ ,   
(ii) a parabola if $e = 1$ ,   
(iii) a hyperbola, if $e > 1$ .
