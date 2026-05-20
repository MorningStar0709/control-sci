$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \left(\frac {\sigma_ {0} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} x ^ {2} + \frac {\sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} x ^ {2} - 2 \frac {\sigma_ {0} ^ {2} z _ {1}}{\sigma^ {2} \sigma_ {0} ^ {2}} x - 2 \frac {\sigma^ {2} x _ {0}}{\sigma^ {2} \sigma_ {0} ^ {2}} x + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} + \frac {\sigma^ {2} x _ {0} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}}\right)}$$

Combine like terms.

$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \left(\frac {\sigma_ {0} ^ {2} + \sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} x ^ {2} - 2 \frac {\sigma_ {0} ^ {2} z _ {1} + \sigma^ {2} x _ {0}}{\sigma^ {2} \sigma_ {0} ^ {2}} x + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2} + \sigma^ {2} x _ {0} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}}\right)}$$

Factor out $\frac { \sigma _ { 0 } ^ { 2 } + \sigma ^ { 2 } } { \sigma ^ { 2 } \sigma _ { 0 } ^ { 2 } }$ 0σ2 σ20 2 +σ2

$$
\begin{array}{l} p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \frac {\sigma_ {0} ^ {2} + \sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} \left(x ^ {2} - 2 \frac {\sigma_ {0} ^ {2} z _ {1} + \sigma^ {2} x _ {0}}{\sigma_ {0} ^ {2} + \sigma^ {2}} x + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2} + \sigma^ {2} x _ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}}\right)} \\ p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \frac {\sigma_ {0} ^ {2} + \sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}}} \bigg (x ^ {2} - 2 \bigg (\frac {\sigma_ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} z _ {1} + \frac {\sigma^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} x _ {0} \bigg) x + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2} + \sigma^ {2} x _ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} \bigg) \\ \end{array}
$$

σ 2 +σ 20 z $\begin{array} { r } { \frac { \sigma _ { 0 } ^ { 2 } } { \sigma ^ { 2 } + \sigma _ { 0 } ^ { 2 } } z _ { 1 } + \frac { \sigma ^ { 2 } } { \sigma _ { 0 } ^ { 2 } + \sigma ^ { 2 } } x _ { 0 } } \end{array}$ σ 20 + σ2σ2+σ2 x0 is the mean of the combined probability distribution, which we’ll denote as $\mu .$ .

$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \frac {\sigma^ {2} + \sigma_ {0} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} \left(x ^ {2} - 2 \mu x + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2} + \sigma^ {2} x _ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}}\right)}$$

Add in $\mu ^ { 2 } - \mu ^ { 2 }$ to perform some factoring.
