We can associate with each resampling a sampled probability density

$$\tilde {p} (x) = \sum_ {i = 1} ^ {s} \tilde {w} _ {i} \delta (x - \tilde {x} _ {i})$$

The resampled density is clearly not the same as the original sampled density. It is likely that we have moved many of the new samples to places where the original density has large weights. But by resampling in the fashion described here, we have not introduced bias into the estimates.

Consider taking many such resamples. We can calculate for each of these resamples a value of the integral of f as follows

$$\int f (x) \tilde {p} (x) d x = \sum_ {i = 1} ^ {s} \tilde {w} _ {i} f (\tilde {x} _ {i})$$

To show this resampling procedure is valid, we show that the average over these values of the f integrals with $\tilde { p } ( x )$ is equal to the original value of the integral using $p ( x )$ . We state this result for the resampling procedure described previously as the following theorem.
