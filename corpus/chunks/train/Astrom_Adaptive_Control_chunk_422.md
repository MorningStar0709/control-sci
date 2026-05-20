# LEMMA 6.2 Key technical lemma

Let $\{s_t\}$ be a sequence of real numbers and let $\{\sigma_t\}$ be a sequence of vectors such that

$$\left\| \sigma_ {t} \right\| \leq c _ {1} + c _ {2} \max _ {0 < k \leq t} | s _ {k} |$$

Assume that

$$z _ {t} = \frac {\mathrm{s} _ {t} ^ {2}}{\alpha_ {1} + \alpha_ {2} \sigma_ {t} ^ {T} \sigma_ {t}} \rightarrow 0 \tag {6.44}$$

and that

$$\lim _ {t \rightarrow \infty} s (t) = 0$$

where $\alpha_{1} > 0$ and $\alpha_{2} > 0$ . Then $\| \sigma_t\|$ is bounded.

Proof: The result is trivial if $s_{t}$ is bounded. Hence assume that $s_{t}$ is not bounded. Then there exists a subsequence $\{t_{n}\}$ such that $|s_{t_{n}}| \to \infty$ and $|s_{t}| \leq s_{t_{n}}$ for $t \leq t_{n}$ . For this sequence it follows that

$$\left| \frac {s _ {t} ^ {2}}{\alpha_ {1} + \alpha_ {2} \sigma_ {t} ^ {T} \sigma_ {t}} \right| \geq \frac {s _ {t} ^ {2}}{\alpha_ {1} + \alpha_ {2} (c _ {1} + c _ {2} | s _ {t} |) ^ {2}} \geq \frac {1}{\alpha_ {3} c _ {2} ^ {2}} > 0$$

where $0 < \alpha_{3} < \alpha_{2}$ . This contradicts Eq. (6.44) and proves the statements. $\square$
