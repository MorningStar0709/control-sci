# 11.5.3 Conversion of discrete transfer function to digital lter

First, we unwrap the transfer function so that it is now the Z transform of a digital lter. Unwrapping is actually a simple step. For example, using our rst example above,

$$C (z) = \frac {F (z)}{E (z)} = \frac {5 0}{1 2} \frac {(z + 1)}{(z + 0 . 6 6 6 7)}$$

we just cross multiply by the two denominators to get

$$F (z) (z + 0. 6 6 6 7) = \frac {5 0}{1 2} E (z) (z + 1)$$

or

$$z F (z) + 0. 6 6 6 7 F (z) = 4. 1 6 6 7 \left(z E (z) + E (z)\right)$$

Now, there is an important property of the Z-transform:

$$Z \{x [ n - k ] \} = z ^ {- k} X (z)$$

In words, shifting a signal in the time domain by k samples is equivalent to multiplying by $z ^ { - k }$ in the Z domain. Looking at it another way, we have a transform pair:

$$x [ n + k ] \leftrightarrow z ^ {k} X (z)$$

Returning to our example, and multiplying through by $z ^ { - 1 }$ will prove useful so we get:

$$F (z) + 0. 6 6 6 7 z ^ {- 1} F (z) = 4. 1 6 6 7 \left(E (z) + z ^ {- 1} E (z)\right)$$

Applying the delay property to our unwrapped transfer function gives:

$$f (n) + 0. 6 6 6 7 f (n - 1) = 4. 1 6 6 7 (e (n) + e (n - 1))$$

Let's step back a bit and recall that our controller is a relationship between the sampled error in our control system (e(n)) and the sampled controller output (f (n), Figure 11.4). Isolating f (n),

$$f (n) = 4. 1 6 6 7 (e (n) + e (n - 1)) - 0. 6 6 6 7 f (n - 1)$$

This is essentially the line of computer code which denes our controller! We could implement this equation with the block diagram of Figure 11.5.
