package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class b14620 {

    static int n;
    static int[][] data;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static List<Pair> flower = new ArrayList<>();
    static int[] check = new int[3];
    static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        data = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                flower.add(new Pair(i, j));
            }
        }

        combination(0, 0);
        System.out.println(result);
    }

    static void combination(int depth, int index) {
        if (depth == 3) {
            boolean[][] visited = new boolean[n][n];
            for (boolean[] booleans : visited) {
                Arrays.fill(booleans, false);
            }

            int flowerValue = 0;

            for (int i = 0; i < 3; i++) {
                Pair pair = flower.get(check[i]);
                int r = pair.x;
                int c = pair.y;
                flowerValue += data[r][c];
                visited[r][c] = true;
                for (int j = 0; j < 4; j++) {
                    int nr = r + dr[j];
                    int nc = c + dc[j];
                    if (visited[nr][nc]) {
                        return;
                    }
                    flowerValue += data[nr][nc];
                    visited[nr][nc] = true;
                }
            }

            result = Integer.min(result, flowerValue);
            return;
        }

        for (int i = index; i < flower.size(); i++) {
            check[depth] = i;
            combination(depth + 1, i + 1);
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
