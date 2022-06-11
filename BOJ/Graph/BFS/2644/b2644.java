import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b2644 {

    static int n, m;
    static int s, e;
    static List<Integer>[] adj;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(br.readLine());

        adj = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int child = Integer.parseInt(st.nextToken());
            int parent = Integer.parseInt(st.nextToken());
            adj[child].add(parent);
            adj[parent].add(child);
        }

        int result = bfs();
        System.out.println(result != Integer.MAX_VALUE ? result : -1);
    }

    private static int bfs() {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(s, 0));
        int[] visited = new int[n + 1];
        Arrays.fill(visited, Integer.MAX_VALUE);

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            for (Integer nxt : adj[node.now]) {

                if (visited[nxt] != Integer.MAX_VALUE) {
                    continue;
                }

                visited[nxt] = node.count + 1;
                queue.add(new Node(nxt, node.count + 1));
            }
        }
        return visited[e];
    }

    static class Node {
        int now, count;

        public Node(int now, int count) {
            this.now = now;
            this.count = count;
        }
    }
}
