Notice that the signal $u'(t-1)$ contains information that is available at time t-1. An implementation of the control algorithm that exploits this to make the computational delay as small as possible is the following:

1. Perform A-D conversion of $y(t)$ and $u_{c}(t)$ .   
2. Compute $u(t) = t_{0}u_{c}(t) - s_{0}y(t) + u'(t - 1)$ .

3. Perform D-A conversion of $u(t)$ .

4. Compute

$$
\begin{array}{l} u ^ {\prime} (t) = t _ {1} u _ {c} (t) + \dots + t _ {m} u _ {c} (t - m + 1) - s _ {1} y (t) - \dots - s _ {l} y (t - l + 1) \\ - r _ {1} u (t) \quad \dots - r _ {k} u (t - k + 1) \\ \end{array}
$$

The computational delay can thus be significantly reduced by a proper implementation of the controller. In a proper implementation the delay can be reduced. Apart from the two multiplications and the two additions, $u(t)$ must be tested for limitations and anti-reset windup must be done in a proper way. Since the computational delay appears in the same way as a time delay in the process dynamics, it is important to take it into account in designing a control system. A common rule of thumb is that the time delay can be neglected if it is less than 10% of the sampling period. For high-performance systems it should always be taken into account. Since the time delay is not known until the algorithm has been coded, the control design may have to be repeated. For an adaptive system it is important that the model structure is chosen so that the computational delay can be accommodated. In multitasking systems it may also happen that the computational delay varies with time.
