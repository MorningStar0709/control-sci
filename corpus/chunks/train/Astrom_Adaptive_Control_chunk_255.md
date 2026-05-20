Minimization of this expression with respect to $\Delta u$ gives

$$\boldsymbol {\Delta} \mathbf {u} = (\mathbf {R} ^ {T} \mathbf {R} + \rho I) ^ {- 1} \mathbf {R} ^ {T} (\mathbf {y} _ {\mathrm{m}} - \bar {\mathbf {y}}) \tag {4.66}$$

The first component in $\Delta u$ is $\Delta u(t)$ , which is the control signal applied to the system. Notice that the controller automatically has an integrator. This is necessary to compensate for the drifting noise term in Eq. (4.62).

Notice that $\mathbf{R}$ is independent of the measurements and the old control signals. Only $\mathbf{y}_{\mathbf{m}}$ and $\bar{\mathbf{y}}$ depend on the measurements. The controller (4.66) is thus a time-invariant controller if the process is time-invariant. The predictive controller can thus be interpreted in terms of a pole placement controller. For instance, $N_{u} = N_{1} = n + 1$ , $N_{2} \geq 2(n + 1) - 1$ , and $\rho = 0$ leads to a deadbeat controller.

The calculation of Eq. (4.66) involves the inversion of an $N \times N$ matrix, where N is the prediction horizon in the loss function. To decrease the computations, it is possible to introduce constraints on the future control signals. For instance, it can be assumed that the control increments are zero after $N_{u} < N$ steps:

$$\Delta u (t + k - 1) = 0 \quad k > N _ {u}$$

This implies that the control signal is assumed to be constant after $N_{u}$ steps. Compare the constraint of Eq. (4.55). The control law (Eq. 4.66) then changes to

$$\boldsymbol {\Delta} \mathbf {u} = (\mathbf {R _ {1}} ^ {T} \mathbf {R _ {1}} + \rho I) ^ {- 1} \mathbf {R _ {1}} ^ {T} (\mathbf {y _ {m}} - \bar {\mathbf {y}}) \tag {4.67}$$

where $\mathbf{R}_{1}$ is the $N\times N_{u}$ matrix

$$
\mathbf {R} _ {1} = \left( \begin{array}{c c c c} r _ {0} & 0 & \dots & 0 \\ r _ {1} & r _ {0} & \dots & 0 \\ \vdots & & \ddots & \vdots \\ & & \dots & r _ {0} \\ \vdots & & & \vdots \\ r _ {N - 1} & r _ {N - 2} & \dots & r _ {N - N _ {u}} \end{array} \right)
$$

The matrix to be inverted is now of order $N_{u} \times N_{u}$ .

One advantage of the receding horizon controllers is that it is possible to include constraints in the states and the control signal. References to this are given at the end of the chapter. One disadvantage with the GPC is that there are many parameters to determine, and it is not obvious how to choose the parameters to get a stable closed-loop system.
