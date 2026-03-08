import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class InputGenerator {

    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("HELP: java -cp src InputGenerator <N> <L> <OutputPrefix>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double L = Double.parseDouble(args[1]);
        String prefix = args[2];

        double r_min = 0.23;
        double r_max = 0.26;
        double max_velocity = 5.0; // arbitrary max velocity
        double property = 1.0; // standard property

        generate(N, L, r_min, r_max, max_velocity, property, prefix);
    }

    public static void generate(int N, double L, double r_min, double r_max, double max_velocity, double property,
            String prefix) {
        try (FileWriter staticWriter = new FileWriter(prefix + "Static.txt");
                FileWriter dynamicWriter = new FileWriter(prefix + "Dynamic.txt")) {

            staticWriter.write(N + "\n");
            staticWriter.write(L + "\n");

            dynamicWriter.write("0\n"); // t0

            Random rand = new Random();
            double[][] positionsAndRadii = new double[N][3]; // x, y, r

            for (int i = 0; i < N; i++) {
                boolean overlaps;
                double rx, ry, radius;

                do {
                    overlaps = false;
                    rx = rand.nextDouble() * L;
                    ry = rand.nextDouble() * L;
                    radius = r_min + rand.nextDouble() * (r_max - r_min);

                    // Basic overlap check without periodic boundaries since generation doesn't
                    // strict require it
                    for (int j = 0; j < i; j++) {
                        double dx = Math.abs(rx - positionsAndRadii[j][0]);
                        double dy = Math.abs(ry - positionsAndRadii[j][1]);

                        double minDistance = radius + positionsAndRadii[j][2];
                        if (Math.sqrt(dx * dx + dy * dy) < minDistance) {
                            overlaps = true;
                            break;
                        }
                    }
                } while (overlaps);

                positionsAndRadii[i][0] = rx;
                positionsAndRadii[i][1] = ry;
                positionsAndRadii[i][2] = radius;

                // Write to static
                staticWriter.write(String.format("%f %f\n", radius, property).replace(',', '.'));

                // Write to dynamic
                double vx = rand.nextDouble() * max_velocity * (rand.nextBoolean() ? 1 : -1);
                double vy = rand.nextDouble() * max_velocity * (rand.nextBoolean() ? 1 : -1);
                dynamicWriter.write(String.format("%f %f %f %f\n", rx, ry, vx, vy).replace(',', '.'));
            }

            System.out.println("Generated files: " + prefix + "Static.txt and " + prefix + "Dynamic.txt");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
