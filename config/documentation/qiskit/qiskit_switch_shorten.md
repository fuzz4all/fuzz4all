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