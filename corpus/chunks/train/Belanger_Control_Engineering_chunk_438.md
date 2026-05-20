# (Pendulum on a Cart)

In the pendulum-and-cart problem of Examples 2.10 (Chapter 2) and 7.7, three of the states—namely, the distance x, cart velocity v, and angle $\theta$ —are relatively easy to measure. The angular velocity $\omega$ , in contrast, is difficult to obtain; it is too small for most tachometers unless friction-inducing gears are used to “gear up” the angular velocity. Devise an estimator of order 1 with an error-system eigenvalue of -4.

Solution Example 7.3 gives the state equations, already in a form where the first three state variables are the measured ones. We write

$$
\frac {d}{d t} \left[ \begin{array}{c} x \\ v \\ \theta \\ \text {…} \\ \omega \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 9. 8 & 0 \\ 0 & 0 & 0 & 1 \\ \hline \text {…} & \text {…} & \text {…} & \text {…} \\ 0 & 0 & 1 9. 6 & 0 \end{array} \right] \left[ \begin{array}{c} x \\ v \\ \theta \\ \text {…} \\ \omega \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ \text {…} \\ - 1 \end{array} \right] u.
$$

Thus,

$$
A _ {m m} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & - 9. 8 \\ 0 & 0 & 0 \end{array} \right]; \qquad A _ {m u} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]; \qquad B _ {m} = \left[ \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right]

A _ {u m} = \left[ \begin{array}{l l l} 0 & 0 & 1 9. 6 \end{array} \right]; \quad A _ {u u} = 0; \quad B _ {u} = - 1.
$$

The observer gain is a $1 \times 3$ matrix. The error system matrix is

$$
A _ {u u} - G A _ {m u} = 0 - \left[ \begin{array}{l l l} g _ {1} & g _ {2} & g _ {3} \end{array} \right] \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] = - g _ {3}.
$$

For an error-system eigenvalue of -4, we use $g_{3} = 4$ . Since $g_{1}$ and $g_{2}$ are irrelevant, we may as well set them to zero. Thus,

$$
G = \left[ \begin{array}{c c c} 0 & 0 & 4 \end{array} \right].
$$

Using the form of Equation 7.84,

$$
\begin{array}{l} \dot {\widehat {\omega}} = \left[ \begin{array}{l l l} 0 & 0 & 1 9. 6 \end{array} \right] \left[ \begin{array}{c} x \\ v \\ \theta \end{array} \right] - u \\ + \left[ \begin{array}{l l l} 0 & 0 & 4 \end{array} \right] \left(\left[ \begin{array}{c} \dot {x} \\ \dot {v} \\ \dot {\theta} \end{array} \right] - \left[ \begin{array}{c} v \\ - 9. 8 \theta \\ 0 \end{array} \right] - \left[ \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right] u - \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right] \widehat {\omega}\right) \\ = 1 9. 6 \theta - u + 4 \dot {\theta} - \widehat {\omega}, \\ \end{array}
$$
