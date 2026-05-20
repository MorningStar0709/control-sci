# Bumpless Parameter Changes

A controller is a dynamic system. A change of the parameters of a dynamic system will naturally result in changes of its output even if the input is kept constant. Changes in the output can in some cases be avoided by a simultaneous change of the state of the system. The changes in the output will also depend on the chosen realization. With a PID-controller it is natural to require that there be no drastic changes in the output if the parameters are changed when the error is zero. This will obviously hold for all incremental algorithms, because the output of an incremental algorithm is zero when the input is zero irrespective of the parameter values. It also holds for a position algorithm with the structure shown in Figs. 8.11(b) and (c). For a position algorithm it depends, however, on the implementation. Assume, for example, that the state is chosen as

$$x _ {I} = \int^ {t} e (s) d s$$

when implementing the algorithm. The integral term is then

$$I = \frac {K}{T _ {i}} x _ {I}$$

Any change of K or $T_{i}$ will then result in a change of I. To avoid bumps when the parameters are changed it is therefore essential that the state be chosen as

$$x _ {l} = \int^ {t} \frac {K (s)}{T _ {l} (s)} e (s) d s$$

when implementing the integral term.
