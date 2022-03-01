import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1065 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = solve(n);

        System.out.println(result);
    }

    private static int solve(int n) {
        if (n < 100) {
            return n;
        }

        int result = 99;
        if (n >= 1000) {
            n = 999;
        }

        for (int i = 100; i <= n; i++) {
            int hundreds = i / 100;
            int tens = (i / 10) % 10;
            int units = i % 10;
            if ((hundreds - tens) == (tens - units)) {
                result += 1;
            }
        }

        return result;
    }
}
