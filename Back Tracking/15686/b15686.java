import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class b15686 {

    static int n, m;
    static int[][] data;
    static boolean[] usedIndexes;
    static List<Pair> house = new ArrayList<>();
    static List<Pair> store = new ArrayList<>();
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        init();
        solve(new int[m], 0, 0);
        System.out.println(answer);
    }

    private static void solve(int[] index, int depth, int start) {

        if (depth == m) {
            getChickenDistance(index);
            return;
        }

        for (int i = start; i < store.size(); i++) {
            if (usedIndexes[i]) {
                continue;
            }
            usedIndexes[i] = true;
            index[depth] = i;
            solve(index, depth + 1, i + 1);
            usedIndexes[i] = false;
        }
    }

    private static void getChickenDistance(int[] index) {
        int result = 0;

        for (int i = 0; i < house.size(); i++) {
            Pair housePosition = house.get(i);
            int minDistance = Integer.MAX_VALUE;

            for (int j = 0; j < m; j++) {
                Pair storePosition = store.get(index[j]);
                int difference = Math.abs(housePosition.x - storePosition.x) +
                        Math.abs(housePosition.y - storePosition.y);
                minDistance = Integer.min(minDistance, difference);
            }

            result += minDistance;
        }

        answer = Integer.min(answer, result);
    }



    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());

                if (data[i][j] == 1) {
                    house.add(new Pair(i, j));
                }
                if (data[i][j] == 2) {
                    store.add(new Pair(i, j));
                }
            }
        }

        usedIndexes = new boolean[store.size()];
    }

    private static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
