# 16.3 Justification for $\mathcal { H } _ { \infty }$ Loop Shaping

The objective of this section is to provide justification for the use of parameter  as a design indicator. We will show that  is a measure of both closed-loop robust stability and the success of the design in meeting the loop-shaping specifications. Readers are encouraged to consult the original reference by McFarlane and Glover [1990] for further details.

We first examine the possibility of loop shape deterioration at frequencies of high loop gain (typically low-frequency). At low-frequency [in particular, $\omega \in ( 0 , \omega _ { l } ) ]$ , the deterioration in loop shape at plant output can be obtained by comparing $\underline { { \sigma } } ( P W _ { 1 } K _ { \infty } W _ { 2 } )$

to $\underline { { \sigma } } ( P _ { s } ) = \underline { { \sigma } } ( W _ { 2 } P W _ { 1 } )$ . Note that

$$\underline {{\sigma}} (P K) = \underline {{\sigma}} (P W _ {1} K _ {\infty} W _ {2}) = \underline {{\sigma}} (W _ {2} ^ {- 1} W _ {2} P W _ {1} K _ {\infty} W _ {2}) \geq \underline {{\sigma}} (W _ {2} P W _ {1}) \underline {{\sigma}} (K _ {\infty}) / \kappa (W _ {2}) \tag {16.3}$$

where $\kappa ( \cdot )$ denotes condition number. Similarly, for loop shape deterioration at plant input, we have

$$\underline {{\sigma}} (K P) = \underline {{\sigma}} (W _ {1} K _ {\infty} W _ {2} P) = \underline {{\sigma}} (W _ {1} K _ {\infty} W _ {2} P W _ {1} W _ {1} ^ {- 1}) \geq \underline {{\sigma}} (W _ {2} P W _ {1}) \underline {{\sigma}} (K _ {\infty}) / \kappa (W _ {1}). \tag {16.4}$$

In each case, $\underline { { \sigma } } ( K _ { \infty } )$ is required to obtain a bound on the deterioration in the loop shape at low-frequency. Note that the condition numbers $\kappa ( W _ { 1 } )$ and $\kappa ( W _ { 2 } )$ are selected by the designer.

Next, recalling that $P _ { s }$ denotes the shaped plant and that $K _ { \infty }$ robustly stabilizes the normalized coprime factorization of $P _ { s }$ with stability margin , we have

$$
\left\| \left[ \begin{array}{c} I \\ K _ {\infty} \end{array} \right] (I + P _ {s} K _ {\infty}) ^ {- 1} \tilde {M} _ {s} ^ {- 1} \right\| _ {\infty} \leq \epsilon^ {- 1} := \gamma \tag {16.5}
$$
