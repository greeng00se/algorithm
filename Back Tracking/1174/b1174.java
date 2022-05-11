import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class b1174 {

    static int n;
    static List<Long> numbers = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < 10; i++) {
            bt(String.valueOf(i), i);
        }

        Collections.sort(numbers);
        System.out.println(n > numbers.size() ? -1 : numbers.get(n - 1));
    }

    private static void bt(String now, int start) {

        if (now.length() > 10) {
            return;
        }

        numbers.add(Long.parseLong(now));

        for (int i = start - 1; i >= 0; i--) {
            bt(now + String.valueOf(i), i);
        }
    }
}
