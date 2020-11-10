public class Fraga7 {
    public static void main(String[] args) {
        int[] vec = {3, 6, 1, 12, 8, 10, 5, 3, 15, 8};
        histogram(vec);
    }
    
    public static void histogram(int[] heltalsFält) {
        for (int i=0; i < heltalsFält.length; i++) {
            for (int e=0; e<heltalsFält[i]; e++)
                System.out.print("*");
            System.out.println();
        }
    }
}