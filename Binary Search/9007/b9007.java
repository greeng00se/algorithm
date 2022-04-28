import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b9007 {

    static int t;
    static int k, n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            solve(br);
        }
    }

    private static void solve(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        int[][] data = new int[4][n];
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] groupA = new int[n * n];
        int[] groupB = new int[n * n];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                groupA[idx] = data[0][i] + data[1][j];
                groupB[idx++] = data[2][i] + data[3][j];
            }
        }

        Arrays.sort(groupA);
        Arrays.sort(groupB);

        int result = Integer.MAX_VALUE;
        int minDiff = Integer.MAX_VALUE;

        for (int v : groupA) {
            int l = 0;
            int r = n * n - 1;

            while (l <= r) {
                int mid = (l + r) / 2;
                int sum = v + groupB[mid];
                int diff = Math.abs(k - sum);

                if (sum > k) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }

                if (minDiff > diff) {
                    result = sum;
                    minDiff = diff;
                } else if (minDiff == diff) {
                    result = Integer.min(result, sum);
                }
            }
        }

        System.out.println(result);
    }
}
