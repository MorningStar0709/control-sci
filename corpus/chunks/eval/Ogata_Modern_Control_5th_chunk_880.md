# Laplace Transform Tables

Appendix A first presents the complex variable and complex function.Then it presents tables of Laplace transform pairs and properties of Laplace transforms. Finally, it presents frequently used Laplace transform theorems and Laplace transforms of pulse function and impulse function.

Complex Variable. A complex number has a real part and an imaginary part, both of which are constant. If the real part and/or imaginary part are variables, a complex quantity is called a complex variable. In the Laplace transformation we use the notation s as a complex variable; that is,

$$s = \sigma + j \omega$$

where s is the real part and v is the imaginary part.

Complex Function. A complex function $G ( s )$ , a function of $s ,$ has a real part and an imaginary part or

$$G (s) = G _ {x} + j G _ {y}$$

where $G _ { x }$ and $G _ { y }$ are real quantities. The magnitude of $G ( s )$ is $\sqrt { G _ { x } ^ { 2 } + G _ { y } ^ { 2 } }$ and the, angle u of $G ( s )$ is tan $^ { - 1 } \big ( G _ { y } / \hat { G } _ { x } \big )$ The angle is measured counterclockwise from the pos-. itive real axis. The complex conjugate of $G ( s )$ is ${ \overline { { G } } } ( s ) = G _ { x } - j G _ { y }$ .

Complex functions commonly encountered in linear control systems analysis are single-valued functions of s and are uniquely determined for a given value of s.

A complex function $G ( s )$ is said to be analytic in a region if $G ( s )$ and all its derivatives exist in that region. The derivative of an analytic function $G ( s )$ is given by

$$\frac {d}{d s} G (s) = \lim _ {\Delta s \rightarrow 0} \frac {G (s + \Delta s) - G (s)}{\Delta s} = \lim _ {\Delta s \rightarrow 0} \frac {\Delta G}{\Delta s}$$

Since $\Delta s = \Delta \sigma + j \Delta \omega$ can approach zero along an infinite number of different, ¢s paths. It can be shown, but is stated without a proof here, that if the derivatives taken along two particular paths, that is, $\Delta s = \Delta \sigma$ and $\Delta s = j \Delta \omega$ are equal, then the deriva-, tive is unique for any other path $\Delta s = \Delta \sigma + j \Delta \omega$ and so the derivative exists.

For a particular path $\Delta s = \Delta \sigma$ (which means that the path is parallel to the real axis),

$$\frac {d}{d s} G (s) = \lim _ {\Delta \sigma \rightarrow 0} \left(\frac {\Delta G _ {x}}{\Delta \sigma} + j \frac {\Delta G _ {y}}{\Delta \sigma}\right) = \frac {\partial G _ {x}}{\partial \sigma} + j \frac {\partial G _ {y}}{\partial \sigma}$$
