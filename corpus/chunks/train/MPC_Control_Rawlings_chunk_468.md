Proof. The MHE solution exists for $T \leq N$ by the existence of the full information solution, so we consider $T > N$ . For disturbances satisfying Assumption 4.3, we established in the proof of Theorem 4.8 for the full information problem that $V _ { T } ^ { 0 } \leq V _ { \infty }$ for all $T \geq 1$ including $T = \infty$ . From Proposition 4.18 and (4.23), we have that the MHE optimal cost also has the upper bound $\hat { V } _ { T } ^ { 0 } \le V _ { \infty }$ for all $T \geq 1$ including $T = \infty$ . Since we have assumed $f ( \cdot )$ and $h ( \cdot )$ are continuous, $\Gamma _ { i } ( \cdot )$ is continuous for $i > N$ , and $\ell _ { i } ( \cdot )$ is continuous for all $i \geq 0$ , the MHE cost function $\hat { V } _ { T } ( \cdot )$ is continuous for $T > N$ . The lower bound on $\Gamma _ { i }$ for $i > N$ and $\ell _ { i }$ for all $i \geq 0$ imply that for $T > N , \hat { V } _ { T } ( \chi ( T - N ) , \pmb { \omega } )$ goes to infinity as either $\chi ( T - N )$ or ω goes to infinity. Therefore the MHE optimization takes place over a bounded, closed set for $T > N$ , and the the solution exists by the Weierstrass theorem.

(a) Consider the solution to the MHE problem at time T , $( \hat { x } ( T - N | T ) , \hat { \mathbf { w } } _ { T } )$ . We have that

$$\hat {V} _ {T} ^ {0} = \Gamma_ {T - N} (\hat {\boldsymbol {x}} (T - N | T)) + \sum_ {i = T - N} ^ {T - 1} \ell_ {i} (\hat {\boldsymbol {w}} (i | T), \hat {\boldsymbol {v}} (i | T))$$

From (4.21) we have

$$\Gamma_ {T - N} (\hat {x} (T - N | T)) \geq \hat {V} _ {T - N} ^ {0} + \underline {{\gamma}} _ {p} (| \hat {x} (T - N | T) - \hat {x} (T - N | T - N) |)$$

Using this inequality in the previous equation we have

$$
\begin{array}{l} \hat {V} _ {T} ^ {0} \geq \hat {V} _ {T - N} ^ {0} + \underline {{\gamma}} _ {p} (| \hat {x} (T - N | T) - \hat {x} (T - N | T - N) |) + \\ \sum_ {i = T - N} ^ {T - 1} \ell_ {i} (\hat {w} (i | T), \hat {v} (i | T)) \tag {4.24} \\ \end{array}
$$

and we have established that the sequence $\{ \hat { V } _ { T + i N } ^ { 0 } \}$ is a nondecreasing sequenfor all $i = 1 , 2 , \dots$ $T \geq 1$ . Sinces as $\hat { V } _ { k } ^ { 0 }$ bounde for any $k \geq 1$ $\hat { V } _ { T + i N } ^ { 0 }$ $i  \infty$ $T \geq 1$ $T \to \infty$

$$\underline {{\gamma}} _ {p} \big ( | \hat {x} (T - N | T) - \hat {x} (T - N | T - N) | \big) \to 0 \tag {4.25}\sum_ {i = T - N} ^ {T - 1} \ell_ {i} (\hat {w} (i | T), \hat {v} (i | T)) \rightarrow 0 \tag {4.26}$$
