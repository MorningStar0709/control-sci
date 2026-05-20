# The Sampling Theorem

Very little is lost by sampling a continuous-time signal if the sampling instants are sufficiently close, but much of the information about a signal can be lost if the sampling points are too far apart. This was illustrated in Examples 1.4 and 3.14.

It is, of course, essential to know precisely when a continuous-time signal is uniquely given by its sampled version. The following theorem gives the conditions for the case of periodic sampling.

THEOREM 7.1 SHANNON'S SAMPLING THEOREM A continuous-time signal with a Fourier transform that is zero outside the interval $(- \omega_0, \omega_0)$ is given uniquely by its values in equidistant points if the sampling frequency is higher than $2\omega_0$ . The continuous-time signal can be computed from the sampled signal by the interpolation formula

$$f (t) = \sum_ {k = - \infty} ^ {\infty} f (k h) \frac {\sin (\omega_ {s} (t - k h) / 2)}{\omega_ {s} (t - k h) / 2} = \sum_ {k = - \infty} ^ {\infty} f (k h) \operatorname{sinc} \frac {\omega_ {s} (t - k h)}{2} \tag {7.1}$$

where $\omega_{s}$ is the sampling angular frequency in radians per second (rad/s).

Proof. Let the signal be f and let F be its Fourier transform.

$$F (\omega) = \int_ {- \infty} ^ {\infty} e ^ {- i \omega t} f (t) d tf (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} e ^ {i \omega t} F (\omega) d \omega \tag {7.2}$$

Introduce

$$F _ {s} (\omega) = \frac {1}{h} \sum_ {k = - \infty} ^ {\infty} F (\omega + k \omega_ {s}) \tag {7.3}$$

The proof is based on the observation that the samples $f(kh)$ can be regarded as the coefficients of the Fourier series of the periodic function $F_{s}(\omega)$ . This is shown by a direct calculation. The Fourier expansion of $F_{s}$ is

$$F _ {s} (\omega) = \sum_ {k = - \infty} ^ {\infty} C _ {k} e ^ {- i k h \omega} \tag {7.4}$$

where the coefficients are given by

$$C _ {k} = \frac {1}{\omega_ {s}} \int_ {0} ^ {\omega_ {s}} e ^ {i k h \omega} F _ {s} (\omega) d \omega$$

By using the definition of the Fourier coefficients and the relations given in (7.2) and (7.3), it is straightforward to show that

$$C _ {h} = f (k h) \tag {7.5}$$

It thus follows that the sampled signal $\{f(kh), k = \ldots, -1, 0, 1, \ldots\}$ uniquely determines the function $F_{s}(\omega)$ . Under the assumptions of the theorem the function F is zero outside the interval $(-\omega_{0}, \omega_{0})$ . If $\omega_{s} > 2\omega_{0}$ , it follows from (7.3) that
