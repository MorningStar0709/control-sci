# Missile Flight During Motor Burn

Here we will assume that the thrust is constant during motor burn and that the drag coefficient, air density, and missile mass are also constant. The missile drag D is given by the expression

$$D = 0. 5 \rho V ^ {2} S C _ {D}, \tag {5.74}$$

where

$$\rho = \text { density of air },V = \text { speed },S = \text { reference area },C _ {D} = \text { coefficient of drag }.$$

The acceleration due to drag, AD, is given by

$$A _ {D} = - V ^ {2} \left[ \left(0. 5 \rho S C _ {D}\right) / M \right], \tag {5.75a}$$

where M is the mass of the missile. Since we have assumed that the drag coefficient, air density, and missile mass are constant, the parameter $( 0 . 5 \rho V ^ { 2 } S C _ { D } ) / M$ is also a constant. Denoting this quantity by $D _ { p }$ , then the acceleration due to the drag is given by

$$A _ {D} = - D _ {p} V ^ {2}. \tag {5.75b}$$

If the thrust T is constant, then the net acceleration A is given as follows:

$$A = T - D _ {p} V ^ {2}. \tag {5.76}$$

Therefore, we can write

$$\frac {d s}{d t} = V, \tag {5.77a}\frac {d V}{d t} = T - D _ {p} V ^ {2}. \tag {5.77b}$$

Given the initial conditions $t _ { o } , s _ { o } , V _ { o }$ , if we set

$$u = \exp \left[ D _ {p} \int_ {t _ {0}} ^ {t} V d t \right] = \exp [ D _ {p} (s - s _ {o}) ], \tag {5.78}$$

then we can write

$$\frac {d u}{d t} = D _ {p} u V, \tag {5.79a}\frac {d ^ {2} u}{d t ^ {2}} = D _ {p} \left[ u \left(\frac {d V}{d t}\right) + V \left(\frac {d u}{d t}\right) \right], \tag {5.79b}$$

or

$$\frac {d ^ {2} u}{d t ^ {2}} = D _ {p} [ u (T - D _ {p} V ^ {2}) + D _ {p} u V ^ {2} ] = T D _ {p} u. \tag {5.79c}$$

The general solution is given by

$$u = a \exp [ T ^ {1 / 2} D _ {p} ^ {1 / 2} (t - t _ {o}) ] + b \exp [ - T ^ {1 / 2} D _ {p} ^ {1 / 2} (t - t _ {o}) ]. \tag {5.80}$$

Substituting the initial conditions, we obtain

$$u (t _ {o}) = 1, \left[ \frac {d u}{d t} \right] _ {t} = D _ {p} V _ {o}, \tag {5.81a}a = \left[ 1 + V _ {o} \left(D _ {p} / T\right) ^ {1 / 2} \right] / 2, \tag {5.81b}b = \left[ 1 - V _ {o} \left(D _ {p} / T\right) ^ {1 / 2} \right] / 2. \tag {5.81c}$$

This yields the particular solution

$$u = \cos h [ (T / D _ {p}) ^ {1 / 2} (t - t _ {o}) ] + V _ {o} (D _ {p} / T) \sin h [ (T / D _ {p}) ^ {1 / 2} (t - t _ {o}) ] \tag {5.82}$$

and
