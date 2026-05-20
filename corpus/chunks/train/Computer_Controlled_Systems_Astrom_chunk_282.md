# 5.2 A Simple Design Problem

We will now discuss the same simple design problem that was solved by state-space methods in Sec. 4.6, namely, to find a two-degree-of-freedom controller for a linear system with output feedback. The design problem is stated, and the solution is given and illustrated by two examples. It turns out that an algebraic equation plays a key role in the solution. The properties of this equation will be explored in the next section, where we also will resolve some technicalities.

A general discussion of the design problem was given in Sec. 4.2. It is recommended to review that section before proceeding. In this case we will consider command signal following, attenuation of load disturbances, and effects of measurement noise.

It is assumed that the system has one control variable, u, and one measured output, y, which are related by the following input-output model:

$$A (q) y (k) = B (q) u (k) \tag {5.1}$$

where $A(q)$ and $B(q)$ are polynomials in the forward-shift operator q. It is assumed that the degree of $B(q)$ is less than the degree of $A(q)$ , that the polynomials $A(q)$ and $B(q)$ do not have any common factors, and that the polynomial $A(q)$ is normalized so that the coefficient of the term with the highest power in q is one. Such a polynomial is called monic.

The dynamics of the process has the pulse-transfer function $B(z)/A(z)$ , which includes a hold circuit, an actuator, a sensor, and antialiasing filter. Recall from Sec. 2.3 that the model of (5.1) may represent a discrete-time model of a continuous-time system with a rational transfer function and an arbitrary time delay.

As in Sec. 4.5 we will assume that the disturbances are widely spaced impulses. The response of the closed-loop system can thus be judged by how well it will respond to perturbations in initial conditions of the process.

In pole-placement design it is assumed that specifications are primarily given by the closed-loop characteristic polynomial. In addition it may be specified that the controller should have certain properties, for example, integral action. The design variables are the closed-loop characteristic polynomial and the sampling period. Notice that the sampling period appears implicitly in the model (5.1).

The controller has one output, u, and two inputs: the command signal, $u_{c}$ , and the measured output, y. A general linear controller can be represented by

$$R (q) u (k) = T (q) u _ {c} (k) - S (q) y (k) \tag {5.2}$$

where $R(q)$ , $S(q)$ , and $T(q)$ are polynomials in the forward-shift operator. The polynomial $R(q)$ can be chosen so that the coefficient of the term of highest power in q is unity.

The control law (5.2) represents a combination of a feedforward with the pulse-transfer function $H_{ff}(z) = T(z)/R(z)$ and a feedback with the pulse-transfer function $H_{fb}(z) = S(z)/R(z)$ . To have a causal controller it must be required that the degree of $R(z)$ is larger than or equal to the degrees of $S(z)$ and $T(z)$ .
