package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b3019 {

    static int n, m;
    static int[] dr = {-1, 0, 1};
    static int[] dc = {1, 1, 1};
    static char[][] data;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        init();

        int result = 0;
        for (int i = 0; i < n; i++) {
            if (dfs(i, 0)) {
                result++;
            }
        }
        System.out.println(result);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new char[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                data[i][j] = s.charAt(j);
            }
        }
    }

    private static boolean dfs(int r, int c) {
        visited[r][c] = true;

        if (c == m - 1) {
            return true;
        }

        for (int i = 0; i < 3; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (isOut(nr, nc)) {
                continue;
            }

            if (visited[nr][nc] || data[nr][nc] == 'x') {
                continue;
            }

            if (dfs(nr, nc)) {
                return true;
            }
        }

        return false;
    }

    private static boolean isOut(int x, int y) {
        return x < 0 || x >= n || y < 0 || y >= m;
    }
}
