For another particular path $\Delta s = j \Delta \omega$ (which means that the path is parallel to the imaginary axis),

$$\frac {d}{d s} G (s) = \lim _ {j \Delta \omega \rightarrow 0} \left(\frac {\Delta G _ {x}}{j \Delta \omega} + j \frac {\Delta G _ {y}}{j \Delta \omega}\right) = - j \frac {\partial G _ {x}}{\partial \omega} + \frac {\Delta G _ {y}}{\partial \omega}$$

If these two values of the derivative are equal,

$$\frac {\partial G _ {x}}{\partial \sigma} + j \frac {\partial G _ {y}}{\partial \sigma} = \frac {\partial G _ {y}}{\partial \omega} - j \frac {\partial G _ {x}}{\partial \omega}$$

or if the following two conditions

$$\frac {\partial G _ {x}}{\partial \sigma} = \frac {\partial G _ {y}}{\partial \omega} \quad \text { and } \quad \frac {\partial G _ {y}}{\partial \sigma} = - \frac {\partial G _ {x}}{\partial \omega}$$

are satisfied, then the derivative dG $( s ) / d s$ is uniquely determined.These two conditions are known as the Cauchy–Riemann conditions. If these conditions are satisfied, the function $G ( s )$ is analytic.

As an example, consider the following $G ( s )$ :

$$G (s) = \frac {1}{s + 1}$$

Then

$$G (\sigma + j \omega) = \frac {1}{\sigma + j \omega + 1} = G _ {x} + j G _ {y}$$

where

$$G _ {x} = \frac {\sigma + 1}{(\sigma + 1) ^ {2} + \omega^ {2}} \quad \text { and } \quad G _ {y} = \frac {- \omega}{(\sigma + 1) ^ {2} + \omega^ {2}}$$

It can be seen that, except at $s = - 1$ (that is, $\sigma = - 1 , \omega = 0 )$ , G(s) satisfies the Cauchy–Riemann conditions:

$$\frac {\partial G _ {x}}{\partial \sigma} = \frac {\partial G _ {y}}{\partial \omega} = \frac {\omega^ {2} - (\sigma + 1) ^ {2}}{[ (\sigma + 1) ^ {2} + \omega^ {2} ] ^ {2}}\frac {\partial G _ {y}}{\partial \sigma} = - \frac {\partial G _ {x}}{\partial \omega} = \frac {2 \omega (\sigma + 1)}{[ (\sigma + 1) ^ {2} + \omega^ {2} ] ^ {2}}$$

Hence $G ( s ) = 1 / ( s + 1 )$ is analytic in the entire s plane except at $s = - 1$ . The derivative $d G \left( s \right) / d s$ , except at $s = 1$ , is found to be

$$
\begin{array}{l} \frac {d}{d s} G (s) = \frac {\partial G _ {x}}{\partial \sigma} + j \frac {\partial G _ {y}}{\partial \sigma} = \frac {\partial G _ {y}}{\partial \omega} - j \frac {\partial G _ {x}}{d \omega} \\ = - \frac {1}{(\sigma + j \omega + 1) ^ {2}} = - \frac {1}{(s + 1) ^ {2}} \\ \end{array}
$$

Note that the derivative of an analytic function can be obtained simply by differentiating $G ( s )$ with respect to s. In this example,
