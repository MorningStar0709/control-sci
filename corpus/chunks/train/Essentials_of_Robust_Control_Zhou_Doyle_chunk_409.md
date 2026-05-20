$\Delta _ { k } = ( \hat { K } - K ) W$ then stabi $T _ { z _ { 1 } w _ { 1 } } =$ $G _ { 2 2 } ( I - K G _ { 2 2 } ) ^ { - 1 }$ $\mathcal { F } _ { \ell } \left( \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { W ^ { - 1 } } \end{array} \right] T _ { \hat { z } \hat { w } } , \Delta _ { k } \right) = \mathcal { F } _ { \ell } ( G , \hat { K } )$ $\hat { K }$ system and satisfies $\begin{array} { r } { \left\| \mathcal { F } _ { \ell } ( G , \bar { K } ) \right\| _ { \infty } < 1 \mathrm { ~ i f ~ } \| \Delta _ { k } \| _ { \infty } = \left\| ( \hat { K } - K ) W \right\| _ { \infty } \leq 1 } \end{array}$ and part 2 of

Problem 15.4 is satisfied by a controller K. Hence to reduce the order of the controller K, it is sufficient to solve a frequency-weighted model reduction problem if W can be calculated. In the single-input and single-output case, a “smallest” weighting function $W ( s )$ can be calculated using part 2 of Problem 15.4 as follows:

$$| W (j \omega) | \geq \sup _ {\overline {{\sigma}} (\Delta_ {p}) \leq 1} | \mathcal {F} _ {u} (T _ {\hat {z} \hat {w}} (j \omega), \Delta_ {p}) |.$$

Repeat Problems 15.1 and 15.2 using the foregoing method. (Hint: W can be computed frequency by frequency using µ software and then fitted by a stable and minimum phase transfer function.)

Problem 15.6 One way to generalize the method in Problem 15.5 to the MIMO case is to take a diagonal W

$$W = \operatorname{diag} (W _ {1}, W _ {2}, \dots , W _ {m})$$

and let $\hat { W } _ { i }$ be computed from

$$| \hat {W} _ {i} (j \omega) | \geq \sup _ {\overline {{\sigma}} (\Delta_ {p}) \leq 1} \left\| e _ {i} ^ {T} \mathcal {F} _ {u} (T _ {\hat {z} \hat {w}} (j \omega), \Delta_ {p}) \right\|$$

where $e _ { i }$ is the ith unit vector. Next let $\alpha ( s )$ be computed from

$$| \alpha (j \omega) | \geq \sup _ {\overline {{\sigma}} (\Delta_ {p}) \leq 1} \left\| \hat {W} ^ {- 1} \mathcal {F} _ {u} (T _ {\hat {z} \hat {w}} (j \omega), \Delta_ {p}) \right\|$$

where $\hat { W } = \mathrm { d i a g } ( \hat { W } _ { 1 } , \hat { W } _ { 2 } , \dots , \hat { W } _ { m } )$ . Then a suitable W can be taken as

$$W = \alpha \hat {W}.$$

Apply this method to Problem 15.3.

Problem 15.7 Generalize the procedures in Problems 15.5 and 15.6 to problems with additional structured uncertainty cases. (A more general case can be found in Yang and Packard [1995].)
