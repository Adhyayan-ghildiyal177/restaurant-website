
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="DeltaX Food | Order Online",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# Real food image URLs
# ---------------------------------------------------------
IMG = {
    "biryani": "https://images.unsplash.com/photo-1563379091339-03246963d7d4?auto=format&fit=crop&w=900&q=80",
    "pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=900&q=80",
    "burger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=80",
    "dosa": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?auto=format&fit=crop&w=900&q=80",
    "chinese": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?auto=format&fit=crop&w=900&q=80",
    "dessert": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80",
    "rolls": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=900&q=80",
    "thali": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=900&q=80",
    "momos": "https://images.unsplash.com/photo-1625398407796-82650a8c135f?auto=format&fit=crop&w=900&q=80",
    "cake": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80",
    "paratha": "https://images.unsplash.com/photo-1631452180539-96aca7d48617?auto=format&fit=crop&w=900&q=80",
    "coffee": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=900&q=80",
    "noodles": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?auto=format&fit=crop&w=900&q=80",
    "icecream": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=900&q=80",
    "sandwich": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=900&q=80",
    "juice": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=900&q=80",
}

CATEGORIES = [
    ("Biryani", IMG["biryani"]),
    ("Pizza", IMG["pizza"]),
    ("Burger", IMG["burger"]),
    ("Dosa", IMG["dosa"]),
    ("Chinese", IMG["chinese"]),
    ("Momos", IMG["momos"]),
    ("Desserts", IMG["dessert"]),
    ("Thali", IMG["thali"]),
]

COUPONS = {
    "DELTAX50": {"kind": "percent", "value": 50, "cap": 100, "label": "50% OFF up to ₹100"},
    "FREEDEL": {"kind": "delivery", "value": 29, "cap": 29, "label": "Free delivery"},
    "NEWUSER": {"kind": "flat", "value": 75, "cap": 75, "label": "Flat ₹75 OFF"},
    "TASTY20": {"kind": "percent", "value": 20, "cap": 80, "label": "20% OFF up to ₹80"},
}

RESTAURANTS = [
    {
        "id": "r1",
        "name": "DeltaX Biryani House",
        "cuisine": "Biryani, North Indian",
        "rating": 4.6,
        "rating_count": "1.2K+",
        "eta_min": 25,
        "eta_max": 30,
        "distance": 2.1,
        "price_for_two": 350,
        "offer": "50% OFF up to ₹100",
        "promoted": True,
        "pure_veg": False,
        "image": IMG["biryani"],
        "menu": {
            "Recommended": [
                {"id": "i101", "name": "Chicken Dum Biryani", "price": 199, "veg": False, "image": IMG["biryani"], "bestseller": True, "rating": 4.5, "desc": "Aromatic rice cooked with tender chicken and spices."},
                {"id": "i102", "name": "Veg Hyderabadi Biryani", "price": 159, "veg": True, "image": IMG["biryani"], "bestseller": True, "rating": 4.4, "desc": "Loaded with vegetables, herbs, and classic biryani masala."},
            ],
            "Starters": [
                {"id": "i103", "name": "Paneer Tikka", "price": 179, "veg": True, "image": IMG["thali"], "bestseller": False, "rating": 4.2, "desc": "Soft paneer cubes grilled with spicy marinade."},
                {"id": "i104", "name": "Boondi Raita", "price": 49, "veg": True, "image": IMG["dessert"], "bestseller": False, "rating": 4.1, "desc": "Cool curd with boondi and mild spices."},
            ],
        },
    },
    {
        "id": "r2",
        "name": "Pizza Planet DX",
        "cuisine": "Pizza, Italian, Fast Food",
        "rating": 4.4,
        "rating_count": "900+",
        "eta_min": 20,
        "eta_max": 25,
        "distance": 1.6,
        "price_for_two": 450,
        "offer": "Buy 1 Get 1",
        "promoted": False,
        "pure_veg": True,
        "image": IMG["pizza"],
        "menu": {
            "Recommended": [
                {"id": "i201", "name": "Margherita Pizza", "price": 199, "veg": True, "image": IMG["pizza"], "bestseller": True, "rating": 4.5, "desc": "Classic cheese pizza with fresh tomato sauce."},
                {"id": "i202", "name": "Farmhouse Pizza", "price": 279, "veg": True, "image": IMG["pizza"], "bestseller": True, "rating": 4.3, "desc": "Capsicum, onion, tomato, corn and extra cheese."},
            ],
            "Sides": [
                {"id": "i203", "name": "Garlic Bread", "price": 119, "veg": True, "image": IMG["sandwich"], "bestseller": False, "rating": 4.2, "desc": "Buttery garlic bread baked golden."},
                {"id": "i204", "name": "Cold Coffee", "price": 99, "veg": True, "image": IMG["coffee"], "bestseller": False, "rating": 4.1, "desc": "Chilled coffee with creamy foam."},
            ],
        },
    },
    {
        "id": "r3",
        "name": "Burger Junction",
        "cuisine": "Burgers, Snacks, Beverages",
        "rating": 4.2,
        "rating_count": "700+",
        "eta_min": 18,
        "eta_max": 22,
        "distance": 0.9,
        "price_for_two": 250,
        "offer": "₹75 OFF",
        "promoted": True,
        "pure_veg": False,
        "image": IMG["burger"],
        "menu": {
            "Recommended": [
                {"id": "i301", "name": "Veg Cheese Burger", "price": 99, "veg": True, "image": IMG["burger"], "bestseller": True, "rating": 4.4, "desc": "Crispy veg patty with cheese and sauces."},
                {"id": "i302", "name": "Chicken Burger", "price": 139, "veg": False, "image": IMG["burger"], "bestseller": True, "rating": 4.3, "desc": "Juicy chicken patty with fresh lettuce and cheese."},
            ],
            "Add-ons": [
                {"id": "i303", "name": "Peri Peri Fries", "price": 89, "veg": True, "image": IMG["burger"], "bestseller": False, "rating": 4.0, "desc": "Crispy fries tossed with peri peri spice."},
                {"id": "i304", "name": "Chocolate Shake", "price": 129, "veg": True, "image": IMG["dessert"], "bestseller": False, "rating": 4.1, "desc": "Thick chocolate shake with creamy finish."},
            ],
        },
    },
    {
        "id": "r4",
        "name": "South Express",
        "cuisine": "South Indian, Breakfast",
        "rating": 4.7,
        "rating_count": "2K+",
        "eta_min": 15,
        "eta_max": 20,
        "distance": 1.2,
        "price_for_two": 220,
        "offer": "Free delivery",
        "promoted": False,
        "pure_veg": True,
        "image": IMG["dosa"],
        "menu": {
            "Recommended": [
                {"id": "i401", "name": "Masala Dosa", "price": 109, "veg": True, "image": IMG["dosa"], "bestseller": True, "rating": 4.7, "desc": "Crispy dosa filled with spicy potato masala."},
                {"id": "i402", "name": "Idli Sambar", "price": 79, "veg": True, "image": IMG["dosa"], "bestseller": False, "rating": 4.4, "desc": "Soft idlis served with hot sambar and chutney."},
            ],
            "Breakfast Combos": [
                {"id": "i403", "name": "Vada Sambar", "price": 89, "veg": True, "image": IMG["dosa"], "bestseller": False, "rating": 4.2, "desc": "Crispy vada served with sambar."},
                {"id": "i404", "name": "Filter Coffee", "price": 49, "veg": True, "image": IMG["coffee"], "bestseller": True, "rating": 4.5, "desc": "Authentic South Indian filter coffee."},
            ],
        },
    },
    {
        "id": "r5",
        "name": "Chinese Wok DX",
        "cuisine": "Chinese, Momos, Noodles",
        "rating": 4.1,
        "rating_count": "600+",
        "eta_min": 30,
        "eta_max": 35,
        "distance": 3.3,
        "price_for_two": 300,
        "offer": "20% OFF",
        "promoted": False,
        "pure_veg": False,
        "image": IMG["chinese"],
        "menu": {
            "Recommended": [
                {"id": "i501", "name": "Veg Hakka Noodles", "price": 139, "veg": True, "image": IMG["noodles"], "bestseller": True, "rating": 4.3, "desc": "Wok-tossed noodles with crunchy vegetables."},
                {"id": "i502", "name": "Chicken Fried Rice", "price": 169, "veg": False, "image": IMG["chinese"], "bestseller": False, "rating": 4.1, "desc": "Fried rice with chicken and Asian sauces."},
            ],
            "Momos": [
                {"id": "i503", "name": "Veg Momos", "price": 99, "veg": True, "image": IMG["momos"], "bestseller": True, "rating": 4.2, "desc": "Steamed veg momos with spicy chutney."},
                {"id": "i504", "name": "Chilli Chicken", "price": 199, "veg": False, "image": IMG["chinese"], "bestseller": False, "rating": 4.0, "desc": "Spicy Indo-Chinese chicken starter."},
            ],
        },
    },
    {
        "id": "r6",
        "name": "Sweet Treats",
        "cuisine": "Desserts, Cakes, Ice Cream",
        "rating": 4.5,
        "rating_count": "850+",
        "eta_min": 20,
        "eta_max": 30,
        "distance": 2.8,
        "price_for_two": 280,
        "offer": "Flat ₹50 OFF",
        "promoted": True,
        "pure_veg": True,
        "image": IMG["cake"],
        "menu": {
            "Recommended": [
                {"id": "i601", "name": "Chocolate Cake", "price": 149, "veg": True, "image": IMG["cake"], "bestseller": True, "rating": 4.6, "desc": "Rich chocolate pastry with creamy layers."},
                {"id": "i602", "name": "Gulab Jamun", "price": 99, "veg": True, "image": IMG["dessert"], "bestseller": False, "rating": 4.3, "desc": "Soft gulab jamun served warm."},
            ],
            "Ice Cream": [
                {"id": "i603", "name": "Vanilla Ice Cream", "price": 89, "veg": True, "image": IMG["icecream"], "bestseller": False, "rating": 4.1, "desc": "Creamy vanilla scoop."},
                {"id": "i604", "name": "Brownie Sundae", "price": 129, "veg": True, "image": IMG["dessert"], "bestseller": True, "rating": 4.5, "desc": "Brownie with ice cream and chocolate sauce."},
            ],
        },
    },
]

# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------
defaults = {
    "cart": {},
    "selected_restaurant": None,
    "category_filter": "",
    "coupon_code": "",
    "applied_coupon": "",
    "order_placed": False,
    "last_order_id": "",
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown(
    """
<style>
:root {
    --brand: #fc8019;
    --brand-dark: #e46d12;
    --green: #1ba672;
    --text: #111827;
    --muted: #6b7280;
    --bg: #fff7ed;
    --card: #ffffff;
    --border: #eee2d5;
}
html, body, [class*="css"] {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.stApp {
    background:
      radial-gradient(circle at 8% 0%, rgba(252,128,25,.18), transparent 28%),
      radial-gradient(circle at 90% 6%, rgba(255,188,87,.22), transparent 26%),
      linear-gradient(180deg, #fff7ed 0%, #fffaf4 30%, #ffffff 100%);
    color: var(--text);
}
[data-testid="stHeader"] { background: transparent; }
.block-container {
    padding-top: 1rem;
    max-width: 1240px;
}
.dx-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255,255,255,.94);
    border: 1px solid #f1e4d8;
    border-radius: 22px;
    padding: 14px 20px;
    position: sticky;
    top: 0;
    z-index: 10;
    box-shadow: 0 12px 30px rgba(17,24,39,.08);
    backdrop-filter: blur(14px);
}
.dx-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: -.8px;
}
.dx-logo-badge {
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: linear-gradient(135deg, #fc8019, #ffb347);
    display: grid;
    place-items: center;
    color: white;
    font-size: 24px;
    box-shadow: 0 10px 24px rgba(252,128,25,.28);
}
.dx-logo span { color: var(--brand); }
.dx-nav {
    color: #374151;
    font-weight: 800;
}
.dx-nav-item {
    display: inline-block;
    margin-left: 18px;
}
.hero {
    margin: 22px 0 26px;
    border-radius: 32px;
    overflow: hidden;
    background: linear-gradient(135deg, #fc8019 0%, #ff9f37 46%, #ffcf86 100%);
    color: white;
    padding: 40px;
    position: relative;
    box-shadow: 0 22px 55px rgba(252,128,25,.26);
}
.hero::after {
    content: "";
    position: absolute;
    right: -80px;
    top: -120px;
    width: 360px;
    height: 360px;
    border-radius: 50%;
    background: rgba(255,255,255,.18);
}
.hero-title {
    font-size: 56px;
    line-height: 1.02;
    letter-spacing: -2px;
    font-weight: 900;
    margin: 0;
}
.hero-subtitle {
    font-size: 19px;
    max-width: 670px;
    margin-top: 12px;
    opacity: .96;
}
.hero-chip {
    display: inline-block;
    background: rgba(0,0,0,.18);
    border: 1px solid rgba(255,255,255,.28);
    padding: 9px 14px;
    border-radius: 999px;
    font-weight: 900;
    margin-bottom: 12px;
}
.search-panel {
    background: white;
    border: 1px solid #f1e4d8;
    border-radius: 26px;
    padding: 20px;
    box-shadow: 0 18px 40px rgba(17,24,39,.07);
    margin-bottom: 20px;
}
.section-heading {
    font-size: 28px;
    font-weight: 900;
    margin: 24px 0 14px;
    letter-spacing: -.7px;
}
.category-tile {
    background: white;
    border: 1px solid #f1e4d8;
    border-radius: 22px;
    padding: 10px;
    box-shadow: 0 12px 28px rgba(17,24,39,.06);
    text-align: center;
    transition: transform .15s ease, box-shadow .15s ease;
}
.category-tile:hover {
    transform: translateY(-3px);
    box-shadow: 0 18px 36px rgba(252,128,25,.14);
}
.category-img {
    height: 96px;
    border-radius: 18px;
    background-size: cover;
    background-position: center;
}
.category-name {
    font-weight: 900;
    margin-top: 9px;
}
.offer-row {
    background: #fff;
    border: 1px dashed #fc8019;
    color: #9a4b08;
    border-radius: 20px;
    padding: 16px 18px;
    font-weight: 900;
    margin: 18px 0 8px;
}
.restaurant-card {
    background: white;
    border: 1px solid #f1e4d8;
    border-radius: 26px;
    overflow: hidden;
    box-shadow: 0 16px 34px rgba(17,24,39,.07);
    margin-bottom: 18px;
    transition: transform .15s ease, box-shadow .15s ease;
}
.restaurant-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 22px 44px rgba(252,128,25,.16);
}
.rest-img {
    height: 180px;
    background-size: cover;
    background-position: center;
    position: relative;
}
.rest-offer {
    position: absolute;
    left: 12px;
    bottom: 12px;
    background: linear-gradient(90deg, #111827, #374151);
    color: #fff;
    border-radius: 999px;
    padding: 8px 12px;
    font-size: 13px;
    font-weight: 900;
}
.promoted {
    position: absolute;
    left: 12px;
    top: 12px;
    background: rgba(255,255,255,.92);
    color: #111827;
    border-radius: 999px;
    padding: 7px 11px;
    font-size: 12px;
    font-weight: 900;
}
.rest-body {
    padding: 16px;
}
.rest-title {
    font-size: 21px;
    font-weight: 900;
    margin-bottom: 4px;
}
.rest-meta {
    color: #6b7280;
    font-size: 14px;
    line-height: 1.5;
}
.rating-pill {
    display: inline-block;
    color: white;
    background: #1ba672;
    border-radius: 999px;
    padding: 3px 8px;
    font-size: 13px;
    font-weight: 900;
}
.menu-panel {
    background: #fff;
    border: 1px solid #f1e4d8;
    border-radius: 28px;
    padding: 22px;
    box-shadow: 0 18px 40px rgba(17,24,39,.07);
    margin: 22px 0;
}
.menu-top {
    background: #fff7ed;
    border: 1px solid #f4d4b8;
    border-radius: 22px;
    padding: 18px;
    margin-bottom: 18px;
}
.menu-category {
    font-size: 22px;
    font-weight: 900;
    margin: 22px 0 12px;
}
.item-card {
    background: #fff;
    border: 1px solid #f1e4d8;
    border-radius: 22px;
    padding: 14px;
    margin-bottom: 14px;
}
.item-img {
    height: 110px;
    border-radius: 18px;
    background-size: cover;
    background-position: center;
    border: 1px solid #eee;
}
.item-name {
    font-size: 17px;
    font-weight: 900;
}
.item-desc {
    color: #6b7280;
    font-size: 13px;
    margin-top: 5px;
}
.price {
    font-weight: 900;
    color: #111827;
    margin-top: 5px;
}
.bestseller {
    display: inline-block;
    color: #b45309;
    background: #fff7ed;
    border: 1px solid #fed7aa;
    border-radius: 999px;
    padding: 3px 8px;
    font-size: 12px;
    font-weight: 900;
}
.cart-panel {
    background: white;
    border: 1px solid #f1e4d8;
    border-radius: 28px;
    padding: 20px;
    box-shadow: 0 18px 40px rgba(17,24,39,.10);
    position: sticky;
    top: 90px;
}
.cart-line {
    border-bottom: 1px solid #f3f4f6;
    padding: 10px 0;
}
.qty-pill {
    display: inline-block;
    background: #fff7ed;
    border: 1px solid #fed7aa;
    border-radius: 999px;
    padding: 4px 10px;
    font-weight: 900;
    color: #c2410c;
}
.bill-line {
    display: flex;
    justify-content: space-between;
    margin: 7px 0;
    color: #374151;
}
.bill-total {
    display: flex;
    justify-content: space-between;
    margin-top: 11px;
    padding-top: 12px;
    border-top: 1px solid #e5e7eb;
    font-size: 20px;
    font-weight: 900;
}
.tracker-step {
    padding: 12px 14px;
    border-radius: 16px;
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    margin-bottom: 8px;
    font-weight: 800;
}
.tracker-step.active {
    background: #ecfdf5;
    border-color: #bbf7d0;
    color: #047857;
}
.footer {
    text-align: center;
    color: #6b7280;
    margin: 24px 0 10px;
    padding: 18px;
    background: #fff;
    border: 1px solid #f1e4d8;
    border-radius: 22px;
}
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stSelectbox"] div {
    border-radius: 14px;
}
.stButton > button {
    border-radius: 14px;
    border: 1px solid #fc8019;
    background: #fc8019;
    color: white;
    font-weight: 900;
}
.stButton > button:hover {
    background: #e46d12;
    color: white;
    border: 1px solid #e46d12;
}
@media (max-width: 900px) {
    .hero-title { font-size: 38px; }
    .dx-nav { display: none; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def all_items(restaurant):
    items = []
    for section_items in restaurant["menu"].values():
        items.extend(section_items)
    return items


def get_restaurant(restaurant_id):
    return next((r for r in RESTAURANTS if r["id"] == restaurant_id), None)


def get_item(item_id):
    for restaurant in RESTAURANTS:
        for item in all_items(restaurant):
            if item["id"] == item_id:
                return restaurant, item
    return None, None


def add_item(restaurant, item):
    item_id = item["id"]
    if item_id not in st.session_state.cart:
        st.session_state.cart[item_id] = {
            "qty": 0,
            "restaurant_id": restaurant["id"],
            "restaurant_name": restaurant["name"],
            "name": item["name"],
            "price": item["price"],
            "veg": item["veg"],
        }
    st.session_state.cart[item_id]["qty"] += 1


def decrease_item(item_id):
    if item_id in st.session_state.cart:
        st.session_state.cart[item_id]["qty"] -= 1
        if st.session_state.cart[item_id]["qty"] <= 0:
            del st.session_state.cart[item_id]


def bill_amounts():
    subtotal = sum(line["price"] * line["qty"] for line in st.session_state.cart.values())
    delivery = 29 if subtotal else 0
    platform = 5 if subtotal else 0
    taxes = round(subtotal * 0.05) if subtotal else 0

    discount = 0
    coupon = st.session_state.applied_coupon
    if coupon in COUPONS and subtotal:
        c = COUPONS[coupon]
        if c["kind"] == "flat":
            discount = min(c["value"], subtotal)
        elif c["kind"] == "percent":
            discount = min(round(subtotal * c["value"] / 100), c["cap"])
        elif c["kind"] == "delivery":
            discount = min(delivery, c["value"])

    total = max(subtotal + delivery + platform + taxes - discount, 0)
    return subtotal, delivery, platform, taxes, discount, total


# ---------------------------------------------------------
# Header and hero
# ---------------------------------------------------------
st.markdown(
    """
<div class="dx-header">
    <div class="dx-logo"><div class="dx-logo-badge">D</div>Delta<span>X</span> Food</div>
    <div class="dx-nav">
        <span class="dx-nav-item">Search</span>
        <span class="dx-nav-item">Offers</span>
        <span class="dx-nav-item">Help</span>
        <span class="dx-nav-item">Cart</span>
    </div>
</div>

<div class="hero">
    <div class="hero-chip">🔥 Food delivery demo website</div>
    <div class="hero-title">Order food online<br>near you</div>
    <div class="hero-subtitle">
        Browse real food images, restaurants, categories, offers, coupons, cart, checkout and demo order tracking.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Search panel
# ---------------------------------------------------------
st.markdown('<div class="search-panel">', unsafe_allow_html=True)
c1, c2, c3 = st.columns([1.6, 2.2, 1.2])
with c1:
    location = st.text_input("📍 Delivery location", placeholder="Rajnagar Extension, Ghaziabad")
with c2:
    search = st.text_input("🔍 Search restaurant or food", placeholder="Search for biryani, pizza, burger, dosa...")
with c3:
    sort_by = st.selectbox("Sort", ["Recommended", "Fast Delivery", "Rating", "Low Price", "Nearest"])

f1, f2, f3, f4 = st.columns(4)
with f1:
    veg_only = st.toggle("Pure Veg")
with f2:
    under_30 = st.toggle("Under 30 min")
with f3:
    top_rated = st.toggle("Ratings 4.3+")
with f4:
    offer_only = st.toggle("Offers")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Categories
# ---------------------------------------------------------
st.markdown('<div class="section-heading">What are you craving?</div>', unsafe_allow_html=True)
cat_cols = st.columns(4)
for i, (cat_name, cat_image) in enumerate(CATEGORIES[:4]):
    with cat_cols[i]:
        st.markdown(
            f"""
<div class="category-tile">
    <div class="category-img" style="background-image:url('{cat_image}')"></div>
    <div class="category-name">{cat_name}</div>
</div>
""",
            unsafe_allow_html=True,
        )
        if st.button(cat_name, key=f"cat_{cat_name}", use_container_width=True):
            st.session_state.category_filter = cat_name

cat_cols2 = st.columns(4)
for i, (cat_name, cat_image) in enumerate(CATEGORIES[4:]):
    with cat_cols2[i]:
        st.markdown(
            f"""
<div class="category-tile">
    <div class="category-img" style="background-image:url('{cat_image}')"></div>
    <div class="category-name">{cat_name}</div>
</div>
""",
            unsafe_allow_html=True,
        )
        if st.button(cat_name, key=f"cat2_{cat_name}", use_container_width=True):
            st.session_state.category_filter = cat_name

if st.session_state.category_filter:
    c_info, c_clear = st.columns([4, 1])
    with c_info:
        st.info(f"Category filter applied: {st.session_state.category_filter}")
    with c_clear:
        if st.button("Clear filter", use_container_width=True):
            st.session_state.category_filter = ""

st.markdown(
    """
<div class="offer-row">
🎁 Try coupon codes: DELTAX50 | FREEDEL | NEWUSER | TASTY20
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Filtering
# ---------------------------------------------------------
query = (search or st.session_state.category_filter or "").lower().strip()
filtered = RESTAURANTS.copy()

if query:
    filtered = [
        r
        for r in filtered
        if query in r["name"].lower()
        or query in r["cuisine"].lower()
        or any(query in item["name"].lower() for item in all_items(r))
    ]

if veg_only:
    filtered = [r for r in filtered if r["pure_veg"]]
if under_30:
    filtered = [r for r in filtered if r["eta_max"] <= 30]
if top_rated:
    filtered = [r for r in filtered if r["rating"] >= 4.3]
if offer_only:
    filtered = [r for r in filtered if bool(r["offer"])]

if sort_by == "Fast Delivery":
    filtered = sorted(filtered, key=lambda r: r["eta_min"])
elif sort_by == "Rating":
    filtered = sorted(filtered, key=lambda r: r["rating"], reverse=True)
elif sort_by == "Low Price":
    filtered = sorted(filtered, key=lambda r: r["price_for_two"])
elif sort_by == "Nearest":
    filtered = sorted(filtered, key=lambda r: r["distance"])
else:
    filtered = sorted(filtered, key=lambda r: (not r["promoted"], -r["rating"], r["eta_min"]))

# ---------------------------------------------------------
# Main content and cart
# ---------------------------------------------------------
left_col, right_col = st.columns([2.25, 1])

with left_col:
    st.markdown('<div class="section-heading">Restaurants near you</div>', unsafe_allow_html=True)

    if not filtered:
        st.warning("No restaurants found. Try another search or remove filters.")

    rest_cols = st.columns(2)
    for idx, r in enumerate(filtered):
        with rest_cols[idx % 2]:
            promoted = '<div class="promoted">PROMOTED</div>' if r["promoted"] else ""
            st.markdown(
                f"""
<div class="restaurant-card">
    <div class="rest-img" style="background-image:url('{r['image']}')">
        {promoted}
        <div class="rest-offer">{r['offer']}</div>
    </div>
    <div class="rest-body">
        <div class="rest-title">{r['name']}</div>
        <div class="rest-meta">{r['cuisine']}</div>
        <div class="rest-meta">
            <span class="rating-pill">★ {r['rating']}</span>
            &nbsp; {r['eta_min']}-{r['eta_max']} min • {r['distance']} km • ₹{r['price_for_two']} for two
        </div>
    </div>
</div>
""",
                unsafe_allow_html=True,
            )
            if st.button("View Menu", key=f"view_{r['id']}", use_container_width=True):
                st.session_state.selected_restaurant = r["id"]

    selected = get_restaurant(st.session_state.selected_restaurant)
    if selected:
        st.markdown('<div class="menu-panel">', unsafe_allow_html=True)
        st.markdown(
            f"""
<div class="menu-top">
    <h2 style="margin:0">{selected['name']}</h2>
    <div style="color:#6b7280; margin-top:5px;">
        {selected['cuisine']} • ★ {selected['rating']} ({selected['rating_count']}) • {selected['eta_min']}-{selected['eta_max']} min • {selected['distance']} km
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

        menu_search = st.text_input("Search in this menu", placeholder="Search dishes in selected restaurant")
        menu_query = menu_search.lower().strip()

        for section, items in selected["menu"].items():
            section_items = [
                item for item in items
                if not menu_query or menu_query in item["name"].lower() or menu_query in item["desc"].lower()
            ]
            if not section_items:
                continue

            st.markdown(f'<div class="menu-category">{section}</div>', unsafe_allow_html=True)
            for item in section_items:
                m1, m2, m3 = st.columns([1.1, 2.6, 1])
                with m1:
                    st.markdown(
                        f"""<div class="item-img" style="background-image:url('{item['image']}')"></div>""",
                        unsafe_allow_html=True,
                    )
                with m2:
                    veg_mark = "🟢 Veg" if item["veg"] else "🔴 Non-Veg"
                    best = '<span class="bestseller">⭐ Bestseller</span>' if item["bestseller"] else ""
                    st.markdown(
                        f"""
<div class="item-card">
    <div class="item-name">{item['name']}</div>
    <div>{veg_mark} &nbsp; ★ {item['rating']} &nbsp; {best}</div>
    <div class="item-desc">{item['desc']}</div>
    <div class="price">₹{item['price']}</div>
</div>
""",
                        unsafe_allow_html=True,
                    )
                with m3:
                    if st.button("ADD", key=f"add_{selected['id']}_{item['id']}", use_container_width=True):
                        add_item(selected, item)
                        st.toast(f"Added {item['name']}")
        st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="cart-panel">', unsafe_allow_html=True)
    st.markdown("### 🛒 Cart")

    if not st.session_state.cart:
        st.caption("Good food is always cooking. Add items to your cart.")
    else:
        for item_id, line in list(st.session_state.cart.items()):
            st.markdown(
                f"""
<div class="cart-line">
    <b>{line['name']}</b><br>
    <span style="color:#6b7280; font-size:13px;">{line['restaurant_name']}</span><br>
    ₹{line['price']} × <span class="qty-pill">{line['qty']}</span>
</div>
""",
                unsafe_allow_html=True,
            )
            q1, q2 = st.columns(2)
            with q1:
                if st.button("−", key=f"minus_{item_id}", use_container_width=True):
                    decrease_item(item_id)
                    st.rerun()
            with q2:
                restaurant, item = get_item(item_id)
                if restaurant and item and st.button("+", key=f"plus_{item_id}", use_container_width=True):
                    add_item(restaurant, item)
                    st.rerun()

        st.markdown("#### Coupon")
        coupon_input = st.text_input("Enter coupon", value=st.session_state.coupon_code, placeholder="DELTAX50")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Apply", use_container_width=True):
                code = coupon_input.upper().strip()
                st.session_state.coupon_code = code
                if code in COUPONS:
                    st.session_state.applied_coupon = code
                    st.success(COUPONS[code]["label"])
                else:
                    st.session_state.applied_coupon = ""
                    st.warning("Invalid coupon.")
        with c2:
            if st.button("Remove", use_container_width=True):
                st.session_state.coupon_code = ""
                st.session_state.applied_coupon = ""
                st.rerun()

        subtotal, delivery, platform, taxes, discount, total = bill_amounts()

        st.markdown("#### Bill Details")
        st.markdown(f'<div class="bill-line"><span>Item total</span><b>₹{subtotal}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bill-line"><span>Delivery fee</span><b>₹{delivery}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bill-line"><span>Platform fee</span><b>₹{platform}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bill-line"><span>Taxes</span><b>₹{taxes}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bill-line"><span>Discount</span><b>-₹{discount}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bill-total"><span>To pay</span><span>₹{total}</span></div>', unsafe_allow_html=True)

        st.markdown("#### Delivery Details")
        customer_name = st.text_input("Name")
        phone = st.text_input("Mobile")
        address = st.text_area("Address", value=location)
        payment = st.selectbox("Payment", ["Cash on Delivery", "UPI Demo", "Card Demo", "Wallet Demo"])

        if st.button("Place Demo Order", use_container_width=True):
            if not customer_name or not phone or not address:
                st.warning("Please fill name, mobile and address.")
            else:
                st.session_state.order_placed = True
                st.session_state.last_order_id = "DX" + datetime.now().strftime("%H%M%S")
                st.success(f"Order placed: {st.session_state.last_order_id}")
                st.balloons()

        if st.button("Clear Cart", use_container_width=True):
            st.session_state.cart = {}
            st.session_state.applied_coupon = ""
            st.session_state.coupon_code = ""
            st.session_state.order_placed = False
            st.session_state.last_order_id = ""
            st.rerun()

    if st.session_state.order_placed:
        st.markdown("### 🚚 Order Tracking")
        st.markdown('<div class="tracker-step active">✅ Order confirmed</div>', unsafe_allow_html=True)
        st.markdown('<div class="tracker-step active">👨‍🍳 Food is being prepared</div>', unsafe_allow_html=True)
        st.markdown('<div class="tracker-step">🛵 Delivery partner assigned</div>', unsafe_allow_html=True)
        st.markdown('<div class="tracker-step">🏠 Delivered</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
<div class="footer">
    © 2026 DeltaX Food. Original food-ordering demo website. Real payments and restaurant orders are not enabled.
</div>
""",
    unsafe_allow_html=True,
)
