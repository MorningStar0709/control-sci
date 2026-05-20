Figure A.9: Multivariate normal in two dimensions.

$$\xi \sim N (m, P)$$

The matrix P is a real, symmetric matrix. Figure A.9 displays a multivariate normal for

$$
P ^ {- 1} = \left[ \begin{array}{c c} 3. 5 & 2. 5 \\ 2. 5 & 4. 0 \end{array} \right] \qquad m = \left[ \begin{array}{c} 0 \\ 0 \end{array} \right]
$$

As displayed in Figure A.9, lines of constant probability in the multivariate normal are lines of constant

$$(x - m) ^ {\prime} P ^ {- 1} (x - m)$$

To understand the geometry of lines of constant probability (ellipses in two dimensions, ellipsoids or hyperellipsoids in three or more dimensions) we examine the eigenvalues and eigenvectors of the $P ^ { - 1 }$ matrix.

$$x ^ {\prime} A x = bA v _ {i} = \lambda_ {i} v _ {i}$$

![](image/d080b2dedde04ca61a375af465529d138a127c22bfdbb2bb886edc5c0c72ad7a.jpg)

<details>
<summary>text_image</summary>

x₂
√(b/λ₂) v₂
√(b/λ₁) v₁
√(b̃A₂₂)
x₁
√(b̃A₁₁)
</details>

Figure A.10: The geometry of quadratic form $x ^ { \prime } A x = b $ .

Consider the quadratic function x0Ax depicted in Figure A.10. Each eigenvector of A points along one of the axes of the ellipse $x ^ { \prime } A x = b$ . The eigenvalues show us how stretched the ellipse is in each eigenvector direction. If we want to put simple bounds on the ellipse, then we draw a box around it as shown in Figure A.10. Notice the box contains much more area than the corresponding ellipse and we have lost the correlation between the elements of x. This loss of information means we can put different tangent ellipses of quite different shapes inside the same box. The size of the bounding box is given by

$$\text { length of } i \text { th side } = \sqrt {b \tilde {A} _ {i i}}$$

in which

$$\tilde {A} _ {i i} = (i, i) \text { element of } A ^ {- 1}$$

See Exercise A.45 for a derivation of the size of the bounding box. Figure A.10 displays these results: the eigenvectors are aligned with the ellipse axes and the eigenvalues scale the lengths. The lengths of the sides of the box that are tangent to the ellipse are proportional to the square root of the diagonal elements of A−1.

Singular or degenerate normal distributions. It is often convenient to extend the definition of the normal distribution to admit positive semidefinite covariance matrices. The distribution with a semidefinite covariance is known as a singular or degnerate normal distribution (Anderson, 2003, p. 30). Figure A.11 shows a nearly singular normal distribution.
