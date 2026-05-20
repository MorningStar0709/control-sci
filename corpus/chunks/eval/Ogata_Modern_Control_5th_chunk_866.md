$$J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} \mathbf {x} d t = \mathbf {x} ^ {T} (0) \mathbf {P} (0) \mathbf {x} (0)$$

is minimized, where the matrix P is determined from Equation (10–115), rewritten

$$(\mathbf {A} - \mathbf {B K}) ^ {*} \mathbf {P} + \mathbf {P} (\mathbf {A} - \mathbf {B K}) = - (\mathbf {Q} + \mathbf {K} ^ {*} \mathbf {R K})$$

Since in this system Q=I and R=0, this last equation can be simplified to

$$(\mathbf {A} - \mathbf {B K}) ^ {*} \mathbf {P} + \mathbf {P} (\mathbf {A} - \mathbf {B K}) = - \mathbf {I} \tag {10-176}$$

Since the system involves only real vectors and real matrices, P becomes a real symmetric matrix. Then Equation (10–176) can be written as

$$
\left[ \begin{array}{c c} 0 & - 4 \\ 1 & - k _ {2} \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ - 4 & - k _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - 1 \end{array} \right]
$$

Solving for the matrix P, we obtain

$$
\mathbf {P} = \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} \frac {5}{2 k _ {2}} + \frac {k _ {2}}{8} & \frac {1}{8} \\ \frac {1}{8} & \frac {5}{8 k _ {2}} \end{array} \right]
$$

The performance index is then

$$
\begin{array}{l} J = \mathbf {x} ^ {T} (0) \mathbf {P x} (0) \\ = \left[ \begin{array}{l l} c & 0 \end{array} \right] \left[ \begin{array}{l l} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] \left[ \begin{array}{l} c \\ 0 \end{array} \right] = p _ {1 1} c ^ {2} \\ = \left(\frac {5}{2 k _ {2}} + \frac {k _ {2}}{8}\right) c ^ {2} \tag {10-177} \\ \end{array}
$$

To minimize J, we differentiate J with respect to $k _ { 2 }$ and set $\partial J / \partial k _ { 2 }$ equal to zero as follows:

$$\frac {\partial J}{\partial k _ {2}} = \left(\frac {- 5}{2 k _ {2} ^ {2}} + \frac {1}{8}\right) c ^ {2} = 0$$

Hence,

$$k _ {2} = \sqrt {2 0}$$

With this value of $k _ { 2 }$ , we have $\partial ^ { 2 } J / \partial k _ { 2 } ^ { 2 } > 0 .$ Thus, the minimum value of J is obtained by substituting $k _ { 2 } = \sqrt { 2 0 }$ into Equation (10–177), or

$$J _ {\min} = \frac {\sqrt {5}}{2} c ^ {2}$$

The designed system has the control law

$$u = - 4 x _ {1} - \sqrt {2 0} x _ {2}$$

The designed system is optimal in that it results in a minimum value for the performance index J under the assumed initial condition.
