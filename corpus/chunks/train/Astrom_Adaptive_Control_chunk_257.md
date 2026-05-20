$$
\begin{array}{l} \Delta u (t) = \left( \begin{array}{l l l l} 1 & 0 & \dots & 0 \end{array} \right) \left(\mathbf {R} _ {\mathbf {1}} ^ {T} \mathbf {R} _ {\mathbf {1}} + \rho I\right) ^ {- 1} \mathbf {R} _ {\mathbf {1}} ^ {T} \left(\mathbf {y} _ {\mathbf {m}} - \bar {\mathbf {y}}\right) \\ = \left( \begin{array}{l l l} \alpha_ {1} & \dots & \alpha_ {N} \end{array} \right) (\mathbf {y} _ {\mathbf {m}} - \bar {\mathbf {y}}) \\ \end{array}
$$

Further, from Eq. (4.62), using Eq. (4.54),

$$
\bar {y} = \left( \begin{array}{c} \bar {R} _ {1} ^ {*} \Delta u (t - 1) + G _ {1} ^ {*} y (t) \\ \vdots \\ \bar {R} _ {N} ^ {*} \Delta u (t - 1) + G _ {N} ^ {*} y (t) \end{array} \right) = \left( \begin{array}{c} \frac {\bar {R} _ {1} ^ {*} A ^ {*} \Delta}{B ^ {*}} q ^ {d _ {0} - 1} + G _ {1} ^ {*} \\ \vdots \\ \frac {\bar {R} _ {N} ^ {*} A ^ {*} \Delta}{B ^ {*}} q ^ {d _ {0} - 1} + G _ {N} ^ {*} \end{array} \right) y (t)
$$

The closed-loop system has the characteristic equation

$$
A ^ {*} \Delta + \left( \begin{array}{c c c} \alpha_ {1} & \dots & \alpha_ {N} \end{array} \right) \left( \begin{array}{c} \bar {R} _ {1} ^ {*} A ^ {*} \Delta q ^ {d _ {i} - 1} + B ^ {*} G _ {1} ^ {*} \\ \vdots \\ \bar {R} _ {N} ^ {*} A ^ {*} \Delta q ^ {d _ {0} - 1} + B ^ {*} G _ {N} ^ {*} \end{array} \right)
$$

The identity of Eq. (4.63) gives

$$
\begin{array}{l} B ^ {*} = A ^ {*} \Delta B ^ {*} F _ {d} ^ {*} + q ^ {- d} G _ {d} ^ {*} B ^ {*} \\ = A ^ {*} \Delta (R _ {d} ^ {*} + q ^ {- (d - d _ {0} + 1)} \bar {R} _ {d} ^ {*}) + q ^ {- d} G _ {d} ^ {*} B ^ {*} \\ \end{array}
$$

This gives the characteristic equation

$$
\begin{array}{l} A ^ {*} \Delta + \left( \begin{array}{c c c} \alpha_ {1} & \dots & \alpha_ {N} \end{array} \right) \left( \begin{array}{c} (B ^ {*} - A ^ {*} \Delta R _ {1} ^ {*}) q \\ \vdots \\ (B ^ {*} - A ^ {*} \Delta R _ {N} ^ {*}) q ^ {N} \end{array} \right) \\ = A ^ {*} \Delta + \sum_ {i = 1} ^ {N} \alpha_ {i} q ^ {i} (B ^ {*} - A ^ {*} \Delta R _ {i} ^ {*}) \tag {4.68} \\ \end{array}
$$

Equation (4.68) gives an expression for the closed-loop characteristic equation, but it is still difficult to draw any general conclusions about the properties of the closed-loop system even when the process is known.

If $N_{u} = 1$ , then

$$\alpha_ {i} = \frac {r _ {i}}{\rho + \sum_ {j = 1} ^ {N} r _ {j} ^ {2}}$$
