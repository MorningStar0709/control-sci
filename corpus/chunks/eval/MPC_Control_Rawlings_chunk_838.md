The function f is globally Lipschitz continuous if the inequality holds for all $x , x ^ { \prime } \in \mathbb { R } ^ { n }$ . The constant L is called the Lipschitz constant of $f .$ . It should be noted that the existence of partial derivatives of $f ( \cdot )$ does not ensure the existence of the derivative $D f ( \cdot )$ of $f ( \cdot )$ ; see e.g. Apostol (1974, p.103). Thus consider the function

$$f (x, y) = x + y \text { if } x = 0 \text { or } y = 0f (x, y) = 1 \text { otherwise }$$

In this case

$$
\begin{array}{l} \frac {\partial f (0 , 0)}{\partial x} = \lim _ {t \rightarrow 0} \frac {f (t , 0) - f (0 , 0)}{t} = 1 \\ \frac {\partial f (0 , 0)}{\partial y} = \lim _ {t \rightarrow 0} \frac {f (0 , t) - f (0 , 0)}{t} = 1 \\ \end{array}
$$

but the function is not even continuous at $( 0 , 0 )$ . In view of this, the following result is relevant.

Proposition A.9 (Continuous partial derivatives). Consider a function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ such that the partial derivatives $\partial f ^ { i } ( x ) / d x ^ { j }$ exist in a neighborhood of xˆ, for $i = 1 , 2 , \ldots , n , j = 1 , 2 , \ldots , m$ . If these partial derivatives are continuous at $\hat { x }$ , then the derivative $D f ( { \hat { x } } )$ exists and is equal to $f _ { x } ( { \hat { x } } )$ .

The following chain rule holds.

Proposition A.10 (Chain rule). Suppose that $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is defined by $f ( x ) = h ( g ( x ) )$ with both $h : \mathbb { R } ^ { l }  \mathbb { R } ^ { m }$ and $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { l }$ differentiable. Then

$$\frac {\partial f (\hat {x})}{\partial x} = \frac {\partial h (g (\hat {x}))}{\partial y} \frac {\partial g (\hat {x})}{\partial x}$$

The following result Dieudonne (1960), replaces, inter alia, the mean value theorem for functions $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ when $m > 1$ .

Proposition A.11 (Mean value theorem for vector functions).

(a) Suppose that $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ has continuous partial derivatives at each point x of $\mathbb { R } ^ { n }$ . Then for any $x , y \in \mathbb { R } ^ { n }$ ,

$$f (y) = f (x) + \int_ {0} ^ {1} f _ {x} (x + s (y - x)) (y - x) d s$$

(b) Suppose that $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ has continuous partial derivatives of order two at each point $x o f \mathbb { R } ^ { n }$ . Then for any $x , y \in \mathbb { R } ^ { n }$ ,

$$f (y) = f (x) + f _ {x} (x) (y - x) + \int_ {0} ^ {1} (1 - s) (y - x) ^ {\prime} f _ {x x} (x + s (y - x)) (y - x) d s$$

Proof.

(a) Consider the function $g ( s ) = f ( x + s ( y - x ) )$ where $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ . Then $g ( 1 ) = f ( y ) , g ( 0 ) = f ( x )$ and
