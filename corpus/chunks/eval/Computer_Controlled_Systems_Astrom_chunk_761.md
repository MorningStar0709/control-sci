# Sensitivity and Robustness

It is important that a control system be insensitive or robust with respect to measurement errors, plant disturbances, and modeling errors. This may be analyzed as in Sec. 5.5 for the pole-placement problem. The robustness properties are conveniently expressed in terms of the loop gain:

$$\mathcal {L} = \frac {B S}{A R}$$

or the return difference

$$H _ {r d} = \frac {1}{S} = 1 + \frac {B S}{A R} = \frac {A R + B S}{A R} = \frac {P C}{A R}$$

The loop gain $\mathcal{L}(\exp i\omega h)$ is normally high for low frequencies and small for high frequencies. The crossover frequency $\omega_{c}$ is the lowest frequency, where

$$\left| \mathcal {L} \left(e ^ {i \omega_ {c} h}\right) \right| = 1$$

The closed-loop system is insensitive to plant disturbances at those frequencies where the loop gain is high. To have low sensitivity to poor modeling of the high-frequency dynamics of the plant, it is desirable that the loop gain decreases rapidly above the crossover frequency. It is possible to make sure that the loop gain is high for certain frequencies by choosing models with special structure, as was done in Examples 12.14 and 12.15. Plots similar to those in Fig. 5.6 are also useful in evaluating the sensitivity. In a properly designed sample-data system, there will be antialiasing filters, which eliminate signal transmission above the Nyquist frequency. The selection of a proper sampling rate is one way to make sure that the loop gain is low over a given frequency. This also means that high-frequency modeling errors have little influence. Notice, however, that plots of the loop gain and the return difference will not give the complete picture because there may be pole-zero cancellations that do not show up in these plots.

An analysis of the characteristic equations is useful in such a case. To perform such an analysis, assume that the system is governed by

$$A ^ {0} (q) y (k) = B ^ {0} (q) u (k) + C ^ {0} (q) e (k) \tag {12.71}$$

but that a regulator is designed based on a different model, as in (12.70). The regulators given by Theorems 12.4 and 12.5 give a closed-loop system with the characteristic polynomial

$$
\begin{array}{l} A ^ {0} R + B ^ {0} S = A ^ {0} R - A R + B ^ {0} S - B S + A R + B S \\ = P C + (A ^ {0} - A) R + (B ^ {0} - B) S \\ \end{array}
$$

When the model of (12.70) is equal to the system of (12.71) the characteristic polynomial is $PC = P_{1}A_{2}C$ , as expected. By continuity it also follows that small changes in the system give small changes in the closed-loop poles. The system is sensitive to changes in the parameters if polynomial $P_{1}$ or C have zeros close to the unit circle.

To guarantee systems with a low sensitivity, it is necessary to impose further constraints. Recall that both C and P were obtained as solutions to a spectral-factorization problem.
