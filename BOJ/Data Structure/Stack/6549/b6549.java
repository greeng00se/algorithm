import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class b6549 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            if (n == 0) {
                break;
            }

            int[] data = new int[n + 2];
            data[0] = n;
            for (int i = 1; i <= n; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }
            data[n + 1] = 0;

            long result = 0;
            Stack<Integer> stack = new Stack<>();

            for (int i = 1; i < data.length; i++) {
                while (!stack.empty() && data[stack.lastElement()] > data[i]) {
                    int idx = stack.pop();
                    if (!stack.empty()) {
                        result = Long.max(result, (long) (i - stack.lastElement() - 1) * data[idx]);
                    } else {
                        result = Long.max(result, (long) (i - 1) * data[idx]);
                    }
                }
                stack.add(i);
            }
            System.out.println(result);
        }
    }
}
