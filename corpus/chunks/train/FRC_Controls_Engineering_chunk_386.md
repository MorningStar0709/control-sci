# 12.5.1 Force derivation

Consider figure 12.6a, which shows the forces acting on a pendulum.

Note that the path of the pendulum sweeps out an arc of a circle. The angle θ is measured in radians. The blue arrow is the gravitational force acting on the bob, and the violet arrows are that same force resolved into components parallel and perpendicular to the bob’s instantaneous motion. The direction of the bob’s instantaneous velocity always points along the red axis, which is considered the tangential axis because its direction is always tangent to the circle. Consider Newton’s second law

$$F = m a$$

where F is the sum of forces on the object, m is mass, and a is the acceleration. Because we are only concerned with changes in speed, and because the bob is forced to stay in a circular path, we apply Newton’s equation to the tangential axis only. The short violet arrow represents the component of the gravitational force in the tangential axis, and trigonometry can be used to determine its magnitude. Therefore

$$
\begin{array}{l} - m g \sin \theta = m a \\ a = - g \sin \theta \\ \end{array}
$$

where g is the acceleration due to gravity near the surface of the earth. The negative sign on the right hand side implies that θ and a always point in opposite directions. This makes sense because when a pendulum swings further to the left, we would expect it to accelerate back toward the right.

This linear acceleration a along the red axis can be related to the change in angle θ by the arc length formulas; s is arc length and l is the length of the pendulum.

$$s = l \theta \tag {12.26}v = \frac {d s}{d t} = l \frac {d \theta}{d t}a = \frac {d ^ {2} s}{d t ^ {2}} = l \frac {d ^ {2} \theta}{d t ^ {2}}$$

Therefore,

$$l \frac {d ^ {2} \theta}{d t ^ {2}} = - g \sin \theta{\frac {d ^ {2} \theta}{d t ^ {2}}} = - {\frac {g}{l}} \sin \theta\ddot {\theta} = - \frac {g}{l} \sin \theta$$
