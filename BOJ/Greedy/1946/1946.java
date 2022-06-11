package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class b1946 {

    static class Rank implements Comparable<Rank> {
        int paper;
        int interview;

        public Rank(int paper, int interview) {
            this.paper = paper;
            this.interview = interview;
        }

        public int getInterview() {
            return interview;
        }

        @Override
        public int compareTo(Rank o) {
            return Integer.compare(this.paper, o.paper);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int rep = Integer.parseInt(br.readLine());

        for (int i = 0; i < rep; i++) {
            solve(br);
        }
    }

    private static void solve(BufferedReader br) throws IOException {
        ArrayList<Rank> rank = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int paper = Integer.parseInt(st.nextToken());
            int interview = Integer.parseInt(st.nextToken());
            rank.add(new Rank(paper, interview));
        }

        Collections.sort(rank);

        int result = 1;
        int highRank = rank.get(0).getInterview();
        for (int i = 1; i < n; i++) {
            int interviewRank = rank.get(i).getInterview();
            if (highRank > interviewRank) {
                result += 1;
                highRank = interviewRank;
            }
        }
        System.out.println(result);
    }
}
