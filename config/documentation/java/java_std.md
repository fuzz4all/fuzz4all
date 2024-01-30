Java® Platform, Standard Edition & Java Development Kit
Version 20 API Specification
This document is divided into two sections:

Java SE
The Java Platform, Standard Edition (Java SE) APIs define the core Java platform for general-purpose computing. These APIs are in modules whose names start with java.
JDK
The Java Development Kit (JDK) APIs are specific to the JDK and will not necessarily be available in all implementations of the Java SE Platform. These APIs are in modules whose names start with jdk.
All ModulesJava SEJDKOther Modules
Module
Description
java.base
Defines the foundational APIs of the Java SE Platform.
java.compiler
Defines the Language Model, Annotation Processing, and Java Compiler APIs.
java.datatransfer
Defines the API for transferring data between and within applications.
java.desktop
Defines the AWT and Swing user interface toolkits, plus APIs for accessibility, audio, imaging, printing, and JavaBeans.
java.instrument
Defines services that allow agents to instrument programs running on the JVM.
java.logging
Defines the Java Logging API.
java.management
Defines the Java Management Extensions (JMX) API.
java.management.rmi
Defines the RMI connector for the Java Management Extensions (JMX) Remote API.
java.naming
Defines the Java Naming and Directory Interface (JNDI) API.
java.net.http
Defines the HTTP Client and WebSocket APIs.
java.prefs
Defines the Preferences API.
java.rmi
Defines the Remote Method Invocation (RMI) API.
java.scripting
Defines the Scripting API.
java.se
Defines the API of the Java SE Platform.
java.security.jgss
Defines the Java binding of the IETF Generic Security Services API (GSS-API).
java.security.sasl
Defines Java support for the IETF Simple Authentication and Security Layer (SASL).
java.smartcardio
Defines the Java Smart Card I/O API.
java.sql
Defines the JDBC API.
java.sql.rowset
Defines the JDBC RowSet API.
java.transaction.xa
Defines an API for supporting distributed transactions in JDBC.
java.xml
Defines the Java API for XML Processing (JAXP), the Streaming API for XML (StAX), the Simple API for XML (SAX), and the W3C Document Object Model (DOM) API.
java.xml.crypto
Defines the API for XML cryptography.
jdk.accessibility
Defines JDK utility classes used by implementors of Assistive Technologies.
jdk.attach
Defines the attach API.
jdk.charsets
Provides charsets that are not in java.base (mostly double byte and IBM charsets).
jdk.compiler
Defines the implementation of the system Java compiler and its command line equivalent, javac.
jdk.crypto.cryptoki
Provides the implementation of the SunPKCS11 security provider.
jdk.crypto.ec
Provides the implementation of the SunEC security provider.
jdk.dynalink
Defines the API for dynamic linking of high-level operations on objects.
jdk.editpad
Provides the implementation of the edit pad service used by jdk.jshell.
jdk.hotspot.agent
Defines the implementation of the HotSpot Serviceability Agent.
jdk.httpserver
Defines the JDK-specific HTTP server API, and provides the jwebserver tool for running a minimal HTTP server.
jdk.incubator.concurrent
Defines non-final APIs for concurrent programming.
jdk.incubator.vector
Defines an API for expressing computations that can be reliably compiled at runtime into SIMD instructions, such as AVX instructions on x64, and NEON instructions on AArch64.
jdk.jartool
Defines tools for manipulating Java Archive (JAR) files, including the jar and jarsigner tools.
jdk.javadoc
Defines the implementation of the system documentation tool and its command-line equivalent, javadoc.
jdk.jcmd
Defines tools for diagnostics and troubleshooting a JVM such as the jcmd, jps, jstat tools.
jdk.jconsole
Defines the JMX graphical tool, jconsole, for monitoring and managing a running application.
jdk.jdeps
Defines tools for analysing dependencies in Java libraries and programs, including the jdeps, javap, and jdeprscan tools.
jdk.jdi
Defines the Java Debug Interface.
jdk.jdwp.agent
Provides the implementation of the Java Debug Wire Protocol (JDWP) agent.
jdk.jfr
Defines the API for JDK Flight Recorder.
jdk.jlink
Defines the jlink tool for creating run-time images, the jmod tool for creating and manipulating JMOD files, and the jimage tool for inspecting the JDK implementation-specific container file for classes and resources.
jdk.jpackage
Defines the Java Packaging tool, jpackage.
jdk.jshell
Provides the jshell tool for evaluating snippets of Java code, and defines a JDK-specific API for modeling and executing snippets.
jdk.jsobject
Defines the API for the JavaScript Object.
jdk.jstatd
Defines the jstatd tool for starting a daemon for the jstat tool to monitor JVM statistics remotely.
jdk.localedata
Provides the locale data for locales other than US locale.
jdk.management
Defines JDK-specific management interfaces for the JVM.
jdk.management.agent
Defines the JMX management agent.
jdk.management.jfr
Defines the Management Interface for JDK Flight Recorder.
jdk.naming.dns
Provides the implementation of the DNS Java Naming provider.
jdk.naming.rmi
Provides the implementation of the RMI Java Naming provider.
jdk.net
Defines the JDK-specific Networking API.
jdk.nio.mapmode
Defines JDK-specific file mapping modes.
jdk.sctp
Defines the JDK-specific API for SCTP.
jdk.security.auth
Provides implementations of the javax.security.auth.* interfaces and various authentication modules.
jdk.security.jgss
Defines JDK extensions to the GSS-API and an implementation of the SASL GSSAPI mechanism.
jdk.xml.dom
Defines the subset of the W3C Document Object Model (DOM) API that is not part of the Java SE API.
jdk.zipfs
Provides the implementation of the Zip file system provider.