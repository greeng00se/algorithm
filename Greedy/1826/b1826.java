import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b1826 {

    static int n;
    static LinkedList<Pair> gasStations = new LinkedList<>();
    static int l, p;

    public static void main(String[] args) throws IOException {
        init();
        int result = solve(gasStations, l, p);
        System.out.println(result);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int station = Integer.parseInt(st.nextToken());
            int fuel = Integer.parseInt(st.nextToken());
            gasStations.add(new Pair(station, fuel));
        }

        st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
    }

    private static int solve(LinkedList<Pair> gasStations, int destination, int currentGas) {
        Collections.sort(gasStations);
        int result = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        while (currentGas < destination) {
            while (!gasStations.isEmpty() && gasStations.getLast().station <= currentGas) {
                Pair pair = gasStations.pollLast();
                pq.add(pair.fuel);
            }

            if (pq.isEmpty()) {
                break;
            }

            currentGas += pq.poll();
            result += 1;
        }

        return destination <= currentGas ? result : -1;
    }

    private static class Pair implements Comparable<Pair> {
        int station, fuel;

        public Pair(int station, int fuel) {
            this.station = station;
            this.fuel = fuel;
        }

        @Override
        public int compareTo(Pair o) {
            if (this.station == o.station) {
                return this.fuel - o.fuel;
            }
            return o.station - this.station;
        }
    }
}
