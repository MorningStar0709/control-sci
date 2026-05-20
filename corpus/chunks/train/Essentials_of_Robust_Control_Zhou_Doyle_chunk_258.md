$$\boldsymbol {\Delta} = \left\{\operatorname{diag} \left[ \delta_ {1} I _ {r _ {1}}, \dots , \delta_ {s} I _ {r _ {S}}, \Delta_ {1}, \dots , \Delta_ {F} \right]: \delta_ {i} \in \mathbb {C}, \Delta_ {j} \in \mathbb {C} ^ {m _ {j} \times m _ {j}} \right\}. \tag {10.1}$$

For consistency among all the dimensions, we must have

$$\sum_ {i = 1} ^ {S} r _ {i} + \sum_ {j = 1} ^ {F} m _ {j} = n.$$

Often, we will need norm-bounded subsets of $\Delta ,$ , and we introduce the following notation:

$$\mathbf {B} \boldsymbol {\Delta} = \{\Delta \in \boldsymbol {\Delta}: \overline {{\sigma}} (\Delta) \leq 1 \} \tag {10.2}\mathbf {B} ^ {\mathrm{o}} \boldsymbol {\Delta} = \{\Delta \in \boldsymbol {\Delta}: \overline {{\sigma}} (\Delta) < 1 \} \tag {10.3}$$

where the superscript $^ { 6 } \mathrm { O } ^ { 7 }$ symbolizes the open ball. To keep the notation as simple as possible in equation (10.1), we place all of the repeated scalar blocks first; in actuality, they can come in any order. Also, the full blocks do not have to be square, but restricting them as such saves a great deal in terms of notation.

Now we ask a similar question: Given a matrix $M \in \mathbb { C } ^ { p \times q }$ , what is the smallest perturbation matrix $\Delta \in \Delta$ in the sense of $\overline { { \sigma } } ( \Delta )$ such that

$$\det (I - M \Delta) = 0?$$

That is, we are interested in finding

$$\alpha_ {\min} := \inf \left\{\overline {{\sigma}} (\Delta): \det (I - M \Delta) = 0, \Delta \in \boldsymbol {\Delta} \right\}.$$

Again we have

$$\alpha_ {\min} = \inf \left\{\alpha : \det (I - \alpha M \Delta) = 0, \Delta \in \mathbf {B} \boldsymbol {\Delta} \right\} = \frac {1}{\max _ {\Delta \in \mathbf {B} \boldsymbol {\Delta}} \rho (M \Delta)}.$$

Similar to the unstructured case, we shall call $1 / \alpha _ { \mathrm { m i n } }$ the structured singular value and denote it by $\mu _ { \Delta } ( M )$ .

Definition 10.1 For $M \in \mathbb { C } ^ { n \times n } , \mu _ { \Delta } ( M )$ is defined as

$$\mu_ {\boldsymbol {\Delta}} (M) := \frac {1}{\min \left\{\overline {{\sigma}} (\Delta) : \Delta \in \boldsymbol {\Delta} , \det (I - M \Delta) = 0 \right\}} \tag {10.4}$$

unless no $\Delta \in \Delta$ makes $I - M \Delta$ singular, in which case $\mu _ { \Delta } ( M ) : = 0$ .
