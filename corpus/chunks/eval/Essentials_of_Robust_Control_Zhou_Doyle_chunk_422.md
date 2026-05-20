# 16.2 Loop-Shaping Design

This section considers the $\mathcal { H } _ { \infty }$ loop-shaping design. The objective of this approach is to incorporate the simple performance/robustness tradeoff obtained in the loop-shaping with the guaranteed stability properties of $\mathcal { H } _ { \infty }$ design methods. Recall from Section 6.1 of Chapter 6 that good performance controller design requires that

$$\overline {{\sigma}} \left((I + P K) ^ {- 1}\right), \overline {{\sigma}} \left((I + P K) ^ {- 1} P\right), \overline {{\sigma}} \left((I + K P) ^ {- 1}\right), \overline {{\sigma}} \left(K (I + P K) ^ {- 1}\right) \tag {16.1}$$

be made small, particularly in some low-frequency range. Good robustness requires that

$$\overline {{{\sigma}}} \left(P K (I + P K) ^ {- 1}\right), \quad \overline {{{\sigma}}} \left(K P (I + K P) ^ {- 1}\right) \tag {16.2}$$

be made small, particularly in some high-frequency range. These requirements, in turn, imply that good controller design boils down to achieving the desired loop (and controller) gains in the appropriate frequency range:

$$\underline {{\sigma}} (P K) \gg 1, \underline {{\sigma}} (K P) \gg 1, \underline {{\sigma}} (K) \gg 1$$

in some low-frequency range and

$$\overline {{{{\sigma}}}} (P K) \ll 1, \overline {{{{\sigma}}}} (K P) \ll 1, \overline {{{{\sigma}}}} (K) \leq M$$

in some high-frequency range where M is not too large.

The $\mathcal { H } _ { \infty }$ loop-shaping design procedure is developed by McFarlane and Glover [1990, 1992] and is stated next.
