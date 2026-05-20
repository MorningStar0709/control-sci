with structured $\Delta = \mathrm { d i a g } ( \delta _ { 1 } , \delta _ { 2 } , \delta _ { 3 } )$ . The largest singular value of M is $\overline { { \sigma } } ( M ) = 2 2 $ .9094 and the structured singular value of M computed using the $\mu$ Analysis and Synthesis Toolbox is equal to its upper-bound:

$$\mu_ {\boldsymbol {\Delta}} (M) = \inf _ {D \in \mathcal {D}} \overline {{\sigma}} (D M D ^ {- 1}) = 1 1. 9 6 3 6$$

with the optimal scaling $D _ { \mathrm { o p t } } = \mathrm { d i a g } ( 0 . 3 9 5 5 , 0 . 6 8 4 7 , 1 )$ . The optimal D minimizing

$$\inf _ {D \in \mathcal {D}} \sum_ {i = 1} ^ {F} \sum_ {j = 1} ^ {F} \| M _ {i j} \| ^ {2} \frac {d _ {i} ^ {2}}{d _ {j} ^ {2}}$$

is $D _ { \mathrm { s u b o p t } } = \mathrm { d i a g } ( 0 . 3 2 1 2 , 0 . 4 6 4 3 , 1 )$ , which is solved from equation (10.29). Using this $D _ { \mathrm { s u b o p t } } ,$ we obtain another upper-bound for the structured singular value:

$$\mu_ {\pmb {\Delta}} (M) \leq \overline {{\sigma}} (D _ {\mathrm{subopt}} M D _ {\mathrm{subopt}} ^ {- 1}) = 1 2. 2 5 3 8.$$

One may also use this $D _ { \mathrm { s u b o p t } }$ as an initial guess for the exact optimization.
