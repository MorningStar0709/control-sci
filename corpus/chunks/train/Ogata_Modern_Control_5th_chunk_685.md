and the transfer function between $Y ( s )$ and $X _ { 1 } ( s )$ is

$$\frac {Y (s)}{X _ {1} (s)} = (s + 1) (s + 4)$$

Therefore, the transfer function between the output Y(s) and the input $U ( s )$ is

$$\frac {Y (s)}{U (s)} = \frac {(s + 1) (s + 4)}{(s + 1) (s + 2) (s + 3)}$$

Clearly, the two factors (s+1) cancel each other.This means that there are nonzero initial states x(0), which cannot be determined from the measurement of $y ( t )$ .

Comments. The transfer function has no cancellation if and only if the system is completely state controllable and completely observable.This means that the canceled transfer function does not carry along all the information characterizing the dynamic system.

Alternative Form of the Condition for Complete Observability. Consider the system described by Equations (9–63) and (9–64), rewritten

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} \tag {9-66}\mathbf {y} = \mathbf {C x} \tag {9-67}$$

Suppose that the transformation matrix P transforms A into a diagonal matrix, or

$$\mathbf {P} ^ {- 1} \mathbf {A P} = \mathbf {D}$$

where D is a diagonal matrix. Let us define

$$\mathbf {x} = \mathbf {P z}$$

Then Equations (9–66) and (9–67) can be written

$$\dot {\mathbf {z}} = \mathbf {P} ^ {- 1} \mathbf {A P z} = \mathbf {D z}\mathbf {y} = \mathbf {C P z}$$

Hence,

$$\mathbf {y} (t) = \mathbf {C P} e ^ {\mathbf {D} t} \mathbf {z} (0)$$

or

$$
\mathbf {y} (t) = \mathbf {C P} \left[ \begin{array}{c c c c c c} e ^ {\lambda_ {1} t} & & & & & 0 \\ & e ^ {\lambda_ {2} t} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & e ^ {\lambda_ {n} t} \end{array} \right] \mathbf {z} (0) = \mathbf {C P} \left[ \begin{array}{c} e ^ {\lambda_ {1} t} z _ {1} (0) \\ e ^ {\lambda_ {2} t} z _ {2} (0) \\ \cdot \\ \cdot \\ \cdot \\ e ^ {\lambda_ {n} t} z _ {n} (0) \end{array} \right]
$$

The system is completely observable if none of the columns of the m\*n matrix CP consists of all zero elements. This is because, if the ith column of CP consists of all zero elements, then the state variable $z _ { i } ( 0 )$ will not appear in the output equation and therefore cannot be determined from observation of y(t). Thus, x(0), which is related to z(0) by the nonsingular matrix P, cannot be determined. (Remember that this test applies only if the matrix $\mathbf { \partial } \mathbf { \bar { P } } ^ { - 1 } \mathbf { A P }$ is in diagonal form.)
