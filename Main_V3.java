//Hecho por Christian Lombardi y Daniel Lasso
import java.util.Scanner;
import javax.xml.transform.Templates;
import java.io.*;
import java.util.*;
import java.util.stream.Collectors; 

public class Main_V3{
    public static Scanner palabra_ingresada = new Scanner(System.in);
    public static Scanner player_2 = new Scanner(System.in);
    public static final String ANSI_RED = "\u001B[31m"; 
    public static final String ANSI_RESET = "\u001B[0m"; 
    public static final String ANSI_YELLOW = "\u001B[33m"; //Letra correcta pero posición incorrecta
    public static final String ANSI_GREEN = "\u001B[32m"; //Letra correcta

    public static void main(String[] args) {
        //Definicion de variables
        long startTime = System.currentTimeMillis();
        int attempts = 0; //Intentos
        System.out.println("Bienvenido a Wordle de 2 jugadores! ");
        char[] answer; //La respuesta luego será un CharArray 
        char[] palabra; //El input luego será un CharArray   
        boolean done = false;
        String input_palabra = "";
        String player2;

        System.out.println("Ingrese la palabra que deberá adivinar el otro jugador:");
        player2 = player_2.nextLine().toLowerCase();
        String answerChoosen = player2;
        int lenght_answerChoosen = answerChoosen.length();
        System.out.println("Es turno del otro jugador para adivinar");
        System.out.println("La palabra que buscas tiene "+ lenght_answerChoosen + " letras");
        //System.out.println("Ingresa una palabra de  letras: ");
        while (!done){
            System.out.println("==================");
            input_palabra = palabra_ingresada.nextLine().toLowerCase(); //Leemos y guardamos la palabra ingresada por el usuario y la ponemos en minuscula
            System.out.println("==================");
            while(input_palabra.length() < answerChoosen.length()){ //Si la palabra no tiene la cantidad de letras de la respuesta, entonces no se le permitirá continuar, y su intento no sumará
                System.out.println("Debes ingresar una palabra de " + lenght_answerChoosen + " letras, vuelve a intentarlo");
                input_palabra = palabra_ingresada.nextLine().toLowerCase();
            }

            attempts++; //Los intentos se suman cada vez que se repita el ciclo
            palabra = input_palabra.toCharArray(); //Asignamos el input a un arreglo de caracteres, de "hola" pasa a ["h","o","l","a"]
            answer = answerChoosen.toCharArray(); //la respuesta tambien será un CharArray
            if (PrintWordWithColor(palabra, answer, attempts)) done = true; //Llamamos al metodo PrintWithColor para hacer las comparaciones y pintar las letras

            System.out.println("Llevas "+attempts +" intentos");
        }
        
    System.out.println("Encontraste la palabra correcta, felicidades!, lo hiciste en " + ((System.currentTimeMillis() - startTime) / 1000) + " segundos");

    }

    public static boolean PrintWordWithColor(char[] palabraWord, char[] correctWord, int attempts_max) {
        boolean correct = true;
        
        //int 
        char[] answerTemp = correctWord; //Se asigna de manera temporal la palabra correcta, ya como un CharArray
        int lenght_answer = correctWord.length;
        //int lenght_word = palabraWord.length;
        int[] colorForLetter = new int[lenght_answer]; //0 es gris, amarillo es 1, verde es 2
        int attempts_end = attempts_max;


        //Comparaciones y coloreo de letras
        for (int i = 0; i < lenght_answer; i++) { //Prueba buscar letra que esté en la palabra y que esté en su posición correspondiente (verde)
            if (palabraWord[i] == answerTemp[i]) { //Lee el indice de la palabra del usuario y lo compara con los indices de la respuesta
                answerTemp[i] = '-'; 
                colorForLetter[i] = 2; //Si las letras de la palabra son iguales a la respuesta, el color de la letra sera 2, es decir, verde
            } else correct = false;
        }

        for (int j = 0; j < lenght_answer ; j++) { //Prueba buscar letra correcta (amarilla)
            for (int k = 0; k < lenght_answer; k++){
                if (palabraWord[j] == answerTemp[k] && colorForLetter[j] != 2) { 
                //Si la letra es igual a la letra de la respuesta, pero no ocurrio la condicion anterior, se pintara amarilla (letra correcta, posicion incorrecta)
                    colorForLetter[j] = 1;
                    answerTemp[k] = '-';
                }
            }
        }
        //if (lenght_word != lenght_answer){
            //attempts_end -=1;
        //}
        //System.out.println("Llevas "+attempts_end +" intentos");
        for (int m = 0; m < lenght_answer ; m++) { 
            if(attempts_end == 6){ //Si el jugador ya llega a los 6 intentos, su ultimo palabra será pintado de rojo y se acaba el programa
                for (int t = 0; t < lenght_answer ; t++){
                    System.out.print(ANSI_RED + palabraWord[t] + ANSI_RESET);        
                }
            System.out.print("\nAlcanzaste 6 intentos y ahora ya no tienes más oportunidades, vuelve a intentarlo");
            System.exit(0);
            }

            if (colorForLetter[m] == 0) System.out.print(palabraWord[m]); //Color gris (predeterminado)
            if (colorForLetter[m] == 1) System.out.print(ANSI_YELLOW + palabraWord[m] + ANSI_RESET); //Color amarillo, posicion incorrecta
            if (colorForLetter[m] == 2) System.out.print(ANSI_GREEN + palabraWord[m] + ANSI_RESET);  //Color verde, letra correcta
        }
        System.out.println("");
        System.out.println("==================");
        return correct;
    }
}

   
