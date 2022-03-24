import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b2477 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] d = new int[6];
        int r = 0;
        int maxValue = 0;

        for (int i = 0; i < 6; i++) {
            st = new StringTokenizer(br.readLine());
            st.nextToken();
            d[i] = Integer.parseInt(st.nextToken());
            if (maxValue < d[i]) {
                maxValue = d[i];
                r = i;
            }
        }

        r += 6;
        int c = d[(r + 1) % 6] > d[(r - 1) % 6] ? (r + 1) % 6 : (r - 1) % 6;
        c += 6;
        int area = d[r % 6] * d[c % 6] - d[(r - 3) % 6] * d[(c - 3) % 6];
        System.out.println(n * area);
    }
}
