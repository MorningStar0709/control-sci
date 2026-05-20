# Solution

The claim is true, and to prove it we need to establish that the probability of drawing a sample with value $( a _ { i } , b _ { i } , c _ { i } )$ is equal to the desired density $p ( a _ { i } , b _ { i } , c _ { i } | d , e )$ . We proceed as follows. From the definition of conditional density, we know

$$p _ {\mathrm{sa}} \left(a _ {i}, b _ {i}, c _ {i} \mid d, e\right) = p _ {\mathrm{sa}} \left(a _ {i} \mid b _ {i}, c _ {i}, d, e\right) p _ {\mathrm{sa}} \left(b _ {i}, c _ {i} \mid d, e\right)$$

For the selection of $\alpha _ { i }$ described previously, we know

$$p _ {\mathrm{sa}} \left(a _ {i} \mid b _ {i}, c _ {i}, d, e\right) = p \left(a _ {i} \mid b _ {i}, d\right)$$

The values of $c _ { i }$ and e are irrelevant to the sampling procedure generating the $\alpha _ { i }$ . For the $( b _ { i } , c _ { i } )$ samples, the sampling procedure gives

$$p _ {\mathrm{sa}} (b _ {i}, c _ {i} | d, e) = p (b _ {i}, c _ {i} | e)$$

and the value of d is irrelevant to the procedure for generating the $( b _ { i } , c _ { i } )$ samples. Combining these results, we have for the $( a _ { i } , b _ { i } , c _ { i } )$ samples

$$p _ {\mathrm{sa}} (a _ {i}, b _ {i}, c _ {i} | d, e) = p (a _ {i} | b _ {i}, d) p (b _ {i}, c _ {i} | e)$$

Equation (4.45) then gives

$$p _ {\mathrm{sa}} \left(a _ {i}, b _ {i}, c _ {i} \mid d, e\right) = p \left(a _ {i}, b _ {i}, c _ {i} \mid d, e\right)$$

We conclude the sampling procedure is selecting $( a _ { i } , b _ { i } , c _ { i } )$ samples with the desired probability, and as shown in (4.39), the weights are all equal to $1 / s$ under this kind of sampling. -

Importance sampling. Consider next the case in which we have a smooth density $p ( x )$ that is easy to evaluate but difficult to sample with probability given by (4.38). This situation is not unusual. In fact, it arises frequently in applications for the following reason. Many good algorithms are available for generating samples of the uniform density. One simple method to sample an arbitrary density for a scalar random variable is the following. First compute $P ( x )$ from $p ( x )$ by integration. Let $u _ { i }$ be the samples of the uniform density on the interval [0, 1]. Then samples of $x _ { i }$ of density $p ( x )$ are given by

$$x _ {i} = P ^ {- 1} (u _ {i}) \qquad u _ {i} = P (x _ {i})$$
