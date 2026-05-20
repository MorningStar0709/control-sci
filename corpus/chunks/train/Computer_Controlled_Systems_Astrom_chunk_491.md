# Frequency Prewarping

One problem with the approximations discussed earlier is that the frequency scale is distorted. For instance, if it is desired to design band-pass or notch filters, the digital filters obtained by the approximations may not give the correct frequencies for the band-pass or the notches. This effect is called frequency warping. Consider an approximation obtained by Tustin's approximation. The transmission of sinusoids for the digital filter is given by

![](image/5d0831f202f34a85ec01ae52b11f4fa76aa0e4770fc8d7daeb84a1b9f88b7df4.jpg)

<details>
<summary>text_image</summary>

iω'
-iω'
e^{iω'}
Approximation
e^{-iω'}
</details>

Figure 8.3 Frequency distortion (warping) obtained with approximation.

$$H \left(e ^ {i \omega h}\right) = \frac {1}{i \omega h} (1 - e ^ {- i \omega h}) G \left(\frac {2}{h} \cdot \frac {e ^ {i \omega h} - 1}{e ^ {i \omega h} + 1}\right)$$

The first two factors are due to the sample-and-hold operations; compare with (7.28). The argument of $G$ is

$$\frac {2}{h} \frac {e ^ {i \omega h} - 1}{e ^ {i \omega h} + 1} = \frac {2}{h} \frac {e ^ {i \omega h / 2} - e ^ {- i \omega h / 2}}{e ^ {i \omega h / 2} + e ^ {- i \omega h / 2}} = \frac {2 i}{h} \tan \left(\frac {\omega h}{2}\right)$$

The frequency scale is thus distorted. Assume, for example, that the continuous-time system blocks signals at the frequency $\omega'$ . Because of the frequency distortion, the sampled system will instead block signal transmission at the frequency $\omega$ , where

$$\omega^ {\prime} = \frac {2}{h} \tan \left(\frac {\omega h}{2}\right)$$

That is,

$$\omega = \frac {2}{h} \tan^ {- 1} \left(\frac {\omega^ {\prime} h}{2}\right) \approx \omega^ {\prime} \left(1 - \frac {(\omega^ {\prime} h) ^ {2}}{1 2}\right) \tag {8.7}$$

This expression gives the distortion of the frequency scale (see Fig. 8.3). It follows from (8.7) that there is no frequency distortion at $\omega = 0$ and that the distortion is small if $\omega h$ is small. It is easy to introduce a transformation that eliminates the scale distortion at a specific frequency $\omega_{1}$ by modifying Tustin's transformation from (8.6) to the transformation

$$s ^ {\prime} = \frac {\omega_ {1}}{\tan (\omega_ {1} h / 2)} \cdot \frac {z - 1}{z + 1} \quad (\text { Tustin with prewarping }) \tag {8.8}$$

From (8.8), it follows that

$$H \left(e ^ {i \omega_ {1} h}\right) = G (i \omega_ {1})$$

that is, the continuous-time filter and its approximation have the same value at the frequency $\omega_{1}$ . There is, however, still a distortion at other frequencies.
