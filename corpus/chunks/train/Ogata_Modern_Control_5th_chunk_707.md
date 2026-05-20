$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0)$$

we obtain $e ^ { \mathbf { A } t } = \mathbf { P } e ^ { \mathbf { D } t } \mathbf { P } ^ { - 1 }$ or,

$$
e ^ {\mathbf {A} t} = \mathbf {P} e ^ {\mathbf {D} t} \mathbf {P} ^ {- 1} = \mathbf {P} \left[ \begin{array}{c c c c c c} e ^ {\lambda_ {1} t} & & & & & 0 \\ & e ^ {\lambda_ {2} t} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & e ^ {\lambda_ {n} t} \end{array} \right] \mathbf {P} ^ {- 1} \tag {9-101}
$$

Next, we shall consider the case where matrix A may be transformed into a Jordan canonical form. Consider again the state equation

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}$$

First obtain a transformation matrix S that will transform matrix A into a Jordan canonical form so that

$$\mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} = \mathbf {J}$$

where J is a matrix in a Jordan canonical form. Now define

$$\mathbf {x} = \mathbf {S} \hat {\mathbf {x}}$$

Then

$$\dot {\hat {\mathbf {x}}} = \mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} \hat {\mathbf {x}} = \mathbf {J} \hat {\mathbf {x}}$$

The solution of this last equation is

$$\hat {\mathbf {x}} (t) = e ^ {\mathbf {J} t} \hat {\mathbf {x}} (0)$$

Hence,

$$\mathbf {x} (t) = \mathbf {S} \hat {\mathbf {x}} (t) = \mathbf {S} e ^ {\mathbf {J} t} \mathbf {S} ^ {- 1} \mathbf {x} (0)$$

Since the solution x(t) can also be given by the equation

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0)$$

we obtain

$$e ^ {\mathbf {A} t} = \mathbf {S} e ^ {\mathbf {J} t} \mathbf {S} ^ {- 1}$$

Note that $e ^ { \mathbf { J } t }$ is a triangular matrix [which means that the elements below (or above, as the case may be) the principal diagonal line are zeros] whose elements are $e ^ { \lambda t } , t e ^ { \lambda t } , { \textstyle \frac { 1 } { 2 } } t ^ { 2 } e ^ { \lambda t }$ , and so forth. For example, if matrix J has the following Jordan canonical form:

$$
\mathbf {J} = \left[ \begin{array}{c c c} \lambda_ {1} & 1 & 0 \\ 0 & \lambda_ {1} & 1 \\ 0 & 0 & \lambda_ {1} \end{array} \right]
$$

then

$$
e ^ {\mathbf {J} t} = \left[ \begin{array}{c c c} e ^ {\lambda_ {1} t} & t e ^ {\lambda_ {1} t} & \frac {1}{2} t ^ {2} e ^ {\lambda_ {1} t} \\ 0 & e ^ {\lambda_ {1} t} & t e ^ {\lambda_ {1} t} \\ 0 & 0 & e ^ {\lambda_ {1} t} \end{array} \right]
$$

Similarly, if

$$
\mathbf {J} = \left[ \begin{array}{c c c c c c c} \lambda_ {1} & 1 & 0 & & & & 0 \\ 0 & \lambda_ {1} & 1 & & & & \\ 0 & 0 & \lambda_ {1} & & & & \\ \hline & & & \lambda_ {4} & 1 & & \\ & & & 0 & \lambda_ {4} & & \\ & & & & & \lambda_ {6} & \\ 0 & & & & & & \lambda_ {7} \end{array} \right]
$$

then
