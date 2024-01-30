Union declaration
 C C language Declarations 
A union is a type consisting of a sequence of members whose storage overlaps (as opposed to struct, which is a type consisting of a sequence of members whose storage is allocated in an ordered sequence). The value of at most one of the members can be stored in a union at any one time.

The type specifier for a union is identical to the struct type specifier except for the keyword used:

Syntax
union attr-spec-seq(optional) name(optional) { struct-declaration-list }	(1)	
union attr-spec-seq(optional) name	(2)	
name	-	the name of the union that's being defined
struct-declaration-list	-	any number of variable declarations, bit-field declarations, and static assert declarations. Members of incomplete type and members of function type are not allowed.
attr-spec-seq	-	(C23)optional list of attributes, applied to the union type, not allowed for (2) if such form is not followed by a ; (i.e. not a forward declaration).
Explanation
The union is only as big as necessary to hold its largest member (additional unnamed trailing padding may also be added). The other members are allocated in the same bytes as part of that largest member.

A pointer to a union can be cast to a pointer to each of its members (if a union has bit-field members, the pointer to a union can be cast to the pointer to the bit-field's underlying type). Likewise, a pointer to any member of a union can be cast to a pointer to the enclosing union.

If the member used to access the contents of a union is not the same as the member last used to store a value, the object representation of the value that was stored is reinterpreted as an object representation of the new type (this is known as type punning). If the size of the new type is larger than the size of the last-written type, the contents of the excess bytes are unspecified (and may be a trap representation). Before C99 TC3 (DR 283) this behaviour was undefined, but commonly implemented this way.

(since C99)
Similar to struct, an unnamed member of a union whose type is a union without name is known as anonymous union. Every member of an anonymous union is considered to be a member of the enclosing struct or union keeping their union layout. This applies recursively if the enclosing struct or union is also anonymous.

struct v
{
   union // anonymous union
   {
       struct { int i, j; }; // anonymous structure
       struct { long k, l; } w;
   };
   int m;
} v1;
 
v1.i = 2;   // valid
v1.k = 3;   // invalid: inner structure is not anonymous
v1.w.k = 5; // valid
Similar to struct, the behavior of the program is undefined if union is defined without any named members (including those obtained via anonymous nested structs or unions).

(since C11)
Keywords
union

Notes
See struct initialization for the rules about initialization of structs and unions.