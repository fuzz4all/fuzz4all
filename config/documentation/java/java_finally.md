The finally Block
The finally block always executes when the try block exits. This ensures that the finally block is executed even if an unexpected exception occurs. But finally is useful for more than just exception handling — it allows the programmer to avoid having cleanup code accidentally bypassed by a return, continue, or break. Putting cleanup code in a finally block is always a good practice, even when no exceptions are anticipated.

Note: The finally block may not execute if the JVM exits while the try or catch code is being executed.
The try block of the writeList method that you've been working with here opens a PrintWriter. The program should close that stream before exiting the writeList method. This poses a somewhat complicated problem because writeList's try block can exit in one of three ways.

The new FileWriter statement fails and throws an IOException.
The list.get(i) statement fails and throws an IndexOutOfBoundsException.
Everything succeeds and the try block exits normally.
The runtime system always executes the statements within the finally block regardless of what happens within the try block. So it's the perfect place to perform cleanup.

The following finally block for the writeList method cleans up and then closes the PrintWriter and FileWriter.

finally {
    if (out != null) { 
        System.out.println("Closing PrintWriter");
        out.close(); 
    } else { 
        System.out.println("PrintWriter not open");
    } 
    if (f != null) {
	    System.out.println("Closing FileWriter");
	    f.close();
	}	
} 
Important: Use a try-with-resources statement instead of a finally block when closing a file or otherwise recovering resources. The following example uses a try-with-resources statement to clean up and close the PrintWriter and FileWriter for the writeList method:
public void writeList() throws IOException {
    try (FileWriter f = new FileWriter("OutFile.txt");
         PrintWriter out = new PrintWriter(f)) {
        for (int i = 0; i < SIZE; i++) {
            out.println("Value at: " + i + " = " + list.get(i));
        }
    }
}
The try-with-resources statement automatically releases system resources when no longer needed. See The try-with-resources Statement.