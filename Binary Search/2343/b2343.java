import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b2343 {

    static int n, m;
    static int[] data;

    public static void main(String[] args) throws IOException {
        init();

        int result = 0;
        int l = Arrays.stream(data).max().getAsInt();
        int r = 0x3f3f3f3f;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (check(mid)) {
                r = mid - 1;
                result = mid;
            } else {
                l = mid + 1;
            }
        }

        System.out.println(result);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        data = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
    }

    private static boolean check(int mid) {
        int count = 0;
        int disk = 0;
        for (int i = 0; i < n; i++) {
            if (disk + data[i] > mid) {
                disk = 0;
                count += 1;
            }
            disk += data[i];
        }

        if (disk != 0) {
            count += 1;
        }

        return count <= m;
    }
}
