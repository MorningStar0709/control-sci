# 7.5 Root Locus FAQ

This FAQ refers to the system of Figure 7.1 where K is a real number > 0.

Q: What is the point of the Root Locus?

A: The point is to predict how closed loop pole locations and corresponding performance will change as the gain constant, K, changes, knowing only the open loop poles and zeros.

We have three fundamental facts about the points on the root locus:

<table><tr><td>Question</td><td>Answer</td><td>Reason</td></tr><tr><td>Fact 1. What is true for any value of s on the root locus?</td><td>∠CPH(s) = π,3π,5π..., “Angle Condition”</td><td>(see below)</td></tr><tr><td>Fact 2. What is k for a value of s on the RL?</td><td>|KCPH(s)| = 1 so K = 1/|CPH(s)|. “Magnitude Condition”</td><td>(see below)</td></tr><tr><td>Fact 3. Where do branches of the RL go as k → ∞?</td><td>From poles of CPH(s) to zeros of CPH(s) or they diverge to |s| = ∞</td><td>M</td></tr></table>

Each of the following Root Locus Drawing Rules is the answer to a FAQ. It is recommended to rst plot the open-loop gain poles, and then to draw answers to the following questions in order:

<table><tr><td>Question</td><td>Answer</td><td>Reason</td></tr><tr><td>Rule 1. What parts of the real axis contain some of the RL?</td><td>A segment of the real axis has RL on it if the number of real poles and zeros to the right is ODD.</td><td>A</td></tr><tr><td>Rule 2. How many branches diverge to |s| = ∞?</td><td> $n_d = n_p - n_z$ .</td><td>P</td></tr><tr><td>Rule 3. What angles do the asymptotes have?</td><td> $\theta_d = \frac{\pi(1+2m)}{n_p-n_z}, \quad m = 0,1,2,3\ldots$ </td><td>A</td></tr><tr><td>Rule 4. Where do the asymptotes intersect the real axis?</td><td> $\sigma_a = \frac{\Sigma\text{poles}-\Sigma\text{zeros}}{n_p-n_z}$ </td><td>P</td></tr></table>

The following two rules can be used to make your hand drawn root locus more accurate. In some case they can disambiguate certain situations. However with the ease of computer plotting they are no longer frequently used.

<table><tr><td>Question</td><td>Answer</td><td>Reason</td></tr><tr><td>Rule 6. At which point do branches leave or join the real axis?</td><td>at real values, s, where  $\frac{d}{ds} \frac{P(s)}{Z(s)} = 0$ </td><td>P,A</td></tr><tr><td>Rule 7. At what angle do branches depart from a complex pole? (or join a complex zero?)</td><td> $\theta_d = \pi - \Sigma \angle \text{poles} + \Sigma \angle \text{zeros}$ </td><td>A</td></tr></table>
