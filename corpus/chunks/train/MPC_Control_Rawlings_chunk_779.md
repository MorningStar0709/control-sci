$$V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid (x, \mathbf {u}) \in \mathbb {Z} \right\}$$

Using the fact that for each $i , x ( i ) = A ^ { i } x + M _ { i } \mathbf { u }$ , it is possible to determine matrices $\mathbf { Q } \in \mathbb { R } ^ { n \times n } , \mathbf { R } \in \mathbb { R } ^ { N m \times N m }$ , and $\mathbf { S } \in \mathbb { R } ^ { N m \times n }$ such that

$$V _ {N} (x, \mathbf {u}) = (1 / 2) x ^ {\prime} \mathbf {Q} x ^ {\prime} + (1 / 2) \mathbf {u} ^ {\prime} \mathbf {R} \mathbf {u} + \mathbf {u} ^ {\prime} \mathbf {S} x \tag {7.12}$$

Similarly, as shown above, there exist matrices M, N and a vector p such that

$$\mathbb {Z} = \{(x, \mathbf {u}) \mid \mathbf {M u} \leq \mathbf {N} x + \mathbf {p} \} \tag {7.13}$$

This is precisely the parametric problem studied in Section 7.3, so that the solution $\mathbf { u } ^ { 0 } ( x )$ to $\mathbb { P } ( x )$ is piecewise affine on a polytopic partition ${ \mathcal { P } } = \{ R _ { x } \mid x \in X \}$ of X the projection of $\mathbb { Z } \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { N m }$ onto $\mathbb { R } ^ { n }$ , being affine in each of the constituent polytopes of P. The receding horizon control law is $x \mapsto u ^ { 0 } ( 0 ; x )$ , the first element of $\mathbf { u } ^ { 0 } ( x )$ . Two examples are shown in Figures 7.6 and 7.7.

![](image/89233fb4f0cc045fd8181a276b16836b554b137d646d3f47b3c8830de9b8cb95.jpg)  
Figure 7.7: Regions $R _ { x }$ , $x \in X$ for a second-order example.
