# 9.3.16 Gaussian random variables

A Gaussian random variable has the following properties:

$$E [ x ] = \overline {{{{x}}}}\operatorname{var} (x) = \sigma^ {2}p (x) = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} e ^ {- \frac {(x - \overline {{x}}) ^ {2}}{2 \sigma^ {2}}}$$

While we could use any random variable to represent a random process, we use the Gaussian random variable a lot in probability theory due to the central limit theorem.

Definition 9.3.1 — Central limit theorem. When independent random variables are added, their properly normalized sum tends toward a normal distribution (a Gaussian distribution or “bell curve”).

This is the case even if the original variables themselves are not normally distributed. The theorem is a key concept in probability theory because it implies that probabilistic and statistical methods that work for normal distributions can be applicable to many problems involving other types of distributions.

For example, suppose that a sample is obtained containing a large number of independent observations, and that the arithmetic mean of the observed values is computed. The central limit theorem says that the computed values of the mean will tend toward being distributed according to a normal distribution.

![](image/98bd59dd02b241dbfb99e3c1270d34518b8983f778ed469b505b5667c945179e.jpg)  
“But what is the Central Limit Theorem?” (31 minutes)   
3Blue1Brown   
https://youtu.be/zeJD6dqJ5lo

![](image/2a06c09d3cf9cb162692ced56979d706f90f3a596534007318d8413bc0895180.jpg)  
“A pretty reason why Gaussian + Gaussian = Gaussian” (13 minutes)   
3Blue1Brown   
https://youtu.be/d\_qvLDhkg00
