# 12.5.3 Energy derivation

The equation can also be obtained via the conservation of mechanical energy principle: any object falling a vertical distance h would acquire kinetic energy equal to that which it lost to the fall. In other words, gravitational potential energy is converted into kinetic energy. Change in potential energy is given by

$$\Delta U = m g h$$

The change in kinetic energy (body started from rest) is given by

$$\Delta K = \frac {1}{2} m v ^ {2}$$

Since no energy is lost, the gain in one must be equal to the loss in the other

$$\frac {1}{2} m v ^ {2} = m g h$$

The change in velocity for a given change in height can be expressed as

$$v = \sqrt {2 g h}$$

Using equation (12.26), this equation can be rewritten in terms of $\frac { d \theta } { d t }$ .

$$
\begin{array}{l} v = l \frac {d \theta}{d t} = \sqrt {2 g h} \\ \frac {d \theta}{d t} = \frac {2 g h}{l} \tag {12.27} \\ \end{array}
$$

where $h$ is the vertical distance the pendulum fell. Look at figure 12.6b, which presents the trigonometry of a pendulum. If the pendulum starts its swing from some initial angle $\theta _ { 0 }$ , then $y _ { 0 }$ , the vertical distance from the pivot point, is given by

$$y _ {0} = l \cos \theta_ {0}$$

Similarly for $y _ { 1 }$ , we have

$$y _ {1} = l \cos \theta$$

Then h is the difference of the two

$$h = l (\cos \theta - \cos \theta_ {0})$$

Substituting this into equation (12.27) gives

$$\frac {d \theta}{d t} = \sqrt {\frac {2 g}{l} (\cos \theta - \cos \theta_ {0})}$$

This equation is known as the first integral of motion. It gives the velocity in terms of the location and includes an integration constant related to the initial displacement $( \theta _ { 0 } )$ . We can differentiate by applying the chain rule with respect to time. Doing so gives the acceleration.

$$
\begin{array}{l} {\frac {d}{d t}} {\frac {d \theta}{d t}} = {\frac {d}{d t}} {\sqrt {{\frac {2 g}{l}} (\cos \theta - \cos \theta_ {0})}} \\ {\frac {d ^ {2} \theta}{d t ^ {2}}} = {\frac {1}{2}} {\frac {- {\frac {2 g}{l}} \sin \theta}{\sqrt {{\frac {2 g}{l}} (\cos \theta - \cos \theta_ {0})}}} {\frac {d \theta}{d t}} \\ \end{array}
\frac {d ^ {2} \theta}{d t ^ {2}} = \frac {1}{2} \frac {- \frac {2 g}{l} \sin \theta}{\sqrt {\frac {2 g}{l} (\cos \theta - \cos \theta_ {0})}} \sqrt {\frac {2 g}{l} (\cos \theta - \cos \theta_ {0})}{\frac {d ^ {2} \theta}{d t ^ {2}}} = - {\frac {g}{l}} \sin \theta\ddot {\theta} = - \frac {g}{l} \sin \theta
$$

which is the same result from force analysis.
