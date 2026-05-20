# Example 4.32: Sampling a conditional density

The following result proves useful in the later discussion of particle filtering. Consider conditional densities satisfying the following property

$$p (a, b, c \mid d, e) = p (a \mid b, d) p (b, c \mid e) \tag {4.45}$$

We wish to draw samples of $p ( a , b , c | d , e )$ and we proceed as follows. We draw samples of $p ( b , c | e )$ . Call these samples $( b _ { i } , c _ { i } ) , i = 1 , \ldots , s$ . Next we draw for each $i = 1 , \dots , s$ , one sample of $p ( a | b _ { i } , d )$ . Call these samples $\alpha _ { i }$ . We assemble the s samples $( a _ { i } , b _ { i } , c _ { i } )$ and claim they are samples of the desired density $p ( a , b , c | d , e )$ with uniform weights $\boldsymbol { w } _ { i } = 1 / s$ . Prove or disprove this claim.
