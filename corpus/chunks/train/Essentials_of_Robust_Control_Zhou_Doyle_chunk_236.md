The converse also holds if M satisfies certain conditions.

Lemma 9.2 Let $\mathcal { F } _ { \ell } ( M , Q )$ be a given LFT with $M = \left[ \begin{array} { c c } { { M _ { 1 1 } } } & { { M _ { 1 2 } } } \\ { { M _ { 2 1 } } } & { { M _ { 2 2 } } } \end{array} \right]$ .

(a) $I f M _ { 1 2 }$ is invertible, then

$$\mathcal {F} _ {\ell} (M, Q) = (C + Q D) ^ {- 1} (A + Q B)$$

with $A = M _ { 1 2 } ^ { - 1 } M _ { 1 1 } , \ B = M _ { 2 1 } - M _ { 2 2 } M _ { 1 2 } ^ { - 1 } M _ { 1 1 } , \ C = M _ { 1 2 } ^ { - 1 } , \ a n d \ D = - M _ { 2 2 } M _ { 1 2 } ^ { - 1 } M _ { 1 2 } , \ C = M _ { 2 2 } ^ { - 1 } , \ a n d \ D = - M _ { 2 2 } M _ { 1 2 } ^ { - 1 } M _ { 1 2 } .$ that is,

$$
\begin{array}{l} \left[ \begin{array}{c c} A & C \\ B & D \end{array} \right] = \mathcal {F} _ {\ell} \left(\left[ \begin{array}{c c c} 0 & 0 & - I \\ M _ {2 1} & 0 & M _ {2 2} \\ \hdashline M _ {1 1} & I & 0 \end{array} \right], - M _ {1 2} ^ {- 1}\right) \\ = \mathcal {F} _ {\ell} \left(\left[ \begin{array}{c c c} 0 & 0 & - I \\ M _ {2 1} & 0 & M _ {2 2} \\ \hdashline M _ {1 1} & I & M _ {1 2} + E \end{array} \right], E ^ {- 1}\right) \\ \end{array}
$$

for any nonsingular matrix E.

(b) If $M _ { 2 1 }$ is invertible, then

$$\mathcal {F} _ {\ell} (M, Q) = (A + B Q) (C + D Q) ^ {- 1}$$

with $A = M _ { 1 1 } M _ { 2 1 } ^ { - 1 } , B = M _ { 1 2 } - M _ { 1 1 } M _ { 2 1 } ^ { - 1 } M _ { 2 2 } , C = M _ { 2 1 } ^ { - 1 }$ , and $D = - M _ { 2 1 } ^ { - 1 } M _ { 2 2 }$ ; that is,

$$
\begin{array}{l} \left[ \begin{array}{c c} A & B \\ C & D \end{array} \right] = \mathcal {F} _ {\ell} \left(\left[ \begin{array}{c c c} 0 & M _ {1 2} & M _ {1 1} \\ 0 & 0 & I \\ - I & M _ {2 2} & 0 \end{array} \right], - M _ {2 1} ^ {- 1}\right) \\ = \mathcal {F} _ {\ell} \left(\left[ \begin{array}{c c c} 0 & M _ {1 2} & M _ {1 1} \\ 0 & 0 & I \\ \hdashline - I & M _ {2 2} & M _ {2 1} + E \end{array} \right], E ^ {- 1}\right) \\ \end{array}
$$

for any nonsingular matrix $E .$

However, for an arbitrary LFT $\mathcal { F } _ { \ell } ( M , Q )$ , neither $M _ { 2 1 }$ nor $M _ { 1 2 }$ is necessarily square and invertible; therefore, the alternative fractional formula is more restrictive.

It should be pointed out that some seemingly simple functions do not have simple LFT representations. For example,

$$(A + Q B) (I + Q D) ^ {- 1}$$

cannot always be written in the form of $\mathcal { F } _ { \ell } ( M , Q )$ for some $M ;$ however, it can be written as

$$(A + Q B) (I + Q D) ^ {- 1} = \mathcal {F} _ {\ell} (N, \Delta)$$

with

$$
N = \left[ \begin{array}{c c c} A & I & A \\ \hdashline - B & 0 & - B \\ D & 0 & D \end{array} \right], \quad \Delta = \left[ \begin{array}{c c} Q & \\ & Q \end{array} \right].
$$

Note that the dimension of $\Delta$ is twice of $Q .$

The following lemma shows that the inverse of an LF T is still an LFT.

Lemma 9.3 Let $M = \left[ \begin{array} { c c } { { M _ { 1 1 } } } & { { M _ { 1 2 } } } \\ { { M _ { 2 1 } } } & { { M _ { 2 2 } } } \end{array} \right]$ and $M _ { 2 2 }$ is nonsingular. Then

$$\left(\mathcal {F} _ {u} (M, \Delta)\right) ^ {- 1} = \mathcal {F} _ {u} (N, \Delta)$$

with $N _ { ; }$ , is given by

$$
N = \left[ \begin{array}{c c} M _ {1 1} - M _ {1 2} M _ {2 2} ^ {- 1} M _ {2 1} & - M _ {1 2} M _ {2 2} ^ {- 1} \\ M _ {2 2} ^ {- 1} M _ {2 1} & M _ {2 2} ^ {- 1} \end{array} \right].
$$

LFT is a very convenient tool to formulate many mathematical objects. We shall illustrate this by the following two examples.
