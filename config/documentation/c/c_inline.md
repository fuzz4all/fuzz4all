inline function specifier
 C C language Functions 
Declares an inline function.

Syntax
inline function_declaration		(since C99)
Explanation
The intent of the inline specifier is to serve as a hint for the compiler to perform optimizations, such as function inlining, which usually require the definition of a function to be visible at the call site. The compilers can (and usually do) ignore presence or absence of the inline specifier for the purpose of optimization.

If the compiler performs function inlining, it replaces a call of that function with its body, avoiding the overhead of a function call (placing data on stack and retrieving the result), which may result in a larger executable as the code for the function has to be repeated multiple times. The result is similar to function-like macros, except that identifiers and macros used in the function refer to the definitions visible at the point of definition, not at the point of call.

Regardless of whether inlining takes place, the following semantics of inline functions are guaranteed:

Any function with internal linkage may be declared static inline with no other restrictions.

A non-static inline function cannot define a non-const function-local static and cannot refer to a file-scope static.

static int x;
inline void f(void)
{
    static int n = 1; // error: non-const static in a non-static inline function
    int k = x; // error: non-static inline function accesses a static variable
}
If a non-static function is declared inline, then it must be defined in the same translation unit. The inline definition that does not use extern is not externally visible and does not prevent other translation units from defining the same function. This makes the inline keyword an alternative to static for defining functions inside header files, which may be included in multiple translation units of the same program.

If a function is declared inline in some translation units, it does not need to be declared inline everywhere: at most one translation unit may also provide a regular, non-inline non-static function, or a function declared extern inline. This one translation unit is said to provide the external definition. In order to avoid undefined behavior, one external definition must exist in the program if the name of the function with external linkage is used in an expression, see one definition rule.

The address of an inline function with external linkage is always the address of the external definition, but when this address is used to make a function call, it's unspecified whether the inline definition (if present in the translation unit) or the external definition is called. The static objects defined within an inline definition are distinct from the static objects defined within the external definition:

inline const char *saddr(void) // the inline definition for use in this file
{
    static const char name[] = "saddr";
    return name;
}
int compare_name(void)
{
    return saddr() == saddr(); // unspecified behavior, one call could be external
}
extern const char *saddr(void); // an external definition is generated, too
A C program should not depend on whether the inline version or the external version of a function is called, otherwise the behavior is unspecified.