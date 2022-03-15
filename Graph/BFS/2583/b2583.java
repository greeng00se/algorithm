package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class b2583 {

    static int n, m, k;
    static boolean[][] data;
    static boolean[][] visited;
    static List<Integer> result = new ArrayList<>();
    static int[] dr = new int[]{-1, 0, 1, 0};
    static int[] dc = new int[]{0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        getData(br);
        visited = new boolean[n][m];

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (visited[r][c] || data[r][c]) {
                    continue;
                }
                int count = bfs(r, c);
                result.add(count);
            }
        }

        System.out.println(result.size());
        result.stream()
                .sorted()
                .map(String::valueOf)
                .forEach(v -> System.out.print(v + " "));
    }

    private static void getData(BufferedReader br) throws IOException {
        StringTokenizer st;
        data = new boolean[n][m];
        
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for (int c = x1; c < x2; c++) {
                for (int r = y1; r < y2; r++) {
                    data[r][c] = true;
                }
            }
        }
    }

    private static int bfs(int x, int y) {
        LinkedList<Pair> queue = new LinkedList<>();
        queue.add(new Pair(x, y));
        visited[x][y] = true;
        int rv = 1;

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int r = pair.x;
            int c = pair.y;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (isOut(nr, nc) || visited[nr][nc] || data[nr][nc]) {
                    continue;
                }

                queue.add(new Pair(nr, nc));
                visited[nr][nc] = true;
                rv++;
            }
        }

        return rv;
    }

    private static boolean isOut(int x, int y) {
        return x < 0 || y < 0 || x >= n || y >= m;
    }

    private static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
