package Entitys;

import Service.EntityRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class EventEffect {
    private String name;
    private int value;
    private String group;
    private int count = 1;

    public EventEffect() {}

    public EventEffect(String name, int value) {
        this.name = name;
        this.value = value;
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = Math.max(1, count);
    }

    public String getGroup() {
        return group;
    }

    public Player processes(Player player) {
        if (player == null) {
            return null;
        }

        switch (name) {
            case "lose_health" -> applyLoseHealth(player);
            case "gain_item" -> applyGainItem(player);
            case "gain_info" -> applyGainInfo(player);
            default -> {
                return player;
            }
        }

        return player;
    }

    private void applyLoseHealth(Player player) {
        int damage = value;
        player.health = Math.max(0, player.health - damage);
    }

    private void applyGainItem(Player player) {
        int itemCount = value;

        for (int i = 0; i < itemCount; i++) {
            giveRandomItem(player);
        }
    }

    private void giveRandomItem(Player player) {
        try {
            List<Item> items = EntityRepository.getItems();
            List<Item> filteredItems = filterItemsByGroup(items);
            if (filteredItems.isEmpty()) {
                return;
            }

            Item item = filteredItems.get(ThreadLocalRandom.current().nextInt(filteredItems.size()));
            addOrIncreaseItem(player, item);
            System.out.println("You found an item: " + item.getName());
            if (item.getDescription() != null && !item.getDescription().isEmpty()) {
                System.out.println(item.getDescription());
            }
        } catch (Exception ignored) {
            // If item loading fails, the effect is skipped safely.
        }
    }

    private void applyGainInfo(Player player) {
        int infoCount = value;

        for (int i = 0; i < infoCount; i++) {
            giveRandomInfo(player);
        }
    }

    private void giveRandomInfo(Player player) {
        try {
            List<Info> infos = EntityRepository.getInfos();
            List<Info> filteredInfos = filterInfosByGroup(infos);
            if (filteredInfos.isEmpty()) {
                return;
            }

            Info info = filteredInfos.get(ThreadLocalRandom.current().nextInt(filteredInfos.size()));
            addOrIncreaseInfo(player, info);
            System.out.println("You learned some info: " + info.getName());
            if (info.getDescription() != null && !info.getDescription().isEmpty()) {
                System.out.println(info.getDescription());
            }
        } catch (Exception ignored) {
            // If info loading fails, the effect is skipped safely.
        }
    }

    private List<Item> filterItemsByGroup(List<Item> items) {
        if (group == null || group.isEmpty()) {
            return items;
        }

        List<Item> filteredItems = new ArrayList<>();
        for (Item item : items) {
            if (group.equals(item.getGroup())) {
                filteredItems.add(item);
            }
        }
        return filteredItems.isEmpty() ? items : filteredItems;
    }

    private List<Info> filterInfosByGroup(List<Info> infos) {
        if (group == null || group.isEmpty()) {
            return infos;
        }

        List<Info> filteredInfos = new ArrayList<>();
        for (Info info : infos) {
            if (group.equals(info.getGroup())) {
                filteredInfos.add(info);
            }
        }
        return filteredInfos.isEmpty() ? infos : filteredInfos;
    }

    private ArrayList<Item> ensureItems(Player player) {
        if (player.getItems() == null) {
            player.setItems(new ArrayList<>());
        }
        return player.getItems();
    }

    private ArrayList<Info> ensureInfos(Player player) {
        if (player.getInfos() == null) {
            player.setInfos(new ArrayList<>());
        }
        return player.getInfos();
    }

    private void addOrIncreaseItem(Player player, Item item) {
        ArrayList<Item> inventory = ensureItems(player);
        for (Item owned : inventory) {
            if (owned.getName() != null && owned.getName().equals(item.getName())) {
                owned.increaseCount(item.getCount());
                return;
            }
        }
        inventory.add(copyItem(item));
    }

    private void addOrIncreaseInfo(Player player, Info info) {
        ArrayList<Info> inventory = ensureInfos(player);
        for (Info owned : inventory) {
            if (owned.getName() != null && owned.getName().equals(info.getName())) {
                owned.increaseCount(info.getCount());
                return;
            }
        }
        inventory.add(copyInfo(info));
    }

    private Item copyItem(Item item) {
        return new Item(item.getName(), item.getDescription(), item.getGroup(), item.getCount());
    }

    private Info copyInfo(Info info) {
        return new Info(info.getName(), info.getDescription(), info.getGroup(), info.getCount());
    }
}
