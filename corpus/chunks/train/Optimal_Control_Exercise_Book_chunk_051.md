# Solution:

Since the catenary will take the shape minimizing the potential energy, the problem can be stated as following:

$$\min _ {y: [ a, b ] \rightarrow 0, \infty)} J (y) = \int_ {a} ^ {b} y (x) \sqrt {1 + (y ^ {\prime} (x)) ^ {2}} d x \tag {157}$$

subject to

$$\int_ {a} ^ {b} \sqrt {1 + (y ^ {\prime} (x)) ^ {2}} d x = C _ {0}, \quad y (a) = y _ {0}, \quad y (b) = y _ {1} \tag {158}$$

As in the previous exercises, let’s also consider the simplified notation $y ( x ) = y$ and $y ^ { \prime } ( x ) = y ^ { \prime }$ for convenience.

Let’s consider the no x result of the Euler-Lagrange equations: in this case, the Lagrangian does not depend explicitly on x; therefore, the condition can be simplified as following:

$$L - L _ {y ^ {\prime}} y ^ {\prime} = c \text { with } c \in \mathbb {R} \tag {159}$$

Given that the Langrangian for the problem is $L = y \sqrt { 1 + y ^ { \prime 2 } }$ , we can write the condition as:

$$\frac {y y ^ {\prime}}{\sqrt {1 + y ^ {\prime 2}}} - y \sqrt {1 + y ^ {\prime 2}} = c \tag {160}\frac {y}{\sqrt {1 + y ^ {\prime 2}}} = c \tag {161}$$

Now, we can solve the second order equation to find the first order derivative:

$$y ^ {2} = c ^ {2} + c ^ {2} y ^ {\prime 2} \tag {163}y ^ {\prime 2} = \left(\frac {y}{c}\right) ^ {2} - 1 \tag {164}$$

which yields

$$y ^ {\prime} = \pm \sqrt {\left(\frac {y}{c}\right) ^ {2} - 1} \tag {165}$$

so,

$$\frac {d y}{d x} = \pm \sqrt {\left(\frac {y}{c}\right) ^ {2} - 1} \tag {166}\pm \frac {d y}{\sqrt {y ^ {2} - c ^ {2}}} = \frac {d x}{c} \tag {167}\pm \int \frac {d y}{\sqrt {y ^ {2} - c ^ {2}}} = \int \frac {d x}{c} \tag {168}$$

Solving this integrals leads to the follwing solutions:

$$\ln \left(\frac {y + \sqrt {y ^ {2} - c ^ {2}}}{c}\right) = \frac {x}{c} \tag {170}\ln \left(\frac {y - \sqrt {y ^ {2} - c ^ {2}}}{c}\right) = - \frac {x}{c} \tag {172}$$

which lead to

$$\frac {y + \sqrt {y ^ {2} - c ^ {2}}}{c} = e ^ {\frac {x}{c}} \tag {173}\frac {y - \sqrt {y ^ {2} - c ^ {2}}}{c} = e ^ {- \frac {x}{c}} \tag {175}$$

The solution can then be written as:

$$y = c \left(\frac {e ^ {\frac {x}{c}} + e ^ {- \frac {x}{c}}}{2}\right) \tag {176}$$

we can substitute the exponential terms with the hyperbolic cosine

$$\cosh (x / c) = \left(\frac {e ^ {\frac {x}{c}} + e ^ {- \frac {x}{c}}}{2}\right) \tag {177}$$

which leads us to the final equation

$$y (x) = c \cosh (x / c) \tag {178}$$

which shows the optimal curves for the catenary problem.

Given the numerical conditions, we could also compute the value of c. We notice that if the reference frame is with a vertical y axis pointing ”up” (opposite direction with respect to the gravitational field), then the parameter satisfies the condition $c > 0$ . 
