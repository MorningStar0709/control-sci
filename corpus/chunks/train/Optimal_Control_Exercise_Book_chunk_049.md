# Solution:

We want to maximize the area under a curve of fixed length. Let’s consider the Dido’s problem formulated as following:

$$\max _ {y: [ a, b ] \rightarrow \mathbb {R}} J (y) = \int_ {a} ^ {b} y (x) d x \tag {141}\text { subject to } y (a) = y (b) = 0, \quad \int_ {a} ^ {b} \sqrt {1 + (y ^ {\prime} (x)) ^ {2}} d x = C _ {0} \tag {142}$$

Let’s also consider the simplified notation $y ( x ) = y$ and $y ^ { \prime } ( x ) = y ^ { \prime }$ for convenience. Thus, we can consider the first-order necessary condition for integral constrained optimality:

$$\left(L _ {y} - \frac {d}{d x} L _ {y ^ {\prime}}\right) + \lambda \left(M _ {y} - \frac {d}{d x} M _ {y ^ {\prime}}\right) = 0, \quad \forall x \in [ a, b ] \tag {143}$$

where $L = y$ and $M = \sqrt { 1 + y ^ { \prime 2 } }$ . Substituting, we obtain:

$$1 - \lambda \frac {d}{d x} \frac {y ^ {\prime}}{\sqrt {1 + y ^ {\prime 2}}} = 0 \tag {144}\frac {d}{d x} \frac {\lambda y ^ {\prime}}{\sqrt {1 + y ^ {\prime 2}}} = 1 \tag {145}\frac {d}{d x} \frac {\lambda y ^ {\prime}}{\sqrt {1 + y ^ {\prime 2}}} = x + c _ {0} \tag {146}\lambda^ {2} y ^ {\prime 2} = (1 + y ^ {\prime 2}) (x + c _ {0}) ^ {2} \tag {147}\left(\lambda^ {2} - \left(x - c _ {0}\right) ^ {2}\right) y ^ {\prime 2} = \left(x + c _ {0}\right) ^ {2} \tag {148}y ^ {\prime} = \frac {x + c _ {o}}{\sqrt {\lambda^ {2} - (x - c _ {0}) ^ {2}}} \tag {149}y ^ {\prime} = \int \frac {x + c _ {o}}{\sqrt {\lambda^ {2} - (x - c _ {0}) ^ {2}}} d x \tag {150}$$

We can integrate by substituting $u = \lambda ^ { 2 } - ( x + c _ { 0 } ) ^ { 2 }$ and $- d u / 2 = ( x + c _ { 0 } ) d x$ , thus:

$$y (u) = - \frac {1}{2} \int \frac {d u}{\sqrt {u}} = - \sqrt {u} + c _ {1} \tag {152}$$

Substituting again, we get:

$$y = - \sqrt {\lambda^ {2} - (x + c _ {0}) ^ {2}} + c 1 \tag {153}(x + c _ {0}) ^ {2} + (y - c _ {1}) ^ {2} = \lambda^ {2} \tag {154}$$

which describes a circle. We can assert that, given the geometry of the problem, this extremal should be indeed a maximizer of the area functional and not a minimizer and thus we have shown that curves solving Dido’s problem are circular arcs. 
