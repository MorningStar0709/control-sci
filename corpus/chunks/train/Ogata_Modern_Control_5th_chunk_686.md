If the matrix A cannot be transformed into a diagonal matrix, then by use of a suitable transformation matrix S, we can transform A into a Jordan canonical form, or

$$\mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} = \mathbf {J}$$

where J is in the Jordan canonical form.

Let us define

$$\mathbf {x} = \mathbf {S z}$$

Then Equations (9–66) and (9–67) can be written

$$\dot {\mathbf {z}} = \mathbf {S} ^ {- 1} \mathbf {A} \mathbf {S} \mathbf {z} = \mathbf {J} \mathbf {z}\mathbf {y} = \mathbf {C S z}$$

Hence,

$$\mathbf {y} (t) = \mathbf {C S e} ^ {\mathbf {J} t} \mathbf {z} (0)$$

The system is completely observable if (1) no two Jordan blocks in J are associated with the same eigenvalues, (2) no columns of CS that correspond to the first row of each Jordan block consist of zero elements, and (3) no columns of CS that correspond to distinct eigenvalues consist of zero elements.

To clarify condition (2), in Example 9–16 we have encircled by dashed lines the columns of CS that correspond to the first row of each Jordan block.

EXAMPLE 9–16

The following systems are completely observable.
