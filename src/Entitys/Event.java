package Entitys;

public class Event {
    private String name;
    private String description;
    private EventEffect effect;

    public Event() {}

    public Event(String name, String description, EventEffect effect) {
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

    public EventEffect getEffect() {
        return effect;
    }
}
