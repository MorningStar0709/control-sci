# 8.2 PID CONTROL

The PID controllers are the standard tool for industrial automation. The flexibility of the controller makes it possible to use PID control in many situations. The controllers can also be used in cascade control and other controller configurations. Many simple control problems can be handled very well by PID control, provided that the performance requirements are not too high. The PID algorithm is packaged in the form of standard regulators for process control and is also the basis of many tailor-made control systems. The textbook version of the algorithm is

$$u (t) = K _ {c} \left(e (t) + \frac {1}{T _ {i}} \int_ {0} ^ {t} e (s) d s + T _ {d} \frac {d e}{d t}\right) \tag {8.1}$$

where u is the control variable, e is the error defined as $e = u_{c} - y$ where $u_{c}$ is the reference value, and y is the process output. The algorithm that is actually used contains several modifications. It is standard practice to let the derivative action operate only on the process output. It may be advantageous to let the proportional part act only on a fraction of the reference value. The derivative action is replaced by an approximation that reduces the gain at high frequencies. The integral action is modified so that it does not keep integrating when the control variable saturates (anti-windup). Precautions are also taken so that there will not be transients when the regulator is switched from manual to automatic control or when parameters are changed.

If the nonlinearity of the actuator can be described by the function f, a reasonably realistic PID regulator can be described by

$$u (t) = f (v (t)) \tag {8.2}v (t) = P (t) + I (t) + D (t)$$

where

$$P (t) = K _ {c} \left(\beta u _ {c} (t) - y (t)\right)\frac {d I}{d t} = \frac {K _ {\mathrm{c}}}{T _ {i}} (u _ {c} (t) - y (t)) + \frac {1}{T _ {t}} (v (t) - u (t)) \tag {8.3}\frac {T _ {d}}{N} \frac {d D}{d t} = - D - K _ {c} T _ {d} \frac {d y}{d t}$$

The last term in the expression for $dI/dt$ is introduced to get anti-windup when the output saturates. This guarantees that the integral part $I$ is bounded. The parameter $T_{i}$ is a time constant for resetting the integral action when the actuator saturates. The essential parameters to be adjusted are $K_{c}, T_{i}$ , and $T_{d}$ .

The parameter N can be fixed; a typical value is N = 10. The tracking time constant is typically a fraction of the integration time $T_{i}$ .
