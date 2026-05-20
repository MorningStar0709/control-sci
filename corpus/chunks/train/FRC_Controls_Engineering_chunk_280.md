# 9.3.13 Random vectors

Now we will extend the probability concepts discussed so far to vectors where each element has a PDF.

$$
\mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {n} \end{array} \right]
$$

The elements of x are scalar variables jointly distributed with a joint density $p ( x _ { 1 } , \ldots , x _ { n } )$ . The expectation is

$$
E [ \mathbf {x} ] = \overline {{\mathbf {x}}} = \int_ {- \infty} ^ {\infty} \mathbf {x} p (\mathbf {x}) d \mathbf {x}
E [ \mathbf {x} ] = \left[ \begin{array}{c} E [ x _ {1} ] \\ \vdots \\ E [ x _ {n} ] \end{array} \right]
E [ x _ {i} ] = \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} x _ {i} p (x _ {1}, \ldots , x _ {n}) d x _ {1} \dots d x _ {n}E [ f (\mathbf {x}) ] = \int_ {- \infty} ^ {\infty} f (\mathbf {x}) p (\mathbf {x}) d \mathbf {x}
$$
