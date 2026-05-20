Proof. The necessity is obvious. To prove the sufficiency, it is sufficient to show that $( I - P \hat { K } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ . But this follows from

$$(I - P \hat {K}) ^ {- 1} = I + (I - P \hat {K}) ^ {- 1} P \hat {K}$$

and $( I - P \hat { K } ) ^ { - 1 } P , \ \hat { K } \in \mathcal { R } \mathcal { H } _ { \infty }$ .

Also, we have the following:

Corollary 5.3 Suppose $P \in \mathcal { R } \mathcal { H } _ { \infty }$ . Then the system in Figure 5.2 is internally stable $i f$ and only if it is well-posed and $\hat { K } ( I - P \hat { K } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ .

Corollary 5.4 Suppose $P \in \mathcal { R } \mathcal { H } _ { \infty }$ and $\hat { K } \in \mathcal { R } \mathcal { H } _ { \infty }$ . Then the system in Figure $5 . 2$ is internally stable if and only if $( I - P \hat { K } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ , or, equivalently, det $( I - P ( s ) \hat { K } ( s ) )$ has no zeros in the closed right-half plane.

Note that all the previous discussions and conclusions apply equally to infinite dimensional plants and controllers. To study the more general case, we shall limit our discussions to finite dimensional systems and define

$$n _ {k} := \text { number of open right - half plane (rhp) poles of } \hat {K} (s)n _ {p} := \text { number of open right - half plane (rhp) poles of } P (s).$$

Theorem 5.5 The system is internally stable $i f$ and only if it is well-posed and

(i) the number of open rhp poles of $P ( s ) \hat { K } ( s ) = n _ { k } + n _ { p } ;$

(ii) $( I - P ( s ) \hat { K } ( s ) ) ^ { - 1 }$ is stable.

Proof. It is easy to show that $P \hat { K }$ and $( I - P \hat { K } ) ^ { - 1 }$ have the following realizations:

$$
P \hat {K} = \left[ \begin{array}{c c c} A & B \hat {C} & B \hat {D} \\ 0 & \hat {A} & \hat {B} \\ \hline C & D \hat {C} & D \hat {D} \end{array} \right], (I - P \hat {K}) ^ {- 1} = \left[ \begin{array}{c c} \bar {A} & \bar {B} \\ \hline \bar {C} & \bar {D} \end{array} \right]
$$

where

$$
\bar {A} = \left[ \begin{array}{c c} A & B \hat {C} \\ 0 & \hat {A} \end{array} \right] + \left[ \begin{array}{c} B \hat {D} \\ \hat {B} \end{array} \right] (I - D \hat {D}) ^ {- 1} \left[ \begin{array}{c c} C & D \hat {C} \end{array} \right]

\bar {B} = \left[ \begin{array}{c} B \hat {D} \\ \hat {B} \end{array} \right] (I - D \hat {D}) ^ {- 1}

\bar {C} = (I - D \hat {D}) ^ {- 1} \left[ \begin{array}{c c} C & D \hat {C} \end{array} \right]
\bar {D} = (I - D \hat {D}) ^ {- 1}.
$$

Hence, the system is internally stable iff $\bar { A }$ is stable. (see Problem 5.2.)
