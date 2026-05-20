# B.2 Matrix-Inversion Lemma

The following lemma is used in Sec. 13.5 to invert a matrix.

LEMMA B.1 MATRIX-INVERSION LEMMA Let A, C, and $C^{-1} + DA^{-1}B$ be nonsingular square matrices; then

$$(A + B C D) ^ {- 1} = A ^ {- 1} - A ^ {- 1} B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1}$$

Proof. By direct substitution,

$$
\begin{array}{l} (A + B C D) \left(A ^ {- 1} - A ^ {- 1} B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1}\right) \\ = I + B C D A ^ {- 1} - B \left(C ^ {- 1} + D A ^ {- 1} B\right) ^ {- 1} D A ^ {- 1} \\ - B C D A ^ {- 1} B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1} \\ = I + B C D A ^ {- 1} - B C \left(C ^ {- 1} + D A ^ {- 1} B\right) \left(C ^ {- 1} + D A ^ {- 1} B\right) ^ {- 1} D A ^ {- 1} \\ = I + B C D A ^ {- 1} - B C D A ^ {- 1} = I \\ \end{array}
$$
