# LEMMA 2.1 Matrix inversion lemma

Let $A, C$ , and $C^{-1} + DA^{1}B$ be nonsingular square matrices. Then $A + BCD$ is invertible, and

$$(A + B C D) ^ {- 1} = A ^ {- 1} - A ^ {- 1} B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1}$$

Proof: By direct multiplication we find that

$$
\begin{array}{l} (A + B C D) \left(A ^ {- 1} - A ^ {- 1} B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1}\right) \\ = I + B C D A ^ {- 1} - B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1} \\ - B C D A ^ {- 1} B (C ^ {- 1} + D A ^ {- 1} B) ^ {- 1} D A ^ {- 1} \\ = I + B C D A ^ {- 1} - B C \left(C ^ {- 1} + D A ^ {- 1} B\right) \left(C ^ {- 1} + D A ^ {- 1} B\right) ^ {- 1} D A ^ {- 1} \\ = I \\ \end{array}
$$

Applying Lemma 2.1 to $P(t)$ and using Eq. (2.14), we get

$$
\begin{array}{l} P (t) = \left(\Phi^ {T} (t) \Phi (t)\right) ^ {- 1} = \left(\Phi^ {T} (t - 1) \Phi (t - 1) + \varphi (t) \varphi^ {T} (t)\right) ^ {- 1} \\ = (P (t - 1) ^ {- 1} + \varphi (t) \varphi^ {T} (t)) ^ {- 1} \\ = P (t - 1) - P (t - 1) \varphi (t) \left(I + \varphi^ {T} (t) P (t - 1) \varphi (t)\right) ^ {- 1} \varphi^ {T} (t) P (t - 1) \\ \end{array}
$$

This implies that

$$K (t) = P (t) \varphi (t) = P (t - 1) \varphi (t) \left(I + \varphi^ {T} (t) P (t - 1) \varphi (t)\right) ^ {- 1}$$

Notice that a matrix inversion is necessary to compute P. However, the matrix to be inverted is of the same dimension as the number of measurements. That is, for a single output system it is a scalar.

The recursive calculations are summarized in the following theorem.
