package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b13334 {

    static int n, d;
    static List<Pair> data = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        int result = solve();
        System.out.println(result);
    }

    private static int solve() {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int result = 0;

        for (Pair pair : data) {
            int s = pair.x;
            int e = pair.y;
            int distance = e - d;

            if (distance <= s) {
                pq.add(s);
            }
            while (!pq.isEmpty() && pq.peek() < distance) {
                pq.poll();
            }

            result = Integer.max(result, pq.size());
        }

        return result;
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            data.add(new Pair(s, e));
        }
        Collections.sort(data);
        d = Integer.parseInt(br.readLine());
    }

    private static class Pair implements Comparable<Pair> {
        int x, y;

        public Pair(int x, int y) {
            this.x = Math.min(x, y);
            this.y = Math.max(x, y);
        }

        @Override
        public int compareTo(Pair o) {
            if (this.y == o.y) {
                return this.x - o.x;
            }
            return this.y - o.y;
        }
    }
}
