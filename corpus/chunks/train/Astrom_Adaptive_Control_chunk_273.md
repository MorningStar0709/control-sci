# EXAMPLE 5.2 MRAS for a first-order system

Consider a system described by the model

$$\frac {d y}{d t} = - a y + b u \tag {5.6}$$

where u is the control variable and y is the measured output. Assume that we want to obtain a closed-loop system described by

$$\frac {d y _ {m}}{d t} = - a _ {m} y _ {m} + b _ {m} u _ {c}$$

Let the controller be given by

$$u (t) = \theta_ {1} u _ {c} (t) - \theta_ {2} y (t) \tag {5.7}$$

The controller has two parameters. If they are chosen to be

$$\theta_ {1} = \theta_ {1} ^ {0} = \frac {b _ {m}}{b} \tag {5.8}\theta_ {2} = \theta_ {2} ^ {0} = \frac {a _ {m} - a}{b}$$

the input-output relations of the system and the model are the same. This is called perfect model-following.

To apply the MIT rule, introduce the error

$$e = y - y _ {m}$$

where $y$ denotes the output of the closed-loop system. It follows from Eqs. (5.6) and (5.7) that

$$y = \frac {b \theta_ {1}}{p + a + b \theta_ {2}} u _ {c}$$

where p = d/dt is the differential operator. The notation used is discussed in Section 1.5. The sensitivity derivatives are obtained by taking partial derivatives with respect to the controller parameters $\theta_{1}$ and $\theta_{2}$ :

$$\frac {\partial e}{\partial \theta_ {1}} = \frac {b}{p + a + b \theta_ {2}} u _ {c}\frac {\partial e}{\partial \theta_ {2}} = - \frac {b ^ {2} \theta_ {1}}{(p + a + b \theta_ {2}) ^ {2}} u _ {c} = - \frac {b}{p + a + b \theta_ {2}} y$$

These formulas cannot be used directly because the process parameters a and b are not known. Approximations are therefore required. One possible approximation is based on the observation that $p + a + b\theta_{2}^{0} = p + a_{m}$ when the parameters give perfect model-following. We will therefore use the approximation

![](image/2e77a15f5e38c5da0610db18f0aef8814e580f72427df2f4f6a7ec4de2e31263.jpg)

<details>
<summary>flowchart</summary>
