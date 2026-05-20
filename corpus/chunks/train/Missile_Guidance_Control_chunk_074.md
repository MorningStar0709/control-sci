$$
\begin{array}{l} \delta U = \sum_ {i} (X _ {i} \delta x _ {i} + Y _ {i} \delta y _ {i} + Z _ {i} \delta z _ {i}), \\ = \sum_ {i} m _ {i} \left(\frac {d ^ {2} x _ {i}}{d t ^ {2}} \delta x _ {i} + \frac {d ^ {2} y _ {i}}{d t ^ {2}} \delta y _ {i} + \frac {d ^ {2} z _ {i}}{d t ^ {2}} \delta z _ {i}\right) \\ = \sum_ {i} m _ {i} \left[ \frac {d}{d t} (\dot {x} _ {i} \delta x _ {i} + \dot {y} _ {i} \delta y _ {i} + \dot {z} _ {i} \delta z _ {i}) - \dot {x} _ {i} \delta \dot {x} _ {i} - \dot {y} _ {i} \delta \dot {y} _ {i} - \dot {z} _ {i} \delta \dot {z} _ {i} \right] \tag {2.60} \\ \end{array}
$$

where the symbol $\scriptstyle \sum$ denotes summation over all the particles of the system; this can be either an integration (if the particles are united into rigid bodies) or a summation over a discrete aggregate of particles. The quantity δU is defined by the first equality in (2.60). It is the work done by the forces of the system during the infinitesimal displacement $( \delta x _ { i } , \ldots , \delta z _ { n } )$ and is a function of the time and the independent coordinates of the system. If the forces do not depend explicitly on the time, δU can be expressed as a function of the coordinates only. The last part of (2.60) represents the variation of the kinetic energy δT . Hence the equation can be written as [3]

$$\delta T + \delta U = \sum_ {i} m _ {i} \frac {d}{d t} (x _ {i} \delta x _ {i} + y _ {i} \delta y _ {i} + z _ {i} \delta z _ {i}). \tag {2.61}$$

It should be noted that in the above expressions t is the independent variable. Now, if both sides of (2.61) are integrated with respect to this independent variable between the limits $t _ { 1 }$ and $t _ { 2 }$ , the result is

$$\int_ {t _ {1}} ^ {t _ {2}} (\delta T + \delta U) d t = \delta \int_ {t _ {1}} ^ {t _ {2}} T d t + \int_ {t _ {1}} ^ {t _ {2}} \delta U d t = 0. \tag {2.62}$$

In this equation, we note that the right-hand side is zero because all of the variations are zero at both limits. Therefore, (2.62) is a property of the path that satisfies the equations of motion, and this property furnishes a way of defining the true path of the system. In the special case in which the forces are conservative, that is, when they can be derived from the potential energy, δU is the negative of the variation of the potential energy. Consequently, we have

$$\delta \int_ {t _ {1}} ^ {t _ {2}} (T - U) d t = \delta \int_ {t _ {1}} ^ {t _ {2}} L d t = 0, \tag {2.63}$$

where T is the kinetic energy and U is the potential energy.
