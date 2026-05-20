$$
\begin{array}{l} \frac {d X _ {e}}{d t} = (\cos \theta \cos \psi) u + (\cos \psi \sin \phi \sin \theta - \sin \psi \cos \phi) v \\ + (\cos \psi \cos \phi \sin \theta + \sin \psi \sin \phi) w, \\ \end{array}
\frac {d Y _ {e}}{d t} = (\cos \theta \sin \psi) u + (\sin \psi \sin \phi \sin \theta + \cos \psi \cos \phi) v+ (\sin \psi \cos \phi \sin \theta - \cos \psi \sin \phi) w,\frac {d Z _ {e}}{d t} = - (\sin \theta) u + (\sin \phi \cos \theta) v + (\cos \theta \cos \phi) w,
$$

or in matrix form,

$$
\frac {d}{d t} \left[ \begin{array}{l} X _ {e} \\ Y _ {e} \\ Z _ {e} \end{array} \right] = C _ {e} ^ {b} \left[ \begin{array}{l} u \\ v \\ w \end{array} \right]. \tag {2.49}
$$

From (2.49) we can obtain the equations for $( X _ { e } , Y _ { e } , Z _ { e } )$ in the form

$$X _ {e} = X _ {e, 0} + \int_ {0} ^ {t} \left(\frac {d X _ {e}}{d t}\right) d t, \tag {2.50a}Y _ {e} = Y _ {e, 0} + \int_ {0} ^ {t} \left(\frac {d Y _ {e}}{d t}\right) d t, \tag {2.50b}Z _ {e} = Z _ {e, 0} + \int_ {0} ^ {t} \left(\frac {d Z _ {e}}{d t}\right) d t, \tag {2.50c}$$

and the altitude is

$$h = - Z _ {e}. \tag {2.50d}$$

In the foregoing discussion, only the missile velocities relative to the ground or inertial velocities have been mentioned. If wind is being considered, the missile velocities relative to the wind must be computed, since these velocities are needed in computing the aerodynamic forces and moments (see Chapter 3).
