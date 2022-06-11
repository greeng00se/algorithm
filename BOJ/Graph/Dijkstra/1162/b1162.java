package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class b1162 {

    static int n, m, k;
    static ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
    static long[][] distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n + 1; i++) {
            adj.add(new ArrayList<>());
        }

        distance = new long[n + 1][k + 1];
        for (long[] d : distance) {
            Arrays.fill(d, Long.MAX_VALUE);
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj.get(a).add(new Pair(b, w));
            adj.get(b).add(new Pair(a, w));
        }

        dijkstra(1);
        System.out.println(Arrays.stream(distance[n]).min().getAsLong());
    }

    private static void dijkstra(int start) {
        PriorityQueue<Triple> pq = new PriorityQueue<>();
        distance[start][0] = 0;
        pq.add(new Triple(0, start, 0));

        while (!pq.isEmpty()) {
            Triple triple = pq.poll();
            long dist = triple.dist;
            int now = triple.node;
            int pack = triple.pack;

            if (distance[now][pack] < dist) {
                continue;
            }

            for (Pair pair : adj.get(now)) {
                int node = pair.target;
                int w = pair.weight;

                if (pack < k && distance[node][pack + 1] > dist) {
                    distance[node][pack + 1] = dist;
                    pq.add(new Triple(distance[node][pack + 1], node, pack + 1));
                }

                if (distance[node][pack] > dist + w) {
                    distance[node][pack] = dist + w;
                    pq.add(new Triple(distance[node][pack], node, pack));
                }
            }
        }
    }

    private static class Pair {
        int target, weight;

        public Pair(int target, int weight) {
            this.target = target;
            this.weight = weight;
        }
    }

    private static class Triple implements Comparable<Triple> {
        long dist;
        int node, pack;

        public Triple(long dist, int node, int pack) {
            this.dist = dist;
            this.node = node;
            this.pack = pack;
        }

        @Override
        public int compareTo(Triple o) {
            Long longA = this.dist;
            Long longB = o.dist;
            return longA.compareTo(longB);
        }
    }
}
