# Proof:

We can pick an arbitrary feasible direction d $\in \ R ^ { n }$ . Then $x ^ { * } + \alpha d \in D$ for all small enough $\alpha > 0$ . We can define a new function $g ( \alpha )$ as following:

$$g (\alpha) := f (x ^ {*} + \alpha d), \quad \alpha > 0 \tag {16}$$

Via the Taylor expansion, we obtain:

$$g (\alpha) = g (0) + g ^ {\prime} (0) \stackrel {0} {\alpha} + \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + o \left(\alpha^ {2}\right) \tag {17}$$

where $g ^ { \prime } ( 0 ) \alpha$ cancels out since $g ^ { \prime } ( 0 ) \alpha = \langle \nabla f ( x ^ { * } ) , d \rangle = 0$ by our hypothesis. We claim that $g ^ { \prime \prime } ( 0 ) \geq 0 ;$ ; we can prove the claim by contradiction.

Suppose $g ^ { \prime \prime } ( 0 ) < 0$ . There exists a small enough $\varepsilon > 0$ such that for all α satisfying $0 < \alpha < \varepsilon$ we have, following from the definition of small o:

$$\left| \frac {0 (\alpha^ {2})}{\alpha^ {2}} \right| < - \frac {1}{2} g ^ {\prime \prime} (0) \tag {18}\therefore \left| o \left(\alpha^ {2}\right) \right| < - \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} \tag {19}$$

Hence this yields

$$g (\alpha) - g (0) = \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + o (\alpha) \leq \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + | o (\alpha) | < \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} - \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} = 0 (2 0)$$

However, given that $g ( \alpha ) : = f ( x ^ { * } + \alpha d )$ this implies that

$$f \left(x ^ {*} + \alpha d\right) - f \left(x ^ {*}\right) < 0 \tag {21}$$

Which contradicts the the hypothesis of $x ^ { * }$ being a local minimum. Therefore, the claim $g ^ { \prime \prime } ( 0 ) \geq 0$ is true and by the chain rule:

$$g ^ {\prime \prime} (0) = d ^ {T} \nabla^ {2} f (x ^ {*}) d \geq 0 \tag {22}$$

We have thus shown that given that d is an arbitrary feasible direction, $d ^ { T } \nabla ^ { 2 } f ( x ^ { * } ) d \geq$ 0 for all the feasible directions d. 
