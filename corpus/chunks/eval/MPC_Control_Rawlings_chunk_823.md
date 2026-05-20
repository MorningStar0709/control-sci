The pseudo-inverse $A ^ { \dagger }$ of a matrix $A \in \mathbb { R } ^ { m \times n }$ is a matrix in $\mathbb { R } ^ { n \times m }$ that maps every $\boldsymbol { y } \in \mathbb { R } ^ { m }$ to that point $x \in \mathcal { R } ( A ^ { \prime } )$ of least Euclidean norm that minimizes $| y - A x | _ { 2 }$ . The operation of $A ^ { \dagger }$ is illustrated in

![](image/1c95dd19cfa47530724864b559cefdc11dc8bf846c292ac7a82bb315c5e77cd9.jpg)

<details>
<summary>text_image</summary>

x
A
y
x*
A
y*
R(A')
N(A)
R(A)
</details>

Figure A.2: Matrix A maps into $\mathcal { R } ( A )$ .

Figure A.3. Hence $A A ^ { \dagger }$ projects any point $\boldsymbol { y } \in \mathbb { R } ^ { m }$ orthogonally onto R(A), i.e., $A A ^ { \dagger } y = y ^ { * }$ , and $A ^ { \dagger } A$ projects any $x \in \mathbb { R } ^ { n }$ orthogonally onto ${ \mathcal { R } } ( A ^ { \prime } ) , \mathrm { i . e . , } A ^ { \dagger } A x = x ^ { * }$ .

![](image/dee06b6d8948714461c7d35e9fd7ba3ccf79cbb3e063cf91250d2f7f7f36d277.jpg)

<details>
<summary>text_image</summary>

x
A†
y
x*
A†
y*
R(A')
N(A)
R(A)
</details>

Figure A.3: Pseudo-inverse of A maps into $\mathcal { R } ( A ^ { \prime } )$ .

If $A \in \mathbb { R } ^ { m \times n }$ where $m < n$ has maximal rank m, then $A A ^ { \prime } \in \mathbb { R } ^ { m \times m }$ is invertible and $A ^ { \dagger } = A ^ { \prime } ( A A ^ { \prime } ) ^ { - 1 }$ ; in this case, $\mathcal { R } ( A ) = \mathbb { R } ^ { m }$ and every $\boldsymbol { y } ~ \in ~ \mathbb { R } ^ { m }$ lies in $\mathcal { R } ( A )$ . Similarly, if $n \textless m$ and A has maximal rank n, then $A ^ { \prime } A \in \mathbb { R } ^ { n \times n }$ is invertible and $A ^ { \dagger } = ( A ^ { \prime } A ) ^ { - 1 } A ^ { \prime } ;$ ; in this case, $\mathcal { R } ( A ^ { \prime } ) = \mathbb { R } ^ { n }$ and every $x \in \mathbb { R } ^ { n }$ lies in $\mathcal { R } ( A ^ { \prime } )$ . More generally, if $A \in$ $\mathbb { R } ^ { m \times n }$ has rank $r$ , then A has the singular-value decomposition $A \ =$ $U { \boldsymbol { \Sigma } } V ^ { \prime }$ where $U \in \mathbb { R } ^ { m \times r }$ and $V \in \mathbb { R } ^ { r \times n }$ are orthogonal matrices, i.e., $U ^ { \prime } U = I _ { r }$ and $V ^ { \prime } V = I _ { r }$ , and $\Sigma = \operatorname { d i a g } ( \sigma _ { 1 } , \sigma _ { 2 } , \ldots , \sigma _ { r } ) \in \mathbb { R } ^ { r \times r }$ where $\sigma _ { 1 } > \sigma _ { 2 } . . . . > \sigma _ { r } > 0$ . The pseudo-inverse of A is then

$$A ^ {\dagger} = V \Sigma^ {- 1} U ^ {\prime}$$
