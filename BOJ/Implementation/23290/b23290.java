package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class b23290 {

    static int m, s;
    static int jr, jc;
    static List<Integer>[][] fish = new List[4][4];
    static List<Integer>[][] cloneFish = new List[4][4];
    static int[][] smell = new int[4][4];
    static int[] fr = new int[]{0, 0, -1, -1, -1, 0, 1, 1, 1};
    static int[] fc = new int[]{0, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[] sr = new int[]{0, -1, 0, 1, 0};
    static int[] sc = new int[]{0, 0, -1, 0, 1};
    static int[] bt = new int[3];
    static int maxEat;
    static int[] maxEatIdx = new int[3];

    public static void main(String[] args) throws IOException {
        init();
        for (int i = 0; i < s; i++) {
            setting();
            cloneFish();
            moveFish();
            findEatFish(0);
            eatFish();
            appendFish();
        }
        int result = getResult();
        System.out.println(result);
    }

    private static void printFish(String a) {
        System.out.println(a);
        for (List<Integer>[] lists : fish) {
            for (List<Integer> list : lists) {
                System.out.print(list + " ");
            }
            System.out.println();
        }
        System.out.println("=========");
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fish[i][j] = new ArrayList<>();
            }
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            fish[r - 1][c - 1].add(d);
        }

        st = new StringTokenizer(br.readLine());
        jr = Integer.parseInt(st.nextToken()) - 1;
        jc = Integer.parseInt(st.nextToken()) - 1;
    }

    private static void setting() {
        maxEat = -1;
        maxEatIdx = new int[]{0, 0, 0};
    }

    private static void cloneFish() {
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                cloneFish[r][c] = new ArrayList<>();
                for (Integer d : fish[r][c]) {
                    cloneFish[r][c].add(d);
                }
            }
        }
    }

    private static void moveFish() {
        List<Integer>[][] rv = new List[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                rv[i][j] = new ArrayList<>();
            }
        }

        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                for (Integer d : fish[r][c]) {
                    int nr = r;
                    int nc = c;
                    int nd = d;
                    boolean move = false;
                    for (int i = 0; i < 8; i++) {
                        if (d - i <= 0) {
                            nd = d - i + 8;
                        } else {
                            nd = d - i;
                        }
                        nr = r + fr[nd];
                        nc = c + fc[nd];

                        if (isOut(nr, nc) || smell[nr][nc] >= 1) {
                            continue;
                        }
                        if ((jr == nr) && (jc == nc)) {
                            continue;
                        }
                        move = true;
                        break;
                    }

                    if (move) {
                        rv[nr][nc].add(nd);
                    } else {
                        rv[r][c].add(d);
                    }
                }
            }
        }

        fish = rv.clone();
    }

    private static boolean isOut(int x, int y) {
        return (x >= 4) || (y >= 4) || (x < 0) || (y < 0);
    }

    private static void findEatFish (int idx) {
        if (idx == 3) {
            boolean[][] visited = new boolean[4][4];
            int count = 0;
            int njr = jr;
            int njc = jc;
            for (int i = 0; i < 3; i++) {
                njr += sr[bt[i]];
                njc += sc[bt[i]];
                if (isOut(njr, njc)) {
                    count = Integer.MIN_VALUE;
                    break;
                }
                if (visited[njr][njc]) {
                    continue;
                }
                count += fish[njr][njc].size();
                visited[njr][njc] = true;
            }

            if (count > maxEat) {
                maxEatIdx = bt.clone();
                maxEat = count;
            }
        } else {
            for (int j = 1; j <= 4; j++) {
                bt[idx] = j;
                findEatFish(idx + 1);
            }
        }
    }

    private static void eatFish() {
        int njr = jr;
        int njc = jc;
        for (int i = 0; i < 3; i++) {
            njr += sr[maxEatIdx[i]];
            njc += sc[maxEatIdx[i]];
            if (fish[njr][njc].size() >= 1) {
                smell[njr][njc] = 3;
            }
            fish[njr][njc] = new ArrayList<>();
        }
        jr = njr;
        jc = njc;
    }

    private static void appendFish() {
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                smell[r][c] = Integer.max(smell[r][c] - 1, 0);
                for (Integer d : cloneFish[r][c]) {
                    fish[r][c].add(d);
                }
            }
        }
    }

    private static int getResult() {
        int result = 0;
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                result += fish[r][c].size();
            }
        }
        return result;
    }
}
