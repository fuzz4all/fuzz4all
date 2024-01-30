Switch Operation¶
This release adds a new control flow operation, the switch statement. This is implemented using a new operation class SwitchCaseOp and the QuantumCircuit.switch() method. This allows switching on a numeric input (such as a classical register or bit) and executing the circuit that corresponds to the matching value.

Qiskit now supports the representation of switch statements, using the new SwitchCaseOp instruction and the QuantumCircuit.switch() method. This allows switching on a numeric input (such as a classical register or bit) and executing the circuit that corresponds to the matching value. Multiple values can point to the same circuit, and CASE_DEFAULT can be used as an always-matching label.

You can also use a builder interface, similar to the other control-flow constructs to build up these switch statements:

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

qreg = QuantumRegister(2)
creg = ClassicalRegister(2)
qc = QuantumCircuit(qreg, creg)

qc.h([0, 1])
qc.measure([0, 1], [0, 1])
with qc.switch(creg) as case:
  with case(0):  # if the register is '00'
    qc.z(0)
  with case(1, 2):  # if the register is '01' or '10'
    qc.cx(0, 1)
  with case(case.DEFAULT):  # the default case
    qc.h(0)
The switch statement has support throughout the Qiskit compiler stack; you can transpile() circuits containing it (if the backend advertises its support for the construct), and it will serialize to QPY.

qiskit.circuit.QuantumCircuit.switch¶
QuantumCircuit.switch(target: Clbit | ClassicalRegister | int | slice | Sequence[Clbit | int], cases: None, qubits: None, clbits: None, *, label: str | None)→ qiskit.circuit.controlflow.switch_case.SwitchContext[SOURCE]¶
QuantumCircuit.switch(target: Clbit | ClassicalRegister | int | slice | Sequence[Clbit | int], cases: Iterable[Tuple[Any, QuantumCircuit]], qubits: Sequence[Qubit | QuantumRegister | int | slice | Sequence[Qubit | int]], clbits: Sequence[Clbit | ClassicalRegister | int | slice | Sequence[Clbit | int]], *, label: str | None)→ InstructionSet
Create a switch/case structure on this circuit.

There are two forms for calling this function. If called with all its arguments (with the possible exception of label), it will create a SwitchCaseOp with the given case structure. If cases (and qubits and clbits) are not passed, then this acts as a context manager, which will automatically build a SwitchCaseOp when the scope finishes. In this form, you do not need to keep track of the qubits or clbits you are using, because the scope will handle it for you.

Example usage:

from qiskit.circuit import QuantumCircuit, ClassicalRegister, QuantumRegister
qreg = QuantumRegister(3)
creg = ClassicalRegister(3)
qc = QuantumCircuit(qreg, creg)
qc.h([0, 1, 2])
qc.measure([0, 1, 2], [0, 1, 2])

with qc.switch(creg) as case:
    with case(0):
        qc.x(0)
    with case(1, 2):
        qc.z(1)
    with case(case.DEFAULT):
        qc.cx(0, 1)
Parameters:
target (Union[ClassicalRegister, Clbit]) – The classical value to switch one. This must be integer-like.

cases (Iterable[Tuple[Any, QuantumCircuit]]) – A sequence of case specifiers. Each tuple defines one case body (the second item). The first item of the tuple can be either a single integer value, the special value CASE_DEFAULT, or a tuple of several integer values. Each of the integer values will be tried in turn; control will then pass to the body corresponding to the first match. CASE_DEFAULT matches all possible values. Omit in context-manager form.

qubits (Sequence[Qubit]) – The circuit qubits over which all case bodies execute. Omit in context-manager form.

clbits (Sequence[Clbit]) – The circuit clbits over which all case bodies execute. Omit in context-manager form.

label (Optional[str]) – The string label of the instruction in the circuit.

Returns:
If used in context-manager mode, then this should be used as a with resource, which will return an object that can be repeatedly entered to produce cases for the switch statement. If the full form is used, then this returns a handle to the instructions created.

Return type:
InstructionSet or SwitchCaseContext

Raises:
CircuitError – if an incorrect calling convention is used.