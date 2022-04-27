import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1253 {

    static int n;
    static int[] data;
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        data = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data);

        for (int i = 0; i < n; i++) {
            if (isGood(i)) {
                result++;
            }
        }

        System.out.println(result);
    }

    private static boolean isGood(int idx) {
        int l = 0;
        int r = n - 1;

        while (l < r) {
            int sum = data[l] + data[r];
            if (sum == data[idx]) {
                if (l == idx) l++;
                else if (r == idx) r--;
                else return true;
            } else if (sum > data[idx]) {
                r--;
            } else {
                l++;
            }
        }

        return false;
    }
}
