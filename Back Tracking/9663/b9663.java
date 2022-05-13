package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b9663 {

    static int n;
    static int[] data = new int[15];
    static int result = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        bt(0);
        System.out.println(result);

    }

    private static void bt(int depth) {

        if (depth >= n) {
            result++;
            return;
        }

        for (int i = 0; i < n; i++) {
            data[depth] = i;
            if (check(depth)) {
                bt(depth + 1);
            }
        }
    }

    private static boolean check(int depth) {

        for (int i = 0; i < depth; i++) {
            if (data[depth] == data[i] || Math.abs(data[depth] - data[i]) == Math.abs(depth - i)) {
                return false;
            }
        }

        return true;
    }
}
