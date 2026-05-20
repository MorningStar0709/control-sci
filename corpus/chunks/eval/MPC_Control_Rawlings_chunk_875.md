# Solution

We have already shown that independent implies uncorrelated for any density, so we now show that, for normals, uncorrelated implies independent. Given cov(ξ, η) = 0, we have

$$P _ {x y} = P _ {y x} ^ {\prime} = 0 \quad \det P = \det P _ {x} \det P _ {y}$$

so the density can be written

$$
p _ {\xi , \eta} (x, y) = \frac {\exp \left(- \frac {1}{2} \left[ \begin{array}{l} \bar {x} \\ \bar {y} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} P _ {x} & 0 \\ 0 & P _ {y} \end{array} \right] ^ {- 1} \left[ \begin{array}{l} \bar {x} \\ \bar {y} \end{array} \right]\right)}{(2 \pi) ^ {(n _ {x} + n _ {y}) / 2} (\det P _ {x} \det P _ {y}) ^ {1 / 2}} \tag {A.32}
$$

For any joint normal, we know the marginals are simply

$$\xi \sim N (m _ {x}, P _ {x}) \qquad \eta \sim N (m _ {y}, P _ {y})$$

so we have

$$p _ {\xi} (x) = \frac {1}{(2 \pi) ^ {n _ {x} / 2} (\det P _ {x}) ^ {1 / 2}} \exp \left(- (1 / 2) \bar {x} ^ {\prime} P _ {x} ^ {- 1} \bar {x}\right)p _ {\eta} (y) = \frac {1}{(2 \pi) ^ {n _ {y} / 2} (\det P _ {y}) ^ {1 / 2}} \exp \left(- (1 / 2) \bar {y} ^ {\prime} P _ {y} ^ {- 1} \bar {y}\right)$$

Forming the product and combining terms gives

$$
p _ {\xi} (x) p _ {\eta} (y) = \frac {\exp \left(- \frac {1}{2} \left[ \begin{array}{c} \bar {x} \\ \bar {y} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} P _ {x} ^ {- 1} & 0 \\ 0 & P _ {y} ^ {- 1} \end{array} \right] \left[ \begin{array}{c} \bar {x} \\ \bar {y} \end{array} \right]\right)}{(2 \pi) ^ {(n _ {x} + n _ {y}) / 2} \left(\det P _ {x} \det P _ {y}\right) ^ {1 / 2}}
$$

Comparing this equation to (A.32), and using the inverse of a blockdiagonal matrix, we have shown that $\xi$ and $\eta$ are statistically independent. -
