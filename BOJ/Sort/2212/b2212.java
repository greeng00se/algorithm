import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b2212 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        int[] data = new int[n];
        int[] diff = new int[n - 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data);

        for (int i = 0; i < n - 1; i++) {
            diff[i] = data[i + 1] - data[i];
        }
        Arrays.sort(diff);

        int result = 0;
        // 집중국이 k개가 설치되어 있으면 비교 값은 n - k개
        // 센서 6개, 집중국 2개
        // 비교값 5개 2, 3, 0, 1, 2
        // 0, 1, 2, 2, 3
        // 3을 제외하면 아래 그림이 나온다
        // ex) (1, 3) | (6, 6, 7, 9)
        // 2 | 0, 1, 2
        for (int i = 0; i < n - k; i++) {
            result += diff[i];
        }

        System.out.println(result);
    }
}
