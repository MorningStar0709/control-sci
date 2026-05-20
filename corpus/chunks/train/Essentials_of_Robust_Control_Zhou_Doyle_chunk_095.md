(ii) $\left\| x + y \right\| ^ { 2 } + \left\| x - y \right\| ^ { 2 } = 2 \left\| x \right\| ^ { 2 } + 2 \left\| y \right\| ^ { 2 }$ (Parallelogram law).

(iii) $\left\| x + y \right\| ^ { 2 } = \left\| x \right\| ^ { 2 } + \left\| y \right\| ^ { 2 } ~ i f ~ x ~ \bot ~ y .$

A Hilbert space is a complete inner product space with the norm induced by its inner product. For example, $\mathbb { C } ^ { n }$ with the usual inner product is a (finite dimensional) Hilbert space. More generally, it is straightforward to verify that $\mathbb { C } ^ { n \times m }$ with the inner product defined as

$$\langle A, B \rangle := \operatorname{trace} A ^ {*} B = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \bar {a} _ {i j} b _ {i j} \forall A, B \in \mathbb {C} ^ {n \times m}$$

is also a (finite dimensional) Hilbert space.

A well-know infinite dimensional Hilbert space is $\textstyle { \mathcal { L } } _ { 2 } [ a , b ]$ , which consists of all square integrable and Lebesgue measurable functions defined on an interval $[ a , b ]$ with the inner product defined as

$$\langle f, g \rangle := \int_ {a} ^ {b} f (t) ^ {*} g (t) d t$$

for $f , g \in \mathcal { L } _ { 2 } [ a , b ]$ . Similarly, if the functions are vector or matrix-valued, the inner product is defined correspondingly as

$$\langle f, g \rangle := \int_ {a} ^ {b} \operatorname{trace} [ f (t) ^ {*} g (t) ] d t.$$

Some spaces used often in this book are $\mathcal { L } _ { 2 } [ 0 , \infty ) , \mathcal { L } _ { 2 } ( - \infty , 0 ] , \mathcal { L } _ { 2 } ( - \infty , \infty )$ . More precisely, they are defined as

$\mathcal { L } _ { 2 } = \mathcal { L } _ { 2 } ( - \infty , \infty )$ : Hilbert space of matrix-valued functions on R, with inner product

$$\langle f, g \rangle := \int_ {- \infty} ^ {\infty} \operatorname{trace} [ f (t) ^ {*} g (t) ] d t.$$

$\mathcal { L } _ { 2 + } = \mathcal { L } _ { 2 } [ 0 , \infty )$ : subspace of $\mathcal { L } _ { 2 } ( - \infty , \infty )$ with functions zero for $t < 0$ .

$\mathcal { L } _ { 2 - } = \mathcal { L } _ { 2 } ( - \infty , 0 ]$ : subspace of $\mathcal { L } _ { 2 } ( - \infty , \infty )$ with functions zero for $t > 0$
