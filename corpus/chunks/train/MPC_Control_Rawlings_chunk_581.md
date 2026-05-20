# Exercise 4.22: Sampled density from a weighted importance function when unable to evaluate the density

Given a weighted sample of an importance function $q ( x )$

$$q _ {s} (x) = \sum_ {i = 1} ^ {s} w _ {i} ^ {-} \delta (x - x _ {i}) \quad \sum_ {i} w _ {i} ^ {-} = 1$$

and a density of the following form

$$p (x) = \frac {h (x)}{\int h (x) d x}$$

in which $p ( x )$ cannot be conveniently evaluated but $h ( x )$ can be evaluated.

(a) Show that the sampled density

$$\overline {{p}} _ {s} (x) = \sum_ {i = 1} ^ {s} \overline {{w}} _ {i} \delta (x - x _ {i}) \quad w _ {i} = w _ {i} ^ {-} \frac {h (x _ {i})}{q (x _ {i})} \quad \overline {{w}} _ {i} = \frac {w _ {i}}{\sum_ {j} w _ {j}}$$

converges to $p ( x )$ as sample size increases.

(b) Show that the sampled density is biased for all finite sample sizes.
