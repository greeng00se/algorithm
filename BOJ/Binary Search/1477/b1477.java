import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1477 {

    static int n, m, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[] data = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data);

        int result = solve(data);
        System.out.println(result);
    }

    private static int solve(int[] data) {
        int l = 0;
        int r = k;
        int result = 0;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (countArea(data, mid) > m) {
                l = mid + 1;
            } else {
                r = mid - 1;
                result = mid;
            }
        }

        return result;
    }

    private static int countArea(int[] data, int target) {
        int result = 0;
        int idx = 0;
        int range = 0;

        for (int i = 0; i < k; i++) {
            if (idx < n && data[idx] == i) {
                range = 0;
                idx++;
            }
            if (range >= target) {
                range = 0;
                result++;
            }
            range++;
        }

        return result;
    }
}
