There is a builder interface for the new control-flow operations on QuantumCircuit, such as the new ForLoopOp, IfElseOp, and WhileLoopOp. The interface uses the same circuit methods, i.e. QuantumCircuit.for_loop(), QuantumCircuit.if_test() and QuantumCircuit.while_loop(), which are overloaded so that if the body parameter is not given, they return a context manager. Entering one of these context managers pushes a scope into the circuit, and captures all gate calls (and other scopes) and the resources these use, and builds up the relevant operation at the end. For example, you can now do:

qc = QuantumCircuit(2, 2)
with qc.for_loop(range(5)) as i:
    qc.rx(i * math.pi / 4, 0)

qiskit.circuit.QuantumCircuit.for_loop¶
QuantumCircuit.for_loop(indexset: Iterable[int], loop_parameter: Parameter | None, body: None, qubits: None, clbits: None, *, label: str | None)→ qiskit.circuit.controlflow.for_loop.ForLoopContext[SOURCE]¶
QuantumCircuit.for_loop(indexset: Iterable[int], loop_parameter: Parameter | None, body: QuantumCircuit, qubits: Sequence[Qubit | QuantumRegister | int | slice | Sequence[Qubit | int]], clbits: Sequence[Clbit | ClassicalRegister | int | slice | Sequence[Clbit | int]], *, label: str | None)→ InstructionSet
Create a for loop on this circuit.

There are two forms for calling this function. If called with all its arguments (with the possible exception of label), it will create a ForLoopOp with the given body. If body (and qubits and clbits) are not passed, then this acts as a context manager, which, when entered, provides a loop variable (unless one is given, in which case it will be reused) and will automatically build a ForLoopOp when the scope finishes. In this form, you do not need to keep track of the qubits or clbits you are using, because the scope will handle it for you.

For example:

from qiskit import QuantumCircuit
qc = QuantumCircuit(2, 1)

with qc.for_loop(range(5)) as i:
    qc.h(0)
    qc.cx(0, 1)
    qc.measure(0, 0)
    qc.break_loop().c_if(0, True)
Parameters:
indexset (Iterable[int]) – A collection of integers to loop over. Always necessary.

loop_parameter (Optional[Parameter]) –

The parameter used within body to which the values from indexset will be assigned. In the context-manager form, if this argument is not supplied, then a loop parameter will be allocated for you and returned as the value of the with statement. This will only be bound into the circuit if it is used within the body.

If this argument is None in the manual form of this method, body will be repeated once for each of the items in indexset but their values will be ignored.

body (Optional[QuantumCircuit]) – The loop body to be repeatedly executed. Omit this to use the context-manager mode.

qubits (Optional[Sequence[QubitSpecifier]]) – The circuit qubits over which the loop body should be run. Omit this to use the context-manager mode.

clbits (Optional[Sequence[ClbitSpecifier]]) – The circuit clbits over which the loop body should be run. Omit this to use the context-manager mode.

label (Optional[str]) – The string label of the instruction in the circuit.

Returns:
depending on the call signature, either a context manager for creating the for loop (it will automatically be added to the circuit at the end of the block), or an InstructionSet handle to the appended loop operation.

Return type:
InstructionSet or ForLoopContext

Raises:
CircuitError – if an incorrect calling convention is used.
