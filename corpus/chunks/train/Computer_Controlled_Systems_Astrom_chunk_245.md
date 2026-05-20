# Computing the Observer Gain

The determination of the matrix K in the observer (4.28) is the same mathematical problem as the problem of determining the feedback matrix L in the pole-placement problem. The practical aspects are also closely related. The selection of the observer poles is a compromise between sensitivity to measurement errors and rapid recovery of initial errors. A fast observer will converge quickly, but it will also be sensitive to measurement errors.

Determining the matrix K is the dual of finding the gain matrix L for pole placement by state feedback. This problem is solved by Ackermann's formula, Theorem 4.1. By using the relations

$$L \rightarrow K ^ {T} \quad W _ {r} \rightarrow W _ {o} ^ {T} \quad \Phi \rightarrow \Phi^ {T}$$

it follows from Equation (4.13) that $K$ is given by

$$
K ^ {T} = \left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \end{array} \right) \left(W _ {o} ^ {T}\right) ^ {- 1} P (\Phi^ {T})
$$

or

$$
K = P (\Phi) W _ {o} ^ {- 1} \left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \end{array} \right) ^ {T} \tag {4.31}
$$

The characteristic polynomial of $\Phi - KC$ is then $P(z)$ . The duality with pole placement also implies that K is especially simple to determine if the system is in observable form.

Notice, however, that Ackermann's formula is poorly conditioned numerically. The MATLAB® procedure place is based on better numerical methods. This procedure will also give the observer gain for systems with many measurements.
