import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class b21921 {

    static int n, m;
    static int[] data;
    static int[] psum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        psum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            psum[i + 1] = psum[i] + data[i];
        }

        ArrayList<Integer> visit = new ArrayList<>();
        for (int i = m; i < n + 1; i++) {
            visit.add(psum[i] - psum[i - m]);
        }

        Collections.sort(visit, Collections.reverseOrder());
        int result = visit.get(0);

        if (result == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(result);
            int count = Collections.frequency(visit, result);
            System.out.println(count);
        }
    }
}
