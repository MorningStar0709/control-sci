# A Direct Self-tuner with Integral Action

It is also straightforward to introduce integrators in the direct self-tuners. Consider a process model given by

$$A (q) y (t) = B (q) (u (t) + v (t)) \tag {3.43}$$

where $d = \deg A(q) - \deg B(q)$ . It is assumed that v is constant or changes infrequently. Let the desired response to command signals be given by

$$A _ {m} (q) y (t) = A _ {m} (1) u _ {c} (t - d) \tag {3.44}$$

where $\deg A_m \geq d$ . Let the observer polynomial be $A_o(q)$ . The design equation is

$$A R + B S = B ^ {+} A _ {o} A _ {m} \tag {3.45}$$

where $B = b_{0}B^{+}$ . If we require that the regulator has integral action, we find that the polynomial R has the form

$$R = R ^ {\prime} B ^ {+} = R _ {1} ^ {\prime} B ^ {+} (q - 1) = R _ {1} ^ {\prime} B ^ {+} \Delta \tag {3.46}$$

Equation (3.45) then becomes

$$A \Delta R _ {1} ^ {\prime} + b _ {0} S = A _ {o} A _ {m} \tag {3.47}$$

Hence

$$
\begin{array}{l} A _ {o} A _ {m} y = A R _ {1} ^ {\prime} \Delta y + b _ {0} S y \\ = B R _ {1} ^ {\prime} \Delta u + b _ {0} R ^ {\prime} \Delta v + b _ {0} S y \\ = b _ {0} \left(R ^ {\prime} \Delta u + S y\right) + b _ {0} R ^ {\prime} \Delta v \tag {3.48} \\ \end{array}
$$

where Eq. (3.43) was used to obtain the second equality. Notice that the last term will vanish after a transient if v is constant. If we rewrite Eq. (3.48) in the backwards operator, ignoring v, we get

$$A _ {o} ^ {*} \left(q ^ {- 1}\right) A _ {m} ^ {*} \left(q ^ {- 1}\right) y (t + d) = b _ {0} \left(R ^ {\prime *} \left(q ^ {- 1}\right) \Delta^ {*} \left(q ^ {- 1}\right) u (t) + S ^ {*} \left(q ^ {- 1}\right) y (t)\right) \tag {3.49}$$

This equation can be used as a basis for parameter estimation, but there are several drawbacks in doing so. First, the operation $A_{o}^{*}A_{m}^{*}$ is a high-pass filter that is very sensitive to noise. Furthermore, it follows from Eq. (3.47) that

$$b _ {0} S ^ {*} (1) = A _ {o} ^ {*} (1) A _ {m} ^ {*} (1) = A _ {o} (1) A _ {m} (1) \tag {3.50}$$

All the parameters in the S polynomial are thus not free. If all parameters are estimated, there is, of course, no guarantee that Eq. (3.50) holds. However, it is easy to find a remedy. A polynomial $S^{*}$ with the property given by Eq. (3.50) can be written as

$$
\begin{array}{l} b _ {0} S ^ {*} = A _ {o} (1) A _ {m} (1) + \left(1 - q ^ {- 1}\right) S ^ {\prime *} \left(q ^ {- 1}\right) \\ = A _ {o} (1) A _ {m} (1) + S ^ {\prime *} \left(q ^ {- 1}\right) \Delta^ {*} \\ \end{array}
$$

Equation (3.49) then becomes
