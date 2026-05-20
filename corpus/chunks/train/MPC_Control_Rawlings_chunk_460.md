# 4.3 Moving Horizon Estimation

As displayed in Figure 1.4 of Chapter 1, in MHE we consider only the N most recent measurements, $\mathbf { y } _ { N } ( T ) = \{ y ( T - N ) , y ( T - N + 1 ) , \ldots y ( T -$ 1)}. For $T > N$ , the MHE objective function is given by

$$\hat {V} _ {T} (\chi (T - N), \boldsymbol {\omega}) = \Gamma_ {T - N} (\chi (T - N)) + \sum_ {i = T - N} ^ {T - 1} \ell_ {i} (\omega (i), \nu (i))$$

subject to $\chi ^ { + } = f ( \chi , \omega ) , y = h ( \chi ) + \nu$ . The MHE problem is defined to be

$$\min _ {\chi (T - N), \boldsymbol {\omega}} \hat {V} _ {T} (\chi (T - N), \boldsymbol {\omega}) \tag {4.14}$$

in which $\pmb { \omega } = \{ \omega ( T - N ) , \ldots , \omega ( T - 1 ) \}$ . The designer chooses the prior weighting $\Gamma _ { k } ( \cdot )$ for $k > N$ . Until the data horizon is full, i.e., for times $T \leq N$ , we generally define the MHE problem to be the full information problem.
