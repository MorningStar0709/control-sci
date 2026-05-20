$$
\begin{array}{l} f (t) = \mathscr {L} ^ {- 1} [ F (s) ] \\ = 5 \mathscr {L} ^ {- 1} \left[ \frac {2}{(s + 1) ^ {2} + 2 ^ {2}} \right] + 2 \mathscr {L} ^ {- 1} \left[ \frac {s + 1}{(s + 1) ^ {2} + 2 ^ {2}} \right] \\ = 5 e ^ {- t} \sin 2 t + 2 e ^ {- t} \cos 2 t, \quad \text {   for   } t \geq 0 \\ \end{array}
$$

Partial-Fraction Expansion when $F ( s )$ Involves Multiple Poles. Instead of discussing the general case, we shall use an example to show how to obtain the partialfraction expansion of $F ( s )$ .

Consider the following $F ( s )$ :

$$F (s) = \frac {s ^ {2} + 2 s + 3}{(s + 1) ^ {3}}$$

The partial-fraction expansion of this $F ( s )$ involves three terms,

$$F (s) = \frac {B (s)}{A (s)} = \frac {b _ {1}}{s + 1} + \frac {b _ {2}}{(s + 1) ^ {2}} + \frac {b _ {3}}{(s + 1) ^ {3}}$$

where $b _ { 3 } , \ b _ { 2 }$ , and $b _ { 1 }$ are determined as follows. By multiplying both sides of this last equation by $( s + 1 ) ^ { 3 }$ , we have

$$(s + 1) ^ {3} \frac {B (s)}{A (s)} = b _ {1} (s + 1) ^ {2} + b _ {2} (s + 1) + b _ {3} \tag {B-2}$$

Then letting s=–1, Equation (B–2) gives

$$\left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] _ {s = - 1} = b _ {3}$$

Also, differentiation of both sides of Equation (B–2) with respect to s yields

$$\frac {d}{d s} \left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] = b _ {2} + 2 b _ {1} (s + 1) \tag {B-3}$$

If we let s=–1 in Equation (B–3), then

$$\frac {d}{d s} \left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] _ {s = - 1} = b _ {2}$$

By differentiating both sides of Equation (B–3) with respect to s, the result is

$$\frac {d ^ {2}}{d s ^ {2}} \left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] = 2 b _ {1}$$

From the preceding analysis it can be seen that the values of $b _ { 3 } , b _ { 2 }$ , and $b _ { 1 }$ are found systematically as follows:

$$
\begin{array}{l} b _ {3} = \left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] _ {s = - 1} \\ = (s ^ {2} + 2 s + 3) _ {s = - 1} \\ = 2 \\ b _ {2} = \left\{\frac {d}{d s} \left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] \right\} _ {s = - 1} \\ = \left[ \frac {d}{d s} (s ^ {2} + 2 s + 3) \right] _ {s = - 1} \\ = (2 s + 2) _ {s = - 1} \\ = 0 \\ b _ {1} = \frac {1}{2 !} \left\{\frac {d ^ {2}}{d s ^ {2}} \left[ (s + 1) ^ {3} \frac {B (s)}{A (s)} \right] \right\} _ {s = - 1} \\ = \frac {1}{2 !} \left[ \frac {d ^ {2}}{d s ^ {2}} (s ^ {2} + 2 s + 3) \right] _ {s = - 1} \\ = \frac {1}{2} (2) = 1 \\ \end{array}
$$

We thus obtain
