public class CalculadoraBasica {
    public static void main(String[] args) {
        // 1. Declaración de los dos números
        int num1 = 10;
        int num2 = 5;

        // 2. Realización de las operaciones
        int suma = num1 + num2;
        int resta = num1 - num2;
        int multiplicacion = num1 * num2;

        double division = (double) num1 / num2; 

        System.out.println("Suma: " + suma + ", Tipo implícito: int");
        System.out.println("Resta: " + resta + ", Tipo implícito: int");
        System.out.println("Multiplicación: " + multiplicacion + ", Tipo implícito: int");
        System.out.println("División: " + division + ", Tipo implícito: double");
    }
}