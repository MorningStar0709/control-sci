# Example 2.11

Minimize the performance index

$$J = \int_ {0} ^ {1} [ x ^ {2} (t) + u ^ {2} (t) ] d t \tag {2.6.25}$$

with boundary conditions

$$x (0) = 1; \quad x (1) = 0 \tag {2.6.26}$$

subject to the condition (plant equation)

$$\dot {x} (t) = - x (t) + u (t). \tag {2.6.27}$$

Solution: Let us solve this problem by the two methods, i.e., the direct method and the Lagrange multiplier method.

1 Direct Method: Here, we eliminate $u(t)$ between the performance index (2.6.25) and the plant (2.6.27) to get the functional as

$$
\begin{array}{l} J = \int_ {0} ^ {1} [ x ^ {2} (t) + (\dot {x} (t) + x (t)) ^ {2} ] d t \\ = \int_ {0} ^ {1} [ 2 x ^ {2} (t) + \dot {x} ^ {2} (t) + 2 x (t) \dot {x} (t) ] d t. \tag {2.6.28} \\ \end{array}
$$

Now, we notice that the functional (2.6.28) absorbed the condition (2.6.27) within itself, and we need to consider it as a straight forward extremization of a functional as given earlier. Thus, applying the Euler-Lagrange equation

$$\left(\frac {\partial V}{\partial x}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} = 0 \tag {2.6.29}$$

to the functional (2.6.28), where,

$$V = 2 x ^ {2} (t) + \dot {x} ^ {2} (t) + 2 x (t) \dot {x} (t), \tag {2.6.30}$$

we get

$$4 x ^ {*} (t) + 2 \dot {x} ^ {*} (t) - \frac {d}{d t} (2 \dot {x} ^ {*} (t) + 2 x ^ {*} (t)) = 0. \tag {2.6.31}$$

Simplifying the above

$$\ddot {x} ^ {*} (t) - 2 x ^ {*} (t) = 0 \tag {2.6.32}$$

the solution (see later for use of MATLAB $^{©}$ ) of which gives the optimal as

$$x ^ {*} (t) = C _ {1} e ^ {- \sqrt {2} t} + C _ {2} e ^ {\sqrt {2} t} \tag {2.6.33}$$

where, the constants $C_{1}$ and $C_{2}$ , evaluated using the given boundary conditions (2.6.26), are found to be

$$C _ {1} = 1 / (1 - e ^ {- 2 \sqrt {2}}); \quad C _ {2} = 1 / (1 - e ^ {2 \sqrt {2}}). \tag {2.6.34}$$

Finally, knowing the optimal $x^{*}(t)$ , the optimal control $u^{*}(t)$ is found from the plant (2.6.27) to be

$$
\begin{array}{l} u ^ {*} (t) = \dot {x} ^ {*} (t) + x ^ {*} (t) \\ = C _ {1} (1 - \sqrt {2}) e ^ {- \sqrt {2} t} + C _ {2} (1 + \sqrt {2}) e ^ {\sqrt {2} t}. \tag {2.6.35} \\ \end{array}
$$

Although the method appears to be simple, let us note that it is not always possible to eliminate $u(t)$ from (2.6.25) and (2.6.27) especially for higher-order systems.
