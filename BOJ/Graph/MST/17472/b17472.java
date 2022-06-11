package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b17472 {

    static int n, m;
    static int[][] data;
    static boolean[][] visited;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int landCount;
    static List<Pair> checkList = new ArrayList<>();
    static List<Bridge> bridges = new ArrayList<>();
    static int[] parent;

    public static void main(String[] args) throws IOException {
        init();
        numberingLand();
        findBridge();
        int result = solve();
        System.out.println(result);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        data = new int[n][m];
        visited = new boolean[n][m];

        for (int r = 0; r < n; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < m; c++) {
                data[r][c] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private static void numberingLand() {
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (data[r][c] == 0 || visited[r][c]) {
                    continue;
                }
                landCount++;
                findLand(r, c);
            }
        }
    }

    private static void findLand(int x, int y) {
        visited[x][y] = true;
        data[x][y] = landCount;
        LinkedList<Pair> queue = new LinkedList<>();
        queue.add(new Pair(x, y));

        while(!queue.isEmpty()) {
            Pair pair = queue.poll();
            int r = pair.x;
            int c = pair.y;
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (isOut(nr, nc) || visited[nr][nc]) {
                    continue;
                }
                if (data[nr][nc] == 0) {
                    checkList.add(new Pair(r, c));
                    continue;
                }
                data[nr][nc] = landCount;
                visited[nr][nc] = true;
                queue.add(new Pair(nr, nc));
            }
        }
    }

    private static void findBridge() {
        LinkedList<Pair> queue = new LinkedList<>(checkList);
        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int r = pair.x;
            int c = pair.y;
            int flag = data[r][c];
            for (int i = 0; i < 4; i++) {
                int nr = r;
                int nc = c;
                int count = -1;
                while (true) {
                    count++;
                    nr += dr[i];
                    nc += dc[i];
                    if (isOut(nr, nc) || data[nr][nc] == flag) {
                        break;
                    }
                    if (data[nr][nc] == 0) {
                        continue;
                    }
                    if (data[nr][nc] != flag) {
                        if (count < 2) {
                            break;
                        }
                        bridges.add(new Bridge(count, flag, data[nr][nc]));
                        break;
                    }
                }
            }
        }
    }

    private static int solve() {
        int result = 0;
        parent = new int[landCount + 1];
        for (int i = 0; i < landCount + 1; i++) {
            parent[i] = i;
        }
        Collections.sort(bridges);

        for (Bridge bridge : bridges) {
            int value = bridge.v;
            int a = bridge.x;
            int b = bridge.y;
            if (find(a) == find(b)) {
                continue;
            }
            union(a, b);
            result += value;
        }

        int flag = find(1);
        for (int i = 1; i < landCount + 1; i++) {
            if (flag != find(i)) {
                result = -1;
            }
        }

        return result;
    }

    private static void union(int x, int y) {
        int a = find(x);
        int b = find(y);
        parent[a] = b;
    }

    private static int find(int x) {
        if (parent[x] == x) {
            return x;
        } else {
            parent[x] = find(parent[x]);
            return parent[x];
        }
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

    private static class Bridge implements Comparable<Bridge> {
        int v, x, y;

        public Bridge(int v, int x, int y) {
            this.v = v;
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Bridge o) {
            return this.v - o.v;
        }
    }
}
