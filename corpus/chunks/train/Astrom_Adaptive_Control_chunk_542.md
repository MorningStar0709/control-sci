# 8.4 TRANSIENT RESPONSE METHODS

Several simple tuning methods for PID controllers are based on transient response experiments. Many industrial processes have step responses of the type shown in Fig. 8.1, in which the step response is monotonous after an initial time. A system with a step response of the type shown in Fig. 8.1 can be approximated by the transfer function

$$G (s) = \frac {k}{1 + s T} e ^ {s L} \tag {8.4}$$

where k is the static gain, L is the apparent time delay, and T is the apparent time constant. The parameter a is given by

$$a = k \frac {L}{T} \tag {8.5}$$
