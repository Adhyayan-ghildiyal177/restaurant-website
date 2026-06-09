
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="DeltaX Food | Order Online",
    page_icon="🍽️",
    layout="wide"
)

# -------------------------------------------------
# Real food-style image URLs
# -------------------------------------------------
FOOD_IMAGES = {
    "biryani": "https://images.unsplash.com/photo-1563379091339-03246963d7d4?auto=format&fit=crop&w=900&q=80",
    "pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=900&q=80",
    "burger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=80",
    "dosa": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?auto=format&fit=crop&w=900&q=80",
    "chinese": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?auto=format&fit=crop&w=900&q=80",
    "dessert": "https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=900&q=80",
    "rolls": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=900&q=80",
    "thali": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=900&q=80",
    "momos": "https://images.unsplash.com/photo-1625398407796-82650a8c135f?auto=format&fit=crop&w=900&q=80",
    "cake": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80",
}

categories = [
    {"name": "Biryani", "image": FOOD_IMAGES["biryani"]},
    {"name": "Pizza", "image": FOOD_IMAGES["pizza"]},
    {"name": "Burger", "image": FOOD_IMAGES["burger"]},
    {"name": "Dosa", "image": FOOD_IMAGES["dosa"]},
    {"name": "Chinese", "image": FOOD_IMAGES["chinese"]},
    {"name": "Desserts", "image": FOOD_IMAGES["dessert"]},
    {"name": "Rolls", "image": FOOD_IMAGES["rolls"]},
    {"name": "Thali", "image": FOOD_IMAGES["thali"]},
]

restaurants = [
    {
        "id": 1,
        "name": "DeltaX Biryani House",
        "cuisine": "Biryani, North Indian",
        "rating": 4.6,
        "time": "25-30 min",
        "offer": "50% OFF up to ₹100",
        "veg": False,
        "price_for_two": 350,
        "distance": "2.1 km",
        "image": FOOD_IMAGES["biryani"],
        "promoted": True,
        "menu": {
            "Recommended": [
                {"name": "Chicken Biryani", "price": 199, "veg": False, "image": FOOD_IMAGES["biryani"], "bestseller": True},
                {"name": "Veg Biryani", "price": 149, "veg": True, "image": FOOD_IMAGES["biryani"], "bestseller": False},
            ],
            "Starters": [
                {"name": "Paneer Tikka", "price": 179, "veg": True, "image": FOOD_IMAGES["thali"], "bestseller": True},
                {"name": "Raita", "price": 39, "veg": True, "image": FOOD_IMAGES["dessert"], "bestseller": False},
            ],
        },
    },
    {
        "id": 2,
        "name": "Pizza Planet DX",
        "cuisine": "Pizza, Fast Food",
        "rating": 4.4,
        "time": "20-25 min",
        "offer": "Buy 1 Get 1",
        "veg": True,
        "price_for_two": 450,
        "distance": "1.6 km",
        "image": FOOD_IMAGES["pizza"],
        "promoted": False,
        "menu": {
            "Recommended": [
                {"name": "Margherita Pizza", "price": 199, "veg": True, "image": FOOD_IMAGES["pizza"], "bestseller": True},
                {"name": "Farmhouse Pizza", "price": 279, "veg": True, "image": FOOD_IMAGES["pizza"], "bestseller": False},
            ],
            "Sides": [
                {"name": "Garlic Bread", "price": 119, "veg": True, "image": FOOD_IMAGES["pizza"], "bestseller": True},
                {"name": "Cold Drink", "price": 59, "veg": True, "image": FOOD_IMAGES["dessert"], "bestseller": False},
            ],
        },
    },
    {
        "id": 3,
        "name": "Burger Junction",
        "cuisine": "Burger, Snacks",
        "rating": 4.2,
        "time": "18-22 min",
        "offer": "₹75 OFF",
        "veg": False,
        "price_for_two": 250,
        "distance": "0.9 km",
        "image": FOOD_IMAGES["burger"],
        "promoted": True,
        "menu": {
            "Recommended": [
                {"name": "Veg Cheese Burger", "price": 99, "veg": True, "image": FOOD_IMAGES["burger"], "bestseller": True},
                {"name": "Chicken Burger", "price": 139, "veg": False, "image": FOOD_IMAGES["burger"], "bestseller": True},
            ],
            "Add-ons": [
                {"name": "French Fries", "price": 89, "veg": True, "image": FOOD_IMAGES["burger"], "bestseller": False},
                {"name": "Chocolate Shake", "price": 129, "veg": True, "image": FOOD_IMAGES["dessert"], "bestseller": False},
            ],
        },
    },
    {
        "id": 4,
        "name": "South Express",
        "cuisine": "South Indian, Breakfast",
        "rating": 4.7,
        "time": "15-20 min",
        "offer": "Free delivery",
        "veg": True,
        "price_for_two": 220,
        "distance": "1.2 km",
        "image": FOOD_IMAGES["dosa"],
        "promoted": False,
        "menu": {
            "Recommended": [
                {"name": "Masala Dosa", "price": 109, "veg": True, "image": FOOD_IMAGES["dosa"], "bestseller": True},
                {"name": "Idli Sambar", "price": 79, "veg": True, "image": FOOD_IMAGES["dosa"], "bestseller": False},
            ],
            "Breakfast": [
                {"name": "Vada Sambar", "price": 89, "veg": True, "image": FOOD_IMAGES["dosa"], "bestseller": False},
                {"name": "Filter Coffee", "price": 49, "veg": True, "image": FOOD_IMAGES["dessert"], "bestseller": True},
            ],
        },
    },
    {
        "id": 5,
        "name": "Chinese Wok DX",
        "cuisine": "Chinese, Momos",
        "rating": 4.1,
        "time": "30-35 min",
        "offer": "20% OFF",
        "veg": False,
        "price_for_two": 300,
        "distance": "3.3 km",
        "image": FOOD_IMAGES["chinese"],
        "promoted": False,
        "menu": {
            "Recommended": [
                {"name": "Veg Hakka Noodles", "price": 139, "veg": True, "image": FOOD_IMAGES["chinese"], "bestseller": True},
                {"name": "Chicken Fried Rice", "price": 169, "veg": False, "image": FOOD_IMAGES["chinese"], "bestseller": False},
            ],
            "Snacks": [
                {"name": "Veg Momos", "price": 99, "veg": True, "image": FOOD_IMAGES["momos"], "bestseller": True},
                {"name": "Chilli Chicken", "price": 199, "veg": False, "image": FOOD_IMAGES["chinese"], "bestseller": False},
            ],
        },
    },
    {
        "id": 6,
        "name": "Sweet Treats",
        "cuisine": "Desserts, Ice Cream",
        "rating": 4.5,
        "time": "20-30 min",
        "offer": "Flat ₹50 OFF",
        "veg": True,
        "price_for_two": 280,
        "distance": "2.8 km",
        "image": FOOD_IMAGES["cake"],
        "promoted": True,
        "menu": {
            "Recommended": [
                {"name": "Chocolate Cake", "price": 149, "veg": True, "image": FOOD_IMAGES["cake"], "bestseller": True},
                {"name": "Gulab Jamun", "price": 99, "veg": True, "image": FOOD_IMAGES["dessert"], "bestseller": False},
            ],
            "Ice Cream": [
                {"name": "Vanilla Ice Cream", "price": 89, "veg": True, "image": FOOD_IMAGES["dessert"], "bestseller": False},
                {"name": "Brownie", "price": 129, "veg": True, "image": FOOD_IMAGES["cake"], "bestseller": True},
            ],
        },
    },
]

COUPONS = {
    "DELTAX50": {"type": "percent", "value": 50, "max": 100, "label": "50% OFF up to ₹100"},
    "FREEDEL": {"type": "delivery", "value": 29, "label": "Free delivery"},
    "NEWUSER": {"type": "flat", "value": 75, "label": "Flat ₹75 OFF"},
}

# -------------------------------------------------
# State
# -------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []
if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant = None
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "coupon" not in st.session_state:
    st.session_state.coupon = ""
if "order_placed" not in st.session_state:
    st.session_state.order_placed = False
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "home"

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255, 122, 0, 0.30), transparent 32%),
        radial-gradient(circle at top right, rgba(255, 0, 128, 0.22), transparent 34%),
        radial-gradient(circle at center right, rgba(59, 130, 246, 0.18), transparent 36%),
        linear-gradient(135deg, #120806 0%, #241031 42%, #08111f 100%);
    color: #ffffff;
}

[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 1.2rem; padding-bottom: 2rem; }

.top-nav {
    display:flex; justify-content:space-between; align-items:center;
    padding:18px 24px; border-radius:26px;
    background:rgba(255,255,255,.09);
    border:1px solid rgba(255,255,255,.15);
    box-shadow:0 18px 45px rgba(0,0,0,.28);
    backdrop-filter: blur(18px);
    margin-bottom:20px;
}
.brand {
    font-size:32px; font-weight:900; letter-spacing:-1px;
}
.brand span { color:#ff7a00; }
.nav-actions { display:flex; gap:12px; align-items:center; }
.nav-pill {
    background:linear-gradient(90deg, #ff7a00, #ff3d00);
    color:white; padding:10px 16px; border-radius:999px;
    font-weight:900; box-shadow:0 8px 24px rgba(255,122,0,.35);
}
.hero {
    background:
      linear-gradient(135deg, rgba(255,122,0,.98), rgba(255,61,0,.96), rgba(139,92,246,.92));
    border-radius:36px; padding:42px; color:white; margin-bottom:22px;
    border:1px solid rgba(255,255,255,.26);
    box-shadow:0 28px 75px rgba(255,90,31,.32);
    position:relative; overflow:hidden;
}
.hero:after {
    content:""; position:absolute; right:-90px; top:-100px; width:370px; height:370px;
    border-radius:50%; background:rgba(255,255,255,.13);
}
.hero h1 { font-size:62px; line-height:1.02; margin:0; font-weight:900; letter-spacing:-2px; }
.hero p { font-size:21px; opacity:.96; max-width:760px; margin-top:15px; }
.hero-badges { display:flex; flex-wrap:wrap; gap:10px; margin-top:24px; }
.hero-badge {
    background:rgba(0,0,0,.25); border:1px solid rgba(255,255,255,.24);
    padding:10px 15px; border-radius:999px; font-weight:900;
}
.search-zone {
    background:rgba(255,255,255,.10);
    border:1px solid rgba(255,255,255,.16);
    border-radius:30px; padding:22px; margin-bottom:20px;
    box-shadow:0 18px 45px rgba(0,0,0,.22);
    backdrop-filter:blur(18px);
}
.section-title {
    font-size:28px; font-weight:900; color:#fff; margin:14px 0 16px 0;
}
.category-card {
    background:rgba(255,255,255,.10);
    border:1px solid rgba(255,255,255,.15);
    border-radius:24px; padding:12px; text-align:center;
    box-shadow:0 14px 34px rgba(0,0,0,.22);
}
.category-img {
    height:92px; border-radius:18px; background-size:cover; background-position:center;
    border:1px solid rgba(255,255,255,.14);
}
.category-name { font-weight:900; margin-top:10px; color:white; }
.offer-strip {
    background:linear-gradient(90deg, rgba(34,197,94,.95), rgba(16,185,129,.95), rgba(59,130,246,.85));
    border-radius:24px; padding:18px 22px; margin:18px 0 24px 0;
    font-weight:900; color:white; box-shadow:0 16px 40px rgba(16,185,129,.22);
}
.card {
    background:rgba(255,255,255,.10);
    border:1px solid rgba(255,255,255,.17);
    border-radius:28px; padding:0; overflow:hidden;
    box-shadow:0 18px 42px rgba(0,0,0,.25);
    margin-bottom:18px; backdrop-filter:blur(18px);
    transition: transform .15s ease, border .15s ease;
}
.card:hover { transform:translateY(-4px); border-color:rgba(255,122,0,.72); }
.rest-img { height:180px; background-size:cover; background-position:center; position:relative; }
.promoted {
    position:absolute; top:12px; left:12px; background:rgba(0,0,0,.72);
    color:white; font-size:12px; font-weight:900; padding:6px 10px; border-radius:999px;
}
.discount {
    position:absolute; bottom:12px; left:12px; background:linear-gradient(90deg,#22c55e,#16a34a);
    color:white; padding:7px 12px; border-radius:999px; font-weight:900; font-size:13px;
}
.rest-body { padding:18px; }
.restaurant-title { font-size:22px; font-weight:900; color:#fff; }
.meta { color:#d1d5db; font-size:14px; margin-top:5px; }
.rating { color:#22c55e; font-weight:900; }
.menu-box {
    background:rgba(255,255,255,.10);
    border:1px solid rgba(255,255,255,.16);
    border-radius:30px; padding:24px; margin-top:20px;
    box-shadow:0 18px 44px rgba(0,0,0,.24);
}
.menu-card {
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.14);
    border-radius:24px; padding:14px; margin-bottom:14px;
}
.menu-img {
    height:95px; border-radius:18px; background-size:cover; background-position:center;
}
.price { font-weight:900; color:#22c55e; }
.bestseller {
    display:inline-block; color:#ffcf33; font-size:12px; font-weight:900; margin-top:4px;
}
.cart-box {
    background:linear-gradient(180deg, rgba(17,24,39,.97), rgba(31,16,44,.97));
    color:white; border-radius:30px; padding:24px;
    box-shadow:0 22px 55px rgba(0,0,0,.35);
    border:1px solid rgba(255,122,0,.35);
    position:sticky; top:20px;
}
.cart-item { border-bottom:1px solid rgba(255,255,255,.14); padding:12px 0; }
.total { font-size:28px; font-weight:900; color:#22c55e; margin-top:12px; }
.small-muted { color:#cbd5e1; font-size:13px; }
.step {
    background:rgba(255,255,255,.09);
    border:1px solid rgba(255,255,255,.14);
    border-radius:20px; padding:14px; margin-bottom:10px;
}
.step-active { border-color:#22c55e; box-shadow:0 0 18px rgba(34,197,94,.20); }
div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea, div[data-testid="stSelectbox"] div {
    background:rgba(255,255,255,.96);
    border-radius:16px; color:#111827;
}
.stButton > button {
    border-radius:16px; border:0; font-weight:900;
    background:linear-gradient(90deg,#ff7a00,#ff3d00);
    color:white; box-shadow:0 8px 22px rgba(255,122,0,.25);
}
.stButton > button:hover {
    background:linear-gradient(90deg,#ff8a1f,#ff5a1f); color:white; border:0;
}
.footer {
    text-align:center; color:#cbd5e1; margin-top:28px; padding:22px;
    border-radius:22px; background:rgba(255,255,255,.07);
    border:1px solid rgba(255,255,255,.12);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Helper functions
# -------------------------------------------------
def add_to_cart(restaurant_name, item):
    st.session_state.cart.append({
        "restaurant": restaurant_name,
        "name": item["name"],
        "price": item["price"],
        "image": item["image"],
        "veg": item["veg"]
    })

def flatten_menu(r):
    items = []
    for cat_items in r["menu"].values():
        items.extend(cat_items)
    return items

def calculate_bill():
    subtotal = sum(i["price"] for i in st.session_state.cart)
    delivery_fee = 29 if subtotal else 0
    platform_fee = 5 if subtotal else 0
    discount = 0
    coupon = st.session_state.coupon.strip().upper()

    if coupon in COUPONS and subtotal:
        c = COUPONS[coupon]
        if c["type"] == "percent":
            discount = min(round(subtotal * c["value"] / 100), c["max"])
        elif c["type"] == "flat":
            discount = min(c["value"], subtotal)
        elif c["type"] == "delivery":
            discount = min(c["value"], delivery_fee)

    total = max(subtotal + delivery_fee + platform_fee - discount, 0)
    return subtotal, delivery_fee, platform_fee, discount, total

# -------------------------------------------------
# Top Navigation and Hero
# -------------------------------------------------
st.markdown("""
<div class="top-nav">
    <div class="brand">🍽️ Delta<span>X</span> Food</div>
    <div class="nav-actions">
        <div class="nav-pill">Fresh • Fast • Online</div>
    </div>
</div>

<div class="hero">
    <span class="hero-badge">🔥 Swiggy-style food ordering demo</span>
    <h1>Order Food Online<br>Near You</h1>
    <p>Explore restaurants, real food images, cuisine categories, offers, menu sections, coupons, smart cart, checkout, and demo order tracking.</p>
    <div class="hero-badges">
        <div class="hero-badge">📍 Location Based</div>
        <div class="hero-badge">🍕 Real Food Images</div>
        <div class="hero-badge">🎁 Coupons</div>
        <div class="hero-badge">🛒 Smart Cart</div>
        <div class="hero-badge">🚚 Order Tracking</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Search and Filters
# -------------------------------------------------
st.markdown('<div class="search-zone">', unsafe_allow_html=True)
left, mid, right = st.columns([2, 2, 1])

with left:
    location = st.text_input("📍 Delivery location", placeholder="Enter area, city or pincode")

with mid:
    search = st.text_input("🔍 Search for restaurant or dish", placeholder="Biryani, Pizza, Burger, Dosa...")

with right:
    veg_only = st.toggle("Veg only")

sort_by = st.radio(
    "Sort by",
    ["Recommended", "Rating", "Fast Delivery", "Low Price", "Nearest"],
    horizontal=True
)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# Category carousel style section
# -------------------------------------------------
st.markdown('<div class="section-title">What are you craving today?</div>', unsafe_allow_html=True)
cat_cols = st.columns(4)
for idx, cat in enumerate(categories[:4]):
    with cat_cols[idx]:
        st.markdown(f"""
        <div class="category-card">
            <div class="category-img" style="background-image:url('{cat['image']}')"></div>
            <div class="category-name">{cat['name']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Search {cat['name']}", key=f"cat_{cat['name']}", use_container_width=True):
            st.session_state.selected_category = cat["name"]
            st.rerun()

cat_cols2 = st.columns(4)
for idx, cat in enumerate(categories[4:]):
    with cat_cols2[idx]:
        st.markdown(f"""
        <div class="category-card">
            <div class="category-img" style="background-image:url('{cat['image']}')"></div>
            <div class="category-name">{cat['name']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Search {cat['name']}", key=f"cat2_{cat['name']}", use_container_width=True):
            st.session_state.selected_category = cat["name"]
            st.rerun()

if st.session_state.selected_category:
    st.info(f"Showing results for: {st.session_state.selected_category}")
    if st.button("Clear category filter"):
        st.session_state.selected_category = None
        st.rerun()

st.markdown("""
<div class="offer-strip">
    🎁 Available coupons: DELTAX50 = 50% OFF up to ₹100 • FREEDEL = Free delivery • NEWUSER = Flat ₹75 OFF
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Filter restaurants
# -------------------------------------------------
filtered = restaurants.copy()

query = search or st.session_state.selected_category or ""
if query:
    s = query.lower()
    filtered = [
        r for r in filtered
        if s in r["name"].lower()
        or s in r["cuisine"].lower()
        or any(s in item["name"].lower() for item in flatten_menu(r))
    ]

if veg_only:
    filtered = [r for r in filtered if r["veg"] or all(item["veg"] for item in flatten_menu(r))]

if sort_by == "Rating":
    filtered = sorted(filtered, key=lambda r: r["rating"], reverse=True)
elif sort_by == "Fast Delivery":
    filtered = sorted(filtered, key=lambda r: int(r["time"].split("-")[0]))
elif sort_by == "Low Price":
    filtered = sorted(filtered, key=lambda r: r["price_for_two"])
elif sort_by == "Nearest":
    filtered = sorted(filtered, key=lambda r: float(r["distance"].split()[0]))
else:
    filtered = sorted(filtered, key=lambda r: (not r["promoted"], -r["rating"]))

# -------------------------------------------------
# Main Layout
# -------------------------------------------------
main, cart_col = st.columns([2.25, 1])

with main:
    st.markdown('<div class="section-title">Top restaurants near you</div>', unsafe_allow_html=True)

    if not filtered:
        st.warning("No restaurants found. Try another search.")
    else:
        cols = st.columns(2)
        for index, r in enumerate(filtered):
            with cols[index % 2]:
                promoted = '<div class="promoted">PROMOTED</div>' if r["promoted"] else ""
                st.markdown(f"""
                <div class="card">
                    <div class="rest-img" style="background-image:url('{r['image']}')">
                        {promoted}
                        <div class="discount">{r['offer']}</div>
                    </div>
                    <div class="rest-body">
                        <div class="restaurant-title">{r['name']}</div>
                        <div class="meta">{r['cuisine']}</div>
                        <div class="meta"><span class="rating">⭐ {r['rating']}</span> • {r['time']} • {r['distance']} • ₹{r['price_for_two']} for two</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("View Menu", key=f"view_{r['id']}", use_container_width=True):
                    st.session_state.selected_restaurant = r["id"]

    selected = next((r for r in restaurants if r["id"] == st.session_state.selected_restaurant), None)

    if selected:
        st.markdown('<div class="menu-box">', unsafe_allow_html=True)
        st.markdown(f"### {selected['name']}")
        st.caption(f"{selected['cuisine']} • ⭐ {selected['rating']} • {selected['time']} • {selected['distance']}")

        for menu_category, items in selected["menu"].items():
            st.markdown(f"#### {menu_category}")
            for item in items:
                c1, c2, c3 = st.columns([1.1, 2.4, 1])
                with c1:
                    st.markdown(f"<div class='menu-img' style=\"background-image:url('{item['image']}')\"></div>", unsafe_allow_html=True)
                with c2:
                    veg_label = "🟢 Veg" if item["veg"] else "🔴 Non-Veg"
                    best = "<span class='bestseller'>⭐ Bestseller</span>" if item["bestseller"] else ""
                    st.markdown(f"""
                    <div class="menu-card">
                        <b>{item['name']}</b><br>
                        <span class="small-muted">{veg_label}</span><br>
                        {best}<br>
                        <span class="price">₹{item['price']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                with c3:
                    if st.button("Add", key=f"add_{selected['id']}_{menu_category}_{item['name']}", use_container_width=True):
                        add_to_cart(selected["name"], item)
                        st.success(f"Added {item['name']}")
        st.markdown('</div>', unsafe_allow_html=True)

with cart_col:
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    st.markdown("### 🛒 Your Cart")

    if not st.session_state.cart:
        st.markdown('<p class="small-muted">Your cart is empty. Add items from any restaurant.</p>', unsafe_allow_html=True)
    else:
        for idx, item in enumerate(st.session_state.cart):
            st.markdown(f"""
            <div class="cart-item">
                <b>{item['name']}</b><br>
                <span class="small-muted">{item['restaurant']}</span><br>
                ₹{item['price']}
            </div>
            """, unsafe_allow_html=True)
            if st.button("Remove", key=f"remove_{idx}", use_container_width=True):
                st.session_state.cart.pop(idx)
                st.rerun()

        st.markdown("#### Apply Coupon")
        coupon_input = st.text_input("Coupon code", value=st.session_state.coupon, placeholder="DELTAX50 / FREEDEL / NEWUSER")
        if st.button("Apply Coupon", use_container_width=True):
            st.session_state.coupon = coupon_input.strip().upper()
            if st.session_state.coupon in COUPONS:
                st.success(f"Coupon applied: {COUPONS[st.session_state.coupon]['label']}")
            else:
                st.warning("Invalid coupon code.")

        subtotal, delivery_fee, platform_fee, discount, total = calculate_bill()
        st.markdown("---")
        st.markdown(f"Subtotal: ₹{subtotal}")
        st.markdown(f"Delivery fee: ₹{delivery_fee}")
        st.markdown(f"Platform fee: ₹{platform_fee}")
        st.markdown(f"Discount: -₹{discount}")
        st.markdown(f'<div class="total">Total: ₹{total}</div>', unsafe_allow_html=True)

        st.markdown("#### Checkout")
        name = st.text_input("Your name")
        phone = st.text_input("Mobile number")
        address = st.text_area("Delivery address", value=location if location else "")

        payment = st.selectbox("Payment method", ["Cash on Delivery", "UPI Demo", "Card Demo"])

        if st.button("Place Demo Order", use_container_width=True):
            if not name or not phone or not address:
                st.warning("Please enter name, phone, and address.")
            else:
                st.session_state.order_placed = True
                order_id = "DX" + datetime.now().strftime("%H%M%S")
                st.success(f"Order placed successfully! Order ID: {order_id}")
                st.balloons()

        if st.button("Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.session_state.coupon = ""
            st.session_state.order_placed = False
            st.rerun()

    if st.session_state.order_placed:
        st.markdown("---")
        st.markdown("### 🚚 Order Tracking")
        st.markdown('<div class="step step-active">✅ Order Confirmed</div>', unsafe_allow_html=True)
        st.markdown('<div class="step step-active">👨‍🍳 Food Being Prepared</div>', unsafe_allow_html=True)
        st.markdown('<div class="step">🛵 Rider Assigned</div>', unsafe_allow_html=True)
        st.markdown('<div class="step">🏠 Delivered</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    © 2026 DeltaX Food. Original Swiggy-style demo website. Real payments and real restaurant orders are not enabled.
</div>
""", unsafe_allow_html=True)
