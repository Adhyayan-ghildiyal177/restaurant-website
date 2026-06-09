
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="DeltaX Food | Order Online",
    page_icon="🍽️",
    layout="wide"
)

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
        "image": "🍛",
        "menu": [
            {"name": "Chicken Biryani", "price": 199, "veg": False},
            {"name": "Veg Biryani", "price": 149, "veg": True},
            {"name": "Paneer Tikka", "price": 179, "veg": True},
            {"name": "Raita", "price": 39, "veg": True},
        ],
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
        "image": "🍕",
        "menu": [
            {"name": "Margherita Pizza", "price": 199, "veg": True},
            {"name": "Farmhouse Pizza", "price": 279, "veg": True},
            {"name": "Garlic Bread", "price": 119, "veg": True},
            {"name": "Cold Drink", "price": 59, "veg": True},
        ],
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
        "image": "🍔",
        "menu": [
            {"name": "Veg Cheese Burger", "price": 99, "veg": True},
            {"name": "Chicken Burger", "price": 139, "veg": False},
            {"name": "French Fries", "price": 89, "veg": True},
            {"name": "Chocolate Shake", "price": 129, "veg": True},
        ],
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
        "image": "🥘",
        "menu": [
            {"name": "Masala Dosa", "price": 109, "veg": True},
            {"name": "Idli Sambar", "price": 79, "veg": True},
            {"name": "Vada Sambar", "price": 89, "veg": True},
            {"name": "Filter Coffee", "price": 49, "veg": True},
        ],
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
        "image": "🥡",
        "menu": [
            {"name": "Veg Hakka Noodles", "price": 139, "veg": True},
            {"name": "Chicken Fried Rice", "price": 169, "veg": False},
            {"name": "Veg Momos", "price": 99, "veg": True},
            {"name": "Chilli Chicken", "price": 199, "veg": False},
        ],
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
        "image": "🍰",
        "menu": [
            {"name": "Chocolate Cake", "price": 149, "veg": True},
            {"name": "Gulab Jamun", "price": 99, "veg": True},
            {"name": "Vanilla Ice Cream", "price": 89, "veg": True},
            {"name": "Brownie", "price": 129, "veg": True},
        ],
    },
]

if "cart" not in st.session_state:
    st.session_state.cart = []

if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant = None

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255, 122, 0, 0.28), transparent 34%),
        radial-gradient(circle at top right, rgba(255, 0, 128, 0.22), transparent 35%),
        linear-gradient(135deg, #130a05 0%, #1e102d 38%, #0f172a 100%);
    color: #ffffff;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1f102c, #0f172a);
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 22px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    box-shadow: 0 16px 40px rgba(0,0,0,0.28);
    margin-bottom: 22px;
    backdrop-filter: blur(18px);
}

.brand {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -0.8px;
}

.brand span {
    color: #ff7a00;
}

.nav-pill {
    background: linear-gradient(90deg, #ff7a00, #ff3d00);
    color: white;
    padding: 10px 18px;
    border-radius: 999px;
    font-weight: 800;
    box-shadow: 0 8px 24px rgba(255, 122, 0, .35);
}

.hero {
    position: relative;
    overflow: hidden;
    background:
      linear-gradient(135deg, rgba(255,122,0,.98), rgba(255,61,0,.95), rgba(145,42,255,.95));
    border-radius: 34px;
    padding: 46px;
    color: white;
    box-shadow: 0 28px 70px rgba(255, 93, 0, 0.30);
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,.25);
}

.hero:after {
    content: "";
    position: absolute;
    width: 360px;
    height: 360px;
    right: -90px;
    top: -90px;
    border-radius: 50%;
    background: rgba(255,255,255,.15);
}

.hero h1 {
    font-size: 60px;
    line-height: 1.02;
    margin: 0;
    font-weight: 900;
    letter-spacing: -2px;
}

.hero p {
    font-size: 21px;
    opacity: .96;
    max-width: 720px;
    margin-top: 16px;
}

.brand-pill {
    display:inline-block;
    background:rgba(0,0,0,.22);
    border:1px solid rgba(255,255,255,.35);
    padding:9px 18px;
    border-radius:999px;
    font-weight:900;
    margin-bottom:15px;
}

.search-zone {
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 28px;
    padding: 24px;
    backdrop-filter: blur(16px);
    box-shadow: 0 18px 44px rgba(0,0,0,.25);
    margin-bottom: 22px;
}

.card {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 26px;
    padding: 20px;
    box-shadow: 0 16px 36px rgba(0,0,0,.22);
    margin-bottom: 18px;
    backdrop-filter: blur(18px);
    transition: transform .15s ease, border .15s ease;
}

.card:hover {
    transform: translateY(-4px);
    border: 1px solid rgba(255,122,0,.62);
}

.restaurant-title {
    font-size: 22px;
    font-weight: 900;
    color: #ffffff;
    margin-top: 12px;
}

.restaurant-img {
    font-size: 58px;
    text-align:center;
    background:
        linear-gradient(135deg, rgba(255,122,0,.25), rgba(145,42,255,.28));
    border: 1px solid rgba(255,255,255,.18);
    border-radius: 22px;
    padding: 20px;
}

.offer {
    display:inline-block;
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    padding: 7px 13px;
    border-radius: 999px;
    font-weight: 900;
    font-size: 13px;
    box-shadow: 0 8px 22px rgba(34,197,94,.28);
}

.meta {
    color:#d1d5db;
    font-size:14px;
    margin-top: 4px;
}

.section-title {
    font-size: 28px;
    font-weight: 900;
    color: white;
    margin: 10px 0 18px 0;
}

.menu-box {
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 26px;
    padding: 22px;
    margin-top: 18px;
}

.cart-box {
    background:
        linear-gradient(180deg, rgba(17,24,39,.96), rgba(31,16,44,.96));
    color:white;
    border-radius:28px;
    padding:24px;
    box-shadow: 0 20px 50px rgba(0,0,0,.34);
    border: 1px solid rgba(255,122,0,.32);
    position: sticky;
    top: 20px;
}

.cart-item {
    border-bottom:1px solid rgba(255,255,255,.14);
    padding:12px 0;
}

.total {
    font-size:28px;
    font-weight:900;
    color:#22c55e;
    margin-top: 12px;
}

.small-muted {
    color:#cbd5e1;
    font-size:13px;
}

.badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 22px;
}

.badge {
    background: rgba(0,0,0,.26);
    border: 1px solid rgba(255,255,255,.20);
    border-radius: 999px;
    padding: 10px 14px;
    font-weight: 800;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    background: rgba(255,255,255,.96);
    border-radius: 16px;
    color: #111827;
    border: 1px solid rgba(255,122,0,.35);
}

.stButton > button {
    border-radius: 16px;
    border: 0;
    font-weight: 800;
    background: linear-gradient(90deg, #ff7a00, #ff3d00);
    color: white;
    box-shadow: 0 8px 22px rgba(255, 122, 0, .25);
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff8a1f, #ff5a1f);
    color: white;
    border: 0;
}

div[role="radiogroup"] label {
    background: rgba(255,255,255,.09);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 999px;
    padding: 8px 12px;
}

.footer {
    text-align: center;
    color: #cbd5e1;
    margin-top: 28px;
    padding: 22px;
    border-radius: 22px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.12);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-nav">
    <div class="brand">🍽️ Delta<span>X</span> Food</div>
    <div class="nav-pill">Fresh • Fast • Online</div>
</div>

<div class="hero">
    <span class="brand-pill">🔥 Premium Food Delivery Demo</span>
    <h1>Order Food Online<br>Near You</h1>
    <p>Find restaurants, explore menus, add delicious dishes to your cart, and place a demo order with a colourful modern UI.</p>
    <div class="badges">
        <div class="badge">⚡ Fast Delivery</div>
        <div class="badge">🎁 Live Offers</div>
        <div class="badge">🛒 Smart Cart</div>
        <div class="badge">📱 Mobile Friendly</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="search-zone">', unsafe_allow_html=True)
left, mid, right = st.columns([2, 2, 1])
with left:
    location = st.text_input("📍 Delivery location", placeholder="Enter your area, city or pincode")
with mid:
    search = st.text_input("🔍 Search restaurant or food", placeholder="Biryani, Pizza, Dosa, Burger...")
with right:
    veg_only = st.toggle("Veg only")
sort_by = st.radio("Sort by", ["Recommended", "Rating", "Fast Delivery", "Low Price"], horizontal=True)
st.markdown('</div>', unsafe_allow_html=True)

filtered = restaurants.copy()

if search:
    s = search.lower()
    filtered = [
        r for r in filtered
        if s in r["name"].lower()
        or s in r["cuisine"].lower()
        or any(s in item["name"].lower() for item in r["menu"])
    ]

if veg_only:
    filtered = [r for r in filtered if r["veg"]]

if sort_by == "Rating":
    filtered = sorted(filtered, key=lambda r: r["rating"], reverse=True)
elif sort_by == "Fast Delivery":
    filtered = sorted(filtered, key=lambda r: int(r["time"].split("-")[0]))
elif sort_by == "Low Price":
    filtered = sorted(filtered, key=lambda r: r["price_for_two"])

main, cart_col = st.columns([2.2, 1])

with main:
    st.markdown('<div class="section-title">🍴 Popular restaurants near you</div>', unsafe_allow_html=True)

    if not filtered:
        st.warning("No restaurants found. Try another search.")
    else:
        cols = st.columns(2)
        for index, r in enumerate(filtered):
            with cols[index % 2]:
                st.markdown(f"""
                <div class="card">
                    <div class="restaurant-img">{r['image']}</div>
                    <div class="restaurant-title">{r['name']}</div>
                    <div class="meta">{r['cuisine']}</div>
                    <div class="meta">⭐ {r['rating']} • {r['time']} • ₹{r['price_for_two']} for two</div>
                    <br>
                    <span class="offer">{r['offer']}</span>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"View Menu", key=f"view_{r['id']}", use_container_width=True):
                    st.session_state.selected_restaurant = r["id"]

    selected = next((r for r in restaurants if r["id"] == st.session_state.selected_restaurant), None)

    if selected:
        st.markdown('<div class="menu-box">', unsafe_allow_html=True)
        st.markdown(f"### Menu — {selected['name']}")

        for item in selected["menu"]:
            c1, c2, c3 = st.columns([3, 1, 1])
            with c1:
                veg_label = "🟢 Veg" if item["veg"] else "🔴 Non-Veg"
                st.markdown(f"**{item['name']}**  \n{veg_label}")
            with c2:
                st.markdown(f"**₹{item['price']}**")
            with c3:
                if st.button("Add", key=f"add_{selected['id']}_{item['name']}"):
                    st.session_state.cart.append({
                        "restaurant": selected["name"],
                        "name": item["name"],
                        "price": item["price"]
                    })
                    st.success(f"Added {item['name']}")
        st.markdown('</div>', unsafe_allow_html=True)

with cart_col:
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    st.markdown("### 🛒 Your Cart")

    if not st.session_state.cart:
        st.markdown('<p class="small-muted">Your cart is empty. Add items from any restaurant.</p>', unsafe_allow_html=True)
    else:
        subtotal = sum(i["price"] for i in st.session_state.cart)
        delivery_fee = 29
        platform_fee = 5
        total = subtotal + delivery_fee + platform_fee

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

        st.markdown(f"Subtotal: ₹{subtotal}")
        st.markdown(f"Delivery fee: ₹{delivery_fee}")
        st.markdown(f"Platform fee: ₹{platform_fee}")
        st.markdown(f'<div class="total">Total: ₹{total}</div>', unsafe_allow_html=True)

        name = st.text_input("Your name")
        phone = st.text_input("Mobile number")
        address = st.text_area("Delivery address", value=location if location else "")

        if st.button("Place Demo Order", use_container_width=True):
            if not name or not phone or not address:
                st.warning("Please enter name, phone, and address.")
            else:
                order_id = "DX" + datetime.now().strftime("%H%M%S")
                st.success(f"Order placed successfully! Order ID: {order_id}")
                st.balloons()

        if st.button("Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    © 2026 DeltaX Food. Colourful demo food-ordering website. Real payments and restaurant orders are not enabled.
</div>
""", unsafe_allow_html=True)
