It should also be noted that even though the complex $\mu \left( \mathrm { i . e . , } s _ { r } = 0 \right)$ is a continuous function of the data, the mixed $\mu \ ( { \mathrm { i . e . } } , s _ { r } \neq 0 )$ may only be upper semicontinuous; see Packard and Pandey [1993]. It was also shown in Braatz et al. [1994] and Toker and Ozbay [1995] that the computation of ¨ $\mu$ is a NP hard problem, which means that it may not be computable in a polynomial time. Of course, it should not be interpreted as every µ problem will not be solvable in a polynomial time; merely some might not.

Obviously, the upper bound for the complex µ can be applied for the mixed $\mu$ when the intervals of the real parameters are covered by complex disks. However, a better bound can be obtained for the mixed $\mu$ by exploiting the phase information of the real parameters. To motivate the improved bound for the mixed $\mu ,$ , we consider again the upper bound for the complex $\mu$ problem. It is known that

$$\mu_ {\Delta} (M) \leq \inf _ {D \in \mathcal {D}} \overline {{\sigma}} (D M D ^ {- 1}).$$

This bound can be reformulated using linear matrix inequalities by noting the following:

$$\overline {{\sigma}} (D M D ^ {- 1}) \leq \beta \iff (D M D ^ {- 1}) ^ {*} D M D ^ {- 1} \leq \beta^ {2} I \iff M ^ {*} D ^ {*} D M - \beta^ {2} D ^ {*} D \leq 0.$$

Since $D$ is nonsingular and $D ^ { \ast } D \in { \mathcal { D } }$ , we have

$$\mu_ {\boldsymbol {\Delta}} (M) \leq \inf _ {D \in \mathcal {D}} \min _ {\beta} \left\{\beta : M ^ {*} D M - \beta^ {2} D \leq 0 \right\}.$$

The following upper bound for the mixed $\mu$ was derived by Fan, Tits, and Doyle [1991] and reformulated in the current form by Young [1993].

Theorem 18.3 Let $M \in \mathbb { C } ^ { n \times n }$ and $\Delta \in \Delta$ . Then

$$\mu_ {\boldsymbol {\Delta}} (M) \leq \inf _ {D \in \mathcal {D}, G \in \mathcal {G}} \min _ {\beta} \left\{\beta : M ^ {*} D M + j (G M - M ^ {*} G) - \beta^ {2} D \leq 0 \right\}.$$

Proof. Suppose we have a $Q \in \mathcal { Q }$ such that $Q M$ has a real eigenvalue $\lambda \in \mathbb { R }$ . Then there is a vector $x \in \mathbb { C } ^ { n }$ such that

$$Q M x = \lambda x.$$

Let $D \in \mathcal { D }$ . Then $D ^ { \frac { 1 } { 2 } } \in { \mathcal { D } } , D ^ { \frac { 1 } { 2 } } Q = Q D ^ { \frac { 1 } { 2 } }$ and

$$D ^ {\frac {1}{2}} Q M x = Q D ^ {\frac {1}{2}} M x = \lambda D ^ {\frac {1}{2}} x.$$

Since $\overline { { \sigma } } ( Q ) \leq 1$ , it follows that
