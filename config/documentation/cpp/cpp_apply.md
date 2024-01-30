std::apply
 C++ Utilities library
Defined in header <tuple>
template< class F, class Tuple >
constexpr decltype(auto) apply( F&& f, Tuple&& t );
(since C++17)
(until C++23)
template< class F, tuple-like Tuple >
constexpr decltype(auto) apply( F&& f, Tuple&& t ) noexcept(/* see below */);
(since C++23)
Invoke the Callable object f with the elements of t as arguments.

Given the exposition-only function apply-impl defined as follows: template<class F, tuple-like Tuple, std::size_t... I> // no constraint on Tuple before C++23
constexpr decltype(auto)
    apply-impl(F&& f, Tuple&& t, std::index_sequence<I...>) // exposition only
{
    return INVOKE(std::forward<F>(f), std::get<I>(std::forward<Tuple>(t))...);
}


The effect is equivalent to return apply-impl(std::forward<F>(f), std::forward<Tuple>(t),
                  std::make_index_sequence<
                      std::tuple_size_v<std::decay_t<Tuple>>>{});.

Parameters
f	-	Callable object to be invoked
t	-	tuple whose elements to be used as arguments to f
Return value
The value returned by f.

Exceptions
(none)

(until C++23)
noexcept specification:
noexcept(
    noexcept(std::invoke(std::forward<F>(f),
                         std::get<Is>(std::forward<Tuple>(t))...))
)
where Is... denotes the parameter pack:

0, 1, ..., std::tuple_size_v<std::remove_reference_t<Tuple>> - 1.
(since C++23)
Notes
Tuple need not be std::tuple, and instead may be anything that supports std::get and std::tuple_size; in particular, std::array and std::pair may be used.

(until C++23)
Tuple is constrained to be tuple-like, i.e. each type therein is required to be a specialization of std::tuple or another type (such as std::array and std::pair) that models tuple-like.

(since C++23)