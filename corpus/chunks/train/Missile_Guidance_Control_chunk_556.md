(a) First, the missile velocity is constrained to lie in the plane formed by the present missile position, the center of the Earth, and the target position at the time of impact. This is accomplished by using a yaw steering error signal of the form

$$\varepsilon_ {y a w} = [ \mathbf {r} _ {v} (t _ {o}) \times \mathbf {r} _ {t} (t _ {i}) ] \cdot \mathbf {V} _ {m} (t _ {o}). \tag {8}$$

(b) Secondly, the required velocity to impact is constrained to lie along the missile velocity vector ${ \bf V } _ { m } ( t _ { o } )$ . Thus, whenever the amplitudes of ${ \bf V } _ { m } ( t _ { o } )$ and ${ \bf V } _ { v } ( t _ { o } )$ are equal, the thrust will be terminated. The value obtained in using a guidance scheme of this type is that an arbitrary pitch program can be used. The scheme is, however, complicated by the fact that a variable total time of flight results, necessitating the consideration of a moving target.∗ The development of this guidance scheme will begin with a spherical Earth model and a nonmoving target, and then be expanded to take into account effects of target motion due to the Earth’s angular rate.

(2) Spherical Earth Case: Nonmoving Target For the spherical Earth case, (4) is often written in the form

$$\mathbf {a} _ {v} = - \left(\mu / \mathbf {r} _ {v} ^ {3}\right) \mathbf {r} _ {v}, \tag {9}$$

and it can be shown that the required velocity with a nonmoving target is given by the vis viva integral (6.59)

$$V _ {R} ^ {2} = \mu [ (2 / r _ {v}) - (1 / a) ], \tag {10}$$

where a is the semimajor axis of the resulting elliptical trajectory between the missile’s present position and the target’s position, and is given as (see (6.77))

$$a = (r _ {v} / 2) \{1 + [ r _ {t} (1 - \cos \phi) / (r _ {v} - r _ {t} - r _ {v} \cos 2 \gamma + r _ {t} \cos (2 \gamma - \phi)) ] \}, \tag {11}$$

where $\gamma = \cos ^ { - 1 } ( \mathbf { r } _ { v } \cdot \mathbf { V } _ { v m } / r _ { v } r _ { t } )$ , the angle between the missile local vertical (L.V.) and the velocity heading

$$\phi = \cos^ {- 1} (\mathbf {r} _ {v} \cdot \mathbf {r} _ {t} / r _ {v} r _ {t}),$$

the angle between the missile position and target position.

Substituting (11) into (10) gives (see (6.89))

$$V _ {R} ^ {2} = (2 \mu / r) \{(1 - \cos \phi) / ((r _ {v} / r _ {t}) (1 - \cos 2 \gamma)) - \cos \phi + \cos (2 \gamma - \phi) \}. \tag {12}$$
