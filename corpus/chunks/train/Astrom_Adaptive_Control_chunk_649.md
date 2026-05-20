# Robust Pole Placement

The Youla parameterization can be used to impose extra conditions on the controller. This idea was used in Section 3.6 to obtain controllers that have integral action. We now use it to improve the robustness of the controller. One way to do this is to require that the controller have small gain for those frequencies at which the process is very uncertain. For example, it is useful to require that the controller should have zero gain at the Nyquist frequency. This is accomplished by the condition $S(-1) = 0$ . We can also require that the controller gain be zero at frequency $\omega_0$ . This is equivalent to requiring that the polynomial

$$q ^ {2} - 2 \cos (\omega_ {0} h) q + 1$$

be a factor of $S(q)$ . To satisfy such requirements, the order of the closed-loop system must thus be increased. The additional poles introduced are specified by the polynomial X. We illustrate this by an example.
