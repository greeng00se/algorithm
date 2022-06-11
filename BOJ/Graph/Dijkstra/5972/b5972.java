package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class b5972 {

    static int n, m;
    static ArrayList<Node>[] adj;
    static int[] distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            adj[s].add(new Node(e, cost));
            adj[e].add(new Node(s, cost));
        }

        distance = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        int startIdx = 1;
        int result = dijkstra(startIdx);
        System.out.println(result);
    }

    public static int dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        distance[1] = 0;
        pq.offer(new Node(start, 0));

        while(!pq.isEmpty()) {
            Node now = pq.poll();

            ArrayList<Node> nodes = adj[now.getIdx()];
            for (Node nxt : nodes) {
                int nxtIdx = nxt.getIdx();
                int nxtCost = now.getCost() + nxt.getCost();
                if (distance[nxtIdx] > nxtCost) {
                    distance[nxtIdx] = nxtCost;
                    pq.offer(new Node(nxtIdx, distance[nxtIdx]));
                }
            }
        }

        return distance[n];
    }

    static class Node implements Comparable<Node> {

        int idx;
        int cost;

        public Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }

        public int getIdx() {
            return idx;
        }

        public int getCost() {
            return cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }
}
