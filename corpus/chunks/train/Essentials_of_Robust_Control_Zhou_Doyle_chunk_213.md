# UNSTRUCTURED ANALYSIS THEOREM

Given NS & Perturbed Model Sets

Then Closed-Loop Robust Stability

if and only if Robust Stability Tests

The table also indicates representative types of physical uncertainties that can be usefully represented by cone-bounded perturbations inserted at appropriate locations. For example, the representation $P _ { \Delta } = ( I + W _ { 1 } \Delta W _ { 2 } ) P$ in the first row is useful for output errors at high frequencies (HF), covering such things as unmodeled high-frequency dynamics of sensors or plants, including diffusion processes, transport lags, electromechanical resonances, etc. The representation $P _ { \Delta } = P ( I + W _ { 1 } \Delta W _ { 2 } )$ in the second row covers similar types of errors at the inputs. Both cases should be contrasted with the third and the fourth rows, which treat $P ( I + W _ { 1 } \Delta W _ { 2 } ) ^ { - 1 }$ and $( I + W _ { 1 } \Delta W _ { 2 } ) ^ { - 1 } P _ { \cdot }$ These representations are more useful for variations in modeled dynamics, such as lowfrequency (LF) errors produced by parameter variations with operating conditions, with aging, or across production copies of the same plant.

Note from the table that the stability requirements on $\Delta$ do not limit our ability to represent variations in either the number or locations of rhp singularities, as can be seen from some simple examples.

Example 8.3 Suppose an uncertain system with changing numbers of right-half plane poles is described by

$$P _ {\Delta} = \left\{\frac {1}{s - \delta}: \delta \in \mathbb {R}, | \delta | \leq 1 \right\}.$$

Then $P _ { 1 } = \frac { 1 } { s - 1 } \in P _ { \Delta }$ s − 1 has one right-half plane pole and $P _ { 2 } = \frac { 1 } { s + 1 } \in P _ { \Delta }$ s + 1 has no right-half plane pole. Nevertheless, the set of $P _ { \Delta }$ can be covered by a set of feedback uncertain plants:

$$P _ {\Delta} \subset \boldsymbol {\Pi} := \left\{P (1 + \delta P) ^ {- 1}: \delta \in \mathcal {R H} _ {\infty}, \| \delta \| _ {\infty} \leq 1 \right\}$$

with $P = { \frac { 1 } { s } } .$

Example 8.4 As another example, consider the following set of plants:

$$P _ {\Delta} = \frac {s + 1 + \alpha}{(s + 1) (s + 2)}, | \alpha | \leq 2.$$

This set of plants has changing numbers of right-half plane zeros since the plant has no right-half plane zero when $\alpha = 0$ and has one right-half plane zero when α = −2. The uncertain plant can be covered by a set of multiplicative perturbed plants:

$$P _ {\Delta} \subset \Pi := \left\{\frac {1}{s + 2} (1 + \frac {2 \delta}{s + 1}), \delta \in \mathcal {R H} _ {\infty}, \| \delta \| _ {\infty} \leq 1 \right\}.$$

It should be noted that this covering can be quite conservative.
