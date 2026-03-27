package Entitys;

import java.util.List;

public class Location {
    private String name;
    private String description;
    private List<String> possibleEvents;

    public Location() {}

    public Location(String name, String description, List<String> possibleEvents) {
        this.name = name;
        this.description = description;
        this.possibleEvents = possibleEvents;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public List<String> getPossibleEvents() {
        return possibleEvents;
    }
}

