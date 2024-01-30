SMT2 is a standardized input language supported by many SMT solvers. Its syntax is based on S-expressions, inspired by languages in the LISP family. We review some basic elements of its syntax here, particularly the parts that are used by F*’s SMT encoding.

Multi-sorted logic

The logic provided by the SMT solver is multi-sorted: the sorts provide a simple type system for the logic, ensuring, e.g., that terms from two different sorts can never be equal. A user can define a new sort T, as shown below:

(declare-sort T)
Every sort comes with a built-in notion of equality. Given two terms p and q of the same sort T, (= p q) is a term of sort Bool expressing their equality.

Declaring uninterpreted functions

A new function symbol F, with arguments in sorts sort_1 .. sort_n and returning a result in sort is declared as shown below,

(declare-fun F (sort_1 ... sort_n) sort)
The function symbol F is uninterpreted, meaning that the only information the solver has about F is that it is a function, i.e., when applied to equal arguments F produces equal results.

Theory symbols

SMT2 provides support for several theories, notably integer and real arithmetic. For example, on terms i and j of Int sort, the sort of unbounded integers, the following terms define the expected arithmetic functions:

(+ i j)       ; addition
(- i j)       ; subtraction
(* i j)       ; multiplication
(div i j)     ; Euclidean division
(mod i j)     ; Euclidean modulus
Logical connectives

SMT2 provides basic logical connectives as shown below, where p and q are terms of sort Bool

(and p q)                ; conjunction
(or p q)                 ; disjunction
(not p)                  ; negation
(implies p q)            ; implication
(iff p q)                ; bi-implication
SMT2 also provides support for quantifiers, where the terms below represent a term p with the variables x1 ... xn universally and existentially quantified, respectively.

(forall ((x1 sort_1) ... (xn sort_n)) p)
(exists ((x1 sort_1) ... (xn sort_n)) p)
Attribute annotations

A term p can be decorated with attributes names a_1 .. a_n with values v_1 .. v_n using the following syntax—the ! is NOT to be confused with logical negation.

(! p
   :a_1 v_1
   ...
   :a_n v_n)
A common usage is with quantifiers, as we’ll see below, e.g.,

(forall ((x Int))
        (! (implies (>= x 0) (f x))
           :qid some_identifier))
An SMT2 theory and check-sat

An SMT2 theory is a collection of sort and function symbol declarations, and assertions of facts about them. For example, here’s a simple theory declaring a function symbol f and an assumption that f x y is equivalent to (>= x y)—note, unlike in F*, the assert keyword in SMT2 assumes that a fact is true, rather than checking that it is valid, i.e., assert in SMT2 is like assume in F*.

(declare-fun f (Int Int) Bool)

(assert (forall ((x Int) (y Int))
                (iff (>= y x) (f x y))))
In the context of this theory, one can ask whether some facts about f are valid. For example, to check if f is a transitive function, one asserts the negation of the transitivity property for f and then asks solver to check (using the (check-sat) directive) if the resulting theory is satisfiable.

(assert (not (forall ((x Int) (y Int) (z Int))
                     (implies (and (f x y) (f y z))
                              (f x z)))))
(check-sat)
In this case, the solver very quickly responds with unsat, meaning that there are no models for the theory that contain an interpretation of f compatible with both assertions, or, equivalently, the transitivity of f is true in all models. That is, we expect successful queries to return unsat.