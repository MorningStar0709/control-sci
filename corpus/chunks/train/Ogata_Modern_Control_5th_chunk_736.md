$$
\begin{array}{l} \left| s \mathbf {I} - \mathbf {T} ^ {- 1} \mathbf {A T} + \mathbf {T} ^ {- 1} \mathbf {B K T} \right| \\ = \left| s \mathbf {I} - \left[ \begin{array}{c c c c} 0 & 1 & \dots & 0 \\ \cdot & \cdot & & \cdot \\ \cdot & \cdot & & \cdot \\ \cdot & \cdot & & \cdot \\ 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & \dots & - a _ {1} \end{array} \right] + \left[ \begin{array}{c} 0 \\ \cdot \\ \cdot \\ \cdot \\ 0 \\ 1 \end{array} \right] \left[ \begin{array}{c c c c} \delta_ {n} & \delta_ {n - 1} & \dots & \delta_ {1} \end{array} \right] \right| \\ = \left| \begin{array}{c c c c} s & - 1 & \dots & 0 \\ 0 & s & \dots & 0 \\ . & . & & . \\ . & . & & . \\ . & . & & . \\ a _ {n} + \delta_ {n} & a _ {n - 1} + \delta_ {n - 1} & \dots & s + a _ {1} + \delta_ {1} \end{array} \right| \\ = s ^ {n} + \left(a _ {1} + \delta_ {1}\right) s ^ {n - 1} + \dots + \left(a _ {n - 1} + \delta_ {n - 1}\right) s + \left(a _ {n} + \delta_ {n}\right) = 0 \tag {10-12} \\ \end{array}
$$

This is the characteristic equation for the system with state feedback. Therefore, it must be equal to Equation (10–10), the desired characteristic equation. By equating the coefficients of like powers of s, we get

$$
\begin{array}{l} a _ {1} + \delta_ {1} = \alpha_ {1} \\ a _ {2} + \delta_ {2} = \alpha_ {2} \\ a _ {n} + \delta_ {n} = \alpha_ {n} \\ \end{array}
$$

Solving the preceding equations for the $\delta _ { i }$ ’s and substituting them into Equation (10–11), we obtain

$$
\begin{array}{l} \mathbf {K} = \left[ \begin{array}{c c c c} \delta_ {n} & \delta_ {n - 1} & \dots & \delta_ {1} \end{array} \right] \mathbf {T} ^ {- 1} \\ = \left[ \alpha_ {n} - a _ {n} \mid \alpha_ {n - 1} - a _ {n - 1} \mid \dots \mid \alpha_ {2} - a _ {2} \mid \alpha_ {1} - a _ {1} \right] \mathbf {T} ^ {- 1} \tag {10-13} \\ \end{array}
$$

Thus, if the system is completely state controllable, all eigenvalues can be arbitrarily placed by choosing matrix K according to Equation (10–13) (sufficient condition).

We have thus proved that a necessary and sufficient condition for arbitrary pole placement is that the system be completely state controllable.

It is noted that if the system is not completely state controllable, but is stabilizable, then it is possible to make the entire system stable by placing the closed-loop poles at desired locations for $q$ controllable modes.The remaining n-q uncontrollable modes are stable. So the entire system can be made stable.

Determination of Matrix K Using Transformation Matrix T. Suppose that the system is defined by
