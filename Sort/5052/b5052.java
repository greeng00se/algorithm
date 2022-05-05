import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b5052 {

    static int t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            boolean result = solve(br);
            System.out.println(result ? "YES" : "NO");
        }
    }

    private static boolean solve(BufferedReader br) throws IOException {
        int n = Integer.parseInt(br.readLine());

        List<String> numbers = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            numbers.add(br.readLine());
        }
        Collections.sort(numbers);

        Map<String, Boolean> check = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String number = numbers.get(i);
            for (int j = 1; j < number.length() + 1; j++) {
                if (check.getOrDefault(number.substring(0, j), false)) {
                    return false;
                }
            }
            check.put(number, true);
        }
        return true;
    }
}
