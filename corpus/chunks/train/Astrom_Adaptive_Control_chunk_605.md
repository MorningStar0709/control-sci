# The Dual-Input Describing Function

It is assumed that $b(t)$ varies so slowly that it can be approximated by a constant. The input signal to the relay is thus of the form

$$u (t) = a \sin \omega t + b$$

The relay input and output are shown in Fig. 10.8. The relay output can be expanded in a Fourier series

$$y (t) = b N _ {B} + a N _ {A} \sin \omega t + a N _ {A _ {2}} \sin 2 \omega t + \dots \tag {10.2}$$

where the numbers $N_{A}$ and $N_{B}$ are given by

$$
\begin{array}{l} N _ {B} = \frac {1}{2 \pi b} \int_ {0} ^ {2 \pi} y (t) d t = \frac {d (\pi + \alpha)}{2 \pi b} \frac {- d (\pi - 2 \alpha) + \alpha d}{2 \pi b} \\ = \frac {4 \alpha d}{2 \pi b} = \frac {2 \alpha d}{\pi b} = \frac {2 d}{\pi b} \sin^ {- 1} \left(\frac {b}{a}\right) \\ \end{array}
N _ {A} = \frac {1}{\pi a} \int_ {0} ^ {2 \pi} y (t) \sin \omega t d t = \frac {2 d}{\pi a} \int_ {\alpha} ^ {\pi - \alpha} \sin \omega t d t= \frac {4 d}{\pi a} \cos \alpha = \frac {4 d}{\pi a} \sqrt {1 - (b / a) ^ {2}}
$$

![](image/1bdb590d15b1904a8aacadec19c985c831b88b63bdba0c491386348610c514f4.jpg)

<details>
<summary>line</summary>

| Time | y(t) |
| --- | --- |
| 0 | 0 |
| a | b |
| b | 0 |
| d | d |
</details>

Figure 10.8 Relay inputs and outputs.

Small values of b/a give the approximations

$$N _ {A} \approx \frac {4 d}{\pi a} \quad N _ {B} \approx \frac {2 d}{\pi a}$$

Notice that

$$N _ {A} \approx 2 N _ {B} \tag {10.3}$$
