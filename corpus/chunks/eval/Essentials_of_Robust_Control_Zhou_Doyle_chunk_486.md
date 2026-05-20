# 18.2 Mixed µ Analysis and Synthesis

In Chapter 10, we considered analysis and synthesis of systems with complex uncertainties. However, in practice, many systems involve parametric uncertainties that are real (for example, the uncertainty about a spring constant in a mechanical system). In this case, one has to cover this real parameter variation with a complex disk in order to use the complex $\mu$ analysis and synthesis tools, which usually results in a conservative solution. In this section, we shall consider briefly the analysis and synthesis problems with possibly both real parametric and complex uncertainties.

The mixed real and complex $\mu$ involves three types of blocks: repeated real scalar, repeated complex scalar, and full blocks. Three nonnegative integers, $S _ { r } , \ S _ { c } .$ and $F _ { ; }$ represent the number of repeated real scalar blocks, the number of repeated complex scalar blocks, and the number of full blocks, and they satisfy

$$\sum_ {i = 1} ^ {S _ {r}} k _ {i} + \sum_ {i = 1} ^ {S _ {c}} r _ {i} + \sum_ {j = 1} ^ {F} m _ {j} = n.$$

The ith repeated real scalar block is $k _ { i } \times k _ { i }$ , the jth repeated complex scalar block is $r _ { j } \times r _ { j }$ , and the \`th full block is $m _ { \ell } \times m _ { \ell }$ . The admissible set of uncertainties $\Delta \subset \mathbb { C } ^ { n \times }$ n is defined as

$$\pmb {\Delta} = \left\{\mathrm{diag} \left[ \phi_ {1} I _ {k _ {1}}, \dots , \phi_ {s _ {r}} I _ {k _ {s _ {r}}}, \delta_ {1} I _ {r _ {1}}, \dots , \delta_ {s _ {c}} I _ {r _ {s _ {c}}} \right. \right.,\left. \Delta_ {1}, \dots , \Delta_ {F} \right]: \phi_ {i} \in \mathbb {R}, \delta_ {j} \in \mathbb {C}, \Delta_ {\ell} \in \mathbb {C} ^ {m _ {\ell} \times m _ {\ell}} \}. \tag {18.1}$$

The mixed $\mu$ is defined in the same way as for the complex $\mu { : }$ Let $M \in \mathbb { C } ^ { n \times n }$ ; then

$$\mu_ {\boldsymbol {\Delta}} (M) := (\min \left\{\overline {{\sigma}} (\Delta): \Delta \in \boldsymbol {\Delta}, \det \left(I - M \Delta\right) = 0 \right\}) ^ {- 1} \tag {18.2}$$

unless no $\Delta \in \Delta$ makes $I - M \Delta$ singular, in which case $\mu _ { \Delta } ( M ) : = 0$ . Or, equivalently,

$$\frac {1}{\mu_ {\boldsymbol {\Delta}} (M)} := \inf \left\{\alpha : \det (I - \alpha M \Delta) = 0, \overline {{\sigma}} (\Delta) \leq 1, \Delta \in \boldsymbol {\Delta} \right\}.$$
