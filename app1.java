import java.util.*;
import java.util.stream.Collectors;

// ─── Product ────────────────────────────────────────────────────────────────

class Product {
    private final int id;
    private final String name;
    private final String category;
    private final double price;   // USD
    private final String emoji;
    private final String tag;     // "sale", "new", or ""
    private final int stars;      // 1–5

    public Product(int id, String name, String category,
                   double price, String emoji, String tag, int stars) {
        this.id       = id;
        this.name     = name;
        this.category = category;
        this.price    = price;
        this.emoji    = emoji;
        this.tag      = tag;
        this.stars    = stars;
    }

    public int    getId()       { return id; }
    public String getName()     { return name; }
    public String getCategory() { return category; }
    public double getPrice()    { return price; }
    public String getEmoji()    { return emoji; }
    public String getTag()      { return tag; }
    public int    getStars()    { return stars; }

    @Override
    public String toString() {
        String starStr = "★".repeat(stars) + "☆".repeat(5 - stars);
        String tagStr  = tag.isEmpty() ? "" : " [" + tag.toUpperCase() + "]";
        return String.format("%-20s %-12s $%6.2f  %s%s",
                name, category, price, starStr, tagStr);
    }
}

// ─── Cart ────────────────────────────────────────────────────────────────────

class Cart {
    private final Map<Integer, Integer> items = new LinkedHashMap<>(); // productId → qty
    private final Map<Integer, Product> catalog;

    public Cart(Map<Integer, Product> catalog) {
        this.catalog = catalog;
    }

    public void addItem(int productId) {
        if (!catalog.containsKey(productId))
            throw new NoSuchElementException("Product ID " + productId + " not found.");
        items.merge(productId, 1, Integer::sum);
    }

    public void removeItem(int productId) {
        if (!items.containsKey(productId))
            throw new NoSuchElementException("Product ID " + productId + " not in cart.");
        items.compute(productId, (k, v) -> (v == 1) ? null : v - 1);
    }

    public void clear() { items.clear(); }

    public int getTotalItems() {
        return items.values().stream().mapToInt(Integer::intValue).sum();
    }

    public double getSubtotal() {
        return items.entrySet().stream()
                .mapToDouble(e -> catalog.get(e.getKey()).getPrice() * e.getValue())
                .sum();
    }

    public void printReceipt() {
        if (items.isEmpty()) { System.out.println("  Cart is empty."); return; }
        System.out.println("  ┌─────────────────────────────────────────────────┐");
        System.out.println("  │                   CART RECEIPT                  │");
        System.out.println("  ├─────────────────────────────────────────────────┤");
        items.forEach((id, qty) -> {
            Product p = catalog.get(id);
            System.out.printf("  │  %-20s x%-3d  $%7.2f          │%n",
                    p.getName(), qty, p.getPrice() * qty);
        });
        System.out.println("  ├─────────────────────────────────────────────────┤");
        System.out.printf("  │  %-25s       $%7.2f          │%n",
                "Subtotal (" + getTotalItems() + " items)", getSubtotal());
        System.out.printf("  │  %-25s       $%7.2f          │%n", "Tax (8%)", getSubtotal() * 0.08);
        System.out.printf("  │  %-25s       $%7.2f          │%n", "TOTAL", getSubtotal() * 1.08);
        System.out.println("  └─────────────────────────────────────────────────┘");
    }
}

// ─── Store ───────────────────────────────────────────────────────────────────

class Store {
    private final String name;
    private final Map<Integer, Product> catalog = new LinkedHashMap<>();
    private final List<String> navCategories = List.of(
            "All", "Electronics", "Fashion", "Home & Living", "Sports", "Beauty");

    public Store(String name) {
        this.name = name;
    }

    public void addProduct(Product p) {
        catalog.put(p.getId(), p);
    }

    public Map<Integer, Product> getCatalog() {
        return Collections.unmodifiableMap(catalog);
    }

    public List<Product> getByCategory(String category) {
        if (category.equalsIgnoreCase("All")) return new ArrayList<>(catalog.values());
        return catalog.values().stream()
                .filter(p -> p.getCategory().equalsIgnoreCase(category))
                .collect(Collectors.toList());
    }

    public List<Product> getByTag(String tag) {
        return catalog.values().stream()
                .filter(p -> p.getTag().equalsIgnoreCase(tag))
                .collect(Collectors.toList());
    }

    public Cart newCart() { return new Cart(catalog); }

    public void printHeader() {
        System.out.println("╔═══════════════════════════════════════════════════╗");
        System.out.printf( "║            Welcome to %-28s║%n", name);
        System.out.println("╚═══════════════════════════════════════════════════╝");
        System.out.println("  Nav: " + String.join("  |  ", navCategories));
        System.out.println();
    }

    public void printAllProducts() {
        System.out.printf("  %-20s %-12s %-8s %-7s %s%n",
                "Name", "Category", "Price", "Rating", "Tag");
        System.out.println("  " + "─".repeat(62));
        catalog.values().forEach(p -> System.out.println("  " + p));
        System.out.println();
    }
}

// ─── Main ────────────────────────────────────────────────────────────────────

public class EcommerceApp {

    public static void main(String[] args) {

        // Build store
        Store store = new Store("ShopArc  🛍️");

        store.addProduct(new Product(1, "Wireless Buds",   "Audio",       35.99, "🎧", "sale", 4));
        store.addProduct(new Product(2, "Smart Watch",     "Wearables",   99.99, "⌚", "new",  5));
        store.addProduct(new Product(3, "Running Shoes",   "Footwear",    39.99, "👟", "sale", 4));
        store.addProduct(new Product(4, "Desk Lamp",       "Home",        13.99, "💡", "",     4));
        store.addProduct(new Product(5, "Mechanical KB",   "Accessories", 64.99, "⌨️", "new",  5));
        store.addProduct(new Product(6, "Yoga Mat",        "Fitness",     10.99, "🧘", "sale", 4));

        // Print storefront
        store.printHeader();
        System.out.println("  ── All Products ──────────────────────────────────");
        store.printAllProducts();

        // Filter: sale items
        System.out.println("  ── On Sale ───────────────────────────────────────");
        store.getByTag("sale").forEach(p ->
                System.out.printf("  %-20s  $%.2f%n", p.getName(), p.getPrice()));
        System.out.println();

        // Simulate shopping session
        System.out.println("  ── Shopping Session ──────────────────────────────");
        Cart cart = store.newCart();
        cart.addItem(1);   // Wireless Buds
        cart.addItem(2);   // Smart Watch
        cart.addItem(1);   // Wireless Buds (add again → qty 2)
        cart.addItem(5);   // Mechanical KB
        cart.removeItem(2); // changed mind on Watch

        System.out.println();
        cart.printReceipt();

        // Checkout confirmation
        System.out.printf("%n  ✔  Order placed! $%.2f charged. Thank you for shopping at ShopArc!%n",
                cart.getSubtotal() * 1.08);
    }
}