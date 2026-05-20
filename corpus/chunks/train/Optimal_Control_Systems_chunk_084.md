# 2.3.3 Different Cases for Euler-Lagrange Equation

We now discuss various cases of the EL equation.

Case 1: $V$ is dependent of $\dot{x}(t)$ , and $t$ . That is, $V = V(\dot{x}(t), t)$ . Then $V_x = 0$ . The Euler-Lagrange equation (2.3.16) becomes

$$\frac {d}{d t} \left(V _ {\dot {x}}\right) = 0. \tag {2.3.20}$$

This leads us to

$$V _ {\dot {x}} = \frac {\partial V (\dot {x} ^ {*} (t) , t)}{\partial \dot {x}} = C \tag {2.3.21}$$

where, $C$ is a constant of integration.

Case 2: $V$ is dependent of $\dot{x}(t)$ only. That is, $V = V(\dot{x}(t))$ . Then $V_{x} = 0$ . The Euler-Lagrange equation (2.3.16) becomes

$$\frac {d}{d t} \left(V _ {\dot {x}}\right) = 0 \longrightarrow V _ {\dot {x}} = C. \tag {2.3.22}$$

In general, the solution of either (2.3.21) or (2.3.22) becomes

$$\dot {x} ^ {*} (t) = C _ {1} \longrightarrow x ^ {*} (t) = C _ {1} t + C _ {2}. \tag {2.3.23}$$

This is simply an equation of a straight line.

Case 3: $V$ is dependent of $x(t)$ and $\dot{x}(t)$ . That is, $V = V(x(t), \dot{x}(t))$ . Then $V_{t\dot{x}} = 0$ . Using the other form of the Euler-Lagrange equation (2.3.19), we get

$$V _ {x} - V _ {x \dot {x}} \dot {x} ^ {*} (t) - V _ {\dot {x} \dot {x}} \ddot {x} ^ {*} (t) = 0. \tag {2.3.24}$$

Multiplying the previous equation by $\dot{x}^{*}(t)$ , we have

$$\dot {x} ^ {*} (t) \left[ V _ {x} - V _ {x \dot {x}} \dot {x} ^ {*} (t) - V _ {\dot {x} \dot {x}} \ddot {x} ^ {*} (t) \right] = 0. \tag {2.3.25}$$

This can be rewritten as

$$\frac {d}{d t} \left(V - \dot {x} ^ {*} (t) V _ {\dot {x}}\right) = 0 \longrightarrow V - \dot {x} ^ {*} (t) V _ {\dot {x}} = C. \tag {2.3.26}$$

The previous equation can be solved using any of the techniques such as, separation of variables.

Case 4: $V$ is dependent of $x(t)$ , and $t$ , i.e., $V = V(x(t), t)$ . Then, $V_{\dot{x}} = 0$ and the Euler-Lagrange equation (2.3.16) becomes

$$\frac {\partial V (x ^ {*} (t) , t)}{\partial x} = 0. \tag {2.3.27}$$

The solution of this equation does not contain any arbitrary constants and therefore generally speaking does not satisfy the boundary conditions $x(t_0)$ and $x(t_f)$ . Hence, in general, no solution exists for this variational problem. Only in rare cases, when the function $x(t)$ satisfies the given boundary conditions $x(t_0)$ and $x(t_f)$ , it becomes an optimal function.

Let us now illustrate the application of the EL equation with a very simple classic example of finding the shortest distance between two points. Often, we omit the \* (which indicates an optimal or extremal value) during the working of a problem and attach the same to the final solution.
