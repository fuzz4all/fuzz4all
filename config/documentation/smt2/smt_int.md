(theory Ints
 :sorts ((Int 0))

 :funs ((NUMERAL Int) 
        (- Int Int)                 ; negation
        (- Int Int Int :left-assoc) ; subtraction
        (+ Int Int Int :left-assoc) 
        (* Int Int Int :left-assoc)
        (div Int Int Int :left-assoc)
        (mod Int Int Int)
        (abs Int Int)
        (<= Int Int Bool :chainable)
        (<  Int Int Bool :chainable)
        (>= Int Int Bool :chainable)
        (>  Int Int Bool :chainable)
       )

 :funs_description
 "All ranked function symbols of the form
    ((_ divisible n) Int Bool)
  where n is a positive numeral.
 "

 :values
 "The set of values for the sort Int consists of 
  - all numerals,
  - all terms of the form (- n) where n is a numeral other than 0.
 "

 :definition 
 "For every expanded signature, the instance of Ints with that 
  signature is the theory consisting of all Sigma-models that interpret:

  - the sort Int as the set of all integer numbers, 

  - each numeral as the corresponding natural number,

  - (_ divisible n) as the function mapping to true all and only
    the integers that are divisible by n,

  - abs as the absolute value function,

  - div and mod according to Boute's Euclidean definition, that is,
    so as to satify the formula

    (for all ((m Int) (n Int))
      (=> (distinct n 0)
          (let ((q (div m n)) (r (mod m n)))
            (and (= m (+ (* n q) r))
                 (<= 0 r (- (abs n) 1))))))

  - the other function symbols of Ints as expected.
 "

 :notes
 "Regardless of sign of m, 
  when n is positive, (div m n) is the floor of the rational number m/n;
  when n is negative, (div m n) is the ceiling of m/n.

  This contrasts with alternative but less robust definitions of div and mod
  where (div m n) is 
  - always the integer part of m/n (rounding towards 0), or 
  - always the floor of x/y (rounding towards -infinity).
 "
)