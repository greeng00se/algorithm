package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class b1092 {

    static int n, m;
    static List<Integer> cranes = new ArrayList<>();
    static List<Integer> boxes = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        cranes = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .boxed()
                .sorted(Collections.reverseOrder())
                .collect(Collectors.toList());

        m = Integer.parseInt(br.readLine());
        boxes = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .boxed()
                .sorted(Collections.reverseOrder())
                .collect(Collectors.toList());

        int result = solve();
        System.out.println(result);
    }

    private static int solve() {
        if (cranes.get(0) < boxes.get(0)) {
            return -1;
        }

        int result = 0;

        while (!boxes.isEmpty()) {
            int craneIdx = 0;
            for (int i = 0; i < boxes.size(); i++) {
                if (boxes.size() == 0 || craneIdx == n) break;
                if (cranes.get(craneIdx) >= boxes.get(i)) {
                    craneIdx++;
                    boxes.remove(i);
                    i--;
                }
            }
            result++;
        }

        return result;
    }
}
