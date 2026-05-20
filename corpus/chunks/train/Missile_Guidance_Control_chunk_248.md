![](image/65e9ce0b81764b9be034fcbb74e48ccb140297e81c3953db35bcb5123c6482b4.jpg)

<details>
<summary>text_image</summary>

V = Velocity
T = Thrust vector
</details>

L = Lift acceleration vector = aL1L   
N = Normal acceleration vector   
A = Total aerodynamic acceleration vector   
D = Drag acceleration vector = –av1v   
X = Axial acceleration vector   
= Angle-of-attack

Fig. 4.5. Definition of aerodynamic and thrust acceleration vectors.

In these equations, r, v, and a are the missile’s position, velocity, and acceleration vectors, respectively; ${ \bf 1 } _ { v }$ and $\mathbf { 1 } _ { L }$ are unit vectors in the velocity and lift directions; $a _ { v }$ and $a _ { L }$ are the corresponding components of thrust and aerodynamic acceleration; and g is the gravitational acceleration. The gravity term is assumed to be constant (i.e., Earth-surface value). The acceleration terms $a _ { v }$ and $a _ { L }$ are given as follows:

$$a _ {v} = (1 / m) [ (T - C _ {x} Q A) \cos \alpha - C _ {N} Q A \sin \alpha ], \tag {4.2a}a _ {L} = (1 / m) [ (T - C _ {x} Q A) \sin \alpha + C _ {N} Q A \cos \alpha ], \tag {4.2b}$$

where

T = delivered thrust,

m = current mass of the missile,

Q = dynamic pressure = 1 ρv·v,

ρ = atmospheric density, computed as a piecewise exponential function of the missile’s altitude,

$C _ { x }$ = axial aerodynamic force coefficient,

$C _ { N }$ = normal aerodynamic force coefficient.

Two alternative models for the thrust profile are available to the designer. The first assumes a constant vacuum thrust for the duration of the stage burn time,

$$T _ {\text { vac }} = T _ {o}, \tag {4.3a}$$

while the second model assumes a decreasing vacuum thrust shaped to yield constant axial acceleration and is given by

$$T _ {\text { vac }} = T _ {o} [ W _ {f} / W _ {o} ] ^ {(t - t _ {1}) / t _ {b}}, \tag {4.3b}$$

where $t _ { I }$ is the ignition time of the current stage. The delivered thrust is then obtained from the vacuum thrust by the expression

$$T = T _ {\text { vac }} - p A _ {e}, \tag {4.3c}$$

where

$$
\begin{array}{l} \begin{array}{l} p = \text { ambient   atmospheric   pressure   (i.e.,corresponding   to } \\ \text { the   missile's   altitude) } \end{array} \\ = \rho g c ^ {2} / \gamma [ N / m ^ {2} ], \\ c = \text { local   velocity   of   sound } [ \mathrm{m/sec} ], \\ \gamma = \text { gas   ratio   of   specific   heat } [ 1. 4 0 1 ], \\ g = \text { gravitational   constant } [ \mathrm{m} / \sec^ {2} ]. \\ \end{array}
$$
