# 6.6 SYSTEMS WITH DELAY

System descriptions often include pure delays. For example, in a system that includes a communication link, the finite speed of light causes delay; this is particularly important if part of the system is on another planet. Another, more down-to-earth example of delay is the time taken to transport materials on a conveyor belt or via a moving web.

A pure delay has the input-output description

$$y (t) = u (t - T), \quad T > 0. \tag {6.49}$$

This element does not have a finite-state description. From Equation 6.49, it is seen that the output $y(t), t > 0$ , depends not only on future inputs but also on the immediate past inputs, i.e., on $u(t), -T < t \leq 0$ . We may think of this as a delay line, where what first comes out is what is initially stored in the line. Thus, the state is actually a function, $u(t), -T < t \leq 0$ . Since this function has an infinite number of points, it cannot be represented by a finite set of numbers. (Approximations are possible, of course.)

Taking Laplace transforms of Equation 6.49 yields

$$y (s) = e ^ {- s T} u (s). \tag {6.50}$$

The transfer function $e^{-sT}$ is analytic everywhere in the complex plane, including

the $j$ -axis. Since

$$\left| e ^ {- j \omega T} \right| = 1 \tag {6.51}\neq e ^ {- j \omega T} = - \omega T \tag {6.52}$$

the delay element is "all-pass" and has phase lag increasing linearly with frequency.

As we will show presently, frequency-response methods are applicable to systems with delay.
