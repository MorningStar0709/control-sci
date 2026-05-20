In Figure 6.32, the values of $T _ { v o } t _ { I }$ (ignition time), $t _ { T o }$ (tailoff time from ignition), $t _ { B }$ (burn time from ignition) are, except for second-stage ignition $\left( t _ { \mathrm { I 2 } } \right)$ , inputs for each stage $( t _ { \mathrm { I } 2 }$ is assumed to be the time of first-stage separation). However, these values are subject to perturbation. With constant weight flow rate, the mass (m) is a linear function of time:

$$m = m _ {o} + \left(\frac {d m}{d t}\right) (t - t _ {I}), \tag {6.218a}\frac {d m}{d t} = (m _ {F} - m _ {o}) / t _ {B} = \text { constant }, \tag {6.218b}$$

where $m _ { o } = m ( t _ { I } )$ and $m _ { F } = m ( t _ { I } + t _ { B } )$ are inputs for each stage and are subject to perturbation. Equation (6.218b) is a realistic assumption, stating that a constant rate of fuel consumption leads to a constant thrust. Aerodynamic drag (D) is determined by the drag coefficient $C _ { D }$ , cross-sectional reference area S, and the dynamic pressure $q \mathrm { . }$ :

$$D = C _ {D} S q, \tag {6.219a}$$

where S is an input for each stage (usually identical values), and

$$q = \frac {1}{2} \rho V _ {R} ^ {2}, \tag {6.219b}$$

with $\rho$ the air density (nominally an exponential function of altitude, but subject to a perturbation that also depends on altitude), and $V _ { R }$ is the magnitude of the missile velocity relative to the atmosphere. Thus,

$$\mathbf {V} _ {R} = \mathbf {V} _ {m} + \mathbf {V} _ {L P} - (\omega_ {i e} \times \mathbf {R} + \mathbf {V} _ {W}), \tag {6.220}$$

where $\mathbf { V } _ { L P }$ is the launch-point velocity, ${ \bf V } _ { W }$ is the wind-velocity vector perturbation that depends on altitude, and $( \omega _ { i e } \times \mathbf { R } )$ ) represents the nominal $( \mathbf { V } _ { W } = 0 )$ velocity of the atmosphere. Earth rate $\omega _ { i e }$ in guidance axes is given by

$$\omega_ {i e X} = \omega_ {i e} (\cos \varphi_ {L P} \cos \psi \cos \alpha_ {X} + \sin \varphi_ {L P} \sin \alpha_ {X}),\omega_ {i e Y} = - \omega_ {i e} \cos \varphi_ {L P} \sin \psi ,\omega_ {i e Z} = \omega_ {i e} (\cos \varphi_ {L P} \cos \psi \sin \alpha_ {X} - \sin \varphi_ {L P} \cos \alpha_ {X}), \tag {6.221}$$
