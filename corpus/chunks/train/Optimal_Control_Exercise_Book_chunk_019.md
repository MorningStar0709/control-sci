# Proof:

We can pick an arbitrary feasible direction $d \in R ^ { n }$ . Then $x ^ { * } + \alpha d \in D$ for all small enough $\alpha > 0$ . We can define a new function $g ( \alpha )$ as following:

$$g (\alpha) := f (x ^ {*} + \alpha d), \quad \alpha > 0 \tag {6}$$

Via the Taylor expansion, we obtain:

$$g (\alpha) = g (0) + g ^ {\prime} (0) \alpha + o (\alpha) \tag {7}$$

We now claim that $g ^ { \prime } ( 0 ) \geq 0 ;$ we can prove this claim by contradiction. Suppose that $g ^ { \prime } ( 0 ) < 0$ . By the definition of small o we can assert

$$\lim _ {\alpha \rightarrow 0} \frac {o (\alpha)}{\alpha} = 0 \tag {8}$$

There exists a small enough $\varepsilon > 0$ such that for all α satisfying $0 < \alpha < \varepsilon$ we have

$$\left| \frac {o (\alpha)}{\alpha} \right| < - g ^ {\prime} (0) \tag {9}\therefore | o (\alpha) | < - g ^ {\prime} (0) \alpha \tag {10}$$

Hence we have

$$g (\alpha) - g (0) = g ^ {\prime} (0) \alpha + o (\alpha) \leq g ^ {\prime} (0) \alpha + | o (\alpha) | < g ^ {\prime} (0) \alpha - g ^ {\prime} (0) \alpha = 0 \tag {11}$$

However, given that $g ( \alpha ) : = f ( x ^ { * } + \alpha d )$ this implies that

$$f \left(x ^ {*} + \alpha d\right) - f \left(x ^ {*}\right) < 0 \tag {12}$$

Which contradicts the the hypothesis of $x ^ { * }$ being a local minimum. Therefore, the claim $g ^ { \prime } ( 0 ) \geq 0$ is true and by the chain rule:

$$g ^ {\prime} (0) = \left\langle \nabla f \left(x ^ {*}\right), d \right\rangle \geq 0 \tag {13}$$

We have thus shown that given that d is an arbitrary feasible direction, $\langle \nabla f ( x ^ { * } , d ) \geq$ 0 for all the feasible directions d.
