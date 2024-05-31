using System;
class OperadoresLogicos {
    static void Main() {
        bool a = true;
        bool b = false;
        bool c = true;

        // AND Logical Operator
        bool resultAND = a && b;    // False
        bool resultAND2 = a && c;   // True

        // OR Logical Operator
        bool resultOR = a || b; // True

        // NOT Logical Operator
        bool resultNOT = !b; // True
    }
}