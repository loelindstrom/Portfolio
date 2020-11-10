import java.util.*;

public class Fraga2 {
    public static String VÄLKOMST_MSG = "********** VÄLKOMMEN **********\n"
                                     + "I detta program kan du ta reda på om du"
                                     + " har rätt till att göra avdrag för"
                                     + " dubbel bosättning.\n"
                                     + "Var god ange avstånd till ditt arbete i"
                                     + " km:";
    
    public static String EJ_AVDRAG_MSG = "\nDu kan inte göra avdrag för "
                                       + "dubbel bosättning.";
    
    public static String BOENDE_MSG = "\nÄr du:\n"
                                    + "1. Ensamboende\n"
                                    + "eller\n"
                                    + "2. Sammanboende\n"
                                    + "Svara med antingen siffran '1' eller '2':";
    
    public static String VARAKTIGHET_MSG = "\nHur många år varar arbetet?\n"
                                         + "Avrunda uppåt.";
    
    public static String FEL_BOENDE_MSG = "\nOj, du angav en annan siffra än 1"
                                        + " eller 2 på frågan om boende.\n"
                                        + "Var god starta om programmet!";
    
    public static String AVDRAG_MSG = "\nDu kan göra avdrag för "
                                    + "dubbel bosättning.";
    
    
    public static void main (String[] args) {
        System.out.println(VÄLKOMST_MSG);
        Scanner sc = new Scanner(System.in);
        int avståndArbete = sc.nextInt();
        
        if (avståndArbete <= 50) {
            System.out.println(EJ_AVDRAG_MSG);
        }
        
        else {
            System.out.println(VARAKTIGHET_MSG);
            int varaktighetArbete = sc.nextInt();
            
            System.out.println(BOENDE_MSG);
            int boendeForm = sc.nextInt();
            
            int meddelande = kollaOmAvdrag(varaktighetArbete, boendeForm);
            switch (meddelande) {
                case 1: System.out.println(AVDRAG_MSG);
                        break;
                case 2: System.out.println(EJ_AVDRAG_MSG);
                        break;
                case 3: System.out.println(FEL_BOENDE_MSG);
                        break;
            }
        }
    }
    
    public static int kollaOmAvdrag(int varaktighetArbete, int boendeForm) {
        if (boendeForm == 1) {
            if (varaktighetArbete <= 1)
                return 1;
            else
                return 2;
        }
        if (boendeForm == 2) {
            if (varaktighetArbete <= 3)
                return 1;
            else
                return 2;
        }
        return 3;
    }
}