$$\frac {d}{d t} \equiv \left(\frac {d \theta}{d t}\right) \left(\frac {d}{d \theta}\right) = (h / r ^ {2}) \left(\frac {d}{d \theta}\right). \tag {6.69a}$$

This relationship will facilitate writing the solution to (6.9a) so as to obtain the geometric relation between r and θ . First, let us define (see also Section 6.2)

$$u (\theta) = 1 / r (\theta) \tag {6.69b}$$

and

$$\lambda = r _ {i} V _ {R} ^ {2} / \mu . \tag {6.70}$$

The parameter λ (identified with the parameter $\Delta _ { o ; }$ see also (6.24) and Sections 6.3 and 6.4.1) is the dimensionless ratio of twice the kinetic energy at burnout to the potential energy at burnout [18]. For elliptic orbits, λ varies between zero and two and has a value of two at escape velocity. Specifically, the parameter λ gives the following conics:

λ < 2, elliptic trajectory,

λ = 2, parabolic trajectory,

λ > 2, hyperbolic trajectory.

Using (6.69a), (6.69b), and (6.70) in (6.9a), one obtains for the transformed equation of motion the following expression:

$$d ^ {2} u / d \theta^ {2} + u = \mu / h ^ {2} = 1 / (\lambda r _ {i} \sin^ {2} \gamma). \tag {6.71}$$

This is (6.18). From Figure 6.11, letting t = 0 corresponds to θ = 0, so that the appropriate initial conditions are

$$u (0) = 1 / r _ {i}, \tag {6.72a}d u / d \theta | _ {\theta = 0} = - (1 / r _ {i}) \cot \gamma . \tag {6.72b}$$

Therefore, the complete solution to the differential equation (6.71) is

$$
\begin{array}{l} r _ {i} u (\theta) = r _ {i} / r (\theta) = \left[ (1 - \cos \theta) / \left(\lambda \sin^ {2} \gamma\right) \right] + \left[ \sin (\gamma - \theta) / \sin \gamma \right] \\ = [ \mu (1 - \cos \theta) / r _ {i} V ^ {2} \sin^ {2} \gamma ] + [ \sin (\gamma - \theta) / \sin \gamma ]. \tag {6.73} \\ \end{array}
$$

It should be noted that the solution has been written in terms of the burnout variables, since these are the quantities that are actually controlled by a guidance system. Given the above development, we can now proceed to write the hit equation. The conditions necessary that the vehicle impact the target are

$$r = r _ {t}, \tag {6.74a}$$

when

$$\theta = \phi . \tag {6.74b}$$

Substituting (6.74) into (6.73) we obtain the spherical Earth hit equation [9], [16]:

$$r _ {i} / r _ {t} = \left[ (1 - \cos \phi) / \lambda \sin^ {2} \gamma \right] + \left[ \sin (\gamma - \phi) / \sin \gamma \right], \tag {6.75}$$

Solving (6.75) for λ results in the following expression:
