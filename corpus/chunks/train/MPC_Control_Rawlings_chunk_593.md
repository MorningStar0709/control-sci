# 5.2 A Method for Output MPC

Suppose the system to be controlled is described by

$$x ^ {+} = f (x, u, w) \tag {5.4}y = h (x, v) \tag {5.5}$$

where $x \in \mathbb { R } ^ { n } , u \in \mathbb { R } ^ { m }$ and $\boldsymbol { y } \in \mathbb { R } ^ { p }$ ; the disturbance $w$ lies in $\mathbb { R } ^ { n }$ , and the measurement noise ν lies in Rp A prime requirement for simplification is replacement of the infinite dimensional hyperstate $p _ { : }$ , which is $n ( { \hat { x } } , \Sigma )$ in the linear Gaussian case, by something considerably simpler. The hyperstate $p _ { : }$ , being a conditional density, may be regarded as a continuum of nested confidence regions, each of which is a subset of $\mathbb { R } ^ { n }$ . Our initial simplification is the replacement, if this is possible, of this continuum of confidence regions by a single region of the form {xˆ} ⊕ $\mathbb { Z } \subseteq \mathbb { R } ^ { n }$ , where $\hat { x }$ is the “center” of the confidence region and $\mathbb { \Sigma }$ now denotes a subset of $\mathbb { R } ^ { n }$ rather than a variance. If the problem is stochastic, {xˆ}⊕Σ may be a $\beta$ confidence region for p, i.e., a region satisfying Pr $\{ x \in \{ \hat { x } \} \oplus { \mathbb { \Sigma } } | I \} = \beta$ . When all disturbances are bounded, the usual assumption in robust MPC, Σ is chosen to ensure that all possible values of x lie in the set $\{ { \hat { x } } \} \oplus { \mathbb { \Sigma } }$ . The finite dimensional variable $( { \hat { x } } , { \mathbb { \Sigma } } )$ replaces the infinite dimensional object $p . { } ^ { 1 }$ In the linear time-invariant case, the state estimator (x, ˆ Σ) evolves, as shown in the sequel, according to

![](image/4e4524ce92b375c21530652d18803ec9970ee0de6c956c65e9f0bce8d7556482.jpg)

<details>
<summary>text_image</summary>

{\hat{x}(0)\} \oplus \Sigma\n\hat{x}(k)\nx_1\nx_2\nx(k)
</details>

Figure 5.1: State estimator tube.

$$\hat {x} ^ {+} = \phi (\hat {x}, u, \psi) \tag {5.6}\Sigma^ {+} = \Phi (\Sigma) \tag {5.7}$$

in which $\psi$ is a random variable in the stochastic case and a bounded disturbance taking values in Ψ when w and ν are bounded. In the latter case, $x \in \{ \hat { x } \} \oplus \Sigma$ implies $x ^ { + } \in \{ \hat { x } ^ { + } \} \oplus \mathbb { Z } ^ { + }$ for all $\psi \in \Psi$ .
