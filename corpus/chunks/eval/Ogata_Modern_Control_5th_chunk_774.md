Obtain the observer gain matrix $\mathbf { K } _ { e }$ and draw a block diagram for the observed-state feedback control system. Then obtain the transfer function $U ( s ) / [ - \bar { Y ( s ) } ]$ for the observer controller, and draw another block diagram with the observer controller as a series controller in the feedforward path. Finally, obtain the response of the system to the following initial condition:

$$
\mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right], \qquad \mathbf {e} (0) = \mathbf {x} (0) - \widetilde {\mathbf {x}} (0) = \left[ \begin{array}{c} 0. 5 \\ 0 \end{array} \right]
$$

For the system defined by Equation (10–75), the characteristic polynomial is

$$
| s \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c} s & - 1 \\ - 2 0. 6 & s \end{array} \right| = s ^ {2} - 2 0. 6 = s ^ {2} + a _ {1} s + a _ {2}
$$

Thus,

$$a _ {1} = 0, \quad a _ {2} = - 2 0. 6$$

The desired characteristic polynomial for the observer is

$$
\begin{array}{l} (s - \mu_ {1}) (s - \mu_ {2}) = (s + 8) (s + 8) = s ^ {2} + 1 6 s + 6 4 \\ = s ^ {2} + \alpha_ {1} s + \alpha_ {2} \\ \end{array}
$$

Hence,

$$\alpha_ {1} = 1 6, \quad \alpha_ {2} = 6 4$$

For the determination of the observer gain matrix, we use Equation (10–61), or

$$
\mathbf {K} _ {e} = (\mathbf {W N} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \alpha_ {2} - a _ {2} \\ \alpha_ {1} - a _ {1} \end{array} \right]
$$

where

$$
\mathbf {N} = \left[ \begin{array}{c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right]

\mathbf {W} = \left[ \begin{array}{c c} a _ {1} & 1 \\ 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right]
$$

Hence,

$$
\begin{array}{l} \mathbf {K} _ {e} = \left\{\left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \right\} ^ {- 1} \left[ \begin{array}{c} 6 4 + 2 0. 6 \\ 1 6 - 0 \end{array} \right] \\ = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l} 8 4. 6 \\ 1 6 \end{array} \right] = \left[ \begin{array}{l} 1 6 \\ 8 4. 6 \end{array} \right] \tag {10-77} \\ \end{array}
$$

Equation (10–77) gives the observer gain matrix Ke. The observer equation is given by Equation (10–60):

$$\tilde {\mathbf {x}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \tilde {\mathbf {x}} + \mathbf {B} u + \mathbf {K} _ {e} y \tag {10-78}$$

Since

$$u = - \mathbf {K} \widetilde {\mathbf {x}}$$

Equation (10–78) becomes
