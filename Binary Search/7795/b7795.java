import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b7795 {

    static int t;
    static int n, m;
    static int[] dataA;
    static int[] dataB;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            dataA = new int[n];
            dataB = new int[m];

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                dataA[j] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                dataB[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(dataA);
            Arrays.sort(dataB);
            int result = 0;

            for (int value : dataA) {
                result += find(value) + 1;
            }
            System.out.println(result);
        }
    }

    private static int find(int value) {
        int l = 0;
        int r = m - 1;
        int result = -1;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (dataB[mid] >= value) {
                r = mid - 1;
            } else {
                l = mid + 1;
                result = mid;
            }
        }

        return result;
    }
}
