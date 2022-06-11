import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class b10800 {

    static int n;
    static List<Triple> balls = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        solve();
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int color = Integer.parseInt(st.nextToken());
            int size = Integer.parseInt(st.nextToken());
            balls.add(new Triple(color, size, i));
        }

        Collections.sort(balls);
    }

    private static void solve() {
        int[] result = new int[n];
        int[] ballSum = new int[n + 1];
        int sum = 0;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            for (int j = idx; j < n; j++) {
                if (balls.get(i).size <= balls.get(j).size) {
                    break;
                }
                Triple ball = balls.get(j);
                sum += ball.size;
                ballSum[ball.color] += ball.size;
                idx++;
            }

            Triple now = balls.get(i);
            result[now.idx] += sum - ballSum[now.color];
        }

        for (int i = 0; i < n; i++) {
            System.out.println(result[i]);
        }
    }

    private static class Triple implements Comparable<Triple>{
        int color, size, idx;

        public Triple(int color, int size, int idx) {
            this.color = color;
            this.size = size;
            this.idx = idx;
        }

        @Override
        public int compareTo(Triple o) {
            return this.size - o.size;
        }
    }
}
