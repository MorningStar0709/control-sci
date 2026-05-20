$$(d u / d t) = \text { forward (or longitudinal) acceleration },(d v / d t) = \text { right wing (or lateral) acceleration },(d w / d t) = \text { downward (or vertical) acceleration },$$

![](image/d0ed16c6f2f9aa9381ed3810380616c5274bdd7a149d3fbf7fc5b917c2b644b2.jpg)  
Fig. 2.4. General rigid body with angular velocity vector ω about its center of mass.

and the vector cross product as

$$
\boldsymbol {\omega} \times \mathbf {V} _ {M} = \left[ \begin{array}{c c c} \mathbf {i} & \mathbf {j} & \mathbf {k} \\ P & Q & R \\ u & v & w \end{array} \right] = (w Q - v R) \mathbf {i} + (u R - w P) \mathbf {j} + (v P - u Q) \mathbf {k}. \tag {2.25}
$$

Next, from (2.17a) we can write the sum of the forces as

$$\sum \Delta \mathbf {F} = \sum \Delta F _ {x} \mathbf {i} + \sum \Delta F _ {y} \mathbf {j} + \sum \Delta F _ {z} \mathbf {k}. \tag {2.26}$$

Equating the components of (2.24), (2.25), and (2.26) yields the missile’s linear equations of motion. Thus, for a missile with an $X _ { b } - Z _ { b }$ plane of symmetry (see rigid-body assumption #1) we have

$$\sum \Delta F _ {x} = m (\dot {u} + w Q - v R), \tag {2.27a}\sum \Delta F _ {y} = m (\dot {v} + u R - w P), \tag {2.27b}\sum \Delta F _ {z} = m (\dot {w} + v P - u Q). \tag {2.27c}$$

From (2.17b) we can obtain in a similar manner the equations of angular motion. However, before we develop these equations, an expression for H is needed. To this end, consider Figure 2.4.

Now let dm be an element of mass of the missile, V the velocity of the elemental mass relative to the inertial frame, and δF the resulting force acting on the elemental mass.

First of all, and with reference to Figure 2.4(a), the position vector of any particle of the rigid body in a Newtonian frame of reference is the vector sum of the position vector of the center of the mass and the position vector of the particle with respect to the center of mass. Mathematically,

$$\boldsymbol {r} _ {p} = \boldsymbol {r} _ {c m} + \boldsymbol {r} _ {p / c m},$$

where

$$
\boldsymbol {r} _ {p} = \text { the position vector of the particle },\boldsymbol {r} _ {c m} = \text { position vector of the center of mass of the particle },
\begin{array}{c} \boldsymbol {r} _ {p / c m} = \text { position   vector   of   the   particle   with   respect   to   the } \\ \text { center   of   mass. } \end{array}
$$

Note that if this equation is differentiated, we obtain

$$\frac {d \boldsymbol {r} _ {p}}{d t} = \frac {d \boldsymbol {r} _ {c m}}{d t} + \frac {d \boldsymbol {r} _ {p / c m}}{d t}.$$
