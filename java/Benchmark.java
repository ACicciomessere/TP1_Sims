import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Benchmark {

    // Archivo usado para comparar brute force y cell index method
    // Y buscar el M optimo
    public static void main(String[] args) {
        double L = 20.0;
        double rc = 1.0;
        boolean periodic = true;
        double r_min = 0.23;
        double r_max = 0.26;
        int runs = 10;

        // 1. Time vs N
        List<Integer> N_values = Arrays.asList(100, 250, 500, 750, 1000);
        int fixed_M = 13; // 20 / (1 + 0.52) = 13.15 -> 13 maximo M (optimo)

        System.out.println("Starting Benchmark 1: Time vs N (Fixed M=" + fixed_M + ")");
        try (FileWriter writer = new FileWriter("benchmark_N.txt")) {
            writer.write("N BF_Avg BF_Std CIM_Avg CIM_Std\n");
            for (int N : N_values) {
                double[] bfTimes = new double[runs];
                double[] cimTimes = new double[runs];
                System.out.println("Running for N=" + N);

                for (int r = 0; r < runs; r++) {
                    ArrayList<Particle> particles = generateParticles(N, L, r_min, r_max, periodic);
                    bfTimes[r] = App.bruteForce(particles, L, rc, periodic) / 1_000_000.0; // to ms
                    cimTimes[r] = App.cellIndexMethod(particles, L, fixed_M, rc, periodic) / 1_000_000.0;
                }

                double[] bfStats = getStats(bfTimes);
                double[] cimStats = getStats(cimTimes);
                writer.write(String.format("%d %f %f %f %f\n", N, bfStats[0], bfStats[1], cimStats[0], cimStats[1]));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 2. Time vs M
        List<Integer> M_values = Arrays.asList(1, 2, 4, 5, 8, 10, 13);
        int fixed_N = 1000;

        System.out.println("\nStarting Benchmark 2: Time vs M (Fixed N=" + fixed_N + ")");
        try (FileWriter writer = new FileWriter("benchmark_M.txt")) {
            writer.write("M BF_Avg BF_Std CIM_Avg CIM_Std\n");
            for (int M : M_values) {
                double[] bfTimes = new double[runs];
                double[] cimTimes = new double[runs];
                System.out.println("Running for M=" + M);

                for (int r = 0; r < runs; r++) {
                    ArrayList<Particle> particles = generateParticles(fixed_N, L, r_min, r_max, periodic);
                    bfTimes[r] = App.bruteForce(particles, L, rc, periodic) / 1_000_000.0;
                    cimTimes[r] = App.cellIndexMethod(particles, L, M, rc, periodic) / 1_000_000.0;
                }

                double[] bfStats = getStats(bfTimes);
                double[] cimStats = getStats(cimTimes);
                writer.write(String.format("%d %f %f %f %f\n", M, bfStats[0], bfStats[1], cimStats[0], cimStats[1]));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("\nBenchmarks Complete.");
    }

    private static ArrayList<Particle> generateParticles(int N, double L, double r_min, double r_max,
            boolean periodic) {
        ArrayList<Particle> particles = new ArrayList<>();
        Random rand = new Random();
        for (int i = 0; i < N; i++) {
            boolean overlaps;
            double rx, ry, radius;
            do {
                overlaps = false;
                rx = rand.nextDouble() * L;
                ry = rand.nextDouble() * L;
                radius = r_min + rand.nextDouble() * (r_max - r_min);
                for (Particle p : particles) {
                    double dx = Math.abs(rx - p.getX());
                    double dy = Math.abs(ry - p.getY());
                    if (periodic) {
                        if (dx > L / 2)
                            dx = L - dx;
                        if (dy > L / 2)
                            dy = L - dy;
                    }
                    if (Math.sqrt(dx * dx + dy * dy) < radius + p.getRadius()) {
                        overlaps = true;
                        break;
                    }
                }
            } while (overlaps);
            particles.add(new Particle(i, rx, ry, 0.0, 0.0, radius, 1.0));
        }
        return particles;
    }

    private static double[] getStats(double[] times) {
        double sum = 0;
        for (double t : times)
            sum += t;
        double mean = sum / times.length;

        double sqSum = 0;
        for (double t : times)
            sqSum += Math.pow(t - mean, 2);
        double std = Math.sqrt(sqSum / times.length);

        return new double[] { mean, std };
    }
}
