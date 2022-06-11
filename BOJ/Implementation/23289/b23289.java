package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b23289 {

    static int x, y, k;
    static int w;
    static int result = 0;
    static int[] dr = {0, 0, 0, -1, 1};
    static int[] dc = {0, 1, -1, 0, 0};
    static int[][] wdr = {{0, 0, 0}, {-1, 0, 1}, {-1, 0, 1}, {-1, -1, -1}, {1, 1, 1}};
    static int[][] wdc = {{0, 0, 0}, {1, 1, 1}, {-1, -1, -1}, {-1, 0, 1}, {-1, 0, 1}};

    static int[][] data;
    static int[][] wind;
    static Map<Pair, List<Pair>> wall = new HashMap<>();
    static List<Pair> checkers = new ArrayList<>();
    static List<Triple> heaters = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        while (result <= 100) {
            step1();
            step2();
            step3();
            result += 1;
            if (step4()) {
                break;
            }
        }

        System.out.println(result);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        data = new int[x][y];
        wind = new int[x][y];
        for (int r = 0; r < x; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < y; c++) {
                data[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        w = Integer.parseInt(br.readLine());
        for (int i = 0; i < w; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            r -= 1;
            c -= 1;


            List<Pair> listA = wall.computeIfAbsent(new Pair(r, c), k -> new ArrayList<>());
            if (t == 0) {
                listA.add(new Pair(r - 1, c));
                List<Pair> listB = wall.computeIfAbsent(new Pair(r - 1, c), k -> new ArrayList<>());
                listB.add(new Pair(r, c));
            } else {
                listA.add(new Pair(r, c + 1));
                List<Pair> listB = wall.computeIfAbsent(new Pair(r, c + 1), k -> new ArrayList<>());
                listB.add(new Pair(r, c));
            }
        }

        for (int r = 0; r < x; r++) {
            for (int c = 0; c < y; c++) {
                if (data[r][c] == 0) {
                    continue;
                }

                if (data[r][c] == 5) {
                    checkers.add(new Pair(r, c));
                    continue;
                }

                heaters.add(new Triple(r, c, data[r][c]));
            }
        }
    }

    private static void step1() {
        for (Triple heater : heaters) {
            int r = heater.x;
            int c = heater.y;
            int d = heater.d;

            int nr = r + dr[d];
            int nc = c + dc[d];

            boolean[][] visited = new boolean[x][y];
            visited[nr][nc] = true;
            LinkedList<Triple> queue = new LinkedList<>();
            queue.add(new Triple(nr, nc, 5));
            wind[nr][nc] += 5;

            while (!queue.isEmpty()) {
                Triple triple = queue.poll();
                r = triple.x;
                c = triple.y;
                int v = triple.d;

                if (v == 1) {
                    continue;
                }

                for (int i = 0; i < 3; i++) {
                    nr = r + wdr[d][i];
                    nc = c + wdc[d][i];

                    if (isOut(nr, nc) || isNotValid(r, c, d, i) || visited[nr][nc]) {
                        continue;
                    }

                    visited[nr][nc] = true;
                    wind[nr][nc] += v - 1;
                    queue.add(new Triple(nr, nc, v - 1));
                }
            }
        }
    }

    private static void step2() {
        int[][] newWind = new int[x][y];

        for (int r = 0; r < x; r++) {
            for (int c = 0; c < y; c++) {
                for (int i = 1; i < 5; i++) {
                    int nr = r + dr[i];
                    int nc = c + dc[i];

                    if (isOut(nr, nc)) {
                        continue;
                    }

                    if (wind[nr][nc] > wind[r][c]) {
                        continue;
                    }

                    if (wall.getOrDefault(new Pair(nr, nc), new ArrayList<>()).contains(new Pair(r, c))) {
                        continue;
                    }

                    int diff = (wind[r][c] - wind[nr][nc]) / 4;
                    newWind[nr][nc] += diff;
                    newWind[r][c] -= diff;
                }
                newWind[r][c] += wind[r][c];
            }
        }

        wind = newWind;
    }

    private static void step3() {
        for (int r = 0; r < x; r++) {
            for (int c = 0; c < y; c++) {
                if (r == 0 || c == 0 || r == x - 1 || c == y - 1) {
                    wind[r][c] = Integer.max(0, wind[r][c] - 1);
                }
            }
        }
    }

    private static boolean step4() {
        int result = checkers.size();
        for (Pair checker : checkers) {
            int r = checker.x;
            int c = checker.y;
            if (wind[r][c] >= k) {
                result -= 1;
            }
        }

        return result > 0 ? false : true;
    }

    private static void print() {
        System.out.println();
        for (int[] ints : wind) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
    }

    public static boolean isNotValid(int r, int c, int d, int i) {
        int nr = r + wdr[d][i];
        int nc = c + wdc[d][i];

        ArrayList<Pair> o = new ArrayList<>();

        if (i == 1 && wall.getOrDefault(new Pair(r, c), o).contains(new Pair(nr, nc))) {
            return true;
        }

        if (dr[d] == 0 && (wall.getOrDefault(new Pair(r, c), o).contains(new Pair(nr, c))
                || wall.getOrDefault(new Pair(nr, nc), o).contains(new Pair(nr, c)))) {
            return true;
        }

        if (dc[d] == 0 && (wall.getOrDefault(new Pair(r, c), o).contains(new Pair(r, nc))
                || wall.getOrDefault(new Pair(nr, nc), o).contains(new Pair(r, nc)))) {
            return true;
        }

        return false;
    }

    public static boolean isOut(int r, int c) {
        return r < 0 || c < 0 || r >= x || c >= y;
    }

    private static class Triple {
        int x, y, d;

        public Triple(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }
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
