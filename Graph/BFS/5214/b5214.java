import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b5214 {

    static int n, k, m;
    static int[][] data;
    static boolean[] stationVisited;
    static boolean[] tubeVisited;
    static Map<Integer, List<Integer>> adj = new HashMap<>();

    public static void main(String[] args) throws IOException {

        init();
        int result = bfs(1);
        System.out.println(result);
    }

    private static int bfs(int start) {
        LinkedList<Pair> queue = new LinkedList<>();
        queue.add(new Pair(start, 1));
        stationVisited[start] = true;

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int now = pair.x;
            int dist = pair.y;

            if (now == n) {
                return dist;
            }

            if (adj.get(now) == null) {
                continue;
            }

            for (int tubeIdx : adj.get(now)) {

                if (tubeVisited[tubeIdx]) {
                    continue;
                }
                tubeVisited[tubeIdx] = true;

                for (int i : data[tubeIdx]) {
                    if (stationVisited[i]) {
                        continue;
                    }
                    stationVisited[i] = true;
                    queue.add(new Pair(i, dist + 1));
                }
            }
        }
        return -1;
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        data = new int[m][k];
        stationVisited = new boolean[n + 1];
        tubeVisited = new boolean[m];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < k; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
                List<Integer> list = adj.computeIfAbsent(data[i][j], k -> new ArrayList<>());
                list.add(i);
            }
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
