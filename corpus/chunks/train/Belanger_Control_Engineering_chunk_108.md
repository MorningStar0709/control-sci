# Example 3.9 (dc Servo)

Assess the observability of the dc servo of Example 2.1 (Chapter 2) under the two separate measurement conditions $y = \theta$ and $y = \omega$ .

Solution In this example,

$$
A = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & \frac {N K _ {m}}{J _ {e}} \\ 0 & \frac {- N K _ {m}}{L} & \frac {- R}{L} \end{array} \right] \quad C = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right].
$$

Here, $n = 3$ , so the observability matrix is

$$
\mathcal {O} = \left[ \begin{array}{c} C \\ C A \\ C A ^ {2} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {N K _ {m}}{J _ {e}} \end{array} \right]
$$

which is clearly of rank 3: the system is observable with angular position as output. For $y = \omega, C = \begin{bmatrix} 0 & 1 & 0 \end{bmatrix}$ and the observability matrix is

$$
\mathcal {O} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & \frac {N K _ {m}}{J _ {e}} \\ 0 & \frac {- N ^ {2} K _ {m} {} ^ {2}}{L J _ {e}} & \frac {- N K _ {m} R}{L J _ {e}} \end{array} \right].
$$

The column of zeros establishes that this square matrix is singular and hence of rank less than 3. The state vector $\begin{bmatrix} a \\ 0 \\ 0 \end{bmatrix}$ is orthogonal to all rows and hence unobservable. This makes physical sense: if the velocity is observed but not the angular position, it is impossible to tell what the initial angle was, and hence what the angle is at any t.
