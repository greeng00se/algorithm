import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.StringTokenizer;

public class b1525 {

    static String ANSWER = "123456780";
    static int[] dr = new int[]{-1, 0, 1, 0};
    static int[] dc = new int[]{0, 1, 0, -1};
    static Map<String, Boolean> visited = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String s = "";
        for (int i = 0; i < 3; i++) {
            s += br.readLine().replaceAll(" ", "");
        }

        int result = bfs(s);
        System.out.println(result);
    }

    private static int bfs(String s) {
        LinkedList<Pair> queue = new LinkedList<>();
        queue.add(new Pair(s, 0));
        visited.put(s, true);

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            String string = pair.s;
            int now = pair.x;

            if (string.equals(ANSWER)) {
                return now;
            }

            int idx = string.indexOf('0');
            int r = idx / 3;
            int c = idx % 3;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (isOut(nr, nc)) {
                    continue;
                }

                int nextIdx = nr * 3 + nc;
                StringBuilder sb = new StringBuilder(string);
                sb.setCharAt(idx, string.charAt(nextIdx));
                sb.setCharAt(nextIdx, string.charAt(idx));
                String nextString = sb.toString();

                if (visited.getOrDefault(nextString, false)) {
                    continue;
                }
                visited.put(nextString, true);
                queue.add(new Pair(nextString, now + 1));
            }
        }

        return -1;
    }

    private static boolean isOut(int x, int y) {
        return x < 0 || y < 0 || x >= 3 || y >= 3;
    }

    private static class Pair {
        String s;
        int x;

        public Pair(String s, int x) {
            this.s = s;
            this.x = x;
        }
    }
}
