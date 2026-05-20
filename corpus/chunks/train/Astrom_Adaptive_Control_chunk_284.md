# Summary

Having derived the MIT rule and investigated some of its properties, we can now summarize some of the key issues. The model-reference control problem can be described as follows: Let the desired performance be specified by a reference model having the transfer function $G_{m}(s)$ , and let the closed-loop transfer function of the plant be $G(s,\theta)$ , where $\theta$ are the adjustable parameters. Furthermore, let $u_{c}$ be the command signal. The model-reference adaptive system tries to change the controller parameters so that the error

$$e (t) = (G (p, \theta) - G _ {m} (p)) u _ {c} (t)$$

goes to zero. The MIT rule given by

$$\frac {d \theta}{d t} = \gamma \varphi e$$

where $\varphi = \partial e/\partial\theta$ and $\gamma$ is the adaptation gain, can be interpreted as a gradient method for minimizing the error. The MIT rule can be applied in many different cases; a few examples have been given in this section. The choice of the adaptation gain is critical and depends on the signal levels. The normalized algorithm

$$\frac {d \theta}{d t} = \gamma \frac {\varphi e}{\alpha + \varphi^ {T} \varphi}$$

is less sensitive to signal levels. Notice that a normalization of a similar type is obtained automatically in the self-tuning regulator. Compare with Eq. (3.22).

Preliminary numerical experiments indicate that the systems obtained with the MIT rule work as expected for small adaptation gains. Very complex behavior may be obtained for high adaptation gains. To proceed to develop our understanding of adaptive systems, we will investigate the stability problem.
