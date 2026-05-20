# 11.1 Existence of Stabilizing Controllers

Consider a system described by the standard block diagram in Figure 11.1. Assume that $G ( s )$ has a stabilizable and detectable realization of the form

$$
G (s) = \left[ \begin{array}{l l} G _ {1 1} (s) & G _ {1 2} (s) \\ G _ {2 1} (s) & G _ {2 2} (s) \end{array} \right] = \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & D _ {1 1} & D _ {1 2} \\ C _ {2} & D _ {2 1} & D _ {2 2} \end{array} \right]. \tag {11.1}
$$

The stabilization problem is to find feedback mapping K such that the closed-loop system is internally stable; the well-posedness is required for this interconnection.

Definition 11.1 A proper system G is said to be stabilizable through output feedback if there exists a proper controller K internally stabilizing G in Figure 11.1. Moreover, a proper controller $K ( s )$ is said to be admissible if it internally stabilizes G.

The following result is standard and follows from Chapter 3.

Lemma 11.1 There exists a proper K achieving internal stability $i f f \left( A , B _ { 2 } \right)$ is stabilizable and $( C _ { 2 } , A )$ is detectable. Further, let $F$ and L be such that $A + B _ { 2 } F$ and $A + L C _ { 2 }$ are stable; then an observer-based stabilizing controller is given by

$$
K (s) = \left[ \begin{array}{c c} A + B _ {2} F + L C _ {2} + L D _ {2 2} F & - L \\ \hline F & 0 \end{array} \right].
$$

Proof. (⇐) By the stabilizability and detectability assumptions, there exist F and L such that $A + B _ { 2 } F$ and $A + L C _ { 2 }$ are stable. Now let $K ( s )$ be the observer-based controller given in the lemma, then the closed-loop A matrix is given by

$$
\tilde {A} = \left[ \begin{array}{c c} A & B _ {2} F \\ - L C _ {2} & A + B _ {2} F + L C _ {2} \end{array} \right].
$$

It is easy to check that this matrix is similar to the matrix

$$
\left[ \begin{array}{c c} A + L C _ {2} & 0 \\ - L C _ {2} & A + B _ {2} F \end{array} \right].
$$

Thus the spectrum of $\tilde { A }$ equals the union of the spectra of $A + L C _ { 2 }$ and $A + B _ { 2 } F$ . In particular, A˜ is stable.

(⇒) If $( A , B _ { 2 } )$ is not stabilizable or if $( C _ { 2 } , A )$ is not detectable, then there are some eigenvalues of A˜ that are fixed in the right-half plane, no matter what the compensator is. The details are left as an exercise. ✷

The stabilizability and detectability conditions of $( A , B _ { 2 } , C _ { 2 } )$ are assumed throughout the remainder of this chapter.1 It follows that the realization for $G _ { 2 2 }$ is stabilizable and detectable, and these assumptions are enough to yield the following result.
