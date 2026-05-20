# 6.2.3 Transformations

When blocks are combined into block diagrams, the denitions above can easily be applied to gure out the meaning of the particular combination. Connections include (Figure 6.2):

Series: the output of the rst block is connected to the input of a second block.

Parallel: The output is the sum of the outputs of two blocks with the same input.

Some tranformations are slightly less obvious, but arise easily from Equation 6.1 as well as the properties of linearity.

The simple relationships

$$A (s) \left(x (s) + y (s)\right) \Leftrightarrow A (s) x (s) + A (s) y (s)$$

and

$$y _ {1} (s) = A (s) x (s), \quad y _ {2} (s) = y _ {1} (s) \Leftrightarrow y _ {1} (s) = A (s) x (s), \quad y _ {2} (s) = A (s) x (s)$$

Can be used to manipulate block diagrams as shown in Figure 6.3
