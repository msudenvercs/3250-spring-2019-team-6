import java.util.Stack;

public class JavaTestStuff {


   public static void main (String [] args) {
   
      int a = 10;
      int b = 2;
      int c = 0;
      Stack<Integer> stack = new Stack<Integer>();
      
      c = a + b;        // iadd
      c = a & b;        // iand
      stack.push(-1);   // iconst_m1
      stack.push(0);    // iconst_0
      stack.push(1);    // iconst_1
      stack.push(2);    // iconst_2
      stack.push(3);    // iconst_3
      stack.push(4);    // iconst_4
      stack.push(5);    // iconst_5
      c = a / b;        // idiv
      c = a * b;        // imul
      c = -a;           // ineg
      c = a | b;        // ior
      c = a % b;        // irem
      c = a << 1;       // ishl
      c = a >> 1;       // ishr
      c = a - b;        // isub
      c = a >>> 1;      // iushr
      c = a ^ b;        // ixor
     
   }
}