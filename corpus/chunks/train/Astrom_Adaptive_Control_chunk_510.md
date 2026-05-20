# Certainty Equivalence Control

When the parameters $x(t + 1)$ are not known, it can be tempting to replace Eq. (7.12) with

$$u (t) = \frac {u _ {c} (t + 1) - \bar {\varphi} ^ {T} (t) \hat {x} (t + 1)}{\hat {b} _ {0} (t + 1)} \tag {7.13}$$

The true parameter values are replaced by the expected values, given $Y_{t}$ . The controller of Eq. (7.13) is called the certainty equivalence controller. Certainty equivalence control is the strategy used in the self-tuning regulators in Chapters 3 and 4 and in the model-reference adaptive systems in Chapter 5. In these controllers it was also necessary to ensure that $\hat{b}_{0} \neq 0$ .
