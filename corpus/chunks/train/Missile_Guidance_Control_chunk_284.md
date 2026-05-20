where the closing $v _ { c }$ is equal $\mathbf { t o } - ( d R / d t )$ , and N is given in terms of (4.32). Equation (4.35) is the well-known general classical proportional navigation guidance equation and is similar to (4.24). This equation is used to generate the guidance commands, with the missile velocity expressed in terms of the closing velocity $v _ { c }$ (between the missile and the target) and the seeker gimbal angle $( \gamma _ { m } - \lambda )$ . Note that sometimes, the gimbal angle is simply written as $\theta _ { h }$ (assuming that a gimbaled seeker is used). Equation (4.35) appears in the literature in many variations.

At this point, let us consider the special case of a nonmaneuvering target. Specifically, we will investigate the LOS rate $d \lambda / d t$ . Furthermore, we will introduce the range R in (4.28) as the independent variable. Thus, we can form the operator

$$\frac {d}{d t} = \left(\frac {d}{d R}\right) \left(\frac {d R}{d t}\right). \tag {4.36}$$

With this operator, (4.28) becomes

$$R \left(\frac {d R}{d t}\right) \left(\frac {d \dot {\lambda}}{d R}\right) + \dot {\lambda} [ 2 \dot {R} + N v _ {m} \cos (\gamma_ {m} - \lambda) ] = \dot {\gamma} _ {t} v _ {t} \cos (\gamma_ {t} - \lambda). \tag {4.37}$$

From (4.32) we have

$$N v _ {m} \cos (\gamma_ {m} - \lambda) = - N ^ {\prime} \left(\frac {d R}{d t}\right), \tag {4.38}$$

so that (4.37) takes the form

$$R \left(\frac {d R}{d t}\right) \left(\frac {d \dot {\lambda}}{d t}\right) + \dot {\lambda} [ 2 R - N ^ {\prime} R ] = \gamma_ {t} v _ {t} \cos (\gamma_ {t} - \lambda),R \left(\frac {d \dot {\lambda}}{d t}\right) + \dot {\lambda} (2 - N ^ {\prime}) = \dot {\gamma} _ {t} (v _ {t} / R) \cos (\gamma_ {t} - \lambda). \tag {4.39}$$

Substituting

$$\xi = \ln (R _ {o} / R) = - \ln (R / R _ {o}) \tag {4.40}$$

with

$$R = R _ {o} (\text { launch }) \quad \text { corresponding to } \xi = 0,R = 0 (\text { intercept }) \quad \text { corresponding to } \xi = \infty ,$$

from (4.40) one obtains

$$d \xi = - (R _ {o} / R) (d R / R _ {o}), \tag {4.41a}d / d R = - (1 / R) (d / d \xi). \tag {4.41b}$$

Therefore, (4.39) becomes∗

$$d \dot {\lambda} / d \xi + \dot {\lambda} (N ^ {\prime} - 2) = - \dot {\gamma} _ {t} (v _ {t} / \dot {R}) \cos (\gamma_ {t} - \lambda). \tag {4.42}$$

If we assume that the target is flying a straight-line course, then ${ d \gamma _ { t } } / { d t } = 0$ , and the solution of homogeneous differential equation takes the form

$$\dot {\lambda} (\xi) = \dot {\lambda} _ {o} e ^ {(2 - N ^ {\prime}) \xi}. \tag {4.43}$$
