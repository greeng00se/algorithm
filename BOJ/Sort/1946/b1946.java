package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class b1946 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            List<Pair> rank = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int paper = Integer.parseInt(st.nextToken());
                int interview = Integer.parseInt(st.nextToken());
                rank.add(new Pair(paper, interview));
            }

            solve(rank, n);
        }
    }

    private static void solve(List<Pair> rank, int n) {
        Collections.sort(rank);

        int result = 1;
        int highRank = rank.get(0).y;

        for (int i = 1; i < n; i++) {
            int volunteerRank = rank.get(i).y;
            if (highRank > volunteerRank) {
                highRank = volunteerRank;
                result++;
            }
        }

        System.out.println(result);
    }

    private static class Pair implements Comparable<Pair>{
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pair o) {
            return this.x - o.x;
        }
    }
}
