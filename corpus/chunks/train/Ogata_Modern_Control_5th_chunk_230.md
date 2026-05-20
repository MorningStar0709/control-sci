$$\mathbf {x} = \dot {\mathbf {z}} = \mathbf {A} \mathbf {z} + \mathbf {B} u \tag {5-55}$$

The solution of Equations (5–54) and (5–55) gives the response to the initial condition.

Summarizing, the response of Equation (5–49) to the initial condition x(0) is obtained by solving the following state-space equations:

$$
\begin{array}{l} \dot {\mathbf {z}} = \mathbf {A} \mathbf {z} + \mathbf {B} u \\ \mathbf {x} = \mathbf {A z} + \mathbf {B u} \\ \end{array}
$$

where

$$\mathbf {B} = \mathbf {x} (0), \quad u = 1 (t)$$

MATLAB commands to obtain the response curves, where we do not specify the time vector t (that is, we let the time vector be determined automatically by MATLAB), are given next.

$$
\begin{array}{l} \% \text {Specify matrices A and B} \\ [ x, z, t ] = \operatorname{step} (A, B, A, B); \\ x 1 = [ 1 0 0 \dots 0 ] ^ {*} x ^ {\prime}; \\ x 2 = [ 0 1 0 \dots 0 ] ^ {*} x ^ {\prime}; \\ \operatorname{plot} (t, x 1, t, x 2, \dots , t, x n) \\ \end{array}
$$

If we choose the time vector t (for example, let the computation time duration be from $\mathrm { t } = 0 \mathrm { t o } \mathrm { t } = \mathrm { t p }$ with the computing time increment of ), then we use the following¢t MATLAB commands:

$$
\begin{array}{l} t = 0: \Delta t: t p; \\ \% \text {Specify matrices A and B} \\ [ x, z, t ] = \operatorname{step} (A, B, A, B, 1, t); \\ x 1 = [ 1 0 0 \dots 0 ] ^ {*} x ^ {\prime}; \\ \mathrm{x} 2 = [ 0 \quad 1 \quad 0 \dots 0 ] ^ {*} \mathrm{x} ^ {\prime}; \\ \cdot \\ \cdot \\ \cdot \\ x n = [ 0 0 0 \dots 1 ] ^ {*} x ^ {\prime}; \\ \operatorname{plot} (t, x 1, t, x 2, \dots , t, x n) \\ \end{array}

\begin{array}{l} \cdot \\ \cdot \\ \cdot \\ x n = [ 0 0 0 \dots 1 ] ^ {*} x ^ {\prime}; \\ \operatorname{plot} (t, x 1, t, x 2, \dots , t, x n) \\ \end{array}
$$

(See, for example, Example 5–9.)

Response to Initial Condition (State-Space Approach, Case 2). Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}, \quad \mathbf {x} (0) = \mathbf {x} _ {0} \tag {5-56}\mathbf {y} = \mathbf {C x} \tag {5-57}$$

(Assume that x is an n-vector and y is an m-vector.)

Similar to case 1, by defining

$$\dot {\mathbf {z}} = \mathbf {x}$$

we can obtain the following equation:

$$\dot {\mathbf {z}} = \mathbf {A} \mathbf {z} + \mathbf {x} (0) 1 (t) = \mathbf {A} \mathbf {z} + \mathbf {B} u \tag {5-58}$$

where

$$\mathbf {B} = \mathbf {x} (0), \quad u = 1 (t)$$

Noting that Equation (5–57) can be written asx = z  ,

$$\mathbf {y} = \mathbf {C} \dot {\mathbf {z}} \tag {5-59}$$

By substituting Equation (5–58) into Equation (5–59), we obtain
