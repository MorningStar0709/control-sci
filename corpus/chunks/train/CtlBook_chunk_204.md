# Root Locus (RL) Drawing Steps:

1. RL Starts (when K = 0) at the roots of CP H(s) so start out by plotting these poles and zeros (as x's and o's).   
2. Find which parts of the real line contain parts of the RL. For each point on the real axis, if the total number of poles and zeros to right is ODD, that part is ON the RL. Conversely, if the total number of poles and zeros to the right is EVEN, that segment is OFF the RL.   
3. The number of asymptotes (diverging branches which go out to innity) is $n _ { p } \mathrm { ~ - ~ } n _ { z }$ , where $n _ { p }$ is the number of loop gain poles and $n _ { z }$ is the number of zeros.   
4. If $n _ { p } - n _ { z } \neq 0$ , the place where the asymptotes intersect the real line is:

$$\sigma_ {a} = \frac {\Sigma \mathrm{poles} - \Sigma \mathrm{zeros}}{n _ {p} - n _ {z}}$$

5. The angles of the diverging branches are:

$$\frac {\pi (1 + 2 m)}{n _ {p} - n _ {z}}$$

where m is the integers 0, 1, 2, 3, . . . .

6. Poles which do NOT diverge on asymptotes out to ∞ circle back to the loop-gain zeros.
