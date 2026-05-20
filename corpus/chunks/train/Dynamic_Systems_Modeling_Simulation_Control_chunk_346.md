# 7.2 ANALYTICAL SOLUTIONS TO LINEAR DIFFERENTIAL EQUATIONS

In this section we present an overview of the solution of linear ODEs with constant coefficients. To begin, consider the general nth-order input-output (I/O) equation

$$a _ {n} y ^ {(n)} + a _ {n - 1} y ^ {(n - 1)} + \dots + a _ {2} \ddot {y} + a _ {1} \dot {y} + a _ {0} y = b _ {m} u ^ {(m)} + \dots + b _ {1} \dot {u} + b _ {0} u \tag {7.1}$$

where $y ^ { ( n ) } \equiv d ^ { n } y / d t ^ { n }$ and $u ^ { ( m ) } \equiv d ^ { m } u / d t ^ { m }$ . We can replace the right-hand side (the input terms) with a general “forcing function” f (t) so that Eq. (7.1) becomes

$$a _ {n} y ^ {(n)} + a _ {n - 1} y ^ {(n - 1)} + \dots + a _ {2} \ddot {y} + a _ {1} \dot {y} + a _ {0} y = f (t) \tag {7.2}$$

The complete or total solution to Eq. (7.2) has the general form

$$y (t) = y _ {H} (t) + y _ {P} (t) \tag {7.3}$$

where $y _ { H } ( t )$ is the called the homogeneous solution and $y _ { P } ( t )$ is called the particular solution. The homogeneous (or complementary) solution $y _ { H } ( t )$ is the solution to the differential equation (7.2) when the right-hand side (the input) is zero:

$$a _ {n} y _ {H} ^ {(n)} + a _ {n - 1} y _ {H} ^ {(n - 1)} + \dots + a _ {2} \ddot {y} _ {H} + a _ {1} \dot {y} _ {H} + a _ {0} y _ {H} = 0 \tag {7.4}$$

Equation (7.4) is the homogeneous differential equation. Euler noted that the homogeneous solution has the form $y _ { H } ( t ) = c e ^ { r t }$ , where c is a constant. Taking successive time derivative of this assumed solution form yields

$$\dot {y} _ {H} (t) = r c e ^ {r t}, \ddot {y} _ {H} (t) = r ^ {2} c e ^ {r t}, \dddot {y} _ {H} (t) = r ^ {3} c e ^ {r t}, \dots y _ {H} ^ {(n)} (t) = r ^ {n} c e ^ {r t}$$

After substituting these derivatives into Eq. (7.4) we obtain

$$\left(a _ {n} r ^ {n} + a _ {n - 1} r ^ {n - 1} + \dots + a _ {2} r ^ {2} + a _ {1} r + a _ {0}\right) c e ^ {r t} = 0 \tag {7.5}$$

Because $c e ^ { r t }$ cannot be zero for all time, the terms in the bracket in Eq. (7.5) must be zero. Therefore, we obtain the nth-order polynomial equation

$$a _ {n} r ^ {n} + a _ {n - 1} r ^ {n - 1} + \dots + a _ {2} r ^ {2} + a _ {1} r + a _ {0} = 0 \tag {7.6}$$

Equation (7.6) is called the characteristic equation, and its solution yields the characteristic roots $r _ { i } ,$ $i = 1 , 2 , \dots , n .$ If all n roots are distinct or unique, then the homogeneous solution is

$$y _ {H} (t) = c _ {1} e ^ {r _ {1} t} + c _ {2} e ^ {r _ {2} t} + c _ {3} e ^ {r _ {3} t} + \dots + c _ {n} e ^ {r _ {n} t} \tag {7.7}$$

If we have two repeated roots (say $r _ { 1 } = r _ { 2 } )$ , then the homogeneous solution is
