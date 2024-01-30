Overview ¶
Package big implements arbitrary-precision arithmetic (big numbers). The following numeric types are supported:

Int    signed integers
Rat    rational numbers
Float  floating-point numbers
The zero value for an Int, Rat, or Float correspond to 0. Thus, new values can be declared in the usual ways and denote 0 without further initialization:

var x Int        // &x is an *Int of value 0
var r = &Rat{}   // r is a *Rat of value 0
y := new(Float)  // y is a *Float of value 0
Alternatively, new values can be allocated and initialized with factory functions of the form:

func NewT(v V) *T
For instance, NewInt(x) returns an *Int set to the value of the int64 argument x, NewRat(a, b) returns a *Rat set to the fraction a/b where a and b are int64 values, and NewFloat(f) returns a *Float initialized to the float64 argument f. More flexibility is provided with explicit setters, for instance:

var z1 Int
z1.SetUint64(123)                 // z1 := 123
z2 := new(Rat).SetFloat64(1.25)   // z2 := 5/4
z3 := new(Float).SetInt(z1)       // z3 := 123.0
Setters, numeric operations and predicates are represented as methods of the form:

func (z *T) SetV(v V) *T          // z = v
func (z *T) Unary(x *T) *T        // z = unary x
func (z *T) Binary(x, y *T) *T    // z = x binary y
func (x *T) Pred() P              // p = pred(x)
with T one of Int, Rat, or Float. For unary and binary operations, the result is the receiver (usually named z in that case; see below); if it is one of the operands x or y it may be safely overwritten (and its memory reused).

Arithmetic expressions are typically written as a sequence of individual method calls, with each call corresponding to an operation. The receiver denotes the result and the method arguments are the operation's operands. For instance, given three *Int values a, b and c, the invocation

c.Add(a, b)
computes the sum a + b and stores the result in c, overwriting whatever value was held in c before. Unless specified otherwise, operations permit aliasing of parameters, so it is perfectly ok to write

sum.Add(sum, x)
to accumulate values x in a sum.

(By always passing in a result value via the receiver, memory use can be much better controlled. Instead of having to allocate new memory for each result, an operation can reuse the space allocated for the result value, and overwrite that value with the new result in the process.)

Notational convention: Incoming method parameters (including the receiver) are named consistently in the API to clarify their use. Incoming operands are usually named x, y, a, b, and so on, but never z. A parameter specifying the result is named z (typically the receiver).

For instance, the arguments for (*Int).Add are named x and y, and because the receiver specifies the result destination, it is called z:

func (z *Int) Add(x, y *Int) *Int
Methods of this form typically return the incoming receiver as well, to enable simple call chaining.

Methods which don't require a result value to be passed in (for instance, Int.Sign), simply return the result. In this case, the receiver is typically the first operand, named x:

func (x *Int) Sign() int
Various methods support conversions between strings and corresponding numeric values, and vice versa: *Int, *Rat, and *Float values implement the Stringer interface for a (default) string representation of the value, but also provide SetString methods to initialize a value from a string in a variety of supported formats (see the respective SetString documentation).

Finally, *Int, *Rat, and *Float satisfy the fmt package's Scanner interface for scanning and (except for *Rat) the Formatter interface for formatted printing.

Example (EConvergents) ¶
Example (Fibonacci) ¶
Example (Sqrt2) ¶
Index ¶
Constants
func Jacobi(x, y *Int) int
type Accuracy
func (i Accuracy) String() string
type ErrNaN
func (err ErrNaN) Error() string
type Float
func NewFloat(x float64) *Float
func ParseFloat(s string, base int, prec uint, mode RoundingMode) (f *Float, b int, err error)
func (z *Float) Abs(x *Float) *Float
func (x *Float) Acc() Accuracy
func (z *Float) Add(x, y *Float) *Float
func (x *Float) Append(buf []byte, fmt byte, prec int) []byte
func (x *Float) Cmp(y *Float) int
func (z *Float) Copy(x *Float) *Float
func (x *Float) Float32() (float32, Accuracy)
func (x *Float) Float64() (float64, Accuracy)
func (x *Float) Format(s fmt.State, format rune)
func (z *Float) GobDecode(buf []byte) error
func (x *Float) GobEncode() ([]byte, error)
func (x *Float) Int(z *Int) (*Int, Accuracy)
func (x *Float) Int64() (int64, Accuracy)
func (x *Float) IsInf() bool
func (x *Float) IsInt() bool
func (x *Float) MantExp(mant *Float) (exp int)
func (x *Float) MarshalText() (text []byte, err error)
func (x *Float) MinPrec() uint
func (x *Float) Mode() RoundingMode
func (z *Float) Mul(x, y *Float) *Float
func (z *Float) Neg(x *Float) *Float
func (z *Float) Parse(s string, base int) (f *Float, b int, err error)
func (x *Float) Prec() uint
func (z *Float) Quo(x, y *Float) *Float
func (x *Float) Rat(z *Rat) (*Rat, Accuracy)
func (z *Float) Scan(s fmt.ScanState, ch rune) error
func (z *Float) Set(x *Float) *Float
func (z *Float) SetFloat64(x float64) *Float
func (z *Float) SetInf(signbit bool) *Float
func (z *Float) SetInt(x *Int) *Float
func (z *Float) SetInt64(x int64) *Float
func (z *Float) SetMantExp(mant *Float, exp int) *Float
func (z *Float) SetMode(mode RoundingMode) *Float
func (z *Float) SetPrec(prec uint) *Float
func (z *Float) SetRat(x *Rat) *Float
func (z *Float) SetString(s string) (*Float, bool)
func (z *Float) SetUint64(x uint64) *Float
func (x *Float) Sign() int
func (x *Float) Signbit() bool
func (z *Float) Sqrt(x *Float) *Float
func (x *Float) String() string
func (z *Float) Sub(x, y *Float) *Float
func (x *Float) Text(format byte, prec int) string
func (x *Float) Uint64() (uint64, Accuracy)
func (z *Float) UnmarshalText(text []byte) error
type Int
func NewInt(x int64) *Int
func (z *Int) Abs(x *Int) *Int
func (z *Int) Add(x, y *Int) *Int
func (z *Int) And(x, y *Int) *Int
func (z *Int) AndNot(x, y *Int) *Int
func (x *Int) Append(buf []byte, base int) []byte
func (z *Int) Binomial(n, k int64) *Int
func (x *Int) Bit(i int) uint
func (x *Int) BitLen() int
func (x *Int) Bits() []Word
func (x *Int) Bytes() []byte
func (x *Int) Cmp(y *Int) (r int)
func (x *Int) CmpAbs(y *Int) int
func (z *Int) Div(x, y *Int) *Int
func (z *Int) DivMod(x, y, m *Int) (*Int, *Int)
func (z *Int) Exp(x, y, m *Int) *Int
func (x *Int) FillBytes(buf []byte) []byte
func (x *Int) Format(s fmt.State, ch rune)
func (z *Int) GCD(x, y, a, b *Int) *Int
func (z *Int) GobDecode(buf []byte) error
func (x *Int) GobEncode() ([]byte, error)
func (x *Int) Int64() int64
func (x *Int) IsInt64() bool
func (x *Int) IsUint64() bool
func (z *Int) Lsh(x *Int, n uint) *Int
func (x *Int) MarshalJSON() ([]byte, error)
func (x *Int) MarshalText() (text []byte, err error)
func (z *Int) Mod(x, y *Int) *Int
func (z *Int) ModInverse(g, n *Int) *Int
func (z *Int) ModSqrt(x, p *Int) *Int
func (z *Int) Mul(x, y *Int) *Int
func (z *Int) MulRange(a, b int64) *Int
func (z *Int) Neg(x *Int) *Int
func (z *Int) Not(x *Int) *Int
func (z *Int) Or(x, y *Int) *Int
func (x *Int) ProbablyPrime(n int) bool
func (z *Int) Quo(x, y *Int) *Int
func (z *Int) QuoRem(x, y, r *Int) (*Int, *Int)
func (z *Int) Rand(rnd *rand.Rand, n *Int) *Int
func (z *Int) Rem(x, y *Int) *Int
func (z *Int) Rsh(x *Int, n uint) *Int
func (z *Int) Scan(s fmt.ScanState, ch rune) error
func (z *Int) Set(x *Int) *Int
func (z *Int) SetBit(x *Int, i int, b uint) *Int
func (z *Int) SetBits(abs []Word) *Int
func (z *Int) SetBytes(buf []byte) *Int
func (z *Int) SetInt64(x int64) *Int
func (z *Int) SetString(s string, base int) (*Int, bool)
func (z *Int) SetUint64(x uint64) *Int
func (x *Int) Sign() int
func (z *Int) Sqrt(x *Int) *Int
func (x *Int) String() string
func (z *Int) Sub(x, y *Int) *Int
func (x *Int) Text(base int) string
func (x *Int) TrailingZeroBits() uint
func (x *Int) Uint64() uint64
func (z *Int) UnmarshalJSON(text []byte) error
func (z *Int) UnmarshalText(text []byte) error
func (z *Int) Xor(x, y *Int) *Int
type Rat
func NewRat(a, b int64) *Rat
func (z *Rat) Abs(x *Rat) *Rat
func (z *Rat) Add(x, y *Rat) *Rat
func (x *Rat) Cmp(y *Rat) int
func (x *Rat) Denom() *Int
func (x *Rat) Float32() (f float32, exact bool)
func (x *Rat) Float64() (f float64, exact bool)
func (x *Rat) FloatString(prec int) string
func (z *Rat) GobDecode(buf []byte) error
func (x *Rat) GobEncode() ([]byte, error)
func (z *Rat) Inv(x *Rat) *Rat
func (x *Rat) IsInt() bool
func (x *Rat) MarshalText() (text []byte, err error)
func (z *Rat) Mul(x, y *Rat) *Rat
func (z *Rat) Neg(x *Rat) *Rat
func (x *Rat) Num() *Int
func (z *Rat) Quo(x, y *Rat) *Rat
func (x *Rat) RatString() string
func (z *Rat) Scan(s fmt.ScanState, ch rune) error
func (z *Rat) Set(x *Rat) *Rat
func (z *Rat) SetFloat64(f float64) *Rat
func (z *Rat) SetFrac(a, b *Int) *Rat
func (z *Rat) SetFrac64(a, b int64) *Rat
func (z *Rat) SetInt(x *Int) *Rat
func (z *Rat) SetInt64(x int64) *Rat
func (z *Rat) SetString(s string) (*Rat, bool)
func (z *Rat) SetUint64(x uint64) *Rat
func (x *Rat) Sign() int
func (x *Rat) String() string
func (z *Rat) Sub(x, y *Rat) *Rat
func (z *Rat) UnmarshalText(text []byte) error
type RoundingMode
func (i RoundingMode) String() string
type Word