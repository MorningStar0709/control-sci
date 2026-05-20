# 10.3.4 Approximation of Multiple Full Block $\mu$

The approximations given in the last subsection can be generalized to the multiple-block $\mu$ problem by assuming that M is partitioned consistently with the structure of

$$\Delta = \operatorname{diag} (\Delta_ {1}, \Delta_ {2}, \dots , \Delta_ {F})$$

so that

$$
M = \left[ \begin{array}{c c c c} M _ {1 1} & M _ {1 2} & \dots & M _ {1 F} \\ M _ {2 1} & M _ {2 2} & \dots & M _ {2 F} \\ \vdots & \vdots & & \vdots \\ M _ {F 1} & M _ {F 2} & \dots & M _ {F F} \end{array} \right]
$$

and

$$D = \operatorname{diag} (d _ {1} I, \dots , d _ {F - 1} I, I).$$

Now

$$D M D ^ {- 1} = \left[ M _ {i j} \frac {d _ {i}}{d _ {j}} \right], d _ {F} := 1.$$

Hence

$$
\begin{array}{l} \mu_ {\mathbf {\Delta}} (M) \leq \inf _ {D \in \mathcal {D}} \overline {{\sigma}} (D M D ^ {- 1}) = \inf _ {D \in \mathcal {D}} \overline {{\sigma}} \left[ M _ {i j} \frac {d _ {i}}{d _ {j}} \right] \\ \leq \inf _ {D \in \mathcal {D}} \overline {{\sigma}} \left[ \| M _ {i j} \| \frac {d _ {i}}{d _ {j}} \right] \leq \inf _ {D \in \mathcal {D}} \sqrt {\sum_ {i = 1} ^ {F} \sum_ {j = 1} ^ {F} \| M _ {i j} \| ^ {2} \frac {d _ {i} ^ {2}}{d _ {j} ^ {2}}} \\ \leq \inf _ {D \in \mathcal {D}} \sqrt {\sum_ {i = 1} ^ {F} \sum_ {j = 1} ^ {F} \| M _ {i j} \| _ {F} ^ {2} \frac {d _ {i} ^ {2}}{d _ {j} ^ {2}}}. \\ \end{array}
$$

An approximate D can be found by solving the following minimization problem:

$$\inf _ {D \in \mathcal {D}} \sum_ {i = 1} ^ {F} \sum_ {j = 1} ^ {F} \| M _ {i j} \| ^ {2} \frac {d _ {i} ^ {2}}{d _ {j} ^ {2}}$$

or, more conveniently, by minimizing

$$\inf _ {D \in \mathcal {D}} \sum_ {i = 1} ^ {F} \sum_ {j = 1} ^ {F} \| M _ {i j} \| _ {F} ^ {2} \frac {d _ {i} ^ {2}}{d _ {j} ^ {2}}$$

with $d _ { F } = 1$ . The optimal $d _ { i }$ minimizing the preceding two problems satisfies, respectively,

$$d _ {k} ^ {4} = \frac {\sum_ {i \neq k} \| M _ {i k} \| ^ {2} d _ {i} ^ {2}}{\sum_ {j \neq k} \| M _ {k j} \| ^ {2} / d _ {j} ^ {2}}, \quad k = 1, 2, \dots , F - 1 \tag {10.29}$$

and

$$d _ {k} ^ {4} = \frac {\sum_ {i \neq k} \| M _ {i k} \| _ {F} ^ {2} d _ {i} ^ {2}}{\sum_ {j \neq k} \| M _ {k j} \| _ {F} ^ {2} / d _ {j} ^ {2}}, k = 1, 2, \dots , F - 1. \tag {10.30}$$

Using these relations, $d _ { k }$ can be obtained by iterations.

Example 10.7 Consider a $3 \times 3$ complex matrix

$$
M = \left[ \begin{array}{c c c} 1 + j & 1 0 - 2 j & - 2 0 j \\ 5 j & 3 + j & - 1 + 3 j \\ - 2 & j & 4 - j \end{array} \right]
$$
