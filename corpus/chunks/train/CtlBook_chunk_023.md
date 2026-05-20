# 1.2.2 Solution of First Order LODE

A very basic rst order LODE is

$$\dot {x} + P x = 0$$

If we guess the solution is

$$x (t) = e ^ {p t} \qquad \dot {x} (t) = p e ^ {p t}$$

we can easily check it by plugging in to the original LODE:

$$p e ^ {p t} + P e ^ {p t} = 0 \rightarrow p e ^ {p t} = - P e ^ {p t}$$

giving

$$p = - P$$

so the solution is

$$x (t) = e ^ {- P t}$$

Because of the partial fraction expansion (covered below), this covers a very wide variety of real world LODEs.
