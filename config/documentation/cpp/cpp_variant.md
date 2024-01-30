std::variant
 C++ Utilities library std::variant
Defined in header <variant>
template< class... Types >
class variant;
(since C++17)
The class template std::variant represents a type-safe union. An instance of std::variant at any given time either holds a value of one of its alternative types, or in the case of error - no value (this state is hard to achieve, see valueless_by_exception).

As with unions, if a variant holds a value of some object type T, the object representation of T is allocated directly within the object representation of the variant itself. Variant is not allowed to allocate additional (dynamic) memory.

A variant is not permitted to hold references, arrays, or the type void. Empty variants are also ill-formed (std::variant<std::monostate> can be used instead).

A variant is permitted to hold the same type more than once, and to hold differently cv-qualified versions of the same type.

Consistent with the behavior of unions during aggregate initialization, a default-constructed variant holds a value of its first alternative, unless that alternative is not default-constructible (in which case the variant is not default-constructible either). The helper class std::monostate can be used to make such variants default-constructible.

Template parameters
Types	-	the types that may be stored in this variant. All types must meet the Destructible requirements (in particular, array types and non-object types are not allowed).
Member functions
(constructor)

constructs the variant object
(public member function)
(destructor)

destroys the variant, along with its contained value
(public member function)
operator=

assigns a variant
(public member function)
Observers
index

returns the zero-based index of the alternative held by the variant
(public member function)
valueless_by_exception

checks if the variant is in the invalid state
(public member function)
Modifiers
emplace

constructs a value in the variant, in place
(public member function)
swap

swaps with another variant
(public member function)
Non-member functions
visit

(C++17)

calls the provided functor with the arguments held by one or more variants
(function template)
holds_alternative

(C++17)

checks if a variant currently holds a given type
(function template)
std::get(std::variant)

(C++17)

reads the value of the variant given the index or the type (if the type is unique), throws on error
(function template)
get_if

(C++17)

obtains a pointer to the value of a pointed-to variant given the index or the type (if unique), returns null on error
(function template)
operator==
operator!=
operator<
operator<=
operator>
operator>=
operator<=>

(C++17)
(C++17)
(C++17)
(C++17)
(C++17)
(C++17)
(C++20)

compares variant objects as their contained values
(function template)
std::swap(std::variant)

(C++17)

specializes the std::swap algorithm
(function template)
Helper classes
monostate

(C++17)

placeholder type for use as the first alternative in a variant of non-default-constructible types
(class)
bad_variant_access

(C++17)

exception thrown on invalid accesses to the value of a variant
(class)
variant_size
variant_size_v

(C++17)

obtains the size of the variant's list of alternatives at compile time
(class template) (variable template)
variant_alternative
variant_alternative_t

(C++17)

obtains the type of the alternative specified by its index, at compile time
(class template) (alias template)
std::hash<std::variant>

(C++17)

specializes the std::hash algorithm
(class template specialization)
Helper objects
variant_npos

(C++17)

index of the variant in the invalid state
(constant)
