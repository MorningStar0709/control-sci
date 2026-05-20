# Example 3.3 (Pendulum on a Cart)

Calculate the modes and the corresponding eigenvectors for the linearized inverted pendulum system of Example 2.9, using the parameter values of Example 2.5.

Solution From Example 2.9, the state equations with zero input are

$$
\frac {d}{d t} \left[ \begin{array}{c} x \\ v \\ \theta \\ \omega \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 9. 8 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & + 1 9. 6 & 0 \end{array} \right] \left[ \begin{array}{c} x \\ v \\ \theta \\ \omega \end{array} \right]
$$

To solve for the eigenvalues, solve

$$\det (s I - A) = s ^ {2} \left(s ^ {2} - 1 9. 6\right) = 0.$$

The eigenvalues are 0, 0, and ±4.43.

The eigenvectors are as follows:

$$
\begin{array}{l} \text { For   } s = 0, \quad \alpha \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ 0 \end{array} \right]; \qquad \text { for   } s = 4. 4 3, \quad \beta \left[ \begin{array}{c} -. 5 \\ - 2. 2 1 \\ 1 \\ 4. 4 3 \end{array} \right]; \\ \text { for   } s = - 4. 4 3, \quad \gamma \left[ \begin{array}{c} -. 5 \\ 2. 2 1 \\ 1 \\ - 4. 4 3 \end{array} \right]. \\ \end{array}
$$

Note that there are only three eigenvectors. In cases of repeated eigenvalues, there may be fewer than n eigenvectors, in which case it is also possible to define a generalized eigenvector. (This shall not be pursued here.)

Corresponding to s = 0, the modal vector calls for an initial cart position $x = \alpha$ (arbitrary), with a motionless cart and a motionless vertical pendulum. Since $e^{0t} = 1$ , the system remains in this state, which is a state of equilibrium (albeit unstable).

Corresponding to s = -4.43 is an initial state where the angle is $\gamma$ , the angular velocity is $-4.43\gamma$ (i.e., toward the vertical), and the cart velocity is $2.21\gamma$ (to the right for $\gamma > 0$ ). The cart position is $-.5\gamma$ (to the left of the origin). The motion is described by multiplying this state by $e^{-4.43t}$ , so the system eventually comes to rest with the cart at the origin and a vertical pendulum. It is seen that, with just the right initial conditions, the system is sent to equilibrium.

The other eigenvector produces a time evolution governed by $e^{4.43t}$ . The angle is $\beta$ , the angular velocity is such as to increase it, and the cart is moving leftward.
