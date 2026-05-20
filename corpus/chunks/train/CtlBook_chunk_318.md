$K _ { I }$ is the integral gain. Looking at the second term of Equation 9.9 we see that $K _ { I }$ appears multiplied by $1 / s _ { ; }$ , the integral operator. If the other gains were zero, the control output, $u ,$ would be $K _ { I }$ times the time integral of the error:

$$u (t) = K _ {I} \int_ {0} ^ {t} e (t) d t$$

$K _ { D }$ is the derivative gain. Looking at the third term of Equation 9.8 we see that $K _ { D }$ appears multiplied by s, the derivative operator. If the other gains were zero, the control output, $u ,$ would be $K _ { D }$ times the time derivative of the error:

$$u (t) = K _ {D} \frac {d}{d t} e (t)$$

In fact, using the inverse Laplace transform we can write:

$$u (t) = K _ {P} e (t) + K _ {I} \int_ {0} ^ {t} e (t) d t + K _ {D} \frac {d}{d t} e (t)$$

Some alternate forms of the PID controller are given in of Equation 9.9. These forms are useful as we design the PID controller for a specic system.
