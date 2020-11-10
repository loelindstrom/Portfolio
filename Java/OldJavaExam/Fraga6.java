/**
 * Jag gjorde en krånglig lösning för att få med
 * så många av metoderna som möjligt.
 * Programmet kollar om ett ord finns i en mening.
 * Om ordet finns i meningen så skrivs ordet ut.
 * 
 * Längst ner har jag även lagt med den simplaste lösningen.
 */

import static java.lang.System.*;

public class Fraga6 {
    public static void main(String[] args) {
        String mening = "The three did feed the deer";
        String ord = "did";

        boolean träff = false;
//      Kolla igenom hela meningen för att se om ordet finns:
        for (int i=0; i<mening.length(); i++) {
//          Om första bokstaven i ordet finns i meningen
//          så kollas om resten av ordet finns med:
            if (mening.charAt(i) == ord.charAt(0)) {
                for (int e=1, i2 = 1; e<ord.length(); e++, i2++) {
                    if (mening.charAt(i+i2) != ord.charAt(e))
                        break;
                    else
                        träff = true;
                }
            }
            
            if (träff){
                System.out.println("Ordet fanns i meningen:");
                System.out.println(mening.substring(i, i+ord.length()));
                break;
            }
        }
        
        if (!träff)
            System.out.println("Ordet fanns ej.");
    
//      Enklaste lösningen:
        int pos = mening.indexOf(ord);
        System.out.println(mening.substring(pos, pos+ord.length()));       
    }
}