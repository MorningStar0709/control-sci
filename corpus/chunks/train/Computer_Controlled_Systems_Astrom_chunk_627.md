THEOREM 10.2 FILTERING OF STATIONARY PROCESSES Consider a stationary discrete-time dynamic system with sampling period 1 and the pulse-transfer function H. Let the input signal be a stationary stochastic process with mean $m_{u}$ and spectral density $\phi_{u}$ . If the system is stable, then the output is also a stationary process with the mean

$$m _ {y} = H (1) m _ {u} \tag {10.16}$$

and the spectral density

$$\phi_ {y} (\omega) = H (e ^ {i \omega}) \phi_ {u} (\omega) H ^ {T} (e ^ {- i \omega}) \tag {10.17}$$

The cross-spectral density between the input and the output is given by

$$\phi_ {y u} = H (e ^ {i \omega}) \phi_ {u} (\omega) \tag {10.18}$$

Remark 1. The result has a simple physical interpretation. The number $|H(e^{i\omega})|$ is the steady-state amplitude of the response of the system to a sine wave with frequency $\omega$ . The value of the spectral density of the output is then the product of the power gain $|H(e^{i\omega})|^2$ and the spectral density of the input $\phi_u(\omega)$ .

Remark 2. It follows from Eq. (10.18) that the cross-spectral density is equal to the transfer function of the system if the input is white noise with unit spectral density. This fact can be used to determine the pulse-transfer function of a system.

The result is illustrated by an example.
