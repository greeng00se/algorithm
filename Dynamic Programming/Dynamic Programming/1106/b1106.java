import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1106 {

    static int n, m;
    static int[] dp;
    static final int MAX_VALUE = 101010101;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dp = new int[n + 100];
        Arrays.fill(dp, MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int cost = Integer.parseInt(st.nextToken());
            int customer = Integer.parseInt(st.nextToken());

            for (int j = customer; j < n + 100; j++) {
                dp[j] = Integer.min(dp[j - customer] + cost, dp[j]);
            }
        }

        int result = Integer.MAX_VALUE;
        for (int i = n; i < n + 100; i++) {
            result = Integer.min(result, dp[i]);
        }

        System.out.println(result);
    }
}
