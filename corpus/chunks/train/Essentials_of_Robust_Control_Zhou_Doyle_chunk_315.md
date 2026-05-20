(⇒) This is obvious since $H \in \operatorname { d o m } ( \operatorname { R i c } )$ implies that X is a stabilizing solution and that $A + R X$ is asymptotically stable. It also implies that $( A , R )$ must be stabilizable.

✷

The following result is the so-called bounded real lemma, which follows immediately from the preceding theorem.

Corollary 12.3 Let $\gamma > 0 , G ( s ) = \left[ \frac { A \mid B } { C } \right] \in \mathcal { R H } _ { \infty } ,$ , and

$$
H := \left[ \begin{array}{c c} A + B R ^ {- 1} D ^ {*} C & B R ^ {- 1} B ^ {*} \\ - C ^ {*} (I + D R ^ {- 1} D ^ {*}) C & - (A + B R ^ {- 1} D ^ {*} C) ^ {*} \end{array} \right]
$$

where $R = \gamma ^ { 2 } I - D ^ { * } D$ . Then the following conditions are equivalent:

(i) $\| G \| _ { \infty } < \gamma .$   
(ii) $\bar { \sigma } ( D ) < \gamma$ and H has no eigenvalues on the imaginary axis.   
(iii) $\bar { \sigma } ( D ) < \gamma$ and $H \in \operatorname { d o m } ( \operatorname { R i c } )$ .   
(iv) $\bar { \sigma } ( D ) < \gamma$ and $H \in \operatorname { d o m } ( \operatorname { R i c } )$ and $\operatorname { R i c } ( H ) \geq 0 \ ( \operatorname { R i c } ( H ) > 0 \ i f ( C , A )$ is $o b s e r v a b l e )$   
(v) $\bar { \sigma } ( D ) < \gamma$ and there exists an $X = X ^ { * } \geq 0$ such that

$$X (A + B R ^ {- 1} D ^ {*} C) + (A + B R ^ {- 1} D ^ {*} C) ^ {*} X + X B R ^ {- 1} B ^ {*} X + C ^ {*} (I + D R ^ {- 1} D ^ {*}) C = 0$$

and $A + B R ^ { - 1 } D ^ { * } C + B R ^ { - 1 } B ^ { * } X$ has no eigenvalues on the imaginary axis.

(vi) $\bar { \sigma } ( D ) < \gamma$ and there exists an $X = X ^ { * } > 0$ such that

$$X (A + B R ^ {- 1} D ^ {*} C) + (A + B R ^ {- 1} D ^ {*} C) ^ {*} X + X B R ^ {- 1} B ^ {*} X + C ^ {*} (I + D R ^ {- 1} D ^ {*}) C < 0.$$

(vii) There exists an $X = X ^ { * } > 0$ such that

$$
\left[ \begin{array}{c c c} X A + A ^ {*} X & X B & C ^ {*} \\ B ^ {*} X & - \gamma I & D ^ {*} \\ C & D & - \gamma I \end{array} \right] <   0.
$$

Proof. The equivalence between (i) and (ii) has been shown in Chapter 4. The equivalence between (iii) and (iv) is obvious by noting the fact that $A + B R ^ { - 1 } D ^ { * } C$ is stable if $\| G \| _ { \infty } < \gamma$ (See Problem 12.15). The equivalence between (ii) and (iii) follows from the preceding theorem. It is also obvious that (iv) implies (v). We shall now show that (v) implies (i). Thus suppose that there is an $X \geq 0$ such that

$$X (A + B R ^ {- 1} D ^ {*} C) + (A + B R ^ {- 1} D ^ {*} C) ^ {*} X + X B R ^ {- 1} B ^ {*} X + C ^ {*} (I + D R ^ {- 1} D ^ {*}) C = 0$$

and $A + B R ^ { - 1 } ( B ^ { * } X + D ^ { * } C )$ has no eigenvalues on the imaginary axis. Then

$$
W (s) := \left[ \begin{array}{c c} A & - B \\ \hline B ^ {*} X + D ^ {*} C & R \end{array} \right]
$$

has no zeros on the imaginary axis since
