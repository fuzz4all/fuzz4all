C++ Utilities library std::expected
Defined in header <expected>
template< class T, class E >
class expected;
(since C++23)
The class template std::expected provides a way to store either of two values. An object of std::expected at any given time either holds an expected value of type T, or an unexpected value of type E. std::expected is never valueless.

The stored value is allocated directly within the storage occupied by the expected object. No dynamic memory allocation takes place.

A program is ill-formed if it instantiates an expected with a reference type, a function type, or a specialization of std::unexpected. In addition, T must not be std::in_place_t or std::unexpect_t.

Template parameters
T	-	the type of the expected value. The type must either be (possibly cv-qualified) void, or meet the Destructible requirements (in particular, array and reference types are not allowed).
E	-	the type of the unexpected value. The type must meet the Destructible requirements, and must be a valid template argument for std::unexpected (in particular, arrays, non-object types, and cv-qualified types are not allowed).
Member types
Member type	Definition
value_type (C++23)	T
error_type (C++23)	E
unexpected_type (C++23)	std::unexpected<E>
rebind (C++23)	template< class U >
using rebind = expected<U, error_type>;

Member functions
(constructor)

(C++23)

constructs the expected object
(public member function)
(destructor)

(C++23)

destroys the expected object, along with its contained value
(public member function)
operator=

(C++23)

assigns contents
(public member function)
Observers
operator->
operator*

(C++23)

accesses the expected value
(public member function)
operator bool
has_value

(C++23)

checks whether the object contains an expected value
(public member function)
value

(C++23)

returns the expected value
(public member function)
error

(C++23)

returns the unexpected value
(public member function)
value_or

(C++23)

returns the expected value if present, another value otherwise
(public member function)
Monadic operations
and_then

(C++23)

returns the result of the given function on the expected value if it exists; otherwise, returns the expected itself
(public member function)
transform

(C++23)

returns an expected containing the transformed expected value if it exists; otherwise, returns the expected itself
(public member function)
or_else

(C++23)

returns the expected itself if it contains an expected value; otherwise, returns the result of the given function on the unexpected value
(public member function)
transform_error

(C++23)

returns the expected itself if it contains an expected value; otherwise, returns an expected containing the transformed unexpected value
(public member function)
Modifiers
emplace

(C++23)

constructs the expected value in-place
(public member function)
swap

(C++23)

exchanges the contents
(public member function)
Non-member functions
operator==

(C++23)

compares expected objects
(function template)
swap(std::expected)

(C++23)

specializes the std::swap algorithm
(function)
Helper classes
unexpected

(C++23)

represented as an unexpected value
(class template)
bad_expected_access

(C++23)

exception indicating checked access to an expected that contains an unexpected value
(class template)
unexpect_t
unexpect

(C++23)

in-place construction tag for unexpected value in expected