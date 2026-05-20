The condition $F(e^{j\omega T_{s}}) \approx F_{c}(j\omega)$ will hold to the extent that $\omega_{c}T_{s} \ll 2$ , as before; however, since the bracket on the RHS of Equation 9.38 has no linear term, the Tustin approximation is better at low frequencies than the backward-difference approximation.

As derived, the Tustin approximation is asymptotically exact, as $\omega \rightarrow 0$ . It may be scaled so that the approximation is exact at some other frequency, say, $\omega_{1}$ ; that is known as prewarping. We wish to choose a scaling factor $\alpha$ such that

$$\alpha \frac {e ^ {j \omega_ {1} T _ {s}} - 1}{e ^ {j \omega_ {1} T _ {s}} + 1} = j \omega_ {1}\alpha \frac {e ^ {j \omega_ {1} T _ {s}} (e ^ {j \omega_ {1} T _ {s} / 2} - e ^ {j \omega_ {1} T _ {s} / 2})}{e ^ {j \omega_ {1} T _ {s} / 2} (e ^ {j \omega_ {1} T _ {s} / 2} + e ^ {j \omega_ {1} T _ {s} / 2})} = j \omega_ {1}.$$

Solving for $\alpha$ yields

$$\alpha = \frac {\omega}{\tan (\omega_ {1} T _ {s} / 2)}$$

and the Tustin transformation with prewarping is

$$s \rightarrow \frac {\omega_ {1}}{\tan \frac {(\omega_ {1} T _ {s})}{2}} \frac {z - 1}{z + 1}. \tag {9.39}$$

Prewarping may be used to ensure a good match between $F_{c}(j\omega)$ and $F(e^{j\omega T_{s}})$ at frequencies near crossover. It is often the case that the loop gain is large at low frequencies and small at high frequencies; neither situation requires accurate approximation of the loop gain. On the other hand, the crossover region is critical, so it may be desirable to have accuracy there.
