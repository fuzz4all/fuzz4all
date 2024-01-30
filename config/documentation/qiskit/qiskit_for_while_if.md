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

qiskit.circuit.QuantumCircuit.if_test¶
QuantumCircuit.if_test(condition: tuple[ClassicalRegister | Clbit, int], true_body: None, qubits: None, clbits: None, *, label: str | None)→ qiskit.circuit.controlflow.if_else.IfContext[SOURCE]¶
QuantumCircuit.if_test(condition: tuple[ClassicalRegister | Clbit, int], true_body: QuantumCircuit, qubits: Sequence[Qubit | QuantumRegister | int | slice | Sequence[Qubit | int]], clbits: Sequence[Clbit | ClassicalRegister | int | slice | Sequence[Clbit | int]], *, label: str | None = None)→ InstructionSet
Create an if statement on this circuit.

There are two forms for calling this function. If called with all its arguments (with the possible exception of label), it will create a IfElseOp with the given true_body, and there will be no branch for the false condition (see also the if_else() method). However, if true_body (and qubits and clbits) are not passed, then this acts as a context manager, which can be used to build if statements. The return value of the with statement is a chainable context manager, which can be used to create subsequent else blocks. In this form, you do not need to keep track of the qubits or clbits you are using, because the scope will handle it for you.

For example:

from qiskit.circuit import QuantumCircuit, Qubit, Clbit
bits = [Qubit(), Qubit(), Qubit(), Clbit(), Clbit()]
qc = QuantumCircuit(bits)

qc.h(0)
qc.cx(0, 1)
qc.measure(0, 0)
qc.h(0)
qc.cx(0, 1)
qc.measure(0, 1)

with qc.if_test((bits[3], 0)) as else_:
    qc.x(2)
with else_:
    qc.h(2)
    qc.z(2)
Parameters:
condition (Tuple[Union[ClassicalRegister, Clbit], int]) – A condition to be evaluated at circuit runtime which, if true, will trigger the evaluation of true_body. Can be specified as either a tuple of a ClassicalRegister to be tested for equality with a given int, or as a tuple of a Clbit to be compared to either a bool or an int.

true_body (Optional[QuantumCircuit]) – The circuit body to be run if condition is true.

qubits (Optional[Sequence[QubitSpecifier]]) – The circuit qubits over which the if/else should be run.

clbits (Optional[Sequence[ClbitSpecifier]]) – The circuit clbits over which the if/else should be run.

label (Optional[str]) – The string label of the instruction in the circuit.

Returns:
depending on the call signature, either a context manager for creating the if block (it will automatically be added to the circuit at the end of the block), or an InstructionSet handle to the appended conditional operation.

Return type:
InstructionSet or IfContext

Raises:
CircuitError – If the provided condition references Clbits outside the enclosing circuit.

CircuitError – if an incorrect calling convention is used.

Returns:
A handle to the instruction created.

qiskit.circuit.QuantumCircuit.while_loop¶
QuantumCircuit.while_loop(condition: tuple[ClassicalRegister | Clbit, int], body: None, qubits: None, clbits: None, *, label: str | None)→ qiskit.circuit.controlflow.while_loop.WhileLoopContext[SOURCE]¶
QuantumCircuit.while_loop(condition: tuple[ClassicalRegister | Clbit, int], body: QuantumCircuit, qubits: Sequence[Qubit | QuantumRegister | int | slice | Sequence[Qubit | int]], clbits: Sequence[Clbit | ClassicalRegister | int | slice | Sequence[Clbit | int]], *, label: str | None)→ InstructionSet
Create a while loop on this circuit.

There are two forms for calling this function. If called with all its arguments (with the possible exception of label), it will create a WhileLoopOp with the given body. If body (and qubits and clbits) are not passed, then this acts as a context manager, which will automatically build a WhileLoopOp when the scope finishes. In this form, you do not need to keep track of the qubits or clbits you are using, because the scope will handle it for you.

Example usage:

from qiskit.circuit import QuantumCircuit, Clbit, Qubit
bits = [Qubit(), Qubit(), Clbit()]
qc = QuantumCircuit(bits)

with qc.while_loop((bits[2], 0)):
    qc.h(0)
    qc.cx(0, 1)
    qc.measure(0, 0)
Parameters:
condition (Tuple[Union[ClassicalRegister, Clbit], int]) – An equality condition to be checked prior to executing body. The left-hand side of the condition must be a ClassicalRegister or a Clbit, and the right-hand side must be an integer or boolean.

body (Optional[QuantumCircuit]) – The loop body to be repeatedly executed. Omit this to use the context-manager mode.

qubits (Optional[Sequence[Qubit]]) – The circuit qubits over which the loop body should be run. Omit this to use the context-manager mode.

clbits (Optional[Sequence[Clbit]]) – The circuit clbits over which the loop body should be run. Omit this to use the context-manager mode.

label (Optional[str]) – The string label of the instruction in the circuit.

Returns:
If used in context-manager mode, then this should be used as a with resource, which will infer the block content and operands on exit. If the full form is used, then this returns a handle to the instructions created.

Return type:
InstructionSet or WhileLoopContext

Raises:
CircuitError – if an incorrect calling convention is used.