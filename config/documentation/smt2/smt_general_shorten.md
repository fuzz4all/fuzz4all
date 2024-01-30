SMT2 is a standardized input language supported by many SMT solvers. Its syntax is based on S-expressions, inspired by languages in the LISP family. We review some basic elements of its syntax here, particularly the parts that are used by F*’s SMT encoding.

The logic provided by the SMT solver is multi-sorted: the sorts provide a simple type system for the logic, ensuring, e.g., that terms from two different sorts can never be equal. A user can define a new sort T, as shown below:

Every sort comes with a built-in notion of equality. Given two terms p and q of the same sort T, (= p q) is a term of sort Bool expressing their equality.

A new function symbol F, with arguments in sorts sort_1 .. sort_n and returning a result in sort is declared as shown below,

The function symbol F is uninterpreted, meaning that the only information the solver has about F is that it is a function, i.e., when applied to equal arguments F produces equal results.