Suppose, without loss of generality, that at least one $\alpha ^ { i } < 0$ . Then there exists a $\bar { \theta } > 0$ such that $\bar { \mu } ^ { j } + \bar { \theta } \alpha ^ { j } = 0$ for some j while $\bar { \mu } ^ { i } + \bar { \theta } \alpha ^ { i } \geq 0$ for all other i. Thus we have succeeded in expressing x¯ as a convex combination of $\bar { k } - 1$ vectors in S. Clearly, these reductions can go on as long as $\bar { x }$ is expressed in terms of more than $( n + 1 )$ vectors in S. This completes the proof.

Let $S _ { 1 } , S _ { 2 }$ be any two sets in $\mathbb { R } ^ { n }$ . We say that the hyperplane

$$H = \{x \in \mathbb {R} ^ {n} | \langle x, v \rangle = \alpha \}$$

separates $S _ { 1 }$ and $S _ { 2 }$ if

$$\langle x, v \rangle \geq \alpha \text { for all } x \in S _ {1}\langle y, v \rangle \leq \alpha \text { for all } y \in S _ {2}$$

The separation is said to be strong if there exists an $\varepsilon > 0$ such that

$$\langle x, v \rangle \geq \alpha + \varepsilon \text { for all } x \in S _ {1}\langle y, v \rangle \leq \alpha - \varepsilon \text { for all } y \in S _ {2}$$

![](image/e134271db2a5f513ef0fada57a2003daa0e5a8ed02b59e13a041983b425234f6.jpg)

<details>
<summary>text_image</summary>

S₁
v
H
S₂
</details>

Figure A.5: Separating hyperplane.

Theorem A.14 (Separation of convex sets). Let $S _ { 1 } , S _ { 2 }$ be two convex sets in $\mathbb { R } ^ { n }$ such that $S _ { 1 } \cap S _ { 2 } = \emptyset$ . Then there exists a hyperplane which separates $S _ { 1 }$ and $S _ { 2 }$ . Furthermore, $i f S _ { 1 }$ and $S _ { 2 }$ are closed and either $S _ { 1 }$ or $S _ { 2 }$ is compact, then the separation can be made strict.

Theorem A.15 (Separation of convex set from zero). Suppose that $S \subset$ $\mathbb { R } ^ { n }$ is closed and convex and 0 6∈ S. Let

$$\hat {x} = \arg \min \{| x | ^ {2} \mid x \in S \}$$

Then

$$H = \{x \mid \langle \hat {x}, x \rangle = | \hat {x} | ^ {2} \}$$

separates S from $0 , i . e . , \langle \hat { x } , x \rangle \geq | \hat { x } | ^ { 2 }$ for all $x \in S$ .

Proof. Let $x \in S$ be arbitrary. Then, since S is convex, $[ \hat { x } + \lambda ( x - \hat { x } ) ] \in S$ for all $\lambda \in [ 0 , 1 ]$ . By definition of $\hat { x }$ , we must have

$$
\begin{array}{l} 0 <   | \hat {x} | ^ {2} \leq | \hat {x} + \lambda (x - \hat {x}) | ^ {2} \\ = | \hat {x} | ^ {2} + 2 \lambda \langle \hat {x}, x - \hat {x} \rangle + \lambda^ {2} | x - \hat {x} | ^ {2} \\ \end{array}
$$

Hence, for all $\lambda \in ( 0 , 1 ]$ ,

$$0 \leq 2 \langle \hat {x}, x - \hat {x} \rangle + \lambda | x - \hat {x} | ^ {2}$$

Letting $\lambda  0$ we get the desired result.
