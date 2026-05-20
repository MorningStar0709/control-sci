# 10.6 Problems

Problem 10.1 Let M and N be suitably dimensioned matrices and let ∆ be a structured uncertainty. Prove or disprove

(a) $\mu _ { \Delta } ( M ) = 0 \Longrightarrow M = 0 ;$   
(b) $\mu _ { \Delta } ( M _ { 1 } + M _ { 2 } ) \leq \mu _ { \Delta } ( M _ { 1 } ) + \mu _ { \Delta } ( M _ { 2 } )$ .   
(c) $\mu _ { \Delta } ( \alpha M ) = | \alpha | \mu _ { \Delta } ( M )$ .   
(d) $\mu _ { \Delta } ( I ) = 1$ .   
(e) $\mu _ { \Delta } ( M N ) \leq \overline { { \sigma } } ( M ) \mu _ { \Delta } ( N )$ .   
(f) $\mu _ { \Delta } ( M N ) \leq { \overline { { \sigma } } } ( N ) \mu _ { \Delta } ( M )$ .

Problem 10.2 Let $\Delta = \left[ \begin{array} { c c } { { \Delta _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { \Delta _ { 2 } } } \end{array} \right]$ , where $\Delta _ { i }$ are structured uncertainties. Show that $\mu _ { \Delta } \left( \left[ \begin{array} { c c } { { M _ { 1 1 } } } & { { M _ { 1 2 } } } \\ { { 0 } } & { { M _ { 2 2 } } } \end{array} \right] \right) ^ { - } = \operatorname* { m a x } \{ \mu _ { \Delta _ { 1 } } ( M _ { 1 1 } ) , \ \mu _ { \Delta _ { 2 } } ( M _ { 2 2 } ) \}$

Problem 10.3 Matlab exercise. Let M be a $7 \times 7$ random real matrix. Take the perturbation structure to be

$$
\boldsymbol {\Delta} = \left\{\left[ \begin{array}{c c c} \delta_ {1} I _ {3} & 0 & 0 \\ 0 & \Delta_ {2} & 0 \\ 0 & 0 & \delta_ {3} I _ {2} \end{array} \right]: \delta_ {1}, \delta_ {3} \in \mathbb {C},   \Delta_ {2} \in \mathbb {C} ^ {2 \times 2} \right\}.
$$

Compute $\mu ( M )$ and a singularizing perturbation.

${ \cal M } = \left[ \begin{array} { c c } { { 0 } } & { { M _ { 1 2 } } } \\ { { M _ { 2 1 } } } & { { 0 } } \end{array} \right]$ be a complex matrix and let $\Delta = \left[ \begin{array} { c c } { { \Delta _ { 1 } } } & { { \hfil } } \\ { { \hfil } } & { { \Delta _ { 2 } } } \end{array} \right]$

Show that

$$\mu_ {\Delta} (M) = \sqrt {\overline {{\sigma}} (M _ {1 2}) \overline {{\sigma}} (M _ {2 1})}.$$

$M = \left[ \begin{array} { l l } { { M _ { 1 1 } } } & { { M _ { 1 2 } } } \\ { { M _ { 2 1 } } } & { { M _ { 2 2 } } } \end{array} \right]$ $\Delta = \left[ \begin{array} { c c } { { \Delta _ { 1 } } } & { { } } \\ { { } } & { { \Delta _ { 2 } } } \end{array} \right]$

Show that

$$
\begin{array}{l} \sqrt {\overline {{\sigma}} (M _ {1 2}) \overline {{\sigma}} (M _ {2 1})} - \max \{\overline {{\sigma}} (M _ {1 1}), \overline {{\sigma}} (M _ {2 2}) \} \leq \mu_ {\Delta} (M) \\ \leq \sqrt {\overline {{\sigma}} (M _ {1 2}) \overline {{\sigma}} (M _ {2 1})} + \max \{\overline {{\sigma}} (M _ {1 1}), \overline {{\sigma}} (M _ {2 2}) \}. \\ \end{array}
$$

Problem 10.6 Let $\Delta$ be all diagonal full blocks and M be partitioned as $M = [ M _ { i j } ]$ , where $M _ { i j }$ are matrices with suitable dimensions. Show that
