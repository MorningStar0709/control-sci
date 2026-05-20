Note that $b _ { \mathrm { o p t } } ( L / s ) = 0 . 7 0 7$ for any L and $b _ { \mathrm { o p t } } ( P _ { 2 } ) \longrightarrow 0 . 7 0 7$ as $K \longrightarrow 0$ . This is because $| P _ { 2 } ( j \omega ) |$ around the frequency of the right-half plane zero is very small as $K \longrightarrow 0$ .

Next consider a plant with a pair of complex right-half plane zeros:

$$P _ {3} (s) = \frac {K [ (s - \cos \theta) ^ {2} + \sin^ {2} \theta ]}{s [ (s + \cos \theta) ^ {2} + \sin^ {2} \theta ]}.$$

The magnitude frequency response of $P _ { 3 }$ is the same as that of $P _ { 2 }$ for the same K. The optimal $b _ { \mathrm { o p t } } ( P _ { 3 } )$ for various $\theta \mathrm { { s } }$ are listed in the following table:

<table><tr><td rowspan="2"> $K = 0.1$ </td><td> $\theta$ (degree)</td><td>0</td><td>45</td><td>60</td><td>80</td><td>85</td></tr><tr><td> $b_{\text{opt}}(P_3)$ </td><td>0.5952</td><td>0.6230</td><td>0.6447</td><td>0.6835</td><td>0.6950</td></tr><tr><td rowspan="2"> $K = 1$ </td><td> $\theta$ (degree)</td><td>0</td><td>45</td><td>60</td><td>80</td><td>85</td></tr><tr><td> $b_{\text{opt}}(P_3)$ </td><td>0.2588</td><td>0.3078</td><td>0.3568</td><td>0.4881</td><td>0.5512</td></tr><tr><td rowspan="2"> $K = 10$ </td><td> $\theta$ (degree)</td><td>0</td><td>45</td><td>60</td><td>80</td><td>85</td></tr><tr><td> $b_{\text{opt}}(P_3)$ </td><td>0.0391</td><td>0.0488</td><td>0.0584</td><td>0.0813</td><td>0.0897</td></tr></table>

It can also be concluded from the table that $b _ { \mathrm { o p t } } ( P _ { 3 } )$ will be small if $| P _ { 3 } ( j \omega ) |$ is large around the frequency of $\omega = 1$ (the modulus of the right-half plane zero). It can be further concluded that, for zeros with the same modulus, $b _ { \mathrm { o p t } } ( P _ { 3 } )$ will be smaller for a plant with relatively larger real part zeros than for a plant with relatively larger imaginary part zeros $( { \mathrm { i . e . } }$ , a pair of real right-half plane zeros has a much worse effect on the performance than a pair of almost pure imaginary axis right-half plane zeros of the same modulus).

Example 16.3 Consider an unstable plant

$$P _ {4} (s) = \frac {K (s + 1)}{s (s - 1)}.$$

The magnitude frequency response of $P _ { 4 }$ is again the same as that of $P _ { 2 }$ for the same $K .$ . The following table shows that $b _ { \mathrm { o p t } } ( P _ { 4 } )$ will be small if $| P _ { 4 } ( j \omega ) |$ is small around $\omega = 1$ (the modulus of the right-half plane pole).
