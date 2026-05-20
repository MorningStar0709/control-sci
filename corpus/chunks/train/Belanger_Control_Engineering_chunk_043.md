$$\frac {\partial L}{\partial \dot {x}} = M \dot {x} + m (\dot {x} + \ell \dot {\theta} \cos \theta)\frac {\partial L}{\partial x} = 0\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x}}\right) = M \ddot {x} + m \ddot {x} + m \ell \ddot {\theta} \cos \theta - m \ell (\dot {\theta}) ^ {2} \sin \theta .$$

The equation related to $x$ is

$$(M + m) \ddot {x} + m \ell \ddot {\theta} \cos \theta - m \ell (\dot {\theta}) ^ {2} \sin \theta = F. \tag {2.34}$$

For the $\theta$ equations,

$$
\begin{array}{l} \frac {\partial L}{\partial \dot {\theta}} = m (\dot {x} + \ell \dot {\theta} \cos \theta) \ell \cos \theta + m \ell^ {2} \dot {\theta} \sin^ {2} \theta \\ = m \ell \dot {x} \cos \theta + m \ell^ {2} \dot {\theta} \\ \frac {\partial L}{\partial \theta} = - m (\dot {x} + \ell \dot {\theta} \cos \theta) \ell \dot {\theta} \sin \theta + m \ell^ {2} (\dot {\theta}) ^ {2} \sin \theta \cos \theta + m g \ell \sin \theta \\ = - m \ell \dot {\theta} \dot {x} \sin \theta + m g \ell \sin \theta \\ \end{array}
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {\theta}}\right) = m \ell \ddot {x} \cos \theta - m \ell \dot {\theta} \dot {x} \sin \theta + m \ell^ {2} \ddot {\theta}.
$$

The equation pertaining to $\theta$ is

$$m \ell \ddot {x} \cos \theta - m \ell \dot {\theta} \dot {x} \sin \theta + m \ell^ {2} \ddot {\theta} + m \ell \dot {\theta} \dot {x} \sin \theta - m g \ell \sin \theta = 0$$

or

$$\ddot {x} \cos \theta + \ell \ddot {\theta} - g \sin \theta = 0. \tag {2.35}$$

Equations 2.34 and 2.35 are not state equations.

Define $v = \dot{x}$ and $\omega = \dot{\theta}$ , and write Equations 2.34 and 2.35 as

$$
\left[ \begin{array}{c c} M + m & m \ell \cos \theta \\ \cos \theta & \ell \end{array} \right] \left[ \begin{array}{c} \dot {v} \\ \dot {\omega} \end{array} \right] = \left[ \begin{array}{c} F + m \ell \omega^ {2} \sin \theta \\ g \sin \theta \end{array} \right].
$$

Solving for $\dot{v}$ and $\dot{\omega}$ yields

$$\dot {v} = \frac {F + m \ell \omega^ {2} \sin \theta - m g \sin \theta \cos \theta}{M + m (1 - \cos^ {2} \theta)} \tag {2.36}\dot {\omega} = \frac {- F \cos \theta - m \ell \omega^ {2} \sin \theta \cos \theta + (M + m) g \sin \theta}{\ell [ M + m (1 - \cos^ {2} \theta) ]}. \tag {2.37}$$

Append the definitions

$$\dot {x} = v \tag {2.38}\dot {\theta} = \omega . \tag {2.39}$$

Equations 2.36 to 2.39 are the four state equations. Specific values are $\ell = 1$ m and $M = m = 1$ kg. The state equations are
