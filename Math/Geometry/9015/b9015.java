package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class b9015 {

    static int t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int result = solve(br);
            System.out.println(result);
        }
    }

    private static int solve(BufferedReader br) throws IOException {
        StringTokenizer st;

        ArrayList<Pair> data = new ArrayList<Pair>();
        HashSet<Pair> s = new HashSet<>();
        int result = 0;

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            Pair pair = new Pair(x, y);
            data.add(pair);
            s.add(pair);
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                Pair pair1 = data.get(i);
                Pair pair2 = data.get(j);
                int dx = pair1.x - pair2.x;
                int dy = pair1.y - pair2.y;

                Pair pair3 = new Pair(pair1.x - dy, pair1.y + dx);
                Pair pair4 = new Pair(pair2.x - dy, pair2.y + dx);

                if (s.contains(pair3) && s.contains(pair4)) {
                    result = Integer.max(result, dx * dx + dy * dy);
                }
            }
        }

        return result;
    }

    private static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Pair pair = (Pair) o;

            if (x != pair.x) return false;
            return y == pair.y;
        }

        @Override
        public int hashCode() {
            int result = x;
            result = 31 * result + y;
            return result;
        }
    }
}
