package ItemsValue;

public class ItemValues {
    private double durabilityIncrease;
    private double damageIncrease;
    private double coolDownIncrease;

    public ItemValues() {}

    public ItemValues(double durabilityIncrease, double damageIncrease, double coolDownIncrease) {
        this.durabilityIncrease = durabilityIncrease;
        this.damageIncrease = damageIncrease;
        this.coolDownIncrease = coolDownIncrease;
    }

    public double getDurabilityIncrease() {
        return (durabilityIncrease + 100) / 100;
    }

    public double getDamageIncrease() {
        return (damageIncrease + 100) / 100;
    }

    public double getCoolDownIncrease() {
        return (coolDownIncrease + 100) / 100;
    }
}
