# Parametric Uncertainty: A Mass/Spring/Damper System

One natural type of uncertainty is unknown coefficients in a state-space model. To motivate this type of uncertainty description, we shall begin with a familiar mechanical system, shown in Figure 9.1.

![](image/6a4c749fcc2e8e018c6acb08c1b45610eb3a4b983d2645a3802abc93e1775042.jpg)

<details>
<summary>text_image</summary>

m
k
c
F
</details>

Figure 9.1: A mass/spring/damper system

The dynamical equation of the system motion can be described by

$$\ddot {x} + \frac {c}{m} \dot {x} + \frac {k}{m} x = \frac {F}{m}.$$

Suppose that the three physical parameters $m , c ,$ and k are not known exactly, but are believed to lie in known intervals. In particular, the actual mass m is within 10% of a nominal mass, ¯m, the actual damping value c is within 20% of a nominal value of ${ \bar { c } } ,$ and the spring stiffness is within 30% of its nominal value of ${ \bar { k } } .$ . Now introducing perturbations $\delta _ { m } , \delta _ { c }$ , and $\delta _ { k }$ , which are assumed to be unknown but lie in the interval $[ - 1 , 1 ] .$ , the block diagram for the dynamical system is as shown in Figure 9.2.

It is easy to check that $\begin{array} { l } { { \frac { 1 } { m } } } \end{array}$ can be represented as an LFT in $\delta _ { m }$ :

$$\frac {1}{m} = \frac {1}{\bar {m} (1 + 0 . 1 \delta_ {m})} = \frac {1}{\bar {m}} - \frac {0 . 1}{\bar {m}} \delta_ {m} (1 + 0. 1 \delta_ {m}) ^ {- 1} = \mathcal {F} _ {\ell} (M _ {1}, \delta_ {m})$$

with $M _ { 1 } = \left\lceil \begin{array} { c c } { \frac 1 { \bar { m } } } & { - \frac { 0 . 1 } { \bar { m } } } \\ { 1 } & { - 0 . 1 } \end{array} \right\rceil$ Suppose that the input signals of the dynamical system are selected as $x _ { 1 } = x , x _ { 2 } { \overset { - } { = } } { \dot { x } } , F$ , and the output signals are selected as ${ \dot { x } } _ { 1 }$ and ${ \dot { x } } _ { 2 }$ . To represent the system model as an LFT of the natural uncertainty parameters $\delta _ { m } , \delta _ { c } .$ and $\delta _ { k }$ , we shall first isolate the uncertainty parameters and denote the inputs and outputs of $\delta _ { k } , \delta _ { c } .$ , and $\delta _ { m }$ as $y _ { k } , y _ { c } , y _ { m }$ and $u _ { k } , u _ { c } , u _ { m }$ , respectively, as shown in Figure 9.3.

![](image/c1ad8bab548679f8c9adc4d5f40a9d06072704191b22e8319a9e504f1080927e.jpg)

<details>
<summary>flowchart</summary>
