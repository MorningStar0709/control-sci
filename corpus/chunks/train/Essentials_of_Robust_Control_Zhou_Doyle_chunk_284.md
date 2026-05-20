$$
\left[ \begin{array}{c c} - w _ {t} \tau I & - w _ {t} \tau (d \Sigma) ^ {- 1} \\ w _ {s} \varepsilon d \Sigma & w _ {s} \varepsilon I \end{array} \right] = P _ {1} \mathrm{diag} (M _ {1}, M _ {2}, \ldots , M _ {m}) P _ {2}
$$

where $P _ { 1 }$ and $P _ { 2 }$ are permutation matrices and where

$$
M _ {i} = \left[ \begin{array}{c c} - w _ {t} \tau & - w _ {t} \tau (d \sigma_ {i}) ^ {- 1} \\ w _ {s} \varepsilon d \sigma_ {i} & w _ {s} \varepsilon \end{array} \right].
$$

Hence

$$
\begin{array}{l} \mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \inf _ {d \in \mathbb {R} _ {+}} \max _ {i} \overline {{\sigma}} \left(\left[ \begin{array}{c c} - w _ {t} \tau & - w _ {t} \tau (d \sigma_ {i}) ^ {- 1} \\ w _ {s} \varepsilon d \sigma_ {i} & w _ {s} \varepsilon \end{array} \right]\right) \\ = \inf _ {d \in \mathbb {R} _ {+}} \max _ {i} \overline {{\sigma}} \left(\left[ \begin{array}{c} - w _ {t} \tau \\ w _ {s} \varepsilon d \sigma_ {i} \end{array} \right] \left[ \begin{array}{c c} 1 & (d \sigma_ {i}) ^ {- 1} \end{array} \right]\right) \\ = \inf _ {d \in \mathbb {R} _ {+}} \max _ {i} \sqrt {(1 + | d \sigma_ {i} | ^ {- 2}) (| w _ {s} \varepsilon d \sigma_ {i} | ^ {2} + | w _ {t} \tau | ^ {2})} \\ = \inf _ {d \in \mathbb {R} _ {+}} \max _ {i} \sqrt {| w _ {s} \varepsilon | ^ {2} + | w _ {t} \tau | ^ {2} + | w _ {s} \varepsilon d \sigma_ {i} | ^ {2} + \left| \frac {w _ {t} \tau}{d \sigma_ {i}} \right| ^ {2}}. \\ \end{array}
$$

Using Lemma 10.9, it is easy to show that the maximum is achieved at either $\overline { { \sigma } }$ or σ and that optimal d is given by

$$d ^ {2} = \frac {| w _ {t} \tau |}{| w _ {s} \varepsilon | \underline {{\sigma}} \overline {{\sigma}}},$$

so the structured singular value is

$$\mu_ {\Delta} (G (j \omega)) = \sqrt {| w _ {s} \varepsilon | ^ {2} + | w _ {t} \tau | ^ {2} + | w _ {s} \varepsilon | | w _ {t} \tau | [ \kappa (P) + \frac {1}{\kappa (P)} ]}. \tag {10.27}$$

Note that if $\vert w _ { s } \varepsilon \vert$ and $| w _ { t } \tau |$ are not too large, which is guaranteed if the nominal performance and robust stability conditions are satisfied, then the structured singular value is proportional to the square root of the plant condition number:

$$\mu_ {\Delta} (G (j \omega)) \approx \sqrt {| w _ {s} \varepsilon | | w _ {t} \tau | \kappa (P)}. \tag {10.28}$$

This confirms our intuition that an ill-conditioned plant with skewed specifications is hard to control.
