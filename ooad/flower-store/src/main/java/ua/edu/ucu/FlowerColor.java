package ua.edu.ucu;

public enum FlowerColor {
    /**
     * Flower colors.
     */
    RED("#FF0000"), BLUE("#0000FF");
    private final String hexCode;

    FlowerColor(String hexCode) {
        this.hexCode = hexCode;
    }

    @Override
    public String toString() {
        return hexCode;
    }
}
