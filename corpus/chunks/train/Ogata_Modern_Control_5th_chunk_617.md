# EXAMPLE PROBLEMS AND SOLUTIONS

A–8–1. Describe briefly the dynamic characteristics of the PI controller, PD controller, and PID controller.

Solution. The PI controller is characterized by the transfer function

$$G _ {c} (s) = K _ {p} \bigg (1 + \frac {1}{T _ {i} s} \bigg)$$

The PI controller is a lag compensator. It possesses a zero at $s = - 1 / T _ { i }$ and a pole at $s = 0 ,$ . Thus, the characteristic of the PI controller is infinite gain at zero frequency. This improves the steady-state characteristics. However, inclusion of the PI control action in the system increases the type number of the compensated system by 1, and this causes the compensated system to be less stable or even makes the system unstable.Therefore, the values of $K _ { p }$ and $T _ { i }$ must be chosen carefully to ensure a proper transient response. By properly designing the PI controller, it is possible to make the transient response to a step input exhibit relatively small or no overshoot.The speed of response, however, becomes much slower. This is because the PI controller, being a low-pass filter, attenuates the high-frequency components of the signal.

The PD controller is a simplified version of the lead compensator. The PD controller has the transfer function $G _ { c } ( s )$ where,

$$G _ {c} (s) = K _ {p} \bigl (1 + T _ {d} s \bigr)$$

The value of $K _ { p }$ is usually determined to satisfy the steady-state requirement. The corner frequency $1 / T _ { d }$ is chosen such that the phase lead occurs in the neighborhood of the gain crossover frequency. Although the phase margin can be increased, the magnitude of the compensator continues to increase for the frequency region $1 / T _ { d } < \omega .$ (Thus, the PD controller is a. high-pass filter.) Such a continued increase of the magnitude is undesirable, since it amplifies high-frequency noises that may be present in the system. Lead compensation can provide a sufficient phase lead, while the increase of the magnitude for the high-frequency region is very much smaller than that for PD control. Therefore, lead compensation is preferred over PD control.
