$$v ^ {2} = \left(\frac {d r}{d t}\right) ^ {2} + \left(\frac {d \sigma}{d t}\right) ^ {2} r ^ {2} = \left(\frac {d r}{d t}\right) ^ {2} + (H ^ {2} / r ^ {2}). \tag {15}$$

Therefore,

$$\frac {d r}{d t} = \pm [ v ^ {2} - (H ^ {2} / r ^ {2}) ] ^ {1 / 2}. \tag {16}$$

Equations (8), (12), (14), and (16) define four first-order simultaneous differential equations of motion of the reentry vehicle. These equations must be solved by numerical methods, since the atmospheric density and the drag coefficient are known but are not analytic functions of $r ,$ , and there is no closed-form solution to these equations.

As stated in the beginning of this example, the reentry trajectory can be described by the translational motion of a rigid body. The reentry flight model can also be described by the following dynamic equations [15]:

$$
\begin{array}{l} r = v \sin \gamma , \\ \frac {d v}{d t} = - D - g \sin \gamma + \omega^ {2} r \cos \phi [ \cos \phi \sin \gamma - \sin \phi \cos \gamma \sin \psi ], \\ \frac {d \gamma}{d t} = (1 / v) \{L \cos \sigma - [ g - (v ^ {2} / r) ] \cos \gamma + 2 \omega v \cos \phi \cos \psi \\ + \omega^ {2} r \cos \phi [ \cos \phi \cos \gamma + \sin \phi \sin \gamma \sin \psi ] \}, \\ \frac {d \psi}{d t} = (1 / v) \{L (\sin \sigma / \cos \gamma) \\ - \left(v ^ {2} / r\right) \tan \phi \cos \gamma \cos \psi \left(\omega^ {2} r\right) (\sin \phi \cos \phi \cos \psi / \cos \gamma), \\ + 2 \omega v [ \cos \phi \tan \gamma \sin \psi - \sin \phi ] \}, \\ \frac {d \theta}{d t} = v \cos \gamma \cos \psi / r \cos \phi , \\ \frac {d \phi}{d t} = v \cos \gamma \sin \psi / r, \\ \end{array}
$$

where

$$r = \text { distance from the Earth's center },v = \text { Earth - relative speed },\gamma = \text { flight - path angle },g = \text { acceleration of gravity },D = \text { drag acceleration },L = \text { lift acceleration },\theta = \text { geodetic latitude },\phi = \text { geodetic longitude },\sigma = \text { bank angle },\psi = \text { heading angle },\omega = \text { Earth's angular velocity }.$$

Note that in the above equations, $r , v , g , D , L , \rho _ { ; }$ , and ω are normalized parameters $( \mathrm { i } . \mathrm { e } . , r$ is normalized by $R _ { o }$ , the radius of the Earth; v by $( G _ { o } R _ { o } ) ^ { 1 / 2 }$ ; g by $G _ { o }$ , where $G _ { o }$ is the acceleration of gravity at sea level; D by $G _ { o } ; L$ by $G _ { o } ; \rho$ by $( m / S R _ { o } )$ ; and ω by $( G _ { o } / R _ { o } ) ^ { 1 / 2 } )$ ).
