$$
\begin{array}{l} \delta J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial \mathcal {L}}{\partial x _ {1}}\right) _ {*} \delta x _ {1} (t) + \left(\frac {\partial \mathcal {L}}{\partial x _ {2}}\right) _ {*} \delta x _ {2} (t) \right] d t \\ + \left. \left[ \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \delta x _ {1} (t) \right] \right| _ {t _ {0}} ^ {t _ {f}} + \left. \left[ \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {2}}\right) _ {*} \delta x _ {2} (t) \right] \right| _ {t _ {0}} ^ {t _ {f}} \\ - \int_ {t _ {0}} ^ {t _ {f}} \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \delta x _ {1} (t) d t - \int_ {t _ {0}} ^ {t _ {f}} \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {2}}\right) _ {*} \delta x _ {2} (t) d t. \tag {2.6.9} \\ \end{array}
$$

Since this is a fixed-final time and fixed-final state problem as given by $(2.6.3)$ , no variations are allowed at the final point. This means

$$\delta x _ {1} (t _ {0}) = \delta x _ {2} (t _ {0}) = \delta x _ {1} (t _ {f}) = \delta x _ {2} (t _ {f}) = 0. \tag {2.6.10}$$

Using the boundary variations (2.6.10) in the augmented first variation (2.6.9), we have

$$
\begin{array}{l} \delta J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial \mathcal {L}}{\partial x _ {1}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \right] \delta x _ {1} (t) d t \\ + \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial \mathcal {L}}{\partial x _ {2}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {2}}\right) _ {*} \right] \delta x _ {2} (t) d t. \tag {2.6.11} \\ \end{array}
$$

\- Step 4: Fundamental Theorem: Now, we proceed as follows.

1. We invoke the fundamental theorem of the calculus of variations (Theorem 2.1) and make the first variation (2.6.11) equal to zero.

2. Remembering that both $\delta x_{1}(t)$ and $\delta x_{2}(t)$ are not independent, because $x_{1}(t)$ and $x_{2}(t)$ are related by the condition (2.6.2), we choose $\delta x_{2}(t)$ as the independent variation and $\delta x_{1}(t)$ as the dependent variation.

3. Let us choose the multiplier $\lambda^{*}(t)$ which is arbitrarily introduced and is at our disposal, in such a way that the coefficient of the dependent variation $\delta x_{1}(t)$ in (2.6.11) vanish. That is
