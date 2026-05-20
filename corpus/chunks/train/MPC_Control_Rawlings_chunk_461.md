# 4.3.1 Zero Prior Weighting

Here we discount the early data completely and choose $\Gamma _ { i } ( \cdot ) = 0$ for all $i \geq N$ . Because it discounts the past data completely, this form of MHE must be able to asymptotically reconstruct the state using only the most recent N measurements. The first issue is establishing existence of the solution. Unlike the full information problem, in which the positive definite initial penalty guarantees that the optimization takes place over a bounded (compact) set, here there is zero initial penalty. So we must restrict the system further than i-IOSS to ensure solution existence. We show next that observability is sufficient for this purpose.

Definition 4.11 (Observability). The system $x ^ { + } = f ( x , w ) , y = h ( x )$ is observable if there exist finite $N _ { 0 } \in \mathbb { I } _ { \ge 1 } , \gamma _ { 1 } ( \cdot ) , \gamma _ { 2 } ( \cdot ) \in \mathcal { K }$ such that for every two initial states $z _ { 1 }$ and $z _ { 2 }$ , and any two disturbance sequences $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 }$ , and all $k \geq N _ { 0 }$

$$\left| z _ {1} - z _ {2} \right| \leq \gamma_ {1} \left(\left\| \mathbf {w} _ {1} - \mathbf {w} _ {2} \right\| _ {0: k - 1}\right) + \gamma_ {2} \left(\left| \left| \mathbf {y} _ {z _ {1}, \mathbf {w} _ {1}} - \mathbf {y} _ {z _ {2}, \mathbf {w} _ {2}} \right| \right| _ {0: k}\right)$$

At any time $T \geq N$ consider decision variables $\chi ( T - N ) = x ( T - N )$ and $\boldsymbol { \omega } ( i ) = \boldsymbol { w } ( i )$ for $T - N \leq i \leq T - 1$ . For these decision variables the cost function has the value

$$\hat {V} _ {T} (\chi (T - N), \boldsymbol {\omega}) = \sum_ {i = T - N} ^ {T - 1} \ell_ {i} (\boldsymbol {w} (i), \boldsymbol {v} (i)) \tag {4.15}$$

which is less than $V _ { \infty }$ defined in the full information problem. Observability then ensures that for all $k \geq N \geq N _ { 0 }$

$$\left| x (k - N) - \hat {x} (k - N | k) \right| \leq \gamma_ {2} \left(\left\| \mathbf {v} \right\| _ {k - N: k}\right)$$

Since $\nu ( k )$ is bounded for all $k \geq 0$ by Assumption 4.3, observability has bounded the distance between the initial estimate in the horizon and the system state for all $k \geq N$ . That along with continuity of $\hat { V } _ { T } ( \chi , \pmb { \omega } )$ ensures existence of the solution to the MHE problem by the Weierstrass theorem (Proposition A.7). But the solution does not have to be unique.
