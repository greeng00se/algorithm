package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class b9328 {

    static int h, w;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static char[][] data;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            init(br);
            int result = bfs();
            System.out.println(result);
        }
    }

    private static void init(BufferedReader br) throws IOException {
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());

        data = new char[h + 2][w + 2];
        visited = new boolean[h + 2][w + 2];

        for (char[] chars : data) {
            Arrays.fill(chars, '.');
        }

        for (int i = 1; i < h + 1; i++) {
            String s = br.readLine();
            for (int j = 1; j < w + 1; j++) {
                data[i][j] = s.charAt(j - 1);
            }
        }

        String keyString = br.readLine();
        char[] key = keyString.toCharArray();
        for (int r = 0; r < h + 2; r++) {
            for (int c = 0; c < w + 2; c++) {
                if (!Character.isUpperCase(data[r][c])) {
                    continue;
                }
                for (int i = 0; i < key.length; i++) {
                    if (Character.toLowerCase(data[r][c]) == key[i]) {
                        data[r][c] = '.';
                    }
                }
            }
        }
    }

    private static int bfs() {
        LinkedList<Pair> queue = new LinkedList<>();
        queue.add(new Pair(0, 0));
        int result = 0;
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int r = pair.x;
            int c = pair.y;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (isOut(nr, nc)) {
                    continue;
                }

                if (data[nr][nc] == '*' || visited[nr][nc] || Character.isUpperCase(data[nr][nc])) {
                    continue;
                }

                if (data[nr][nc] == '.') {
                    queue.add(new Pair(nr, nc));
                    visited[nr][nc] = true;
                    continue;
                }

                if (data[nr][nc] == '$') {
                    result++;
                    queue.add(new Pair(nr, nc));
                    visited[nr][nc] = true;
                    data[nr][nc] = '.';
                    continue;
                }

                if (Character.isLowerCase(data[nr][nc])) {
                    char key = data[nr][nc];
                    remove(key);
                    queue.add(new Pair(nr, nc));
                    data[nr][nc] = '.';
                    visited = new boolean[h + 2][w + 2];
                    visited[nr][nc] = true;
                }
            }
        }

        return result;
    }

    private static void remove(char key) {
        for (int i = 0; i < h + 2; i++) {
            for (int j = 0; j < w + 2; j++) {
                if (data[i][j] == Character.toUpperCase(key)) {
                    data[i][j] = '.';
                }
            }
        }
    }

    private static boolean isOut(int x, int y) {
        return x < 0 || x >= h + 2 || y < 0 || y >= w + 2;
    }

    private static void print() {
        for (int i = 0; i < h + 2; i++) {
            System.out.println(data[i]);
        }
    }

    private static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
