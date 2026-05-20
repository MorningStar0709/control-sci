# 5.7.2 Multiple Impacts

Using the geometry of Figure 5.19, the following procedure may be used to calculate the CEP for multiple impacts.

(1) Convert the alongtrack and crosstrack misses for each weapon impact into mils in the normal plane alongtrack and crosstrack using the following equations:

$$\text { Crosstrack: } X _ {M} = \tan^ {- 1} (X / S R _ {T}), \tag {5.7}\text { Alongtrack: } Y _ {M} = \tan^ {- 1} (Y \sin H _ {I Y} / S R _ {T}), \tag {5.6}$$

where $1 ^ { \circ } = 1 7 . 4 5 3 3$ mils.

(2) Compute the alongtrack and crosstrack mean point of impact as follows:

$$\bar {X} _ {M} = (X _ {M 1} + X _ {M 2} + \dots + X _ {M n}) / n, \tag {5.9a}\bar {Y} _ {M} = (Y _ {M 1} + Y _ {M 2} + \dots + Y _ {M n}) / n. \tag {5.9b}$$

(3) Compute the alongtrack and crosstrack standard deviations about their mean points of impact:

$$S _ {X _ {M}} = \left[ \left(\bar {X} _ {M} - X _ {M _ {1}}\right) ^ {2} + \left(\bar {X} _ {M} - X _ {M _ {2}}\right) ^ {2} + \dots + \left(\bar {X} _ {M} - X _ {M _ {n}}\right) ^ {2} / (n - 1) \right] ^ {1 / 2} \tag {5.10a}S _ {Y _ {M}} = \left[ \left(\bar {Y} _ {M} - Y _ {M _ {1}}\right) ^ {2} + \left(\bar {Y} _ {M} - Y _ {M _ {2}}\right) ^ {2} + \dots + \left(\bar {Y} _ {M} - Y _ {M _ {n}}\right) ^ {2} / (n - 1) \right] ^ {1 / 2} \tag {5.10b}$$

(4) Subtract the alongtrack and crosstrack ballistic dispersions (in mils) from the alongtrack and crosstrack standard deviations by the root-sum-square method. When working in mils or in the normal plane the standard deviation of the ballistic dispersion is equal in the alongtrack and crosstrack directions:

$$S _ {X} = (S _ {X _ {M}} ^ {2} - S _ {B} ^ {2}) ^ {1 / 2}, \tag {5.11a}S _ {Y} = (S _ {Y _ {M}} ^ {2} - S _ {B} ^ {2}) ^ {1 / 2}. \tag {5.11b}$$

(5) Compute the CEP (in mils about the mean point of impact) using one of the following methods:

(a) If $\sigma _ { S } / \sigma _ { L } \geq 0 . 2 8 .$ where

$$\sigma_ {S} = \text { smaller of } \sigma_ {X} \text { or } \sigma_ {Y},\sigma_ {L} = \text { larger of } \sigma_ {X} \text { or } \sigma_ {Y},$$

then

$$C E P = 0. 5 8 9 (\sigma_ {X} + \sigma_ {L}). \tag {5.12}$$

Table 5.2. Value of K Corresponding to Probability P
