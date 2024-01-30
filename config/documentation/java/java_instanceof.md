Type Comparison Operator instanceof
The type of the RelationalExpression operand of the instanceof operator must be a reference type or the null type; otherwise, a compile-time error occurs.

It is a compile-time error if the ReferenceType mentioned after the instanceof operator does not denote a reference type that is reifiable (§4.7).

If a cast of the RelationalExpression to the ReferenceType would be rejected as a compile-time error, then the instanceof relational expression likewise produces a compile-time error. In such a situation, the result of the instanceof expression could never be true.

At run time, the result of the instanceof operator is true if the value of the RelationalExpression is not null and the reference could be cast (§15.16) to the ReferenceType without raising a ClassCastException. Otherwise the result is false.

Example 15.20.2-1. The instanceof Operator

class Point   { int x, y; }
class Element { int atomicNumber; }
class Test {
    public static void main(String[] args) {
        Point   p = new Point();
        Element e = new Element();
        if (e instanceof Point) {  // compile-time error
            System.out.println("I get your point!");
            p = (Point)e;  // compile-time error
        }
    }
}
This program results in two compile-time errors. The cast (Point)e is incorrect because no instance of Element or any of its possible subclasses (none are shown here) could possibly be an instance of any subclass of Point. The instanceof expression is incorrect for exactly the same reason. If, on the other hand, the class Point were a subclass of Element (an admittedly strange notion in this example):


class Point extends Element { int x, y; }

then the cast would be possible, though it would require a run-time check, and the instanceof expression would then be sensible and valid. The cast (Point)e would never raise an exception because it would not be executed if the value of e could not correctly be cast to type Point.