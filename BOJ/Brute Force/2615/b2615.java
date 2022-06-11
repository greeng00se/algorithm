import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[][] data;
    static int[] dr = {-1, 0, 1, 1};
    static int[] dc = {1, 1, 1, 0};
    final static int MAX_LINES = 19;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        data = new int[MAX_LINES][MAX_LINES];

        for (int i = 0; i < MAX_LINES; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < MAX_LINES; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solve();
    }

    private static void solve() {
        for (int r = 0; r < MAX_LINES; r++) {
            for (int c = 0; c < MAX_LINES; c++) {
                if (data[r][c] == 0) {
                    continue;
                }

                int flag = data[r][c];

                for (int i = 0; i < 4; i++) {
                    int count = 0;

                    int backR = r - dr[i];
                    int backC = c - dc[i];
                    if (!isOut(backR, backC) && data[backR][backC] == flag) {
                        continue;
                    }

                    for (int multiple = 0; multiple < 5; multiple++) {
                        int nr = r + dr[i] * multiple;
                        int nc = c + dc[i] * multiple;
                        if (isOut(nr, nc) || data[nr][nc] != flag) {
                            break;
                        }
                        count++;
                    }

                    int nr = r + dr[i] * 5;
                    int nc = c + dc[i] * 5;

                    if (count == 5 && (isOut(nr, nc) || data[nr][nc] != flag)) {
                        System.out.println(flag);
                        System.out.println((r + 1) + " " + (c + 1));
                        return;
                    }
                }
            }
        }
        System.out.println(0);
        return;
    }

    private static boolean isOut(int x, int y) {
        return x < 0 || y < 0 || x >= MAX_LINES || y >= MAX_LINES;
    }
}
