class Solution {
    static int[] psum;

    public static String solution(String play_time, String adv_time, String[] logs) {
        int pt = stringToInt(play_time);
        int at = stringToInt(adv_time);

        psum = new int[pt + 1];

        for (String log : logs) {
            int s = stringToInt(log.substring(0, 8));
            int e = stringToInt(log.substring(9, 17));
            psum[s]++;
            psum[e]--;
        }

        for (int i = 1; i < pt; i++) {
            psum[i] += psum[i - 1];
        }

        long maxValue = 0L;
        long currentValue = 0L;
        int answer = 0;

        for (int i = 0; i < at; i++) {
            currentValue += psum[i];
        }
        maxValue = currentValue;

        for (int i = 1; i <= pt - at; i++) {
            currentValue = currentValue - psum[i - 1] + psum[i + at - 1];
            if (currentValue > maxValue) {
                maxValue = currentValue;
                answer = i;
            }
        }

        return intToString(answer);
    }

    static int stringToInt(String s) {
        int H = Integer.parseInt(s.substring(0, 2));
        int M = Integer.parseInt(s.substring(3, 5));
        int S = Integer.parseInt(s.substring(6, 8));
        return H * 3600 + M * 60 + S;
    }

    static String intToString(int n) {;
        String H = String.valueOf(n / 3600);
        n %= 3600;
        String M = String.valueOf(n / 60);
        String S = String.valueOf(n % 60);
        return padding(H) + ":" + padding(M) + ":" + padding(S);
    }

    static String padding(String s) {
        if (s.length() < 2) {
            return "0" + s;
        }
        return s;
    }
}