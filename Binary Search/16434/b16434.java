import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class b16434 {

    final static long MAX_HP = Long.MAX_VALUE;
    static int n, h;
    static List<Room> rooms = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            int attack = Integer.parseInt(st.nextToken());
            int health = Integer.parseInt(st.nextToken());
            rooms.add(new Room(type, attack, health));
        }

        long l = 1;
        long r = MAX_HP;
        long result = MAX_HP;

        while (l <= r) {
            long mid = (l + r) / 2;
            long heroAttack = h;
            long heroHp = mid;

            for (Room room : rooms) {
                if (room.type == 1) {
                    if (room.health % heroAttack == 0) {
                        heroHp -= (room.health / heroAttack - 1) * room.attack;
                    } else {
                        heroHp -= (room.health / heroAttack) * room.attack;
                    }
                } else {
                    heroAttack += room.attack;
                    heroHp = Long.min(mid, heroHp + room.health);
                }

                if (heroHp <= 0) {
                    break;
                }
            }

            if (heroHp <= 0) {
                l = mid + 1;
            } else {
                result = Long.min(result, mid);
                r = mid - 1;
            }
        }

        System.out.println(result);
    }

    static class Room {
        int type, attack, health;
        public Room(int type, int attack, int health) {
            this.type = type;
            this.attack = attack;
            this.health = health;
        }
    }
}
