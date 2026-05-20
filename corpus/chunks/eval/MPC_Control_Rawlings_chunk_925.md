# Exercise A.42: Nothing is revealed

An agitated graduate student shows up at your office. He begins, “I am afraid I have discovered a deep contradiction in the foundations of systems theory.” You ask him to calm down and tell you about it. He continues, “Well, we have the pole placement theorem that says if (A, C) is observable, then there exists a matrix L such that the eigenvalues of an observer

$$A - A L C$$

can be assigned arbitrarily.”

You reply, “Well, they do have to be conjugate pairs because the matrices A, L, C are real-valued, but yeah, sure, so what?”

He continues, “Well we also have the Hautus Lemma that says (A, C) is observable if and only if

$$
\operatorname{rank} \left[ \begin{array}{c} \lambda I - A \\ C \end{array} \right] = n \qquad \forall \lambda \in \mathbb {C}
$$

“You know, the Hautus Lemma has always been one of my favorite lemmas; I don’t see a problem,” you reply.

“Well,” he continues, “isn’t the innovations form of the system, (A − ALC, C), observable if and only if the original system, (A, C), is observable?”

“Yeah . . . I seem to recall something like that,” you reply, starting to feel a little uncomfortable.

“OK, how about if I decide to put all the observer poles at zero?” he asks, innocently.

You object, “Wait a minute, I guess you can do that, but that’s not going to be a very good observer, so I don’t think it matters if . . . .”

“Well,” he interrupts, “how about we put all the eigenvalues of A − ALC at zero, like I said, and then we check the Hautus condition at λ = 0? I get

$$
\operatorname{rank} \left[ \begin{array}{c} \lambda I - (A - A L C) \\ C \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c} 0 \\ C \end{array} \right] \qquad \lambda = 0
$$

“So tell me, how is that matrix on the right ever going to have rank n with that big, fat zero sitting there?” At this point, you start feeling a little dizzy.

What’s causing the contradiction here: the pole placement theorem, the Hautus Lemma, the statement about equivalence of observability in innovations form, something else? How do you respond to this student?
