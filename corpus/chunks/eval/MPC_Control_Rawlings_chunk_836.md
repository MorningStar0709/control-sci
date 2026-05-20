# A.12 Derivatives

We first define some notation. If $f : \mathbb { R } ^ { n }  \mathbb { R }$ , then $( \partial / \partial x ) f ( x )$ is a row vector defined by

$$(\partial / \partial x) f (x) := [ (\partial / \partial x _ {1}) f (x), \dots , (\partial / \partial x _ {n}) f (x) ]$$

provided the partial derivatives $( \partial / \partial x _ { i } ) f ( x ) , i = 1 , 2 , \ldots , n$ exist. Similarly, if $f : \mathbb { R } ^ { n } \to \mathbb { R } ^ { m } , ( \partial / \partial x ) f ( x )$ is defined to be the matrix

$$
(\partial / \partial x) f (x) := \left[ \begin{array}{c c c c} (\partial / \partial x _ {1}) f _ {1} (x) & (\partial / \partial x _ {2}) f _ {1} (x) & ... & (\partial / \partial x _ {n}) f _ {1} (x) \\ (\partial / \partial x _ {1}) f _ {2} (x) & (\partial / \partial x _ {2}) f _ {2} (x) & ... & (\partial / \partial x _ {n}) f _ {2} (x) \\ \vdots & \vdots & \vdots & \vdots \\ (\partial / \partial x _ {1}) f _ {m} (x) & (\partial / \partial x _ {2}) f _ {m} (x) & ... & (\partial / \partial x _ {n}) f _ {m} (x) \end{array} \right]
$$

where $x _ { i }$ and $f _ { i }$ denote, respectively, the ith component of the vectors x and $f .$ . We sometimes use $f _ { x } ( x )$ in place of $( \partial / \partial x ) f ( x ) . { \mathrm { I f ~ } } f : \mathbb { R } ^ { n } \to$ R, then its gradient $\nabla f ( x )$ is a column vector defined by

$$
\nabla f (x) := \left[ \begin{array}{c} (\partial / \partial x _ {1}) f (x) \\ (\partial / \partial x _ {2}) f (x) \\ \vdots \\ (\partial / \partial x _ {n}) f (x) \end{array} \right]
$$

and its Hessian is $\nabla ^ { 2 } f ( x ) = { \bigl ( } \partial ^ { 2 } / \partial x ^ { 2 } { \bigr ) } f ( x ) = f _ { x x } ( x )$ defined by

$$
\nabla^ {2} f (x) := \left[ \begin{array}{c c c c} (\partial^ {2} / \partial x _ {1} ^ {2}) f (x) & (\partial^ {2} / \partial x _ {1} \partial x _ {2}) f (x) & \ldots & (\partial^ {2} / \partial x _ {1} \partial x _ {n}) f (x) \\ (\partial^ {2} / \partial x _ {2} \partial x _ {1}) f (x) & (\partial x _ {2} ^ {2}) f (x) & \ldots & (\partial^ {2} / \partial x _ {2} \partial x _ {n}) f (x) \\ \vdots & \vdots & \ddots & \vdots \\ (\partial^ {2} / \partial x _ {n} \partial x _ {1}) f (x) & (\partial^ {2} / \partial x _ {n} \partial x _ {2}) f (x) & \ldots & (\partial^ {2} / \partial x _ {n} ^ {2}) f (x) \end{array} \right]
$$

We note that $\nabla f ( x ) = [ ( \partial / \partial x ) f ( x ) ] ^ { \prime } = f _ { x } ^ { \prime } ( x )$ .
