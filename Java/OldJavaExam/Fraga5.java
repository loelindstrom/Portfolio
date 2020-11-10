import java.util.*;

public class Fraga5 {
    public static void main(String[] args) {
        System.out.println("Välkommen till talspegeln!\n"
                         + "Var god att ange 3 heltal som är "
                         + ">100 och <999:");
        Scanner sc = new Scanner(System.in);
        String [] talFält = new String[3];
        int i = 0;
        while (talFält[2] == null) {
            int tal = sc.nextInt();
            if (100 < tal && tal < 999) {
                talFält[i] = Integer.toString(tal);
                i++;
            }
            else
                System.out.println("Oj, det där var inte heltal "
                                 + "mellan 100 och 999");
        }
        System.out.println("\nResultat:");
        for (i=0; i<3; i++){
            for (int e = talFält[i].length()-1; e>=0; e--)
                System.out.print(talFält[i].charAt(e));
            System.out.println();
        }
    }
}