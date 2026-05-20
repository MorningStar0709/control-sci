# Exercise 1.12: Partitioned matrix inversion lemma

Let matrix Z be partitioned into

$$
Z = \left[ \begin{array}{c c} B & C \\ D & E \end{array} \right]
$$

and assume $Z ^ { - 1 } , B ^ { - 1 }$ and $E ^ { - 1 }$ exist.

(a) Perform row elimination and show that

$$
Z ^ {- 1} = \left[ \begin{array}{c c} B ^ {- 1} + B ^ {- 1} C (E - D B ^ {- 1} C) ^ {- 1} D B ^ {- 1} & - B ^ {- 1} C (E - D B ^ {- 1} C) ^ {- 1} \\ - (E - D B ^ {- 1} C) ^ {- 1} D B ^ {- 1} & (E - D B ^ {- 1} C) ^ {- 1} \end{array} \right]
$$

Note that this result is still valid if E is singular.

(b) Perform column elimination and show that

$$
Z ^ {- 1} = \left[ \begin{array}{c c} (B - C E ^ {- 1} D) ^ {- 1} & - (B - C E ^ {- 1} D) ^ {- 1} C E ^ {- 1} \\ - E ^ {- 1} D (B - C E ^ {- 1} D) ^ {- 1} & E ^ {- 1} + E ^ {- 1} D (B - C E ^ {- 1} D) ^ {- 1} C E ^ {- 1} \end{array} \right]
$$

Note that this result is still valid if B is singular.

(c) A host of other useful control-related inversion formulas follow from these results. Equate the (1,1) or (2,2) entries of $Z ^ { - 1 }$ and derive the identity

$$(A + B C D) ^ {- 1} = A ^ {- 1} - A ^ {- 1} B (D A ^ {- 1} B + C ^ {- 1}) ^ {- 1} D A ^ {- 1} \tag {1.55}$$

A useful special case of this result is

$$(I + X ^ {- 1}) ^ {- 1} = I - (I + X) ^ {- 1}$$

(d) Equate the (1,2) or (2,1) entries of $Z ^ { - 1 }$ and derive the identity

$$(A + B C D) ^ {- 1} B C = A ^ {- 1} B (D A ^ {- 1} B + C ^ {- 1}) ^ {- 1} \tag {1.56}$$

Equations (1.55) and (1.56) prove especially useful in rearranging formulas in least squares estimation.
