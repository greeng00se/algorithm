package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class b1049 {

    static int n, m;
    static int minBundle = Integer.MAX_VALUE;
    static int minPiece = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int bundle = Integer.parseInt(st.nextToken());
            int piece = Integer.parseInt(st.nextToken());

            if (minBundle > bundle) {
                minBundle = bundle;
            }

            if (minPiece > piece) {
                minPiece = piece;
            }
        }

        List<Integer> results = Arrays.asList(
                (int) Math.ceil((double) n / 6) * minBundle,
                (int) Math.floor((double) n / 6) * minBundle + n % 6 * minPiece,
                n * minPiece
        );

        System.out.println(Collections.min(results));
    }
}
