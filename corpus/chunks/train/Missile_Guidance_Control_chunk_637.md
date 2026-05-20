# 6.6 Derivation of the Force Equation for Ballistic Missiles

A ballistic missile (or rocket) is a variable-mass vehicle that acquires thrust by the ejection of high-speed particles. A short nonrigorous derivation of the linear force equation is given in this section. The sum of the external forces acting on any system of particles equals the rate of change of linear momentum of the system. Mathematically, this can be expressed as [14]

$$\Sigma \mathbf {F} = m \left(\frac {d \mathbf {V}}{d t}\right) + m _ {g} \mathbf {V} _ {g}, \tag {6.212}$$

where

$$
\begin{array}{l} m = \text { mass   of   the   missile }, \\ \mathbf {V} = \text { velocity   of   the   missile }, \\ m _ {g} = \text { mass   of   the   escaping   gas }, \\ \begin{array}{l} \mathbf {V} _ {g} = \text { velocity   of   the   escaping   gas   (this   velocity   should } \\ \text { not   be   confused   with   the   velocity - to - be - gained } \\ \text { vector   discussed   earlier). } \end{array} \\ \end{array}
$$

(Note that as before, the dot over a variable is used to denote differentiation with respect to time.) It will be assumed here that the only external force on the missile arises from gravitational acceleration; hence, (6.212) may be written as

$$m \mathbf {g} = m \left(\frac {d \mathbf {V}}{d t}\right) + \left(\frac {d m}{d t}\right) \mathbf {V} + m \left(\frac {d \mathbf {V} _ {g}}{d t}\right) + \left(\frac {d m _ {g}}{d t}\right) \mathbf {V} _ {g}. \tag {6.213a}$$

Now, $( d \mathbf { V } _ { g } / d t ) = 0$ when the gas exits into free space, and $( d m / d t ) = - ( d m _ { g } / d t )$ , since the total system mass is a constant. Thus,

$$
\begin{array}{l} m \mathbf {g} = m \left(\frac {d \mathbf {V}}{d t}\right) + \left(\frac {d m _ {g}}{d t}\right) (\mathbf {V} _ {g} - \mathbf {V}) \\ = m \left(\frac {d \mathbf {V}}{d t}\right) + \left(\frac {d m _ {g}}{d t}\right) \mathbf {c} = m \left(\frac {d \mathbf {V}}{d t}\right) - \mathbf {T}, \tag {6.213b} \\ \end{array}
$$

where

c = escape gas velocity (or ejection velocity) with respect to the missile; also called specific impulse,

$$\mathbf {T} = \text { missile thrust vector } = - \left(\frac {d m _ {g}}{d t}\right) \mathbf {c}.$$

Equation (6.213b) may be divided by m, resulting in [9], [11]

$$\frac {d ^ {2} \mathbf {R}}{d t ^ {2}} = \left(\frac {d \mathbf {V}}{d t}\right) = \mathbf {g} + \mathbf {a} _ {T}, \tag {6.214}$$

where $\mathbf { a } _ { T }$ is the thrust acceleration and is given by

$$\mathbf {a} _ {T} = \mathbf {T} / m. \tag {6.215}$$
