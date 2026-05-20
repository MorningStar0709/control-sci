# Modification of Linear Response

A pure derivative cannot, and should not be, implemented, because it will give a very large amplification of measurement noise. The gain of the derivative must thus be limited. This can be done by approximating the transfer function $sT_{d}$ as follows:

$$s T _ {d} \approx \frac {s T _ {d}}{1 + s T _ {d} / N}$$

The transfer function on the right approximates the derivative well at low frequencies but the gain is limited to N at high frequencies. N is typically in the range of 3 to 20.

In the work with analog controllers it was also found advantageous not to let the derivative act on the command signal. Later it was also found suitable to let only a fraction b of the command signal act on the proportional part. The PID-algorithm then becomes

$$U (s) = K \left(b U _ {c} (s) - Y (s) + \frac {1}{s T _ {i}} \left(U _ {c} (s) - Y (s)\right) - \frac {s T _ {d}}{1 + s T _ {d} / N} Y (s)\right) \tag {8.22}$$

where $U, U_c$ , and $Y$ denote the Laplace transforms of $u, u_c$ , and $y$ . The idea of providing different signal paths for the process output and the command signal is a good way to separate command signal response from the response to disturbances. Alternatively it may be viewed as a way to position the closed-loop zeros. There are also several other variations of the PID-algorithm that are used in commercial systems. An extra first-order lag may be used in series with the controller to obtain a high-frequency roll-off. In some applications it has also been useful to include nonlinearities. The proportional term $Ke$ can be replaced by $Ke|e|$ and a dead zone can also be included.
