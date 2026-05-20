Figure 6.24 Bode plots for a lead compensator

To summarize,

$$\phi_ {\max} = \sin^ {- 1} \frac {\alpha - 1}{\alpha + 1} \tag {6.37}$$

which occurs at

$$\omega_ {\max} = \frac {1}{T \sqrt {\alpha}}. \tag {6.38}$$

We shall need one more result. We compute

$$
\begin{array}{l} \left| G _ {c} \left(j \omega_ {\max}\right) \right| = k \left[ \frac {\alpha^ {2} \omega_ {\max} {} ^ {2} T ^ {2} + 1}{\omega_ {\max} {} ^ {2} T ^ {2} + 1} \right] ^ {1 / 2} \\ = k \left[ \frac {\alpha + 1}{(1 / \alpha) + 1} \right] ^ {1 / 2} \\ = k \sqrt {\alpha} \\ \end{array}
$$

We redefine the gain in Equation 6.36 and use

$$G _ {c} (s) = \frac {k _ {1}}{\sqrt {\alpha}} \frac {\alpha T s + 1}{T s + 1}. \tag {6.39}$$

This normalization has the advantage that $|G_{c}(j\omega_{\max})|=k_{1}$ .

To design a lead compensator, we follow these steps:

(i) Ascertain the phase to be added at the desired crossover frequency in order that a desired phase margin be achieved. Let this phase be $\phi_{\mathrm{max}}$ .   
(ii) Calculate $\alpha$ from Equation 6.37, given $\phi_{\mathrm{max}}$ .   
(iii) With $\omega_{\mathrm{max}}$ equal to the desired crossover frequency, calculate $T$ from Equation 6.38.   
(iv) Since $|G_c(j\omega_{\max})| = k_1$ , $k_1$ is just that gain required to make $|k_1L(j\omega_{\max})| = 1$ ; in decibels, $k_1 = -|L(j\omega_{\max})|$ db.
