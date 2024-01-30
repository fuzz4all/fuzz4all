package checker;

import java.io.IOException;
import org.xml.sax.SAXException;
import org.antlr.v4.runtime.*;

public class Main {

    public static void main(String[] args) throws SAXException, IOException {

        ANTLRInputStream input = new ANTLRFileStream(args[0]);
        JavaLexer lexer = new JavaLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        JavaParser parser = new JavaParser(tokens);

        final StringBuilder errorMessages = new StringBuilder();

        parser.compilationUnit();
        int syntaxErrors = parser.getNumberOfSyntaxErrors();

        if (syntaxErrors == 0) {
            System.exit(0);
        } else {
            System.exit(1);
        }
    }
}
