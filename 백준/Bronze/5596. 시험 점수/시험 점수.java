import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        int S = 0;
        int T = 0;

        while (st.hasMoreTokens()) {
            S += Integer.parseInt(st.nextToken());
        }

        while (st2.hasMoreTokens()) {
            T += Integer.parseInt(st2.nextToken());
        }

        if (S>=T) {
            System.out.println(S);
        } else {
            System.out.println(T);
        }
    }
}