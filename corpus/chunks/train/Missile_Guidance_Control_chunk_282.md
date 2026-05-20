where N is the navigation constant (see also (4.24)). Equations (4.25a), (4.25b), and (4.26) represent the complete equations of motion for the system. The dependent variables are $R , \gamma _ { m }$ , and λ; the velocities $v _ { m } , v _ { t }$ and the target’s flight path angle $\gamma _ { t }$ must be known or assumed. The usual means of implementing a proportional navigation guidance system is to use the target tracker (or seeker) to measure the line-of-sight rate $( d \lambda / d t )$ .

We will now develop the general proportional navigation guidance equation. In order to do this, we begin by differentiating (4.25a), yielding

$$
\dot {R} \dot {\lambda} + R \ddot {\lambda} = (\dot {\gamma} _ {t} - \dot {\lambda}) v _ {t} \cos (\gamma_ {t} - \lambda) - (\dot {\gamma} _ {m} - \dot {\lambda}) v _ {m} \cos (\gamma_ {m} - \lambda), \tag {4.27a}
\begin{array}{l} \dot {R} \dot {\lambda} + R \ddot {\lambda} = \gamma_ {t} v _ {t} \cos (\gamma_ {t} - \lambda) - \dot {\gamma} _ {m} v _ {m} \cos (\gamma_ {m} - \lambda) - \dot {\lambda} [ v _ {t} \cos (\gamma_ {t} - \lambda) \\ \left. - v _ {m} \cos \left(\gamma_ {m} - \lambda\right) \right]. \tag {4.27b} \\ \end{array}
$$

Substituting (4.25b) and (4.26) into (4.27b), we obtain

$$2 \dot {R} \dot {\lambda} + R \ddot {\lambda} = \dot {\gamma_ {t}} \cos (\gamma_ {t} - \lambda) - N \dot {\lambda} v _ {m} \cos (\gamma_ {m} - \lambda),$$

or

$$\frac {d ^ {2} \lambda}{d t ^ {2}} + (\dot {\lambda} / R) [ 2 \dot {R} + N v _ {m} \cos (\gamma_ {m} - \lambda) ] = (1 / R) \dot {\gamma} _ {t} v _ {t} \cos (\gamma_ {t} - \lambda). \tag {4.28}$$

In the above derivation, we note that the equation system consisting of (4.25b), (4.26), and (4.28) constitutes the proportional navigation guidance in the plane. We will now investigate the case whereby the target flies a straight-line course. For a straightline course, the target’s flight path angle rate in (4.28) is zero; that is, ${ d \gamma _ { t } } / { d t } = 0$ . Therefore, with this condition we have a homogeneous differential equation for $d \lambda / d t$ . Now, in order for $d \lambda / d t$ to approximate the zero line, $d \lambda / d t$ and $d ^ { \bar { 2 } } \lambda / d t ^ { 2 }$ must have different signs. Thus, we have the inequality

$$2 \left(\frac {d R}{d t}\right) + N v _ {m} \cos (\gamma_ {m} - \lambda) > 0, \tag {4.29}$$

since by definition $R > 0$ . From (4.29), we obtain the navigation ratio N as
