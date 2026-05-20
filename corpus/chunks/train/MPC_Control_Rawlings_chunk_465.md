# 4.3.2 Nonzero Prior Weighting

The two drawbacks of zero prior weighting are: the system had to be assumed observable rather than detectable to ensure existence of the solution to the MHE problem; and a large horizon N may be required to obtain performance comparable to full information estimation. We address these two disadvantages by using nonzero prior weighting. To get started, we use forward DP, as we did in Chapter 1 for the unconstrained linear case, to decompose the full information problem exactly into the MHE problem (4.14) in which Γ (·) is chosen as arrival cost.

Definition 4.14 (Full information arrival cost). The full information arrival cost is defined as

$$Z _ {T} (\boldsymbol {p}) = \min _ {\chi (0), \boldsymbol {\omega}} V _ {T} (\chi (0), \boldsymbol {\omega}) \tag {4.18}$$

subject to

$$\chi^ {+} = f (\chi , \omega) \quad y = h (\chi) + v \quad \chi (T; \chi (0), \boldsymbol {\omega}) = p$$

We have the following equivalence.

Lemma 4.15 (MHE and full information estimation). The MHE problem (4.14) is equivalent to the full information problem (4.3) for the choice $\Gamma _ { k } ( \cdot ) = Z _ { k } ( \cdot )$ for all $k > N$ and $N \geq 1$ .

The proof is left as an exercise. This lemma is the essential insight provided by the DP recursion. But notice that evaluating arrival cost in (4.18) has the same computational complexity as solving a full information problem. So next we generate an MHE problem that has simpler computational requirements, but retains the excellent stability properties of full information estimation. We proceed as follows.

Definition 4.16 (MHE arrival cost). The MHE arrival cost $\hat { Z } ( \cdot )$ is defined for $T > N$ as

$$
\begin{array}{l} \hat {Z} _ {T} (\boldsymbol {p}) = \min _ {\boldsymbol {z}, \boldsymbol {\omega}} \hat {V} _ {T} (\boldsymbol {z}, \boldsymbol {\omega}) \\ = \min _ {z, \omega} \Gamma_ {T - N} (z) + \sum_ {i = T - N} ^ {T - 1} \ell_ {i} (\omega (i), \nu (i)) \tag {4.19} \\ \end{array}
$$

subject to

$$\chi^ {+} = f (\chi , \omega) \qquad y = h (\chi) + \nu \qquad \chi (T; z, T - N, \pmb {\omega}) = p$$

For $T \leq N$ we usually define the MHE problem to be the full information problem, so $\hat { Z } _ { T } ( \cdot ) = Z _ { T } ( \cdot )$ and $\hat { V } _ { T } ^ { 0 } = V _ { T } ^ { 0 }$ . Notice from the second equality in the definition that the MHE arrival cost at T is defined in terms of the prior weighting at time $T - N$ .
