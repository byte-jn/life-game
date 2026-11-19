import Service.Instance;

public class Main {
    public static void main(String[] args) {
        try {
            run();
        } catch (Exception exception) {
            System.out.println("Error: " + exception.getMessage());
            System.exit(1);
        }
        System.exit(0);
    }

    private static void run() throws Exception {
        Instance instance = new Instance();

        instance.chosePlayerDifficulty();
        instance.configurePlayerName();
        while (instance.playerAlive()) {
            instance.wanderAround();
            instance.printPlayerInfo();
        }
    }
}