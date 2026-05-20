# Shannon Reconstruction

For the case of periodic sampling of band-limited signals, it follows from the sampling theorem that a reconstruction is given by (7.1). This reconstruction is called the Shannon reconstruction. Equation (7.1) defines an inverse of the sampling operation, which can be considered as a linear operator. It is, however, not a causal operator because the value of f at time t is expressed in terms of past values $\{f(kh):k\leq t/h\}$ as well as future values $\{f(kh):k>t/h\}$ . The characteristics of the Shannon reconstruction are given by the function

$$h (t) = \frac {\sin (\omega_ {s} t / 2)}{\omega_ {s} t / 2} \tag {7.7}$$

See Fig. 7.3. This reconstruction will introduce a delay. The weight is 10% after about three samples and less than 5% after six samples. The delay implies that the Shannon reconstruction is not useful in control applications. It is, however, sometimes used in communication and signal-processing applications, where the delay can be acceptable. Other drawbacks of the Shannon reconstruction are that it is complicated and that it can be applied only to periodic sampling. It is therefore useful to have other reconstructions.
