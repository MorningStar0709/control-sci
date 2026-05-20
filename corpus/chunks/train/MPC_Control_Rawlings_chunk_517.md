# Example 4.34: Importance sampling of a multimodal function

We revisit Example 4.33 but use the following function h(x)

$$
\begin{array}{l} h (x) = e ^ {- (1 / 2) (x - m _ {1}) ^ {2} / P _ {1}} + e ^ {- (1 / 2) (x - m _ {2}) ^ {2} / P _ {2}} \\ m _ {1} = - 4, m _ {2} = 4, P _ {1} = P _ {2} = 1 \\ \end{array}
$$

and we do not have the normalization constant available. We again generate samples using the following importance function

$$q (x) = \frac {1}{\sqrt {2 \pi P}} e ^ {- (1 / 2) (x - m) ^ {2} / P} \quad m = 0, P = 4$$
