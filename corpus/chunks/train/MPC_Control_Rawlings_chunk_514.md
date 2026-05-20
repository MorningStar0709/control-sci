# Solution

Figure 4.17 shows the exact and sampled density of the importance function $q ( x )$ using 5000 samples. The weighted density for $p ( x )$ is shown in Figure 4.18. We obtain a good representation of the bimodal distribution with 5000 samples. Notice also that one should use a broad density for $q ( x )$ to obtain sufficient samples in regions where $p ( x )$ has significant probability. Using $q ( x )$ with variance of $P = 1$ instead of $P = 4$ would require many more samples to obtain an accurate representation of $p ( x )$ . Of course we cannot choose $q ( x )$ too broad or we sample the region of interest too sparsely. Choosing an appropriate importance function for an unknown $p ( x )$ is naturally a significant challenge in many applications. -

Importance sampling when the density cannot be evaluated. In many applications we have a density $p ( x )$ that is difficult to evaluate directly, but it can be expressed as

$$p (x) = \frac {h (x)}{\int h (x) d x} \quad p (x) \propto h (x)$$

in which $h ( x )$ is readily evaluated. We wish to avoid the task of integration of h to find the normalizing constant. Importance sampling can still be used to sample p in this case, but, as we discuss next, we lose the unbiased property of the sampled density for finite sample sizes. In this case, define the candidate sampled density as

$$\overline {{{p}}} _ {s} (x) = \frac {q _ {s} (x)}{d (s)} \frac {h (x)}{q (x)} \quad d (s) = \frac {1}{s} \sum_ {j} \frac {h (x _ {j})}{q (x _ {j})} \tag {4.47}$$

in which the samples are again chosen from the importance function $q ( x )$ . Summarizing, the candidate sampled density is

$$\overline {{p}} _ {s} (x) = \sum_ {i} w _ {i} \delta (x - x _ {i})p _ {\mathrm{is}} (x _ {i}) = q (x _ {i}) \quad w _ {i} = \frac {h (x _ {i}) / q (x _ {i})}{\sum_ {j} h (x _ {j}) / q (x _ {j})} \quad i = 1, \dots , s \tag {4.48}$$

Notice the weights are normalized in the case when we do not know the normalizing constant to convert from $h ( x )$ to $p ( x )$ . We next show that $\overline { { p } } _ { s } ( x )$ converges to $p ( x )$ as sample size increases (Smith and Gelfand,

![](image/516b733a53600291e162db09199c56cb569a3829345bd7241d1f7949d3f205b4.jpg)

<details>
<summary>histogram</summary>
