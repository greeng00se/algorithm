import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

public class b1013 {

    static String pattern = "(100+1+|01)+";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (Pattern.matches(pattern, s)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
