import java.util.ArrayList;

public class isUnique {

    boolean withDataStructure(String word) {
        ArrayList<Character> uniqueCharacters = new ArrayList<>();

        for (int i = 0; i < word.length(); i++) {
            if (contains(word.charAt(i), uniqueCharacters)) {
                return false;
            } else {
                uniqueCharacters.add(word.charAt(i));
            }
        }
        return true;
    }

    boolean contains(char letter, ArrayList<Character> uniqueCharacters) {
        return (uniqueCharacters.contains(letter) ? true : false);
    }

    /*
     * Make an alphabet array with boolean as vals
     */
    boolean AlphabetArray(String word) {
        boolean[] alphabet = new boolean[26];
        for (int i = 0; i < word.length(); i++) {
            char current_char = word.charAt(i);
            int index = (int) current_char % 32;
            if (alphabet[index] == true)
                return false;

            alphabet[index] = true;
        }
        return true;
    }

    public static void main(String[] args) {

        isUnique obj = new isUnique();

        String test1 = "Haris";
        //System.out.println(obj.withDataStructure(test1));
        System.out.println(obj.AlphabetArray(test1));
    }
}