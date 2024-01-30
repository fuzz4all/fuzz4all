goto statement
 C C language Statements 
Transfers control unconditionally to the desired location.

Used when it is otherwise impossible to transfer control to the desired location using conventional constructs.

Syntax
attr-spec-seq(optional) goto label ;		
label	-	target label for the goto statement
attr-spec-seq	-	(C23)optional list of attributes, applied to the goto statement
Explanation
The goto statement causes an unconditional jump (transfer of control) to the statement prefixed by the named label (which must appear in the same function as the goto statement), except when this jump would enter the scope of a variable-length array or another variably-modified type. (since C99)

A label is an identifier followed by a colon (:) and a statement (until C23). Labels are the only identifiers that have function scope: they can be used (in a goto statement) anywhere in the same function in which they appear. There may be multiple labels before any statement.

Entering the scope of a non-variably modified variable is permitted:

goto lab1; // OK: going into the scope of a regular variable
    int n = 5;
lab1:; // Note, n is uninitialized, as if declared by int n;
 
//   goto lab2;   // Error: going into the scope of two VM types
     double a[n]; // a VLA
     int (*p)[n]; // a VM pointer
lab2:
If goto leaves the scope of a VLA, it is deallocated (and may be reallocated if its initialization is executed again):

{
   int n = 1;
label:;
   int a[n]; // re-allocated 10 times, each with a different size
   if (n++ < 10) goto label; // leaving the scope of a VM
}
(since C99)
Keywords
goto

Notes
Because declarations are not statements, a label before a declaration must use a null statement (a semicolon immediately after the colon). Same applies to a label before the end of a block.

(until C23)
C++ imposes additional limitations on the goto statement, but allows labels before declarations (which are statements in C++).