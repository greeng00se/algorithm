package algorithm;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class b20210 {

    static int n;
    static Map<Character, Integer> alpha = new HashMap<>();
    static Pattern p = Pattern.compile("\\d+|[a-zA-Z]");
    static ArrayList<ArrayList<String>> data = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        init(br);

        Collections.sort(data, (o1, o2) -> {

            int lengthA = o1.size();
            int lengthB = o2.size();

            for (int i = 0; i < Integer.min(lengthA, lengthB); i++) {
                String a = o1.get(i);
                String b = o2.get(i);
                if (a.equals(b)) {
                    continue;
                }
                char charA = a.charAt(0);
                char charB = b.charAt(0);

                if (Character.isLetter(charA) && Character.isLetter(charB)) {
                    int diff = alpha.get(charA) - alpha.get(charB);
                    if (diff != 0) {
                        return diff;
                    }
                } else if (Character.isDigit(charA) && Character.isLetter(charB)) {
                    return -1;
                } else if (Character.isLetter(charA) && Character.isDigit(charB)) {
                    return 1;
                } else {
                    String replacedA = a.replaceFirst("^0+(?!$)", "");
                    String replacedB = b.replaceFirst("^0+(?!$)", "");

                    if (replacedA.equals(replacedB)) {
                        if (a.length() != b.length()) {
                            return a.length() - b.length();
                        }
                    } else {
                        if (replacedA.length() > replacedB.length()) {
                            return 1;
                        }
                        if (replacedA.length() < replacedB.length()) {
                            return -1;
                        }
                        int compare = replacedA.compareTo(replacedB);
                        if (compare != 0) {
                            return compare;
                        }
                    }
                }
            }
            return lengthA - lengthB;
        });

        for (ArrayList<String> s : data) {
            sb.append(String.join("", s) + "\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }

    private static void init(BufferedReader br) throws IOException {
        char bigA = 'A';
        char smallA = 'a';
        for (int i = 0; i < 26; i++) {
            alpha.put(bigA++, i * 2);
            alpha.put(smallA++, i * 2 + 1);
        }

        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            ArrayList<String> token = new ArrayList<>();
            String s = br.readLine();
            Matcher matcherA = p.matcher(s);
            while (matcherA.find()) {
                token.add(matcherA.group());
            }
            data.add(token);
        }
    }
}
