# A.6 Partitioned Matrix Inversion Theorem

Let matrix Z be partitioned into

$$
Z = \left[ \begin{array}{c c} B & C \\ D & E \end{array} \right]
$$

and assume $Z ^ { - 1 } , B ^ { - 1 }$ and $E ^ { - 1 }$ exist. Performing row elimination gives

$$
Z ^ {- 1} = \left[ \begin{array}{c c} B ^ {- 1} + B ^ {- 1} C (E - D B ^ {- 1} C) ^ {- 1} D B ^ {- 1} & - B ^ {- 1} C (E - D B ^ {- 1} C) ^ {- 1} \\ - (E - D B ^ {- 1} C) ^ {- 1} D B ^ {- 1} & (E - D B ^ {- 1} C) ^ {- 1} \end{array} \right]
$$

Note that this result is still valid if E is singular. Performing column elimination gives

$$
Z ^ {- 1} = \left[ \begin{array}{c c} (B - C E ^ {- 1} D) ^ {- 1} & - (B - C E ^ {- 1} D) ^ {- 1} C E ^ {- 1} \\ - E ^ {- 1} D (B - C E ^ {- 1} D) ^ {- 1} & E ^ {- 1} + E ^ {- 1} D (B - C E ^ {- 1} D) ^ {- 1} C E ^ {- 1} \end{array} \right]
$$

Note that this result is still valid if B is singular. A host of other useful control-related inversion formulas follow from these results. Equating the (1,1) or (2,2) entries of $Z ^ { - 1 }$ gives the identity

$$(A + B C D) ^ {- 1} = A ^ {- 1} - A ^ {- 1} B (D A ^ {- 1} B + C ^ {- 1}) ^ {- 1} D A ^ {- 1}$$

A useful special case of this result is

$$(I + X ^ {- 1}) ^ {- 1} = I - (I + X) ^ {- 1}$$

Equating the (1,2) or (2,1) entries of $Z ^ { - 1 }$ gives the identity

$$(A + B C D) ^ {- 1} B C = A ^ {- 1} B (D A ^ {- 1} B + C ^ {- 1}) ^ {- 1}$$

Determinants. We require some results on determinants of partitioned matrices when using normal distributions in the discussion of probability. If E is nonsingular

$$\det (A) = \det (E) \det (B - C E ^ {- 1} D)$$

If B is nonsingular

$$\det (A) = \det (B) \det (E - D B ^ {- 1} C)$$
