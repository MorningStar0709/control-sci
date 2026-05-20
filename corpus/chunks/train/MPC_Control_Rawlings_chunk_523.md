Notice there are only three different values for the integral of f . Next, calculating the expectation over the resampling process gives

$$
\begin{array}{l} \mathcal {E} _ {\text {re}} \left(\sum_ {i = 1} ^ {2} \tilde {w} _ {i} f (\tilde {x} _ {i})\right) = w _ {1} ^ {2} f _ {1} + w _ {1} w _ {2} (f _ {1} + f _ {2}) + w _ {2} ^ {2} f _ {2} ^ {2} \\ = \left(w _ {1} ^ {2} + w _ {1} w _ {2}\right) f _ {1} + \left(w _ {1} w _ {2} + w _ {2} ^ {2}\right) f _ {2} \\ = w _ {1} \left(w _ {1} + w _ {2}\right) f _ {1} + w _ {2} \left(w _ {1} + w _ {2}\right) f _ {2} \\ = w _ {1} f _ {1} + w _ {2} f _ {2} \\ = \int f (x) p (x) d x \\ \end{array}
$$

and the conclusion of the theorem is established for s = 2.

One can also change the total number of samples in resampling without changing the conclusions of Theorem 4.35. Exercise 4.17 explores this issue in detail. In many applications of sampling, we use the resampling process to discard samples with excessively small weights in order to reduce the storage requirements and computational burden associated with a large number of samples.

To make this discussion explicit, consider again the bimodal distribution of Example 4.33 shown in Figure 4.18 that was sampled using importance sampling. Many of the samples are located in the interval [−1, 1] because the importance function q has large density in this interval. In fact, 1964 of the 5000 samples fall in this interval given the random sample corresponding to Figure 4.18. But notice the weights in this interval are quite small. If we resample p, we can retain the accuracy with many fewer samples as we show in the next example.
