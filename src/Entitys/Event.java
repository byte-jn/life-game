package Entitys;

public class Event {
    private String name;
    private String description;
    private String effect;

    public Event() {}

    public Event(String name, String description, String effect) {
        this.name = name;
        this.description = description;
        this.effect = effect;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getEffect() {
        return effect;
    }
}

