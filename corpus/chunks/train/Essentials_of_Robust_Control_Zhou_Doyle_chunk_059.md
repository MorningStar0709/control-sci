# 2.5 Vector Norms and Matrix Norms

In this section, we shall define vector and matrix norms. Let X be a vector space. A real-valued function k·k defined on X is said to be a norm on X if it satisfies the following properties:

(i) $\| x \| \geq 0$ (positivity);   
(ii) $\| x \| = 0$ if and only if $x = 0$ (positive definiteness);   
(iii) $\| \alpha x \| = | \alpha | \| x \|$ , for any scalar α (homogeneity);   
(iv) $\| x + y \| \leq \| x \| + \| y \|$ (triangle inequality)

for any $x \in X$ and $y \in X$ .

Let $x \in \mathbb { C } ^ { n }$ . Then we define the vector p-norm of x as

$$\| x \| _ {p} := \left(\sum_ {i = 1} ^ {n} | x _ {i} | ^ {p}\right) ^ {1 / p}, \text { for } 1 \leq p < \infty .$$

In particular, when $p = 1 , 2 , \infty$ we have

$$
\begin{array}{l} \left\| x \right\| _ {1} := \sum_ {i = 1} ^ {n} \left| x _ {i} \right|; \\ \| x \| _ {2} := \sqrt {\sum_ {i = 1} ^ {n} | x _ {i} | ^ {2}}; \\ \end{array}
\| x \| _ {\infty} := \max _ {1 \leq i \leq n} | x _ {i} |.
$$

Clearly, norm is an abstraction and extension of our usual concept of length in threedimensional Euclidean space. So a norm of a vector is a measure of the vector “length” (for example, $\left. { x } \right. _ { 2 }$ is the Euclidean distance of the vector x from the origin). Similarly, we can introduce some kind of measure for a matrix.

Let $A = [ a _ { i j } ] \in \mathbb { C } ^ { m \times n }$ ; then the matrix norm induced by a vector p-norm is defined as

$$\| A \| _ {p} := \sup _ {x \neq 0} \frac {\| A x \| _ {p}}{\| x \| _ {p}}.$$

The matrix norms induced by vector p-norms are sometimes called induced p-norms. This is because $\left\| A \right\| _ { p }$ is defined by or induced from a vector p-norm. In fact, A can be viewed as a mapping from a vector space $\mathbb { C } ^ { n }$ equipped with a vector norm $\left\| \cdot \right\| _ { p }$ to another vector space $\mathbb { C } ^ { m }$ equipped with a vector norm $\left\| \cdot \right\| _ { p } .$ So from a system theoretical point of view, the induced norms have the interpretation of input/output amplification gains.

In particular, the induced matrix 2-norm can be computed as

$$\left\| A \right\| _ {2} = \sqrt {\lambda_ {\max} (A ^ {*} A)}.$$

We shall adopt the following convention throughout this book $f o r$ the vector and matrix norms unless specified otherwise: Let $x \in \mathbb { C } ^ { n }$ and $A \in \mathbb { C } ^ { m \times n }$ ; then we shall denote the Euclidean 2-norm of x simply by

$$\left\| x \right\| := \left\| x \right\| _ {2}$$

and the induced 2-norm of A by

$$\left\| A \right\| := \left\| A \right\| _ {2}.$$
