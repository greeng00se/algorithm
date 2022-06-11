package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b5766 {

    static int n, m;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            if (n == 0 && m == 0) {
                break;
            }

            HashMap<Integer, Integer> point = getPoint();
            LinkedList<Map.Entry<Integer, Integer>> entryList = getSortedEntryList(point);
            printResult(entryList);
        }
    }

    private static HashMap<Integer, Integer> getPoint() throws IOException {
        StringTokenizer st;
        HashMap<Integer, Integer> point = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int key = Integer.parseInt(st.nextToken());
                point.put(key, point.getOrDefault(key, 0) + 1);
            }
        }
        return point;
    }

    private static LinkedList<Map.Entry<Integer, Integer>> getSortedEntryList(HashMap<Integer, Integer> point) {
        LinkedList<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(point.entrySet());
        entryList.sort(new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                if (o1.getValue() == o2.getValue()) {
                    return o1.getKey() - o2.getKey();
                }
                return o2.getValue() - o1.getValue();
            }
        });
        return entryList;
    }

    private static void printResult(LinkedList<Map.Entry<Integer, Integer>> entryList) {
        Integer flag = entryList.get(1).getValue();
        for (Map.Entry<Integer, Integer> integerIntegerEntry : entryList) {
            if (integerIntegerEntry.getValue() == flag) {
                System.out.print(integerIntegerEntry.getKey() + " ");
            }
        }
        System.out.println();
    }
}
