import java.util.*;

public class Fraga8 {
    public static void main(String[] args) {
        Random slump = new Random();
        
        String[] stryktipsRätt = new String[13];
        for (int i = 0; i<stryktipsRätt.length; i++) {
            String ruta = Integer.toString(slump.nextInt(3));
            if (ruta.equals("0"))
                ruta = "x";
            stryktipsRätt[i] = ruta;
        }

        System.out.printf("%-20s", "Skriv in din "
                        + "stryktipsrad: ");
        Scanner sc = new Scanner(System.in);
        String[] stryktipsGissa = sc.nextLine().split(" ");
        
        int rätt = 0;
        for (int i = 0; i < 13; i++) {
            if (stryktipsRätt[i].equalsIgnoreCase(stryktipsGissa[i]))
                rätt += 1;
        }
        
        System.out.print("Rätt stryktipsrad är:      ");
        for (String ruta : stryktipsRätt) {
            System.out.print(ruta + " ");
        }
        
        System.out.printf("\nDu hade %d rätt\n", rätt);
    }
}