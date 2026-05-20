$$
F (\omega) = \left\{ \begin{array}{l l} h F _ {s} (\omega) & | \omega | \leq \frac {\omega_ {s}}{2} \\ 0 & | \omega | > \frac {\omega_ {s}}{2} \end{array} \right. \tag {7.6}
$$

The Fourier transform of the continuous-time signal is thus uniquely given by $F_{s}$ , which in turn is given by the sampled function $\{f(kh), k = \ldots, -1, 0, 1, \ldots\}$ .

The first part of the theorem is thus proved. To show Eq. (7.1), notice that it follows from (7.2) and (7.6) that

$$
\begin{array}{l} f (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} e ^ {i \omega t} F (\omega) d \omega \\ = \frac {h}{2 \pi} \int_ {- \omega_ {s} / 2} ^ {\omega_ {s} / 2} e ^ {i \omega t} F _ {s} (\omega) d \omega \\ = \frac {h}{2 \pi} \int_ {- \omega_ {s} / 2} ^ {\omega_ {s} / 2} e ^ {i \omega t} \sum_ {k = - \infty} ^ {\infty} e ^ {- i k h \omega} f (k h) d \omega \\ \end{array}
$$

where the last equality follows from (7.4) and (7.5). Interchanging the order of integration and summation,

$$
\begin{array}{l} f (t) = \sum_ {k = - \infty} ^ {\infty} f (k h) \frac {h}{2 \pi} \int_ {- \omega_ {e} / 2} ^ {\omega_ {s} / 2} e ^ {i \omega t - i \omega k h} d \omega \\ = \sum_ {k = - \infty} ^ {\infty} f (k h) \frac {h}{2 \pi (t - k h)} e ^ {i \omega t - i \omega k h} \Bigg | _ {- \omega_ {s} / 2} ^ {\omega_ {s} / 2} \\ = \sum_ {k = - \infty} ^ {\infty} f (k h) \frac {\sin \left(\omega_ {s} (t - k h) / 2\right)}{\pi (t - k h) / h} \\ \end{array}
$$

Because $\omega_{s}h = 2\pi$ , Eq. (7.1) now follows.

Remark 1. The frequency $\omega_{N} = \omega_{s}/2$ plays an important role. This frequency is called the Nyquist frequency.

Remark 2. Notice that Eq. (7.1) defines the reconstruction of signals whose Fourier transforms vanish for frequencies larger than the Nyquist frequency $\omega_{N} = \omega_{s}/2$ .

Remark 3. Because of the factor $1/h$ in Eq. (7.3), the sampling operation has a gain of $1/h$ .
