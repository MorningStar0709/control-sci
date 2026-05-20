# The General Case

The solution of the pole-placement problem now will be given for systems with one input signal. Let the system be described by (4.2) and let the characteristic polynomial of the matrix $\Phi$ be

$$z ^ {n} + a _ {1} z ^ {n - 1} + \dots + a _ {n}$$

Assume that the system (4.2) is reachable. It then can be transformed to reachable canonical form by changing state variables through the transformation z = Tx, and the transformed state equation becomes

$$z (k + 1) = \tilde {\Phi} z (k) + \tilde {\Gamma} u (k) \tag {4.5}$$

where

$$
\tilde {\Phi} = \left( \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} & - a _ {n} \\ 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & \dots & 0 & 0 \\ \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right) \quad \tilde {\Gamma} = \left( \begin{array}{l} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{array} \right) \tag {4.6}
$$

The coefficients of the characteristic polynomial that determines the closed-loop poles appear explicitly in this representation. It is also easy to see how the characteristic polynomial is modified by state feedback. It follows from (4.6) that the feedback law

$$u = - \bar {L} z = - \left(p _ {1} - a _ {1} p _ {2} - a _ {2} \dots p _ {n} - a _ {n}\right) z \tag {4.7}$$

gives a closed-loop system with the characteristic polynomial

$$P (z) = z ^ {n} + p _ {1} z ^ {n - 1} + \dots + p _ {n} \tag {4.8}$$

To find the solution to the original problem we simply have to transform back to the original coordinates. This gives

$$u = - \tilde {L} z = - \tilde {L} T x = - L x \tag {4.9}$$

It remains to determine the transformation matrix T. A simple way of determining this matrix is based on a property of the reachability matrices. Let $W_{c}$ be the reachability matrix of the system (4.2), that is,

$$
W _ {c} = \left( \begin{array}{l l l l} \Gamma & \Phi \Gamma & \dots & \Phi^ {n - 1} \Gamma \end{array} \right) \tag {4.10}
$$

and let $\tilde{W}_{c}$ be the reachability matrix of the system (4.5). The matrices are related through $\tilde{W}_{c} = TW_{c}$ . The reachability matrix thus transforms in the same way as the coordinates. It thus follows that

$$T = \tilde {W} _ {c} W _ {c} ^ {- 1} \tag {4.11}$$

and a straightforward calculation gives

$$
\tilde {W} _ {c} ^ {- 1} = \left( \begin{array}{c c c c} 1 & a _ {1} & \dots & a _ {n - 1} \\ 0 & 1 & \dots & a _ {n - 2} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{array} \right) \tag {4.12}
$$
