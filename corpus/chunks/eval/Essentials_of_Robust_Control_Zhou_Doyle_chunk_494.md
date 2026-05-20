# D, G − K Iteration:

(1) Let K be a stabilizing controller. Find initial estimates of the scaling matrices $D _ { \omega } \in \mathcal { D } , G _ { \omega } \in \mathcal { G }$ and a scalar $\beta _ { 1 } > 0$ such that

$$\sup _ {\omega} \overline {{\sigma}} \left[ \left(\frac {D _ {\omega} \left(\mathcal {F} _ {\ell} (P (j \omega) , K (j \omega))\right) D _ {\omega} ^ {- 1}}{\beta_ {1}} - j G _ {\omega}\right) (I + G _ {\omega} ^ {2}) ^ {- \frac {1}{2}} \right] \leq 1, \quad \forall \omega .$$

Obviously, one may start with $D _ { \omega } = I , G _ { \omega } = 0$ , and a large $\beta _ { 1 } > 0$ .

(2) Fit the frequency response matrices $D _ { \omega }$ and $j G _ { \omega }$ with $D ( s )$ and $G ( s )$ so that

$$D (j \omega) \approx D _ {\omega}, \quad G (j \omega) \approx j G _ {\omega}, \quad \forall \omega .$$

Then for $s = j \omega$

$$\sup _ {\omega} \overline {{\sigma}} \left(\left(\frac {D _ {\omega} \left(\mathcal {F} _ {\ell} (P (j \omega) , K (j \omega))\right) D _ {\omega} ^ {- 1}}{\beta_ {1}} - j G _ {\omega}\right) (I + G _ {\omega} ^ {2}) ^ {- \frac {1}{2}}\right)\approx \sup _ {\omega} \overline {{\sigma}} \left[ \left(\frac {D (s) (\mathcal {F} _ {\ell} (P (s) , K (s))) D ^ {- 1} (s)}{\beta_ {1}} - G (s)\right) (I + G ^ {\sim} (s) G (s)) ^ {- \frac {1}{2}} \right].$$

(3) Let $D ( s )$ be factorized as

$$D (s) = D _ {a p} (s) D _ {\min} (s), \quad D _ {a p} ^ {\sim} (s) D _ {a p} (s) = I, \quad D _ {\min} (s), D _ {\min} ^ {- 1} (s) \in \mathcal {H} _ {\infty}.$$

That is, $D _ { a p }$ is an all-pass and $D _ { \mathrm { m i n } }$ is a stable and minimum phase transfer matrix. Find a normalized right coprime factorization

$$D _ {a p} ^ {\sim} (s) G (s) D _ {a p} (s) = G _ {N} G _ {M} ^ {- 1}, \quad G _ {N}, \quad G _ {M} \in \mathcal {H} _ {\infty}$$

such that

$$G _ {M} ^ {\sim} G _ {M} + G _ {N} ^ {\sim} G _ {N} = I.$$

Then

$$G _ {M} ^ {- 1} D _ {a p} ^ {\sim} (I + G ^ {\sim} G) ^ {- 1} D _ {a p} (G _ {M} ^ {- 1}) ^ {\sim} = I$$

and, for each frequency $s = j \omega$ , we have
