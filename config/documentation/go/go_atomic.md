Overview ¶
Package atomic provides low-level atomic memory primitives useful for implementing synchronization algorithms.

These functions require great care to be used correctly. Except for special, low-level applications, synchronization is better done with channels or the facilities of the sync package. Share memory by communicating; don't communicate by sharing memory.

The swap operation, implemented by the SwapT functions, is the atomic equivalent of:

old = *addr
*addr = new
return old
The compare-and-swap operation, implemented by the CompareAndSwapT functions, is the atomic equivalent of:

if *addr == old {
	*addr = new
	return true
}
return false
The add operation, implemented by the AddT functions, is the atomic equivalent of:

*addr += delta
return *addr
The load and store operations, implemented by the LoadT and StoreT functions, are the atomic equivalents of "return *addr" and "*addr = val".

In the terminology of the Go memory model, if the effect of an atomic operation A is observed by atomic operation B, then A “synchronizes before” B. Additionally, all the atomic operations executed in a program behave as though executed in some sequentially consistent order. This definition provides the same semantics as C++'s sequentially consistent atomics and Java's volatile variables.

func AddInt32(addr *int32, delta int32) (new int32)
func AddInt64(addr *int64, delta int64) (new int64)
func AddUint32(addr *uint32, delta uint32) (new uint32)
func AddUint64(addr *uint64, delta uint64) (new uint64)
func AddUintptr(addr *uintptr, delta uintptr) (new uintptr)
func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)
func CompareAndSwapInt64(addr *int64, old, new int64) (swapped bool)
func CompareAndSwapPointer(addr *unsafe.Pointer, old, new unsafe.Pointer) (swapped bool)
func CompareAndSwapUint32(addr *uint32, old, new uint32) (swapped bool)
func CompareAndSwapUint64(addr *uint64, old, new uint64) (swapped bool)
func CompareAndSwapUintptr(addr *uintptr, old, new uintptr) (swapped bool)
func LoadInt32(addr *int32) (val int32)
func LoadInt64(addr *int64) (val int64)
func LoadPointer(addr *unsafe.Pointer) (val unsafe.Pointer)
func LoadUint32(addr *uint32) (val uint32)
func LoadUint64(addr *uint64) (val uint64)
func LoadUintptr(addr *uintptr) (val uintptr)
func StoreInt32(addr *int32, val int32)
func StoreInt64(addr *int64, val int64)
func StorePointer(addr *unsafe.Pointer, val unsafe.Pointer)
func StoreUint32(addr *uint32, val uint32)
func StoreUint64(addr *uint64, val uint64)
func StoreUintptr(addr *uintptr, val uintptr)
func SwapInt32(addr *int32, new int32) (old int32)
func SwapInt64(addr *int64, new int64) (old int64)
func SwapPointer(addr *unsafe.Pointer, new unsafe.Pointer) (old unsafe.Pointer)
func SwapUint32(addr *uint32, new uint32) (old uint32)
func SwapUint64(addr *uint64, new uint64) (old uint64)
func SwapUintptr(addr *uintptr, new uintptr) (old uintptr)
type Bool
func (x *Bool) CompareAndSwap(old, new bool) (swapped bool)
func (x *Bool) Load() bool
func (x *Bool) Store(val bool)
func (x *Bool) Swap(new bool) (old bool)
type Int32
func (x *Int32) Add(delta int32) (new int32)
func (x *Int32) CompareAndSwap(old, new int32) (swapped bool)
func (x *Int32) Load() int32
func (x *Int32) Store(val int32)
func (x *Int32) Swap(new int32) (old int32)
type Int64
func (x *Int64) Add(delta int64) (new int64)
func (x *Int64) CompareAndSwap(old, new int64) (swapped bool)
func (x *Int64) Load() int64
func (x *Int64) Store(val int64)
func (x *Int64) Swap(new int64) (old int64)
type Pointer
func (x *Pointer[T]) CompareAndSwap(old, new *T) (swapped bool)
func (x *Pointer[T]) Load() *T
func (x *Pointer[T]) Store(val *T)
func (x *Pointer[T]) Swap(new *T) (old *T)
type Uint32
func (x *Uint32) Add(delta uint32) (new uint32)
func (x *Uint32) CompareAndSwap(old, new uint32) (swapped bool)
func (x *Uint32) Load() uint32
func (x *Uint32) Store(val uint32)
func (x *Uint32) Swap(new uint32) (old uint32)
type Uint64
func (x *Uint64) Add(delta uint64) (new uint64)
func (x *Uint64) CompareAndSwap(old, new uint64) (swapped bool)
func (x *Uint64) Load() uint64
func (x *Uint64) Store(val uint64)
func (x *Uint64) Swap(new uint64) (old uint64)
type Uintptr
func (x *Uintptr) Add(delta uintptr) (new uintptr)
func (x *Uintptr) CompareAndSwap(old, new uintptr) (swapped bool)
func (x *Uintptr) Load() uintptr
func (x *Uintptr) Store(val uintptr)
func (x *Uintptr) Swap(new uintptr) (old uintptr)
type Value
func (v *Value) CompareAndSwap(old, new any) (swapped bool)
func (v *Value) Load() (val any)
func (v *Value) Store(val any)
func (v *Value) Swap(new any) (old any)