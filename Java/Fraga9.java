import java.util.*;

public class Fraga9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ange dagens datum i följande format: yyyy-mm-dd");
        String dagensDatum = sc.nextLine();
        dagensDatum = dagensDatum.substring(5, 7) + dagensDatum.substring(8, 10);
        
        System.out.println("Ange när du är född i följande format: yyyymmdd");
        String persNr = sc.nextLine();
        String födelsedag = persNr.substring(4, 8);        
        
        if (dagensDatum.equals(födelsedag))
            System.out.println("\nGrattis!");
        else
            System.out.println("\nIngen tårta idag...");
    }
}