import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class b10875 {

    static int n, t, d;
    static Long MAX;
    static Long MAX_VALUE = 100000000000000000L;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static List<Pair[]> lines = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        t = Integer.parseInt(br.readLine());
        MAX = Long.valueOf(n * 2 + 1);

        Long result = solve(br);
        System.out.println(result);
    }

    private static Long solve(BufferedReader br) throws IOException {
        StringTokenizer st;
        long result = 0;
        long r = n, c = n;
        d = 1;

        for (int i = 0; i < t + 1; i++) {
            long count = MAX_VALUE;
            char leftOrRight = 'L';
            if (i != t) {
                st = new StringTokenizer(br.readLine());
                count = Long.parseLong(st.nextToken());
                leftOrRight = st.nextToken().charAt(0);
            }

            long nr = r + dr[d] * count;
            long nc = c + dc[d] * count;

            long v = MAX_VALUE;
            if (nr < 0) v = Long.min(v, r + 1);
            if (nr >= MAX) v = Long.min(v, MAX - r);
            if (nc < 0) v = Long.min(v, c + 1);
            if (nc >= MAX) v = Long.min(v, MAX - c);

            for (int j = 0; j < lines.size() - 1; j++) {
                Pair[] pairs = lines.get(j);
                Pair s = pairs[0];
                Pair e = pairs[1];

                boolean isVerticalLine = s.c == e.c;

                // 조건은 수평선인지 수직선인지, 선이랑 만날 수 있는 위치인지?, 선이랑 만나는지
                if (d == 0) {
                    if (isVerticalLine && s.c == nc && (nr <= e.r && e.r < r)) {
                        v = Long.min(v, r - e.r);
                    }
                    if (!isVerticalLine && (s.c <= nc && nc <= e.c) && (nr <= e.r && e.r < r)) {
                        v = Long.min(v, r - e.r);
                    }
                } else if (d == 1) {
                    if (isVerticalLine && (s.r <= nr && nr <= e.r) && (c < s.c && s.c <= nc)) {
                        v = Long.min(v, s.c - c);
                    }
                    if (!isVerticalLine && s.r == nr && (c < s.c && s.c <= nc)) {
                        v = Long.min(v, s.c - c);
                    }
                } else if (d == 2) {
                    if (isVerticalLine && s.c == nc && (r < s.r && s.r <= nr)) {
                        v = Long.min(v, s.r - r);
                    }
                    if (!isVerticalLine && (s.c <= nc && nc <= e.c) && (r < s.r && s.r <= nr)) {
                        v = Long.min(v, s.r - r);
                    }
                } else if (d == 3) {
                    if (isVerticalLine && (s.r <= nr && nr <= e.r) && (nc <= e.c && e.c < c)) {
                        v = Long.min(v, c - e.c);
                    }
                    if (!isVerticalLine && (nc <= e.c && e.c < c) && s.r == nr) {
                        v = Long.min(v, c - e.c);
                    }
                }
            }

            if (v != MAX_VALUE) {
                return result + v;
            }

            Pair[] pairs = new Pair[2];
            pairs[0] = new Pair(r, c);
            pairs[1] = new Pair(nr, nc);
            Arrays.sort(pairs);
            lines.add(pairs);

            r = nr;
            c = nc;
            result += count;
            d = leftOrRight == 'L' ? (d + 3) % 4 : (d + 1) % 4;
        }

        return result;
    }

    private static class Pair implements Comparable<Pair> {
        long r, c;

        public Pair(long r, long c) {
            this.r = r;
            this.c = c;
        }

        @Override
        public int compareTo(Pair o) {
            int cmp = Long.valueOf(this.r).compareTo(o.r);
            if (cmp == 0) {
                return Long.valueOf(this.c).compareTo(o.c);
            } else {
                return cmp;
            }
        }
    }
}
