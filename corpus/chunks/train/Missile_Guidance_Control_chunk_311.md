$$a _ {n} = N V _ {c} \left(\frac {d \lambda}{d t}\right) + (1 / 2) a _ {T} t _ {g o} ^ {2}. \tag {4.75}$$

Equation (4.75) is known as the augmented proportional navigation (APN) guidance law [17], [26], [35]. Note that since the target acceleration is not known a priori, if APN is chosen as the guidance law, then the target acceleration must be estimated continuously during the flight.

The acceleration required by a missile using the APN guidance law to intercept a step-maneuvering target is given by [17]

$$a _ {n} = \frac {1}{2} N ^ {\prime} a _ {T} [ 1 - (t / t _ {f}) ] ^ {N ^ {\prime} - 2}. \tag {4.76}$$

Equation (4.76) arises from a zero-lag homing loop. Furthermore, we see from (4.76) that as time increases, the intercept missile’s acceleration required to intercept a maneuvering target decreases. As a result, we see from (4.76) that the maximum required acceleration using the APN guidance law at the initial time is expressed as

$$(a _ {n}) _ {\max} = \frac {1}{2} N ^ {\prime} a _ {T}, \tag {4.77}$$

indicating that only half as much acceleration is required by the missile with APN than missiles employing the conventional PN guidance law with N- = 3.

The concept of augmented proportional navigation will now be discussed from a different perspective. Consider a linearized version of the guidance law given by

$$y (t) = w (t) * \left[ \left(y _ {T} - y\right) / (T - t) \right] + v (t) * y _ {T} (t), \tag {4.78}$$

where

y(t) = missile perturbation from a collision course normal to the nominal LOS [ft], yT (t) = corresponding target perturbation [ft],

t = time from the start of the engagement [sec],

T = total time of engagement [sec].

The asterisk (∗) in (4.78) denotes convolution. Furthermore, v(t) is a low-pass filter, and w(t) corresponds to a pure integrator followed by a low-pass filter. When v(t) is zero, (4.78) will be recognized as the usual proportional navigation. Historically, APN has been used for command guidance. Potential exists also for application to systems that detect the target with an onboard interceptor sensor.

In modeling PN, the transforms of v(t) and w(t), V (s) and W (s), respectively, are idealized to

$$V (s) = 0,W (s) = N ^ {\prime} / s, \tag {4.79}$$

where as before, N- is the effective navigation ratio. The solution for interceptor terminal maneuver for PN is

$$a _ {M} / a _ {T} = N ^ {\prime} / (N ^ {\prime} - 1), \tag {4.80}$$

![](image/b80e77424e949e183b839a72c9406f3d5349ada297f48b8804f6237d952b3301.jpg)
