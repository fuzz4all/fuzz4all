LinearFunction¶
CLASSLinearFunction(linear, validate_input=False)[SOURCE]¶
Bases: Gate

A linear reversible circuit on n qubits.

Internally, a linear function acting on n qubits is represented as a n x n matrix of 0s and 1s in numpy array format.

A linear function can be synthesized into CX and SWAP gates using the Patel–Markov–Hayes algorithm, as implemented in cnot_synth() based on reference [1].

For efficiency, the internal n x n matrix is stored in the format expected by cnot_synth, which is the big-endian (and not the little-endian) bit-ordering convention.

Example: the circuit

q_0: ──■──
     ┌─┴─┐
q_1: ┤ X ├
     └───┘
q_2: ─────
is represented by a 3x3 linear matrix



References:

[1] Ketan N. Patel, Igor L. Markov, and John P. Hayes, Optimal synthesis of linear reversible circuits, Quantum Inf. Comput. 8(3) (2008). Online at umich.edu.

Create a new linear function.

Parameters:
linear (list[list] or ndarray[bool] or QuantumCircuit) – either an n x n matrix, describing the linear function, or a quantum circuit composed of linear gates only (currently supported gates are CX and SWAP).

validate_input (bool | None) – if True, performs more expensive input validation checks, such as checking that a given n x n matrix is invertible.

Raises:
CircuitError – if the input is invalid: either a matrix is non {square, invertible}, or a quantum circuit contains non-linear gates.

Methods Defined Here

is_permutation

Returns whether this linear function is a permutation, that is whether every row and every column of the n x n matrix has exactly one 1.

permutation_pattern

This method first checks if a linear function is a permutation and raises a qiskit.circuit.exceptions.CircuitError if not.

synthesize

Synthesizes the linear function into a quantum circuit.

validate_parameter

Parameter validation

Attributes

condition_bits¶
Get Clbits in condition.

decompositions¶
Get the decompositions of the instruction from the SessionEquivalenceLibrary.

definition¶
Return definition in terms of other basic gates.

duration¶
Get the duration.

label¶
Return instruction label

linear¶
Returns the n x n matrix representing this linear function

name¶
Return the name.

num_clbits¶
Return the number of clbits.

num_qubits¶
Return the number of qubits.

original_circuit¶
Returns the original circuit used to construct this linear function (including None, when the linear function is not constructed from a circuit).

params¶
return instruction params.

unit¶
Get the time unit of duration.

Gate¶
CLASSGate(name, num_qubits, params, label=None)[SOURCE]¶
Bases: Instruction

Unitary gate.

Create a new gate.

Parameters:
name (str) – The Qobj name of the gate.

num_qubits (int) – The number of qubits the gate acts on.

params (list) – A list of parameters.

label (str | None) – An optional label for the gate.

Methods

add_decomposition

Add a decomposition of the instruction to the SessionEquivalenceLibrary.

assemble

Assemble a QasmQobjInstruction

broadcast_arguments

Validation and handling of the arguments and its relationship.

c_if

Set a classical equality condition on this instruction between the register or cbit classical and value val.

control

Return controlled version of gate.

copy

Copy of the instruction.

inverse

Invert this instruction.

is_parameterized

Return True .IFF.

power

Creates a unitary gate as gate^exponent.

qasm

Return a default OpenQASM string for the instruction.

repeat

Creates an instruction with gate repeated n amount of times.

reverse_ops

For a composite instruction, reverse the order of sub-instructions.

soft_compare

Soft comparison between gates.

to_matrix

Return a Numpy.array for the gate unitary matrix.

validate_parameter

Gate parameters should be int, float, or ParameterExpression

Attributes

condition_bits¶
Get Clbits in condition.

decompositions¶
Get the decompositions of the instruction from the SessionEquivalenceLibrary.

definition¶
Return definition in terms of other basic gates.

duration¶
Get the duration.

label¶
Return instruction label

name¶
Return the name.

num_clbits¶
Return the number of clbits.

num_qubits¶
Return the number of qubits.

params¶
return instruction params.

unit¶
Get the time unit of duration.