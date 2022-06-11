import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class b2143 {

    static int t, n, m;
    static int[] data1, data2;

    public static void main(String[] args) throws IOException {
        init();
        solve();
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        n = Integer.parseInt(br.readLine());
        data1 = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data1[i] = Integer.parseInt(st.nextToken());
        }

        m = Integer.parseInt(br.readLine());
        data2 = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            data2[i] = Integer.parseInt(st.nextToken());
        }
    }

    private static void solve() {
        ArrayList<Integer> psum1 = new ArrayList<>();
        ArrayList<Integer> psum2 = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int sum = data1[i];
            psum1.add(sum);
            for (int j = i + 1; j < n; j++) {
                sum += data1[j];
                psum1.add(sum);
            }
        }

        for (int i = 0; i < m; i++) {
            int sum = data2[i];
            psum2.add(sum);
            for (int j = i + 1; j < m; j++) {
                sum += data2[j];
                psum2.add(sum);
            }
        }

        Collections.sort(psum1);
        Collections.sort(psum2);

        long result = 0;

        for (Integer target : psum1) {
            result += find(psum2, t - target);
        }

        System.out.println(result);
    }

    private static int find(ArrayList<Integer> data, Integer target) {
        return upperBound(data, target) - lowerBound(data, target);
    }

    private static int upperBound(List<Integer> data, Integer target) {
        int l = 0;
        int r = data.size();

        while (l < r) {
            int mid = (l + r) / 2;

            if (data.get(mid) <= target) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return r;
    }

    private static int lowerBound(List<Integer> data, Integer target) {
        int l = 0;
        int r = data.size();

        while (l < r) {
            int mid = (l + r) / 2;

            if (data.get(mid) >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }
}
