import java.util.*;

public class Fraga10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Hur många sekunder?");
        int sekunder = sc.nextInt();
        if (sekunder > 60) {
            int minuter;
            int timmar;
            int dygn;
            minuter = sekunder / 60;
            sekunder = sekunder % 60;

            timmar = minuter / 60;
            minuter = minuter % 60;

            dygn = timmar / 24;
            timmar = timmar % 24;
            
            if (dygn > 0)
                System.out.printf("Det är %d dygn, "
                                + "%d timmar, "
                                + "%d minuter "
                                + "och %d sekunder.",
                                  dygn, timmar, 
                                  minuter, sekunder);
            else if (timmar > 0)
                System.out.printf("Det är %d timmar, "
                                + "%d minuter "
                                + "och %d sekunder.",
                                  timmar, minuter, 
                                  sekunder);
            else if (minuter > 0)
                System.out.printf("Det är %d minuter "
                                + "och %d sekunder.",
                                  minuter, sekunder);
        }
        else
            System.out.printf("Det är %.1f minuter",
                              sekunder / 60.0);
        System.out.println();
    }
}