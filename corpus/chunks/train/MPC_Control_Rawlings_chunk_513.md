# Example 4.33: Importance sampling of a multimodal density

Given the following bimodal distribution

$$p (x) = \frac {1}{2 \sqrt {2 \pi P _ {1}}} e ^ {- (1 / 2) (x - m _ {1}) ^ {2} / P _ {1}} + \frac {1}{2 \sqrt {2 \pi P _ {2}}} e ^ {- (1 / 2) (x - m _ {2}) ^ {2} / P _ {2}}m _ {1} = - 4 \quad m _ {2} = 4 \quad P _ {1} = P _ {2} = 1$$

generate samples using the following unimodal importance function

$$q (x) = \frac {1}{\sqrt {2 \pi P}} e ^ {- (1 / 2) (x - m) ^ {2} / P} \quad m = 0 \quad P = 4$$
