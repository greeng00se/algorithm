import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b18809 {

    private static final int WATER = 0, NO = 1, YES = 2, GREEN = 3, RED = 4;
    private static final int[] dr = {-1, 0, 1, 0};
    private static final int[] dc = {0, 1, 0, -1};
    static int n, m, green, red;
    static int[][] data;
    static List<Pair> land = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        solve();
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        green = Integer.parseInt(st.nextToken());
        red = Integer.parseInt(st.nextToken());

        data = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
                if (data[i][j] == YES) {
                    land.add(new Pair(i, j));
                }
            }
        }
    }

    private static void solve() {
        List<int[]> combinations = generateCombinations(land.size(), red + green);
        List<int[]> greenCombinations = generateCombinations(red + green, green);
        int result = 0;
        for (int[] combination : combinations) {
            for (int[] greenCombination : greenCombinations) {
                result = Integer.max(result, bfs(combination, greenCombination));
            }
        }
        System.out.println(result);
    }

    private static List<int[]> generateCombinations(int n, int r) {
        List<int[]> combinations = new ArrayList<>();
        generateCombinationsRecursively(combinations, new int[r], 0, n, 0);
        return combinations;
    }

    private static void generateCombinationsRecursively(List<int[]> combinations, int[] elements, int current, int end, int index) {
        if (index == elements.length) {
            combinations.add(elements.clone());
            return;
        }
        if (current >= end) {
            return;
        }
        elements[index] = current;
        generateCombinationsRecursively(combinations, elements, current + 1, end, index + 1);
        generateCombinationsRecursively(combinations, elements, current + 1, end, index);
    }

    private static int bfs(int[] combination, int[] greenCombination) {
        int[][] redVisited = new int[n][m];
        int[][] greenVisited = new int[n][m];
        boolean[][] flower = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(redVisited[i], 0);
            Arrays.fill(greenVisited[i], 0);
            Arrays.fill(flower[i], false);
        }
        LinkedList<Quad> queue = new LinkedList<>();

        int idx = 0;
        for (int i = 0; i < green + red; i++) {
            Pair pair = land.get(combination[i]);
            if (idx < green && i == greenCombination[idx]) {
                greenVisited[pair.x][pair.y] = 1;
                queue.add(new Quad(pair.x, pair.y, 1, GREEN));
                idx++;
            } else {
                redVisited[pair.x][pair.y] = 1;
                queue.add(new Quad(pair.x, pair.y, 1, RED));
            }
        }

        int result = 0;

        while (!queue.isEmpty()) {
            Quad quad = queue.pollFirst();
            int r = quad.r;
            int c = quad.c;
            int v = quad.v;
            int color = quad.color;

            if (flower[r][c]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (isOut(nr, nc)) {
                    continue;
                }

                if (data[nr][nc] == WATER || flower[nr][nc]) {
                    continue;
                }

                if ((color == GREEN && redVisited[nr][nc] == v + 1) ||
                        (color == RED && greenVisited[nr][nc] == v + 1)) {
                    flower[nr][nc] = true;
                    result++;
                    continue;
                }

                if (redVisited[nr][nc] > 0 || greenVisited[nr][nc] > 0) {
                    continue;
                }

                queue.add(new Quad(nr, nc, v + 1, color));
                if (color == RED) {
                    redVisited[nr][nc] = v + 1;
                } else {
                    greenVisited[nr][nc] = v + 1;
                }
            }
        }
        return result;
    }

    private static boolean isOut(int x, int y) {
        return x >= n || y >= m || x < 0 || y < 0;
    }

    private static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Quad {
        int r, c, v, color;

        public Quad(int r, int c, int v, int color) {
            this.r = r;
            this.c = c;
            this.v = v;
            this.color = color;
        }
    }
}
