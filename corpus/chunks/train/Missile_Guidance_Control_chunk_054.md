Table 2.1. Axis and Moment Nomenclature   
(a) Axis Definition

<table><tr><td>Axis</td><td>Direction</td><td>Name</td><td>Linear Velocity</td><td>Angular Displacement</td><td>Angular Rates</td></tr><tr><td>OX</td><td>Forward</td><td>Roll</td><td>u</td><td>φ</td><td>P</td></tr><tr><td>OY</td><td>Right Wing</td><td>Pitch</td><td>v</td><td>θ</td><td>Q</td></tr><tr><td>OZ</td><td>Downward</td><td>Yaw</td><td>w</td><td>ψ</td><td>R</td></tr></table>

(b) Moment Designation

<table><tr><td>Axis</td><td>Moment of Inertia</td><td>Product of Inertia</td><td>Force</td><td>Moment</td></tr><tr><td>OX</td><td> $I_x$ </td><td> $I_{xy} = 0$ </td><td> $F_x$ </td><td>L</td></tr><tr><td>OY</td><td> $I_y$ </td><td> $I_{yx} = 0$ </td><td> $F_y$ </td><td>M</td></tr><tr><td>OZ</td><td> $I_z$ </td><td> $I_{zx} \neq 0$ </td><td> $F_z$ </td><td>N</td></tr></table>

or

$$\left(\frac {d \mathbf {A}}{d t}\right) _ {\text { inertial }} = \left[ \frac {d \mathbf {A}}{d t} \right] _ {\text { body }} + \boldsymbol {\omega} \times \mathbf {V} _ {M}, \tag {2.21b}$$

where $ { \mathbf { \omega } } _ {  { \mathbf { \omega } } }  { \mathbf { \omega } } _ { \omega }$ is the angular velocity of the missile body coordinate system (X, Y, Z) relative to the fixed (inertial) system $( X ^ { \prime } , Y ^ { \prime } , Z ^ { \prime } )$ , and $\times$ denotes the vector cross product. Normally, the missile’s linear velocity $V _ { M }$ is expressed in the Earth-fixed axis system, so that (2.21a) can be written in the form

$$\left(\frac {d \mathbf {V} _ {M}}{d t}\right) _ {E} = \left(\frac {d \mathbf {V} _ {M}}{d t}\right) _ {\text { rot .coord. }} + \boldsymbol {\omega} \times \mathbf {V} _ {M}, \tag {2.22}$$

where $\omega$ is the total angular velocity vector of the missile with respect to the Earth. In terms of the body axes, we can write the force equation in the form

$$\mathbf {F} = m \left[ \frac {d \mathbf {V} _ {M}}{d t} \right] _ {\text { body }} + m (\boldsymbol {\omega} \times \mathbf {V} _ {M}). \tag {2.23}$$

The first part on the right-hand side of (2.22) can be written as

$$\left(\frac {d \mathbf {V} _ {M}}{d t}\right) _ {\text { rot .coord. }} = \left(\frac {d u}{d t}\right) \mathbf {i} + \left(\frac {d v}{d t}\right) \mathbf {j} + \left(\frac {d w}{d t}\right) \mathbf {k}, \tag {2.24}$$

where
