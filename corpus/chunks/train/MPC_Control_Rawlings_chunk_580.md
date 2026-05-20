# Exercise 4.21: Sampled density from a weighted importance function

Given a weighted sample of an importance function $q ( x )$

$$q _ {s} (x) = \sum_ {i = 1} ^ {s} w _ {i} ^ {-} \delta (x - x _ {i}) \quad \sum_ {i} w _ {i} ^ {-} = 1$$

(a) Show that the sampled density

$$\overline {{p}} _ {s} (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i}) \quad w _ {i} = w _ {i} ^ {-} \frac {p (x _ {i})}{q (x _ {i})}$$

converges to $p ( x )$ as sample size increases.

(b) Show that the sampled density is unbiased for all samples sizes.
