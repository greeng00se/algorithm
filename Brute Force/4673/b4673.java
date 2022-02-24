package algorithm;

import java.util.stream.IntStream;

public class b4673 {

    public static void main(String[] args) {
        solution();
    }

    public static void solution() {
        boolean[] flags = new boolean[20002];

        for (int i = 1; i <= 10000; i++) {
            Integer splitSum = getSplitSum(i);
            flags[i + splitSum] = true;
        }

        for (int i = 1; i <= 10000; i++) {
            if (flags[i] == false) {
                System.out.println(i);
            }
        }
    }

    private static Integer getSplitSum(int i) {
        IntStream chars = String.valueOf(i).chars();
        int sumValue = chars.map(Character::getNumericValue).sum();
        return sumValue;
//        return Arrays.stream(Integer.toString(i).split(""))
//                .map(Integer::parseInt).reduce(0, Integer::sum);
    }
}
