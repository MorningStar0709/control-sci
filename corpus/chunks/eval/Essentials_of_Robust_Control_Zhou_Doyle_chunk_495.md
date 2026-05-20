$$
\overline {{\sigma}} \left[ \left(\frac {D (s) (\mathcal {F} _ {\ell} (P (s) , K (s))) D ^ {- 1} (s)}{\beta_ {1}} - G (s)\right) (I + G ^ {\sim} (s) G (s)) ^ {- \frac {1}{2}} \right]= \overline {{\sigma}} \left[ \left(\frac {D _ {\min} \left(\mathcal {F} _ {\ell} (P , K)\right) D _ {\min} ^ {- 1}}{\beta_ {1}} - D _ {a p} ^ {\sim} G D _ {a p}\right) D _ {a p} ^ {\sim} (I + G ^ {\sim} G) ^ {- \frac {1}{2}} \right]
\begin{array}{l} = \overline {{\sigma}} \left[ \left(\frac {D _ {\min} \left(\mathcal {F} _ {\ell} (P , K)\right) D _ {\min} ^ {- 1}}{\beta_ {1}} - G _ {N} G _ {M} ^ {- 1}\right) D _ {a p} ^ {\sim} (I + G ^ {\sim} G) ^ {- \frac {1}{2}} \right] \\ = \overline {{\sigma}} \left[ \left(\frac {D _ {\min} \left(\mathcal {F} _ {\ell} (P , K)\right) D _ {\min} ^ {- 1} G _ {M}}{\beta_ {1}} - G _ {N}\right) G _ {M} ^ {- 1} D _ {a p} ^ {\sim} (I + G ^ {\sim} G) ^ {- \frac {1}{2}} \right] \\ = \overline {{\sigma}} \left[ \frac {D _ {\mathrm{min}} (\mathcal {F} _ {\ell} (P , K)) D _ {\mathrm{min}} ^ {- 1} G _ {M}}{\beta_ {1}} - G _ {N} \right]. \\ \end{array}
$$

(4) Define

$$
P _ {a} = \left[ \begin{array}{l l} D _ {\min} (s) & \\ & I \end{array} \right] P (s) \left[ \begin{array}{l l} D _ {\min} ^ {- 1} (s) G _ {M} (s) & \\ & I \end{array} \right] - \beta_ {1} \left[ \begin{array}{l l} G _ {N} & \\ & 0 \end{array} \right]
$$

and find a controller $K _ { \mathrm { n e w } }$ minimizing $\| \mathcal { F } _ { \ell } ( P _ { a } , K ) \| _ { \infty }$

(5) Compute a new $\beta _ { 1 }$ as

$$\beta_ {1} = \sup _ {\omega} \inf _ {\tilde {D} _ {\omega} \in \mathcal {D}, \tilde {G} _ {\omega} \in \mathcal {G}} \{\beta (\omega): \Gamma \leq 1 \}$$

where

$$\Gamma := \overline {{\sigma}} \left[ \left(\frac {\tilde {D} _ {\omega} \mathcal {F} _ {\ell} (P , K _ {\mathrm{new}}) \tilde {D} _ {\omega} ^ {- 1}}{\beta (\omega)} - j \tilde {G} _ {\omega}\right) (I + \tilde {G} _ {\omega} ^ {2}) ^ {- \frac {1}{2}} \right].$$

(6) Find $\hat { D } _ { \omega }$ and $\hat { G } _ { \omega }$ such that

$$\inf _ {\hat {D} _ {\omega} \in \mathcal {D}, \hat {G} _ {\omega} \in \mathcal {G}} \overline {{\sigma}} \left[ \left(\frac {\hat {D} _ {\omega} \mathcal {F} _ {\ell} (P , K _ {\mathrm{new}}) \hat {D} _ {\omega} ^ {- 1}}{\beta_ {1}} - j \hat {G} _ {\omega}\right) (I + \hat {G} _ {\omega} ^ {2}) ^ {- \frac {1}{2}} \right].$$

(7) Compare the new scaling matrices $\hat { D } _ { \omega }$ and $\hat { G } _ { \omega }$ with the previous estimates $D _ { \omega }$ and $G _ { \omega }$ . Stop if they are close, else replace $D _ { \omega } , \ G _ { \omega }$ and K with $\hat { D } _ { \omega } , \hat { G } _ { \omega }$ and $K _ { \mathrm { n e w } }$ , respectively, and go back to step (2).
