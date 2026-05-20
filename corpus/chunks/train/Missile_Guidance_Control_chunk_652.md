Equation (6.239) is the vector acceleration in polar coordinates in terms of the unit vectors $\mathbf { e } _ { r }$ and $\mathbf { e } _ { \theta }$ . The flight-path angle γ , which is negative for reentry, is given by the relation

$$\tan \gamma = v / u. \tag {6.240}$$

The aerodynamic force ${ \bf F } _ { a }$ can be obtained from Figure 6.34 as follows:

$$\mathbf {F} _ {a} = (- m g + L \cos \gamma - D \sin \gamma) \mathbf {e} _ {r} - (D \cos \gamma + L \sin \gamma) \mathbf {e} _ {\theta}, \tag {6.241}$$

where L is the lift force, D is the drag, g is the acceleration of gravity, and m is the mass of the reentry vehicle. From the acceleration and aerodynamic force equations, we obtain, after dividing through by m,

$$- \left(\frac {d ^ {2} y}{d t ^ {2}}\right) = - \left(\frac {d v}{d t}\right) = g - (u ^ {2} / r) - (L / m) \cos \gamma + (D / m) \sin \gamma , \tag {6.242a}\left(\frac {d u}{d t}\right) + (u v / r) = - (D / m) [ \cos \gamma + (L / D) \sin \gamma ]. \tag {6.242b}$$

It should be noted that g and r are local values in these equations. This system of equations can be further simplified by neglecting the ${ \boldsymbol { u } } { \boldsymbol { v } } / r$ term. The omission of this term can be justified in light of the fact that during reentry, maximum deceleration and heating occur at very small reentry angles and that ${ \boldsymbol { u } } { \boldsymbol { v } } / r$ is on the order of 1% of du/dt. Consequently, (6.242b) reduces to

$$\frac {d u}{d t} = - (D / m) \cos \gamma [ 1 + (L / D) \tan \gamma ]. \tag {6.243}$$

Assuming now that $| ( L / D )$ tan $\gamma | < 1$ , and noting that $V = ( u / \cos \gamma )$ , where $V =$ $( u ^ { 2 } + v ^ { 2 } ) ^ { 1 / 2 }$ , we have

$$\frac {d u}{d t} = - [ \rho_ {\infty} / 2 (m / C _ {D} S) ] (u ^ {2} / \cos \gamma), \tag {6.244}$$

where

$$C _ {D} = \text { coefficient of drag } = C _ {D} = \frac {D}{\frac {1}{2} \rho_ {\infty} V ^ {2} S},$$

S = reference area for drag and lift,

D = drag force,

$\rho _ { \infty }$ = atmospheric density free stream (ambient atmosphere).

Furthermore, selecting as the independent variable the expression

$$\bar {u} \equiv u / u _ {c} \equiv u / \sqrt {g r}, \tag {6.245}$$

where $u _ { c }$ is the circular orbit velocity, we obtain

$$\frac {d u}{d t} = \frac {d (\sqrt {g r} \bar {u})}{d t} = \sqrt {g r} \left(\frac {d \bar {u}}{d t}\right). \tag {6.246}$$

Introducing now the drag coefficient in (6.242a) results in
