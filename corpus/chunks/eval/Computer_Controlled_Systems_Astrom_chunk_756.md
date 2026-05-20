# Command Signals

The discussion in this chapter has so far been limited to the regulator problem. To introduce command signals, refer to the discussion in Chapter 5. The key issue is to introduce the command signals in such a way that they do not generate unnecessary reconstruction errors. This is achieved by the control law

$$R (q) u (k) = t _ {0} A _ {o} (q) u _ {c} (k) - S (q) y (k)$$

where $A_{o}(q)$ is the observer polynomial and to a constant. For the optimal Kalman filter $A_{o}(q) = C(q)$ , where $C(q)$ is given by (12.40). It then follows from (12.5) that the output of the system is given by

$$y (k) = t _ {0} \frac {B (q)}{P (q)} u _ {c} (k) + \frac {\dot {R} (q)}{P (q)} e (k)$$

where $\deg R = n$ .

The pulse-transfer function from the command signal is $B(z)/P(z)$ . This response may be shaped further by cascading with a precompensator that has an arbitrary stable transfer function $H_{f}(z)$ . The control law becomes

$$u (k) = \frac {A _ {o} (q)}{R (q)} H _ {f} (q) u _ {c} (k) - \frac {S (q)}{P (q)} y (k)$$

which gives

$$y (k) = \frac {B (q)}{P (q)} H _ {f} (q) u _ {c} (k) + \frac {R (q)}{P (q)} e (k)$$

Because the polynomial P is stable, this may be canceled by the precompensator. It thus follows that the response for disturbances and command signals may be shaped differently.

The feedback S/R is first designed to ensure a good response to disturbances. The precompensator $H_{f}$ is then chosen to obtain the desired response to command signals.
