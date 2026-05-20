It is well known that the response in α for this system will be a damped oscillatory motion that decays to zero. Equation (3.61) has the solution $\alpha = r e ^ { \lambda t }$ . Substituting results in

$$\lambda^ {2} + 2 \zeta \omega \lambda + \omega^ {2} = 0. \tag {3.62}$$

Solving for the eigenvalue λ yields two solutions as follows:

$$\lambda_ {1, 2} = - \zeta \omega \pm j \omega \sqrt {1 - \zeta^ {2}}, \tag {3.63}$$

where j is a complex number. Now let

$$r _ {1} = a - j b \quad \text { for } \lambda_ {1},r _ {2} = a + j b \quad \text { for } \lambda_ {2}.$$

Substitute both solutions into (3.61) and add the equations to obtain the result for $\alpha ( t )$ . Thus,

$$\alpha (t) = e ^ {- \zeta \omega t} \left(a \cos \omega t \sqrt {1 - \zeta^ {2}} + b \sin \omega t \sqrt {1 - \zeta^ {2}}\right). \tag {3.64}$$

Differentiating $\alpha ( t )$ , we obtain

$$
\begin{array}{l} \frac {d \alpha (t)}{d t} = e ^ {- \zeta \omega t} \left[ \left(b \omega \sqrt {1 - \zeta^ {2}} - a \zeta \omega\right) \cos \omega t \sqrt {1 - \zeta^ {2}} \right. \\ \left. - \left(a \omega \sqrt {1 - \zeta^ {2}} + b \zeta \omega\right) \sin \omega t \sqrt {1 - \zeta^ {2}} \right]. \tag {3.65} \\ \end{array}
$$

Given the initial conditions $\alpha _ { 0 }$ and $d \alpha _ { 0 } / d t$ , a and b can be solved for by setting $t = 0$ . Thus,

$$a = \alpha_ {0},b = \frac {\dot {\alpha} _ {0} + \zeta \omega \alpha_ {0}}{\omega \sqrt {1 - \zeta^ {2}}}.$$

Therefore, the time responses for $\alpha ( t )$ and $d \alpha ( t ) / d t$ become

$$
\alpha (t) = \alpha_ {0} e ^ {- \zeta \omega t} \left(\cos \omega t \sqrt {1 - \zeta^ {2}} + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega t \sqrt {1 - \zeta^ {2}}\right) \tag {3.66}
\begin{array}{l} \frac {d \alpha (t)}{d t} = \dot {\alpha} _ {0} e ^ {- \zeta \omega t} \left(\cos \omega t \sqrt {1 - \zeta^ {2}} - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega t \sqrt {1 - \zeta^ {2}}\right) \\ - \alpha_ {0} \frac {\omega}{\sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega t} \sin \omega t \sqrt {1 - \zeta^ {2}}. \tag {3.67} \\ \end{array}
$$

Next, if a tip-off behavior exists at launch, we can solve for the peaks by setting $d \alpha ( t ) / d t = 0$ :

$$0 = - \alpha_ {0} \frac {\omega}{\sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega t} \sin \omega t \sqrt {1 - \zeta^ {2}}.$$

We note that peaks are periodic according to the sine wave function. Therefore, time to peaks are given by
