# Solution:

Our goal is to find a path between two fixed points in a vertical plane such that a particle sliding without friction along this path takes the shortest possible time to travel from one point to the other. The problem can be formulated as following:

$$\min _ {y: [ a, b ] \rightarrow [ 0, \infty)} J (y) = \int_ {a} ^ {b} \frac {\sqrt {1 + \left(y ^ {\prime} (x)\right) ^ {2}}}{\sqrt {y (x)}} \tag {90}$$

subject to (91)

$$y (a) = y _ {0}, \quad y (b) = y _ {1} \tag {92}$$

Let’s consider the simplified notation $y ( x ) = y$ and $y ^ { \prime } ( x ) = y ^ { \prime }$ for convenience. Moreover, we consider the problem starting at $x = 0$ for the sake of convenience.

We can consider the no x result of the Euler-Lagrange equations: in this case, the Lagrangian does not depend explicitly on $x ;$ therefore, the condition can be simplified as following:

$$L - L _ {y ^ {\prime}} y ^ {\prime} = \sqrt {\frac {1}{2 c}} \text { with } c \in \mathbb {R}, c > 0 \tag {93}$$

where $\sqrt { \frac { 1 } { 2 c } }$ is a non-negative constant. The reason why we chose this formulation will become clear during the derivation.

Given the Lagrangian’s formulation of L = 1+y02√ , $\begin{array} { r } { L = \frac { \sqrt { 1 + y ^ { \prime 2 } } } { \sqrt { y } } } \end{array}$ we can derive that:

$$\frac {\sqrt {1 + y ^ {\prime 2}}}{\sqrt {y}} - \frac {y ^ {\prime 2}}{\sqrt {y} \sqrt {1 + y ^ {\prime 2}}} = \sqrt {\frac {1}{2 c}} \tag {94}\frac {1}{\sqrt {y} \sqrt {1 + y ^ {\prime 2}}} = \sqrt {\frac {1}{2 c}} \tag {95}\frac {1}{y} = \frac {1}{2 c} \left(1 + y ^ {\prime 2}\right) = \dots \tag {96}\dots \frac {1}{y} = \frac {1}{2 c} \left(1 + \left(\frac {d y}{d x}\right) ^ {2}\right) \tag {97}\frac {d y}{d x} = \sqrt {\frac {2 c - y}{y}} \tag {98}d x = \sqrt {\frac {y}{2 c - y}} d y \tag {99}$$

We can operate the following substitution to make the integral easier: $y = c - c t ;$ $d y = - c d t$ yielding:

$$d x = - c \sqrt {\frac {1 - t}{1 + t}} d t \tag {101}$$

In order to proceed with the integration, we can recall the following trigonometric functions:

$$1 + \cos \theta = 2 \cos^ {2} (\theta / 2) \tag {102}1 - \cos \theta = 2 \sin^ {2} (\theta / 2) \tag {103}$$

So, operating the substitution $t = \cos \theta ; d t = - \sin \theta d \theta$ , we can rewrite the equation as:

$$d x = c \sqrt {\frac {1 + \cos \theta}{1 - \cos \theta}} \sin \theta d \theta = c \sqrt {\frac {2 \sin^ {2} (\theta / 2)}{2 \cos^ {2} (\theta / 2)}} = c \tan (\theta / 2) \sin \theta d \theta \tag {105}$$

Given that sin $\theta = 2 \sin ( \theta / 2 ) \cos ( \theta / 2 )$ we get:
