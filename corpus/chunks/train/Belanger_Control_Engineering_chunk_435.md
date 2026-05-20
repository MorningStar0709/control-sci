Figure 7.23 Estimates (dotted) and actual variables for the train problem: coupler 4 extension, car 5 velocity. This is the case with modeling error.

where $\mathbf{x}_m$ and $\mathbf{x}_u$ are, respectively, the measured and unmeasured portions of the state vector.

Next, we partition the system equations:

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c} \dot {\mathbf {x}} _ {m} \\ - \\ \dot {\mathbf {x}} _ {u} \end{array} \right] = \left[ \begin{array}{c c} \overbrace {A _ {m m}} ^ {m} & \overbrace {A _ {m u}} ^ {n - m} \\ - & - \\ A _ {u m} & A _ {u u} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {m} \\ - \\ \mathbf {x} _ {u} \end{array} \right] + \left[ \begin{array}{c} B _ {m} \\ - \\ B _ {u} \end{array} \right] \mathbf {u} \tag {7.79}

\mathbf {y} = \left[ \begin{array}{c c c} & \overbrace {I} ^ {m} & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} _ {m} \\ \mathbf {x} _ {u} \end{array} \right]. \tag {7.80}
$$

Note that Equation 7.80 expresses the fact that $\mathbf{y} = \mathbf{x}_m$ ; i.e., the vector $\mathbf{x}_m$ is the output.

We rewrite Equation 7.79 as

$$\dot {\mathbf {x}} _ {u} = A _ {u u} \mathbf {x} _ {u} + A _ {u m} \mathbf {x} _ {m} + B _ {u} \mathbf {u} \tag {7.81}\mathbf {z} = \dot {\mathbf {x}} _ {m} - A _ {m m} \mathbf {x} _ {m} - B _ {m} \mathbf {u} = A _ {m u} \mathbf {x} _ {u}. \tag {7.82}$$

Equation 7.81 may be viewed as the state equation for $\mathbf{x}_u$ , of order $n - m$ . Here, $\mathbf{u}$ and $\mathbf{x}_m$ serve as inputs. The vector $\mathbf{z}$ is computable since $\mathbf{x}_m$ and $\mathbf{u}$ are given; $\mathbf{z}$ is the effective output.

An observer is designed for $\mathbf{x}_u$ , of the form

$$\dot {\widehat {\mathbf {x}}} _ {u} = A _ {u u} \widehat {\mathbf {x}} _ {u} + A _ {u m} \mathbf {x} _ {m} + B _ {u} \mathbf {u} + G (\mathbf {z} - A _ {m u} \widehat {\mathbf {x}} _ {u}). \tag {7.83}$$

The observer gain $G$ , of dimensions $(n - m) \times m$ , can be chosen by pole placement of the matrix $A_{uu} - GA_{mu}$ as before, or by optimization.

Insertion of Equation 7.82 into Equation 7.83 yields

$$\dot {\widehat {\mathbf {x}}} _ {u} = A _ {u u} \widehat {\mathbf {x}} _ {u} + A _ {u m} \mathbf {x} _ {m} + B _ {u} \mathbf {u} + G (\dot {\mathbf {x}} _ {m} - A _ {m m} \mathbf {x} _ {m} - B _ {m} \mathbf {u} - A _ {m u} \widehat {\mathbf {x}} _ {u}). \tag {7.84}$$
