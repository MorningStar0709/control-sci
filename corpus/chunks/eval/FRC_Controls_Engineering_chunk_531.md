This is fundamentally the same formula we had before. $f ( x )$ has taken the place of $\displaystyle v _ { n } , e ^ { - 2 \pi i x \xi }$ has taken the place of $( { \hat { i } } + { \hat { j } } ) _ { i }$ , and the sum over i has turned into an integral over $d x .$ , but the underlying concept is the same. To change coordinates in a function space, we simply take the orthogonal projection onto our new basis functions. In the case of the Fourier transform, the function basis is the family of functions of the form $f ( x ) = e ^ { - 2 \pi i x \xi }$ for $\xi \in \mathbb { R }$ . Since these functions are oscillatory at a frequency determined by $\xi ,$ , we can think of this as a “frequency basis”.

![](image/0df99101c470a0f20b6d74f536ccb1b8b1f92efeaaf5bcf9892c570d328dc26b.jpg)

Watch the “Abstract vector spaces” video from 3Blue1Brown’s Essence of linear algebra series for a more geometric introduction to using functions as a basis.

![](image/13b9250753d1fb7fcc39d99ded7bb4bbb84ef710528f265c33b21c248027c828.jpg)

“Abstract vector spaces” (17 minutes)

3Blue1Brown

https://www.3blue1brown.com/lessons/abstract-vector-spaces

Now, the Laplace transform is somewhat more complicated - as it turns out, the Fourier basis is orthogonal, so the analogy to the simpler vector space holds almost-precisely. The Laplace transform is not orthogonal, so we can’t interpret it strictly as a change of coordinates in the traditional sense. However, the intuition is the same: we are taking the orthogonal projection of our original function onto the functions of our new basis set.

$$F (s) = \int_ {0} ^ {\infty} f (t) e ^ {- s t} d t, \mathrm{where} s \in \mathbb {C}$$

Here, it becomes obvious that the Laplace transform is a generalization of the Fourier transform in that the basis family is strictly larger (we have allowed the “frequency” parameter to take complex values, as opposed to merely real values). As a result, the Laplace basis contains functions that grow and decay, while the Fourier basis does not.
