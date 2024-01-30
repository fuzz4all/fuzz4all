C keywords
 C C language Keywords 
This is a list of reserved keywords in C. Since they are used by the language, these keywords are not available for re-definition. As an exception, they are not considered reserved in attribute-tokens (since C23)

alignas (C23)
alignof (C23)
auto
bool (C23)
break
case
char
const
constexpr (C23)
continue
default
do
double
else
enum
extern
false (C23)
float
for
goto
if
inline (C99)
int
long
nullptr (C23)
register
restrict (C99)
return
short
signed
sizeof
static
static_assert (C23)
struct
switch
thread_local (C23)
true (C23)
typedef
typeof (C23)
typeof_unqual (C23)
union
unsigned
void
volatile
while
_Alignas (C11)
_Alignof (C11)
_Atomic (C11)
_BitInt (C23)
_Bool (C99)
_Complex (C99)
_Decimal128 (C23)
_Decimal32 (C23)
_Decimal64 (C23)
_Generic (C11)
_Imaginary (C99)
_Noreturn (C11)
_Static_assert (C11)
_Thread_local (C11)
The most common keywords that begin with an underscore are generally used through their convenience macros:

keyword	used as	defined in
_Alignas (C11)	alignas (removed in C23)	stdalign.h
_Alignof (C11)	alignof (removed in C23)	stdalign.h
_Atomic (C11)	atomic_bool, atomic_int, ...	stdatomic.h
_BitInt (C23)	(no macro)	
_Bool (C99)	bool (removed in C23)	stdbool.h
_Complex (C99)	complex	complex.h
_Decimal128 (C23)	(no macro)	
_Decimal32 (C23)	(no macro)	
_Decimal64 (C23)	(no macro)	
_Generic (C11)	(no macro)	
_Imaginary (C99)	imaginary	complex.h
_Noreturn (C11)	noreturn	stdnoreturn.h
_Static_assert (C11)	static_assert (removed in C23)	assert.h
_Thread_local (C11)	thread_local (removed in C23)	threads.h
Also, each name that begins with a double underscore __ or an underscore _ followed by an uppercase letter is reserved: see identifier for details.

Note that digraphs <%, %>, <:, :>, %:, and %:%: provide an alternative way to represent standard tokens.

The following tokens are recognized by the preprocessor when they are used within the context of a preprocessor directive:

if
elif
else
endif
ifdef
ifndef
elifdef (C23)
elifndef (C23)
define
undef
include
embed (C23)
line
error
warning (C23)
pragma
defined
__has_include (C23)
__has_embed (C23)
__has_c_attribute (C23)

The following tokens are recognized by the preprocessor when they are used outside the context of a preprocessor directive:

_Pragma (C99)

The following additional keywords are classified as extensions and conditionally-supported:

asm
fortran

